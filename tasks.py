import datetime
import glob
import hashlib
import os
import posixpath
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
import urllib.parse
import xml.etree.ElementTree as ET
from collections import defaultdict
from collections.abc import Sequence
from pathlib import Path
from string import Template
from urllib.parse import unquote, urlparse

from bs4 import BeautifulSoup
from invoke.exceptions import Exit
from invoke.main import program
from invoke.tasks import task
from pelican import main as pelican_main
from pelican.server import ComplexHTTPRequestHandler, RootedHTTPServer
from pelican.settings import DEFAULT_CONFIG, get_settings_from_file
from PIL.ExifTags import Base as ExifBase
from PIL.Image import Resampling, UnidentifiedImageError
from PIL.Image import open as pil_open

OPEN_BROWSER_ON_SERVE = True
SETTINGS_FILE_BASE = "pelicanconf.py"
SETTINGS = {}
SETTINGS.update(DEFAULT_CONFIG)
LOCAL_SETTINGS = get_settings_from_file(SETTINGS_FILE_BASE)
SETTINGS.update(LOCAL_SETTINGS)

CONFIG = {
    "settings_base": SETTINGS_FILE_BASE,
    "settings_publish": "publishconf.py",
    # Output path. Can be absolute or relative to tasks.py. Default: 'output'
    "deploy_path": SETTINGS["OUTPUT_PATH"],
    # Host and port for `serve`
    "host": "localhost",
    "port": 8000,
}


def _build_pagefind():
    subprocess.run(
        ["uv", "run", "python", "-m", "pagefind", "--site", "output"],
        check=True,
    )


def _find_output_target(output_root: Path, page: Path, href: str) -> Path | None:
    parsed = urlparse(href)
    if parsed.netloc and parsed.netloc != SETTINGS["HOST"]:
        return None
    if parsed.scheme in {"mailto", "tel", "javascript"} or not parsed.path:
        return None

    if parsed.path.startswith("/"):
        target = output_root / unquote(parsed.path.lstrip("/"))
    else:
        target = page.parent / unquote(parsed.path)
    candidates = [target / "index.html"] if target.is_dir() else [target]
    if not target.suffix:
        candidates.extend((target / "index.html", target.with_suffix(".html")))
    return next(
        (candidate.resolve() for candidate in candidates if candidate.is_file()), None
    )


def _cloudflare_route_for_file(output_root: Path, target: Path) -> str:
    relative = target.resolve().relative_to(output_root.resolve())
    if relative.name == "index.html":
        parent = relative.parent.as_posix()
        return "/" if parent == "." else f"/{parent}/"
    if relative.suffix == ".html":
        return f"/{relative.with_suffix('').as_posix()}"
    return f"/{relative.as_posix()}"


def _canonicalize_cloudflare_url(url: str) -> str:
    parsed = urllib.parse.urlsplit(url)
    path = posixpath.normpath(parsed.path)
    if parsed.path.endswith("/") and not path.endswith("/"):
        path += "/"
    if path.endswith("/index.html"):
        path = path[: -len("index.html")]
    elif path.endswith(".html"):
        path = path[: -len(".html")]
    return urllib.parse.urlunsplit(parsed._replace(path=path))


def _add_hreflang_links(soup: BeautifulSoup) -> bool:
    """Add alternate-language metadata for pages with real translations."""
    canonical = soup.select_one('link[rel="canonical"][href]')
    language_menu = soup.select_one("#nav-language-menu")
    if canonical is None or language_menu is None or soup.head is None:
        return False

    canonical_url = canonical["href"]
    canonical_path = urlparse(canonical_url).path
    site_root = urllib.parse.urljoin(canonical_url, "/")
    alternates: dict[str, str] = {}
    for anchor in language_menu.find_all("a", href=True):
        path = urlparse(anchor["href"]).path
        # The language picker falls back to a subsite's home page when no
        # translation exists. Do not advertise that fallback as a translation.
        if path in {"/", "/en/"} and canonical_path not in {"/", "/en/"}:
            continue
        lang = "en" if path.startswith("/en/") or path == "/en/" else "zh-TW"
        alternates[lang] = urllib.parse.urljoin(site_root, path)

    if len(alternates) < 2:
        return False

    for old_link in soup.select('link[rel="alternate"][hreflang]'):
        old_link.decompose()
    for lang, href in sorted(alternates.items()):
        soup.head.append(
            soup.new_tag("link", rel="alternate", hreflang=lang, href=href)
        )
    soup.head.append(
        soup.new_tag(
            "link",
            rel="alternate",
            hreflang="x-default",
            href=alternates["zh-TW"],
        )
    )
    return True


def _normalize_absolute_url(url: str) -> str:
    return _canonicalize_cloudflare_url(url)


def _normalize_sitemap(path: Path) -> int:
    """Fix translated URLs and merge duplicate sitemap entries."""
    if not path.exists():
        return 0

    sitemap_namespace = "http://www.sitemaps.org/schemas/sitemap/0.9"
    xhtml_namespace = "http://www.w3.org/1999/xhtml"
    ET.register_namespace("", sitemap_namespace)
    ET.register_namespace("xhtml", xhtml_namespace)
    tree = ET.parse(path)
    root = tree.getroot()
    loc_tag = f"{{{sitemap_namespace}}}loc"
    alternate_tag = f"{{{xhtml_namespace}}}link"
    seen: dict[str, ET.Element] = {}
    duplicates = 0

    for url_element in list(root):
        loc = url_element.find(loc_tag)
        if loc is None or not loc.text:
            continue
        loc.text = _normalize_absolute_url(loc.text)

        for alternate in url_element.findall(alternate_tag):
            href = alternate.attrib.pop("ref", None) or alternate.get("href")
            if href:
                href = _normalize_absolute_url(href)
                alternate.set("href", href)

        if loc.text in seen:
            target = seen[loc.text]
            existing_languages = {
                link.get("hreflang") for link in target.findall(alternate_tag)
            }
            for alternate in url_element.findall(alternate_tag):
                if alternate.get("hreflang") not in existing_languages:
                    target.append(alternate)
            root.remove(url_element)
            duplicates += 1
            continue

        seen[loc.text] = url_element

    for url_element in root:
        alternate_links = url_element.findall(alternate_tag)
        by_language = {link.get("hreflang"): link for link in alternate_links}
        if "zh-tw" in by_language and "en" in by_language:
            default_link = ET.Element(
                alternate_tag,
                {
                    "rel": "alternate",
                    "hreflang": "x-default",
                    "href": by_language["zh-tw"].get("href", ""),
                },
            )
            url_element.append(default_link)

    tree.write(path, encoding="utf-8", xml_declaration=True)
    return duplicates


def _preserve_atom_entry_ids(output_root: Path) -> int:
    """Keep legacy Atom IDs while canonical article links gain a trailing slash."""
    pattern = re.compile(r"(<id>tag:[^<]+?)/</id>")
    updated = 0
    for feed_path in output_root.rglob("*.atom.xml"):
        content = feed_path.read_text(encoding="utf-8")
        content, count = pattern.subn(r"\1</id>", content)
        if count:
            feed_path.write_text(content, encoding="utf-8")
            updated += count
    return updated


def _fix_internal_links() -> None:
    """Normalize generated links for i18n and Cloudflare Static Assets."""
    output_root = Path(CONFIG["deploy_path"]).resolve()
    pages = list(output_root.rglob("*.html"))
    legacy_routes: dict[str, str] = {}

    for page in pages:
        soup = BeautifulSoup(page.read_text(encoding="utf-8"), "html.parser")
        language = soup.html.get("lang") if soup.html else None
        canonical = soup.select_one('link[rel="canonical"]')
        if not language or canonical is None or not canonical.get("href"):
            continue
        route = urlparse(canonical["href"]).path
        slug = Path(route.rstrip("/")).name
        if not slug:
            continue

        is_article = soup.select_one('meta[property="og:type"][content="article"]')
        if is_article:
            legacy_routes[f"/{slug}-{language}.html"] = route
            legacy_routes[f"/en/{slug}-{language}.html"] = route
        elif "/pages/" in route:
            legacy_routes[f"/pages/{slug}-{language}.html"] = route
            legacy_routes[f"/en/pages/{slug}-{language}.html"] = route

    fixed = 0
    hreflang_pages = 0
    for page in pages:
        html = page.read_text(encoding="utf-8")
        soup = BeautifulSoup(html, "html.parser")
        changed = False
        for anchor in soup.find_all("a", href=True):
            href = anchor["href"]
            parsed = urlparse(href)
            if (
                parsed.netloc
                and parsed.netloc != SETTINGS["HOST"]
                or parsed.scheme in {"mailto", "tel", "javascript"}
                or not parsed.path
            ):
                continue
            target = _find_output_target(output_root, page, href)
            if target is not None:
                replacement = _cloudflare_route_for_file(output_root, target)
                if replacement != parsed.path:
                    anchor["href"] = parsed._replace(path=replacement).geturl()
                    changed = True
                    fixed += 1
                continue
            replacement = legacy_routes.get(parsed.path)
            if replacement is None and anchor.get("data-fallback"):
                replacement = anchor["data-fallback"]
            if replacement is None and "/../" in parsed.path:
                replacement = posixpath.normpath(parsed.path)
            if replacement is None and (
                "/tag/" in parsed.path
                or "/category/" in parsed.path
                or "/author/" in parsed.path
            ):
                replacement = "/en/" if parsed.path.startswith("/en/") else "/"
            if replacement is None:
                continue
            replacement_target = _find_output_target(
                output_root,
                page,
                parsed._replace(path=replacement).geturl(),
            )
            if replacement_target is not None:
                replacement = _cloudflare_route_for_file(
                    output_root, replacement_target
                )
            anchor["href"] = parsed._replace(path=replacement).geturl()
            changed = True
            fixed += 1
        if _add_hreflang_links(soup):
            changed = True
            hreflang_pages += 1
        if changed:
            page.write_text(str(soup), encoding="utf-8")
    sitemap_duplicates = _normalize_sitemap(output_root / "sitemap.xml")
    preserved_feed_ids = _preserve_atom_entry_ids(output_root)
    print(
        f"Fixed {fixed} generated internal link(s); "
        f"added hreflang to {hreflang_pages} page(s); "
        f"removed {sitemap_duplicates} duplicate sitemap URL(s); "
        f"preserved {preserved_feed_ids} Atom entry ID(s)"
    )


@task
def clean(c):
    """Remove generated files"""
    if os.path.isdir(CONFIG["deploy_path"]):
        shutil.rmtree(CONFIG["deploy_path"])
        os.makedirs(CONFIG["deploy_path"])


@task(optional=["--build-pagefind"])
def build(c, build_pagefind=False):
    """Build local version of site"""
    pelican_run("-s {settings_base}".format(**CONFIG))
    _fix_internal_links()
    if build_pagefind:
        _build_pagefind()


@task(optional=["--build-pagefind"])
def rebuild(c, build_pagefind=False):
    """`build` with the delete switch"""
    pelican_run("-d -s {settings_base}".format(**CONFIG))
    _fix_internal_links()
    if build_pagefind:
        _build_pagefind()


@task
def regenerate(c):
    """Automatically regenerate site upon file modification"""
    pelican_run("-r -s {settings_base}".format(**CONFIG))


@task
def serve(c):
    """Serve site at http://$HOST:$PORT/ (default is localhost:8000)"""

    class AddressReuseTCPServer(RootedHTTPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(
        CONFIG["deploy_path"],
        (CONFIG["host"], CONFIG["port"]),
        ComplexHTTPRequestHandler,
    )

    if OPEN_BROWSER_ON_SERVE:
        # Open site in default browser
        import webbrowser

        webbrowser.open("http://{host}:{port}".format(**CONFIG))

    sys.stderr.write("Serving at {host}:{port} ...\n".format(**CONFIG))
    server.serve_forever()


@task
def reserve(c):
    """`build`, then `serve`"""
    build(c, build_pagefind=False)
    serve(c)


@task
def preview(c):
    """Build production version of site"""
    pelican_run("-s {settings_publish}".format(**CONFIG))
    _fix_internal_links()
    _build_pagefind()


@task
def livereload(c):
    """Automatically reload browser tab upon file modification."""
    from livereload import Server

    def cached_build():
        cmd = "-s {settings_base} -e CACHE_CONTENT=true LOAD_CONTENT_CACHE=true"
        pelican_run(cmd.format(**CONFIG))

    cached_build()
    server = Server()
    theme_path = SETTINGS["THEME"]
    watched_globs = [
        CONFIG["settings_base"],
        "{}/templates/**/*.html".format(theme_path),
    ]

    content_file_extensions = [".md", ".rst"]
    for extension in content_file_extensions:
        content_glob = "{0}/**/*{1}".format(SETTINGS["PATH"], extension)
        watched_globs.append(content_glob)

    static_file_extensions = [".css", ".js"]
    for extension in static_file_extensions:
        static_file_glob = "{0}/static/**/*{1}".format(theme_path, extension)
        watched_globs.append(static_file_glob)

    for g in watched_globs:
        server.watch(g, cached_build)

    if OPEN_BROWSER_ON_SERVE:
        # Open site in default browser
        import webbrowser

        webbrowser.open("http://{host}:{port}".format(**CONFIG))

    server.serve(host=CONFIG["host"], port=CONFIG["port"], root=CONFIG["deploy_path"])


@task
def build_publish(c):
    """Build pages with publishconf.py"""
    pelican_run("-s {settings_publish}".format(**CONFIG))
    _fix_internal_links()
    _build_pagefind()


def pelican_run(cmd):
    cmd += " " + program.core.remainder  # allows to pass-through args to pelican
    pelican_main(shlex.split(cmd))


@task(optional=["rev_range"])
def style(c, rev_range="origin/main.."):
    """Run style check on python code"""
    python_targets = "pelicanconf.py publishconf.py tasks.py scripts plugins"
    c.run(f"uv run ruff check {python_targets}")

    commit_count = subprocess.run(
        ["git", "rev-list", "--count", rev_range],
        check=False,
        capture_output=True,
        text=True,
    )
    if commit_count.returncode != 0:
        print(f"Skipping commit style check: invalid rev range {rev_range!r}")
        return

    if commit_count.stdout.strip() == "0":
        print(f"Skipping commit style check: no commits in {rev_range!r}")
        return

    c.run(f"uv run cz check --rev-range {shlex.quote(rev_range)}")


@task
def format(c):
    """Run autoformater on python code"""
    python_targets = "pelicanconf.py publishconf.py tasks.py scripts plugins"
    c.run(
        f"""
        uv run ruff format {python_targets} && \
        uv run ruff check {python_targets} --fix
        """
    )


@task
def security_check(c):
    """Run pip-audit on dependencies"""
    # CVE-2026-4539 ignored since 2026-06-12. Re-check with
    # `uv run pip-audit -r requirements.txt` (no --ignore-vuln) whether a fix
    # has shipped upstream before renewing this ignore.

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".txt", delete=False
    ) as requirements_file:
        requirements_path = requirements_file.name

    try:
        c.run(f"uv pip compile pyproject.toml -o {shlex.quote(requirements_path)}")
        c.run(
            f"uv run pip-audit -r {shlex.quote(requirements_path)} "
            "--ignore-vuln CVE-2026-4539"
        )
    finally:
        Path(requirements_path).unlink(missing_ok=True)


@task
def check_content(c):
    """Run local content quality checks."""
    post_files = sorted(str(path) for path in Path("content/posts").rglob("*.md"))
    metadata_check = subprocess.run(
        [
            sys.executable,
            "scripts/check_post_metadata.py",
            "--categories",
            "Tech,Random Thoughts,Book",
            *post_files,
        ],
        check=False,
    )
    if metadata_check.returncode != 0:
        raise Exit(metadata_check.returncode)

    check_image_usage(c)


def _create_post_from_template(
    template_name: str,
    title: str,
    category: str,
    slug: str = "",
    extra: dict | None = None,
) -> None:
    now = datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8)))
    date_str = now.strftime("%Y-%m-%d %H:%M +0800")
    year = now.strftime("%Y")

    if not slug:
        slug = re.sub(r"[^\w\s-]", "", title.lower())
        slug = re.sub(r"[\s_]+", "-", slug).strip("-") or title

    category_dir = Path("content/posts") / category.lower().replace(" ", "-") / year
    category_dir.mkdir(parents=True, exist_ok=True)

    numbers = []
    pad_width = 0
    for f in category_dir.glob("*.md"):
        m = re.match(r"^(\d+)-", f.name)
        if m:
            num_str = m.group(1)
            numbers.append(int(num_str))
            if num_str.startswith("0"):
                pad_width = len(num_str)

    n = max(numbers, default=0) + 1
    n_str = str(n).zfill(pad_width) if pad_width else str(n)

    template = Template((Path("templates") / template_name).read_text())
    content = template.substitute(
        title=title, date=date_str, category=category, slug=slug, **(extra or {})
    )

    filepath = category_dir / f"{n_str}-{slug}.md"
    filepath.write_text(content)
    print(f"Created: {filepath}")


@task
def new_post(c, title, category, slug="", lang="zh-tw"):
    """Create a new post file from template"""
    _create_post_from_template("post.md", title, category, slug, {"lang": lang})


@task
def new_draft(c, title, category, slug="", lang="zh-tw"):
    """Create a new draft file from template"""
    _create_post_from_template("draft.md", title, category, slug, {"lang": lang})


@task
def new_open_source_report(c, start, end):
    """Create a new 開源貢獻週報 post (--start YYYY-MM-DD --end YYYY-MM-DD)"""
    start_dt = datetime.datetime.strptime(start, "%Y-%m-%d")
    end_dt = datetime.datetime.strptime(end, "%Y-%m-%d")
    title = f"{start_dt.strftime('%Y/%m/%d')} - {end_dt.strftime('%m/%d')} 開源貢獻週報"
    slug = (
        f"{start_dt.strftime('%Y-%m-%d')}-{end_dt.strftime('%m-%d')}-open-source-report"
    )
    _create_post_from_template("open-source-report.md", title, "Tech", slug)


@task
def new_airflow_report(c, title, slug=""):
    """Create a new Airflow 開發生情報 post"""
    _create_post_from_template("airflow-report.md", title, "Tech", slug)


def _dhash(path: Path, hash_size: int = 8) -> int | None:
    """Perceptual difference-hash of an image (None if it can't be opened)."""
    try:
        with pil_open(path) as im:
            small = im.convert("L").resize(
                (hash_size + 1, hash_size), Resampling.LANCZOS
            )
    except UnidentifiedImageError, OSError, ValueError:
        return None
    pixels = list(small.getdata())
    bits = 0
    for row in range(hash_size):
        for col in range(hash_size):
            left = pixels[row * (hash_size + 1) + col]
            right = pixels[row * (hash_size + 1) + col + 1]
            bits = (bits << 1) | int(left > right)
    return bits


@task
def check_image_usage(_) -> None:
    """Report orphan, cross-article reused, and duplicate-content images."""

    ref_patterns = [
        re.compile(r"\]\(\s*(/images/[^)]+?)\s*\)"),
        re.compile(r"src=[\"'](/images/[^\"']+)[\"']"),
        re.compile(r"^(?:Cover|Image):\s*(/images/\S+)", re.M),
    ]
    refs: dict[str, set[str]] = defaultdict(set)
    for md in Path("content").rglob("*.md"):
        if "posts" not in md.parts and "pages" not in md.parts:
            continue
        text = md.read_text()
        for pattern in ref_patterns:
            for match in pattern.findall(text):
                refs[urllib.parse.unquote(match.strip())].add(str(md))

    config_used = {"/images/avatar.jpeg", "/images/cover.jpeg"}
    disk = {
        f"/{path.relative_to('content')}": path
        for path in Path("content/images").rglob("*")
        if path.is_file() and path.name != ".DS_Store"
    }

    orphans = sorted(
        (path.stat().st_size, url)
        for url, path in disk.items()
        if url not in refs and url not in config_used
    )
    print(f"=== Orphan images: {len(orphans)} ===")
    for size, url in reversed(orphans):
        print(f"  {size / 1024 / 1024:6.2f} MB  {url}")

    reused = {
        url: files
        for url, files in refs.items()
        if len(files) > 1 and url in disk and "/meme/" not in url
    }
    print(f"\n=== Reused across articles (outside /images/meme/): {len(reused)} ===")
    print("    (referencing the original post folder is fine;")
    print("     consider moving to /images/meme/ only if it is a meme)")
    for url, files in sorted(reused.items()):
        print(f"  {url}")
        for f in sorted(files):
            print(f"      {f}")

    by_digest: dict[str, list[str]] = defaultdict(list)
    digest_by_url: dict[str, str] = {}
    for url, path in disk.items():
        digest = hashlib.md5(path.read_bytes()).hexdigest()
        by_digest[digest].append(url)
        digest_by_url[url] = digest
    duplicates = [sorted(urls) for urls in by_digest.values() if len(urls) > 1]
    print(f"\n=== Identical file contents: {len(duplicates)} group(s) ===")
    for urls in sorted(duplicates):
        print("  " + " == ".join(urls))

    # Near-duplicates: visually similar but not byte-identical (re-compressed,
    # resized, or EXIF-stripped copies that md5 alone cannot catch).
    near_dup_threshold = 5
    hashes = [(url, h) for url in disk if (h := _dhash(disk[url])) is not None]
    near_dups = []
    for i, (url_a, hash_a) in enumerate(hashes):
        for url_b, hash_b in hashes[i + 1 :]:
            if digest_by_url[url_a] == digest_by_url[url_b]:
                continue  # already reported above as identical contents
            distance = (hash_a ^ hash_b).bit_count()
            if distance <= near_dup_threshold:
                near_dups.append((distance, url_a, url_b))
    near_dups.sort()
    print(
        f"\n=== Near-duplicate images "
        f"(perceptual, Hamming <= {near_dup_threshold}): {len(near_dups)} pair(s) ==="
    )
    for distance, url_a, url_b in near_dups:
        print(f"  d={distance}  {url_a}  ~~  {url_b}")

    dead = sorted(url for url in refs if url not in disk)
    print(f"\n=== Referenced but missing on disk: {len(dead)} ===")
    for url in dead:
        print(f"  {url}")
        for f in sorted(refs[url]):
            print(f"      {f}")


def _get_exif_tag_ids_by_names(names: Sequence[str]) -> set[int]:
    return {getattr(ExifBase, name).value for name in names}


@task
def check_and_remove_image_exif_gps_info(_) -> None:
    """Check and remove GPSInfo from image EXIF if exists."""
    filenames = [
        path
        for path in glob.glob("content/images/**", recursive=True)
        if os.path.isfile(path)
    ]
    exif_tags_to_remove = ["GPSInfo"]
    for name in filenames:
        try:
            with pil_open(name) as im:
                exif = im.getexif()
                tag_ids = _get_exif_tag_ids_by_names(exif_tags_to_remove)
                file_changed = False
                for tag_id in tag_ids:
                    if tag_id in exif:
                        file_changed = True
                        del exif[tag_id]

                if file_changed:
                    im.save(name, exif=exif)
        except FileNotFoundError, UnidentifiedImageError:
            continue
