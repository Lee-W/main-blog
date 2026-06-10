"""
Fetch reviewed PRs from GitHub and generate a contribution report markdown file.
"""

import argparse
import os
import subprocess
from datetime import datetime, timedelta
from pathlib import Path

import requests


def get_github_token() -> str | None:
    """Get GitHub token from GITHUB_TOKEN env var or gh CLI."""
    if token := os.environ.get("GITHUB_TOKEN"):
        return token
    try:
        result = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout.strip()
    except FileNotFoundError:
        pass
    return None


def user_commented_in_range(
    repo_full_name: str,
    issue_number: int,
    username: str,
    start_date: str,
    end_date: str,
    headers: dict[str, str],
) -> bool:
    """Check whether the user posted a comment on an issue/PR within the date range.

    Search's ``commenter:`` qualifier only tells us the user commented at some
    point; it can't filter by comment date. We confirm by walking the issue's
    comments (filtered server-side with ``since``) and matching the author.
    """
    page = 1
    per_page = 100
    while True:
        response = requests.get(
            f"https://api.github.com/repos/{repo_full_name}/issues/{issue_number}/comments",
            headers=headers,
            params={
                "since": f"{start_date}T00:00:00Z",
                "per_page": per_page,
                "page": page,
            },
        )
        response.raise_for_status()
        comments = response.json()
        if not comments:
            return False

        for comment in comments:
            author = (comment.get("user") or {}).get("login", "")
            if author.lower() != username.lower():
                continue
            if comment["created_at"][:10] <= end_date:
                return True

        if len(comments) < per_page:
            return False
        page += 1


def fetch_contributions(
    username: str,
    start_date: str,
    end_date: str,
    excluded_repos: list[str],
    token: str | None,
) -> dict[str, dict[str, list[dict]]]:
    """Fetch all contributions (issues, PRs, reviews, comments, releases) by user."""
    headers = {"Accept": "application/vnd.github.v3+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    # Contribution types to fetch.
    #
    # Authored issues/PRs and reviews filter on `created` (when the thread was
    # opened). Comments instead filter on `updated` so threads opened earlier
    # but replied to this week become candidates; each candidate is then
    # verified against the actual comment timestamps below.
    queries = {
        "issues": f"author:{username} created:{start_date}..{end_date} is:issue",
        "prs": f"author:{username} created:{start_date}..{end_date} is:pr",
        "reviewed": f"reviewed-by:{username} created:{start_date}..{end_date} is:pr",
        "commented": f"commenter:{username} updated:{start_date}..{end_date}",
    }

    contributions_by_repo = {}
    for contribution_type, query in queries.items():
        page = 1
        per_page = 100

        while True:
            url = "https://api.github.com/search/issues"
            params = {
                "q": query,
                "sort": "updated",
                "order": "desc",
                "per_page": per_page,
                "page": page,
            }

            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()

            data = response.json()
            if not (items := data.get("items", [])):
                break

            for item in items:
                repo_full_name = item["repository_url"].split("/")[-2:]
                repo_full_name = "/".join(repo_full_name)

                # Check if repo should be excluded
                if any(excluded in repo_full_name for excluded in excluded_repos):
                    continue

                # `commented` returns threads the user replied to, including
                # ones they authored (already captured as issues/prs) and ones
                # only updated for unrelated reasons. Drop self-authored threads
                # and verify a real comment lands in the date range.
                if contribution_type == "commented":
                    author = (item.get("user") or {}).get("login", "")
                    if author.lower() == username.lower():
                        continue
                    if not user_commented_in_range(
                        repo_full_name,
                        item["number"],
                        username,
                        start_date,
                        end_date,
                        headers,
                    ):
                        continue

                if repo_full_name not in contributions_by_repo:
                    contributions_by_repo[repo_full_name] = {
                        "issues": [],
                        "prs": [],
                        "releases": [],
                        "reviewed": [],
                        "commented": [],
                    }

                contribution = {
                    "title": item["title"],
                    "number": item["number"],
                    "url": item["html_url"],
                    "repo": repo_full_name,
                }

                # Avoid duplicates
                if (
                    contribution
                    not in contributions_by_repo[repo_full_name][contribution_type]
                ):
                    contributions_by_repo[repo_full_name][contribution_type].append(
                        contribution
                    )

            # Check if there are more pages
            if len(items) < per_page:
                break

            page += 1

    repos = []
    page = 1
    per_page = 100

    while True:
        response = requests.get(
            f"https://api.github.com/users/{username}/repos",
            headers=headers,
            params={"per_page": per_page, "page": page},
        )
        response.raise_for_status()
        data = response.json()
        if not data:
            break
        repos.extend(r["full_name"] for r in data)
        if len(data) < per_page:
            break
        page += 1

    start_dt = datetime.strptime(start_date, "%Y-%m-%d")
    end_dt = datetime.strptime(end_date, "%Y-%m-%d")

    for repo_full_name in repos:
        if any(excluded in repo_full_name for excluded in excluded_repos):
            continue

        page = 1
        while True:
            response = requests.get(
                f"https://api.github.com/repos/{repo_full_name}/releases",
                headers=headers,
                params={"per_page": per_page, "page": page},
            )
            response.raise_for_status()
            data = response.json()
            if not data:
                break

            for release in data:
                published_at = release.get("published_at")
                if not published_at:
                    continue
                published_dt = datetime.strptime(published_at[:10], "%Y-%m-%d")
                if not (start_dt <= published_dt <= end_dt):
                    continue

                if repo_full_name not in contributions_by_repo:
                    contributions_by_repo[repo_full_name] = {
                        "issues": [],
                        "prs": [],
                        "releases": [],
                        "reviewed": [],
                        "commented": [],
                    }

                contribution = {
                    "title": release["name"] or release["tag_name"],
                    "tag": release["tag_name"],
                    "url": release["html_url"],
                    "repo": repo_full_name,
                }

                if (
                    contribution
                    not in contributions_by_repo[repo_full_name]["releases"]
                ):
                    contributions_by_repo[repo_full_name]["releases"].append(
                        contribution
                    )

            if len(data) < per_page:
                break
            page += 1

    return contributions_by_repo


def generate_markdown(
    contributions_by_repo: dict[str, dict[str, list[dict]]],
    start_date: str,
    end_date: str,
    username: str = "Lee-W",
) -> str:
    """Generate markdown content for contribution report."""

    start_dt = datetime.strptime(start_date, "%Y-%m-%d")
    end_dt = datetime.strptime(end_date, "%Y-%m-%d")

    # Format dates for Chinese title
    start_formatted = start_dt.strftime("%-m/%-d").lstrip("0")  # Remove leading zero
    end_formatted = end_dt.strftime("%-m/%-d").lstrip("0")

    lines = [
        f"Title: {start_dt.year}/{start_formatted} - {end_formatted} 開源貢獻週報",
        f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M')} +0800",
        "Category: Tech",
        "Tags: Open Source, 開源貢獻週報",
        f"Slug: {start_date}-{end_date}-open-source-report",
        "Authors: Wei Lee",
        "Lang: zh-tw",
        "",
        "<!--more-->",
        "",
    ]

    for repo in sorted(contributions_by_repo.keys()):
        items = contributions_by_repo[repo]

        # Skip repo if no contributions
        if not any(
            [
                items["issues"],
                items["prs"],
                items["releases"],
                items["reviewed"],
                items["commented"],
            ]
        ):
            continue

        lines.append(f"## {repo}")

        # Created Issues
        if items["issues"]:
            lines.append("* 開 Issues")
            for i, item in enumerate(items["issues"], 1):
                lines.append(
                    f"    {i}. [{item['title']} #{item['number']}]({item['url']})"
                )

        # Created PRs
        if items["prs"]:
            lines.append("* 開 PRs")
            for i, item in enumerate(items["prs"], 1):
                lines.append(
                    f"    {i}. [{item['title']} #{item['number']}]({item['url']})"
                )

        if items["releases"]:
            lines.append("* Releases")
            for i, item in enumerate(items["releases"], 1):
                lines.append(
                    f"    {i}. [{item['title']}]({item['url']}) ({item['tag']})"
                )

        # Reviewed PRs
        if items["reviewed"]:
            lines.append("* 審閱 PRs")
            for i, item in enumerate(items["reviewed"], 1):
                lines.append(
                    f"    {i}. [{item['title']} #{item['number']}]({item['url']})"
                )

        # Commented Issues/PRs
        if items["commented"]:
            lines.append("* 參與討論")
            for i, item in enumerate(items["commented"], 1):
                lines.append(
                    f"    {i}. [{item['title']} #{item['number']}]({item['url']})"
                )

        lines.append("")

    return "\n".join(lines)


REPORT_DIR = Path("content/posts/tech")


def resolve_output_path(start_date: str, end_date: str) -> Path:
    """Derive the report's file path from its date range.

    Posts are named ``{seq}-{slug}.md`` under ``content/posts/tech/{year}/``.
    If a report for this week already exists we reuse its path so regenerating
    overwrites in place; otherwise we take the next sequence number in the
    year directory.
    """
    slug = f"{start_date}-{end_date}-open-source-report"
    year_dir = REPORT_DIR / start_date[:4]

    existing = sorted(year_dir.glob(f"*-{slug}.md"))
    if existing:
        return existing[0]

    max_seq = 0
    for path in year_dir.glob("*.md"):
        prefix = path.name.split("-", 1)[0]
        if prefix.isdigit():
            max_seq = max(max_seq, int(prefix))
    return year_dir / f"{max_seq + 1}-{slug}.md"


def main():
    parser = argparse.ArgumentParser(
        description="Fetch reviewed PRs from GitHub and generate contribution report"
    )
    parser.add_argument(
        "--username", default="Lee-W", help="GitHub username (default: Lee-W)"
    )
    parser.add_argument("--start-date", help="Start date in YYYY-MM-DD format")
    parser.add_argument("--end-date", help="End date in YYYY-MM-DD format")
    parser.add_argument(
        "--exclude",
        type=str,
        nargs="+",
        default=[],
        help="Exclude repos containing these strings (e.g., apache/airflow astronomer/)",
    )
    parser.add_argument(
        "--exclude-file",
        type=Path,
        default=Path("scripts/exclude-repos.txt"),
        help="File containing repos to exclude (one per line, default: scripts/exclude-repos.txt)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help=(
            "Output markdown file path. Defaults to the auto-derived post path "
            "under content/posts/tech/{year}/ based on the date range."
        ),
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would be fetched without creating file",
    )

    args = parser.parse_args()

    # Load exclude repos from file
    excluded_repos = list(args.exclude)
    if args.exclude_file and args.exclude_file.exists():
        with open(args.exclude_file, "r") as f:
            file_excludes = [line.strip() for line in f if line.strip()]
            excluded_repos.extend(file_excludes)

    # Remove duplicates
    excluded_repos = list(set(excluded_repos))

    today = datetime.now()
    weekday = today.weekday()

    if args.start_date:
        try:
            start_date = datetime.strptime(args.start_date, "%Y-%m-%d")
        except ValueError:
            parser.error(f"Invalid start-date format: {args.start_date}")
    else:
        if weekday == 6:
            start_date = today - timedelta(days=6)
        else:
            start_date = today - timedelta(days=weekday + 7)

    if args.end_date:
        try:
            end_date = datetime.strptime(args.end_date, "%Y-%m-%d")
        except ValueError:
            parser.error(f"Invalid end-date format: {args.end_date}")
    else:
        if weekday == 6:
            end_date = today
        else:
            end_date = today - timedelta(days=weekday + 1)

    print(f"Fetching contributions by {args.username}")
    print(
        f"Date range: {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}"
    )
    if excluded_repos:
        print(f"Excluding repos: {', '.join(sorted(excluded_repos))}")

    token = get_github_token()

    contributions_by_repo = fetch_contributions(
        args.username,
        start_date.strftime("%Y-%m-%d"),
        end_date.strftime("%Y-%m-%d"),
        excluded_repos,
        token,
    )

    if not contributions_by_repo:
        print("No contributions found")
        return

    total_issues = sum(len(c["issues"]) for c in contributions_by_repo.values())
    total_prs = sum(len(c["prs"]) for c in contributions_by_repo.values())
    total_releases = sum(len(c["releases"]) for c in contributions_by_repo.values())
    total_reviewed = sum(len(c["reviewed"]) for c in contributions_by_repo.values())
    total_commented = sum(len(c["commented"]) for c in contributions_by_repo.values())

    print("Found:")
    print(f"  {total_issues} created issues")
    print(f"  {total_prs} created PRs")
    print(f"  {total_releases} releases")
    print(f"  {total_reviewed} reviewed PRs")
    print(f"  {total_commented} commented issues/PRs")
    print(f"  across {len(contributions_by_repo)} repos")

    if args.dry_run:
        print("\nWould generate markdown with:")
        for repo in sorted(contributions_by_repo.keys()):
            contrib = contributions_by_repo[repo]
            details = []
            if contrib["issues"]:
                details.append(f"{len(contrib['issues'])} issues")
            if contrib["prs"]:
                details.append(f"{len(contrib['prs'])} PRs")
            if contrib["releases"]:
                details.append(f"{len(contrib['releases'])} releases")
            if contrib["reviewed"]:
                details.append(f"{len(contrib['reviewed'])} reviewed")
            if contrib["commented"]:
                details.append(f"{len(contrib['commented'])} commented")
            if details:
                print(f"  {repo}: {', '.join(details)}")
        return

    markdown = generate_markdown(
        contributions_by_repo,
        start_date.strftime("%Y-%m-%d"),
        end_date.strftime("%Y-%m-%d"),
        args.username,
    )

    output = args.output or resolve_output_path(
        start_date.strftime("%Y-%m-%d"),
        end_date.strftime("%Y-%m-%d"),
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(markdown, encoding="utf-8")
    print(f"✓ Markdown written to {output}")


if __name__ == "__main__":
    main()
