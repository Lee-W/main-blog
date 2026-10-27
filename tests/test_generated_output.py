import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import pytest
from bs4 import BeautifulSoup

import tasks
from tasks import (
    _add_hreflang_links,
    _canonicalize_cloudflare_url,
    _collapse_dot_segments,
    _normalize_sitemap,
    _preserve_atom_entry_ids,
)


def test_canonicalize_cloudflare_url_matches_static_asset_html_handling():
    assert _canonicalize_cloudflare_url("https://example.com/pages/about.html") == (
        "https://example.com/pages/about"
    )
    assert _canonicalize_cloudflare_url(
        "https://example.com/posts/example/index.html"
    ) == ("https://example.com/posts/example/")


@pytest.mark.parametrize(
    ("url", "expected"),
    [
        ("data:text/javascript,a/../b", "data:text/javascript,a/../b"),
        ("javascript:void('/../')", "javascript:void('/../')"),
        ("https://host/en/../static/a.css", "https://host/static/a.css"),
        ("/../theme/js/script.js", "/theme/js/script.js"),
        ("//host/en/../a.css", "//host/a.css"),
        ("https://host/a/../b.css?v=1#top", "https://host/b.css?v=1#top"),
        ("https://host/dir/", "https://host/dir/"),
        ("https://host/a/./b/", "https://host/a/b"),
    ],
)
def test_collapse_dot_segments(url, expected):
    assert _collapse_dot_segments(url) == expected


def test_add_hreflang_links_for_translated_page():
    soup = BeautifulSoup(
        """
        <html><head><link rel="canonical" href="https://example.com/pages/about.html"></head>
        <body><ul id="nav-language-menu">
          <li><a href="/pages/about.html">臺灣華語</a></li>
          <li><a href="/en/pages/about.html">English</a></li>
          <li><a href="/ja/pages/about.html">日本語</a></li>
        </ul></body></html>
        """,
        "html.parser",
    )

    assert _add_hreflang_links(soup)

    links = {
        link["hreflang"]: link["href"]
        for link in soup.select('link[rel="alternate"][hreflang]')
    }
    assert links == {
        "en": "https://example.com/en/pages/about.html",
        "ja": "https://example.com/ja/pages/about.html",
        "x-default": "https://example.com/pages/about.html",
        "zh-TW": "https://example.com/pages/about.html",
    }


def test_add_hreflang_links_ignores_language_home_fallback():
    soup = BeautifulSoup(
        """
        <html><head><link rel="canonical" href="https://example.com/posts/only-zh"></head>
        <body><ul id="nav-language-menu">
          <li><a href="/posts/only-zh">臺灣華語</a></li>
          <li><a href="/en/">English</a></li>
          <li><a href="/ja/">日本語</a></li>
        </ul></body></html>
        """,
        "html.parser",
    )

    assert not _add_hreflang_links(soup)
    assert not soup.select('link[rel="alternate"][hreflang]')


def test_add_hreflang_links_skips_pages_without_a_default_language_version():
    """English-only pages drop hreflang instead of pointing it at another language."""
    soup = BeautifulSoup(
        """
        <html><head><link rel="canonical" href="https://example.com/en/pages/cv.html"></head>
        <body><ul id="nav-language-menu">
          <li><a href="/">臺灣華語</a></li>
          <li><a href="/en/pages/cv.html">English</a></li>
          <li><a href="/ja/">日本語</a></li>
        </ul></body></html>
        """,
        "html.parser",
    )

    assert not _add_hreflang_links(soup)
    assert not soup.select('link[rel="alternate"][hreflang]')


def test_normalize_sitemap_adds_x_default_without_an_english_version(tmp_path):
    """x-default follows the HTML rule: any second translation is enough."""
    sitemap = tmp_path / "sitemap.xml"
    sitemap.write_text(
        """<?xml version="1.0" encoding="utf-8"?>
        <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
                xmlns:xhtml="http://www.w3.org/1999/xhtml">
          <url>
            <loc>https://example.com/pages/blogroll.html</loc>
            <xhtml:link rel="alternate" hreflang="zh-tw" href="https://example.com/pages/blogroll.html" />
            <xhtml:link rel="alternate" hreflang="ja" href="https://example.com/ja/pages/blogroll.html" />
          </url>
          <url>
            <loc>https://example.com/en/pages/cv.html</loc>
            <xhtml:link rel="alternate" hreflang="en" href="https://example.com/en/pages/cv.html" />
          </url>
        </urlset>
        """,
        encoding="utf-8",
    )

    _normalize_sitemap(sitemap)

    content = sitemap.read_text(encoding="utf-8")
    assert content.count('hreflang="x-default"') == 1
    assert (
        '<xhtml:link rel="alternate" hreflang="x-default" '
        'href="https://example.com/pages/blogroll" />' in content
    )


def test_normalize_sitemap_merges_translated_page_entries(tmp_path):
    sitemap = tmp_path / "sitemap.xml"
    sitemap.write_text(
        """<?xml version="1.0" encoding="utf-8"?>
        <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
                xmlns:xhtml="http://www.w3.org/1999/xhtml">
          <url>
            <loc>https://example.com/pages/about.html</loc>
            <xhtml:link rel="alternate" hreflang="zh-tw" ref="https://example.com/../pages/about.html" />
          </url>
          <url>
            <loc>https://example.com/pages/about.html</loc>
            <xhtml:link rel="alternate" hreflang="en" ref="https://example.com/en/pages/about.html" />
          </url>
        </urlset>
        """,
        encoding="utf-8",
    )

    assert _normalize_sitemap(sitemap) == 1

    root = ET.parse(sitemap).getroot()
    namespace = {
        "s": "http://www.sitemaps.org/schemas/sitemap/0.9",
        "x": "http://www.w3.org/1999/xhtml",
    }
    urls = root.findall("s:url", namespace)
    assert len(urls) == 1
    links = {
        link.get("hreflang"): link.get("href")
        for link in urls[0].findall("x:link", namespace)
    }
    assert links == {
        "en": "https://example.com/en/pages/about",
        "x-default": "https://example.com/pages/about",
        "zh-tw": "https://example.com/pages/about",
    }
    assert all(link.get("ref") is None for link in urls[0].findall("x:link", namespace))


def test_preserve_atom_entry_ids_removes_only_entry_id_trailing_slash(tmp_path):
    feed = tmp_path / "feeds" / "all.atom.xml"
    feed.parent.mkdir()
    feed.write_text(
        """<feed xmlns="http://www.w3.org/2005/Atom">
        <id>https://example.com/</id>
        <entry>
          <link href="https://example.com/posts/example/" />
          <id>tag:example.com,2026-07-10:/posts/example/</id>
        </entry>
        </feed>""",
        encoding="utf-8",
    )

    assert _preserve_atom_entry_ids(tmp_path) == 1
    content = feed.read_text(encoding="utf-8")
    assert '<link href="https://example.com/posts/example/" />' in content
    assert "<id>tag:example.com,2026-07-10:/posts/example</id>" in content
    assert "<id>https://example.com/</id>" in content


def test_japanese_article_links_resolve_to_main_site_in_local_build(
    tmp_path, monkeypatch
):
    article = tmp_path / "posts/example/index.html"
    article.parent.mkdir(parents=True)
    article.write_text(
        '<html lang="zh-tw"><head>'
        '<link rel="canonical" href="http://localhost:8000/posts/example/">'
        '<meta property="og:type" content="article"></head><body>Article</body></html>'
    )
    page = tmp_path / "ja/pages/blogroll.html"
    page.parent.mkdir(parents=True)
    page.write_text(
        '<html lang="ja"><head>'
        '<link rel="canonical" href="http://localhost:8000/ja/pages/blogroll">'
        '</head><body><a href="http://localhost:8000/ja/example-zh-tw.html">'
        "RSS</a></body></html>"
    )
    monkeypatch.setitem(tasks.CONFIG, "deploy_path", str(tmp_path))
    tasks._fix_internal_links()
    soup = BeautifulSoup(page.read_text(), "html.parser")
    assert soup.a["href"] == "http://localhost:8000/posts/example/"


def test_dead_listing_links_fall_back_to_their_own_subsite(tmp_path, monkeypatch):
    """A tag page that no subsite generated should not dump readers on another one."""
    page = tmp_path / "ja/pages/now.html"
    page.parent.mkdir(parents=True)
    page.write_text(
        '<html lang="ja"><head>'
        '<link rel="canonical" href="http://localhost:8000/ja/pages/now">'
        "</head><body>"
        '<a href="/ja/tag/missing.html">ja</a>'
        '<a href="/en/tag/missing.html">en</a>'
        '<a href="/tag/missing.html">zh-tw</a>'
        "</body></html>"
    )
    monkeypatch.setitem(tasks.CONFIG, "deploy_path", str(tmp_path))

    tasks._fix_internal_links()

    soup = BeautifulSoup(page.read_text(), "html.parser")
    assert [anchor["href"] for anchor in soup.find_all("a")] == ["/ja/", "/en/", "/"]


@pytest.fixture(scope="module")
def built_site(tmp_path_factory):
    """Build the real site once (local config) and run the post-build link pass."""
    output = tmp_path_factory.mktemp("site")
    subprocess.run(
        [sys.executable, "-m", "pelican", "-s", "pelicanconf.py", "-o", str(output)],
        cwd=Path(__file__).resolve().parents[1],
        check=True,
        capture_output=True,
    )
    with pytest.MonkeyPatch.context() as patch:
        patch.setitem(tasks.CONFIG, "deploy_path", str(output))
        tasks._fix_internal_links()
    return output


def test_built_pages_have_no_dot_dot_segments_in_asset_urls(built_site):
    """Subsite <link>/<script> URLs must not carry ``/../`` (e.g. ``/en/../static``)."""
    checked = {"zh-tw": 0, "en": 0}
    offenders = []
    for page in built_site.rglob("*.html"):
        soup = BeautifulSoup(page.read_text(encoding="utf-8"), "html.parser")
        urls = [link["href"] for link in soup.find_all("link", href=True)]
        urls += [script["src"] for script in soup.find_all("script", src=True)]
        offenders += [(page.name, url) for url in urls if "/../" in url]
        relative = page.relative_to(built_site).parts
        checked["en" if relative[0] == "en" else "zh-tw"] += 1
    # Guard against a vacuous pass: both languages must actually have been built.
    assert all(checked.values()), checked
    assert offenders == []
