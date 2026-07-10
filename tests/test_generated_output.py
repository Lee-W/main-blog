import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup

from tasks import (
    _add_hreflang_links,
    _canonicalize_cloudflare_url,
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


def test_add_hreflang_links_for_translated_page():
    soup = BeautifulSoup(
        """
        <html><head><link rel="canonical" href="https://example.com/pages/about.html"></head>
        <body><ul id="nav-language-menu">
          <li><a href="/pages/about.html">台灣漢語</a></li>
          <li><a href="/en/pages/about.html">English</a></li>
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
        "x-default": "https://example.com/pages/about.html",
        "zh-TW": "https://example.com/pages/about.html",
    }


def test_add_hreflang_links_ignores_language_home_fallback():
    soup = BeautifulSoup(
        """
        <html><head><link rel="canonical" href="https://example.com/posts/only-zh"></head>
        <body><ul id="nav-language-menu">
          <li><a href="/posts/only-zh">台灣漢語</a></li>
          <li><a href="/en/">English</a></li>
        </ul></body></html>
        """,
        "html.parser",
    )

    assert not _add_hreflang_links(soup)
    assert not soup.select('link[rel="alternate"][hreflang]')


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
