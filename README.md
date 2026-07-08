# blog.wei-lee.me

Wei's personal blog — tech, books, and random thoughts. Built with [Pelican](https://getpelican.com/) and the customized [Attila](https://github.com/Lee-W/attila) theme. Deployed to Cloudflare Workers.

## Commands

```bash
uv run inv build           # Build local version of site
uv run inv rebuild         # Clean build
uv run inv serve           # Serve at localhost:8000
uv run inv reserve         # Build then serve
uv run inv livereload      # Build and serve with live reload
uv run inv clean           # Remove generated files
uv run inv preview         # Build production version, including Pagefind
uv run inv style           # Lint + commit style check
uv run inv format          # Auto-fix lint issues
uv run inv check-content   # Check post metadata and image usage
uv run inv security-check  # Audit dependencies
uv run inv check-and-remove-image-exif-gps-info  # Strip GPS EXIF from images
uv run inv check-image-usage  # Report orphan, reused, duplicate, and missing images
```

Build with search index:

```bash
uv run inv build --build-pagefind
```

## Content Structure

```text
content/
  posts/
    tech/             # Tech articles
    book/             # Book digests
    random-thoughts/  # Personal posts
  pages/              # Static pages
  images/             # Post images
  places/             # OSM/map data
  static/             # Static files excluded from article processing
  extra/              # Extra static files
```

## Publishing

Drafts (`uv run inv new_draft ...`) and new posts (`uv run inv new_post ...`)
are created without numeric prefixes. Drafts carry `Status: draft` and are
excluded from the build. To publish one:

1. Include a commit named `new post: <title>` in the pull request.
2. Enable auto-merge.

Before the PR merges, a GitHub Actions workflow assigns the final sequence
number, removes the draft status, and rewrites the post's `Date` to the
moment it ships, so the published date is accurate without manual editing. It
also moves any colliding drafts after the publishing post. See
[`.github/workflows/prepare-publication.yaml`](.github/workflows/prepare-publication.yaml)
for the details.

The required pull-request check blocks publishing commits until the automation
commit becomes the branch tip. New posts are prepared automatically; modified
or renamed posts qualify only when their base or current version is a draft, so
already-published posts keep their original publication dates.

## Deployment

Deployed to Cloudflare Workers static assets, configured via `wrangler.toml`.
Cloudflare's Git integration builds and deploys automatically on every push to
`main` — no manual `wrangler deploy` step is needed.
