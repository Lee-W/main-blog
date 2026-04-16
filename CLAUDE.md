# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a personal blog built with [Pelican](https://getpelican.com/) (Python static site generator), using a customized [Attila](https://github.com/Lee-W/attila) theme. Content is written in Markdown. The site is deployed to Cloudflare Pages via `wrangler.toml`.

## Common Commands

All tasks are run via `invoke` (using `uv run`):

```bash
uv run inv build           # Build local version of site
uv run inv rebuild         # Build with delete switch (clean build)
uv run inv serve           # Serve site at localhost:8000
uv run inv reserve         # Build then serve
uv run inv livereload      # Build and serve with live reload on file changes
uv run inv clean           # Remove generated files in output/
uv run inv preview         # Build production version (uses publishconf.py)
uv run inv style           # Run ruff linting + commitizen commit style check
uv run inv format          # Auto-fix ruff lint issues
uv run inv security_check  # Run pip-audit on dependencies
uv run inv check_and_remove_image_exif_gps_info  # Strip GPS EXIF from images
```

Build with pagefind search index:

```bash
uv run inv build --build-pagefind
```

## Architecture

### Configuration

- `pelicanconf.py` — development config (SITEURL is `localhost:8000`, feeds disabled)
- `publishconf.py` — production config (extends pelicanconf, enables feeds, reads `GOOGLE_ANALYTICS` and `UMAMI_WEBSITE_ID` env vars)
- `tasks.py` — all invoke task definitions

### Content Structure

```text
content/
  posts/
    tech/          # Tech articles
    random-thoughts/  # Personal/lifestyle posts
    book/          # Book digests
  pages/           # Static pages (about, etc.)
  images/          # Post images
  static/          # Static files excluded from article processing
  extra/           # Extra files like CNAME
  places/          # OSM/map data
```

Posts are organized by category then year (e.g., `content/posts/tech/2026/`). Filenames are prefixed with a sequential number (e.g., `14-apache-airflow-3-2-0.md`).

### Post Metadata

Each post uses Pelican metadata headers:

```markdown
Title: Post Title
Date: 2026-01-01 12:00 +0800
Category: Tech
Tags: tag1, tag2
Slug: post-slug
Authors: Wei Lee
Series: Series Name  # optional
Cover: /images/posts-image/...  # optional
Lang: en  # optional, defaults to zh-tw
```

The `<!--more-->` marker defines the article summary cutoff.

### Plugins

Key plugins configured in `pelicanconf.py`:
- `pelican.plugins.i18n_subsites` — bilingual site support (zh-tw default, en subsite)
- `pelican.plugins.series` — groups posts into series
- `pelican.plugins.webassets` — CSS/JS asset bundling
- `pelican.plugins.seo` — SEO report and enhancer
- `pelican.plugins.deadlinks` — dead link validation (disabled by default)
- `pagefind` — client-side search (must be built separately with `--build-pagefind`)

### Commit Convention

Uses commitizen with custom types. Valid commit prefixes:
`new post`, `post update`, `new draft`, `draft update`, `post metadata`, `typo`, `config`, `theme`, `dependency`, `static page`

Format: `<type>: <message>`

Run `uv run cz commit` for interactive commit, or `uv run cz check` to validate.
