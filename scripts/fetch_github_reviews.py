"""
Fetch reviewed PRs from GitHub and generate a contribution report markdown file.
"""

import argparse
import os
from datetime import datetime
from pathlib import Path

import requests


def get_github_token() -> str:
    """Get GitHub token from environment."""
    if not (token := os.environ.get("GITHUB_TOKEN")):
        raise ValueError("GITHUB_TOKEN environment variable not set")
    return token


def fetch_contributions(
    username: str,
    start_date: str,
    end_date: str,
    excluded_repos: list[str],
    token: str,
) -> dict[str, dict[str, list[dict]]]:
    """Fetch all contributions (issues, PRs, reviews, commits) by user."""
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json",
    }

    # Contribution types to fetch
    queries = {
        "issues": f"author:{username} created:{start_date}..{end_date} is:issue",
        "prs": f"author:{username} created:{start_date}..{end_date} is:pr",
        "reviewed": f"reviewed-by:{username} created:{start_date}..{end_date} is:pr",
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

                if repo_full_name not in contributions_by_repo:
                    contributions_by_repo[repo_full_name] = {
                        "issues": [],
                        "prs": [],
                        "commits": [],
                        "reviewed": [],
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

    # Fetch commits separately using REST API
    page = 1
    per_page = 100

    while True:
        url = "https://api.github.com/search/commits"
        params = {
            "q": f"author:{username} committer-date:{start_date}..{end_date}",
            "sort": "committer-date",
            "order": "desc",
            "per_page": per_page,
            "page": page,
        }

        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()

            data = response.json()
            if not (items := data.get("items", [])):
                break

            for item in items:
                # Extract repo from HTML URL
                # URL format: https://github.com/owner/repo/commit/sha
                url_parts = item["html_url"].split("/")
                if len(url_parts) >= 5:
                    repo_full_name = f"{url_parts[3]}/{url_parts[4]}"
                else:
                    continue

                # Check if repo should be excluded
                if any(excluded in repo_full_name for excluded in excluded_repos):
                    continue

                if repo_full_name not in contributions_by_repo:
                    contributions_by_repo[repo_full_name] = {
                        "issues": [],
                        "prs": [],
                        "commits": [],
                        "reviewed": [],
                    }

                # Extract commit message (first line)
                message = item["commit"]["message"].split("\n")[0]
                contribution = {
                    "title": message,
                    "sha": item["sha"][:7],  # Short SHA
                    "url": item["html_url"],
                    "repo": repo_full_name,
                }

                # Avoid duplicates
                if contribution not in contributions_by_repo[repo_full_name]["commits"]:
                    contributions_by_repo[repo_full_name]["commits"].append(
                        contribution
                    )

            # Check if there are more pages
            if len(items) < per_page:
                break

            page += 1

        except requests.exceptions.RequestException as e:
            # Commits API might fail on some cases, continue without commits
            print(f"Warning: Could not fetch commits - {e}")
            break

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
        f"Date: {end_dt.strftime('%Y-%m-%d %H:%M')} +0800",
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
            [items["issues"], items["prs"], items["commits"], items["reviewed"]]
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

        # Commits
        if items["commits"]:
            lines.append("* Push")
            for i, item in enumerate(items["commits"], 1):
                lines.append(
                    f"    {i}. [{item['title']}]({item['url']}) ({item['sha']})"
                )

        # Reviewed PRs
        if items["reviewed"]:
            lines.append("* 審閱 PRs")
            for i, item in enumerate(items["reviewed"], 1):
                lines.append(
                    f"    {i}. [{item['title']} #{item['number']}]({item['url']})"
                )

        lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Fetch reviewed PRs from GitHub and generate contribution report"
    )
    parser.add_argument(
        "--username", default="Lee-W", help="GitHub username (default: Lee-W)"
    )
    parser.add_argument(
        "--start-date", required=True, help="Start date in YYYY-MM-DD format"
    )
    parser.add_argument(
        "--end-date", help="End date in YYYY-MM-DD format (default: today)"
    )
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
        help="Output markdown file path (optional, prints to stdout if not provided)",
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

    # Validate dates
    try:
        start_date = datetime.strptime(args.start_date, "%Y-%m-%d")
    except ValueError:
        parser.error(f"Invalid start-date format: {args.start_date}")

    end_date = datetime.now()
    if args.end_date:
        try:
            end_date = datetime.strptime(args.end_date, "%Y-%m-%d")
        except ValueError:
            parser.error(f"Invalid end-date format: {args.end_date}")

    print(f"Fetching contributions by {args.username}")
    print(f"Date range: {args.start_date} to {end_date.strftime('%Y-%m-%d')}")
    if excluded_repos:
        print(f"Excluding repos: {', '.join(sorted(excluded_repos))}")

    token = get_github_token()

    contributions_by_repo = fetch_contributions(
        args.username,
        args.start_date,
        end_date.strftime("%Y-%m-%d"),
        excluded_repos,
        token,
    )

    if not contributions_by_repo:
        print("No contributions found")
        return

    total_issues = sum(len(c["issues"]) for c in contributions_by_repo.values())
    total_prs = sum(len(c["prs"]) for c in contributions_by_repo.values())
    total_commits = sum(len(c["commits"]) for c in contributions_by_repo.values())
    total_reviewed = sum(len(c["reviewed"]) for c in contributions_by_repo.values())

    print("Found:")
    print(f"  {total_issues} created issues")
    print(f"  {total_prs} created PRs")
    print(f"  {total_commits} commits")
    print(f"  {total_reviewed} reviewed PRs")
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
            if contrib["commits"]:
                details.append(f"{len(contrib['commits'])} commits")
            if contrib["reviewed"]:
                details.append(f"{len(contrib['reviewed'])} reviewed")
            if details:
                print(f"  {repo}: {', '.join(details)}")
        return

    markdown = generate_markdown(
        contributions_by_repo,
        args.start_date,
        end_date.strftime("%Y-%m-%d"),
        args.username,
    )

    if args.output:
        args.output.write_text(markdown, encoding="utf-8")
        print(f"✓ Markdown written to {args.output}")
    else:
        print("\n" + markdown)


if __name__ == "__main__":
    main()
