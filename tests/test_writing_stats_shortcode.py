"""Integration tests for the pelican-stat writing-stats shortcode."""

from pathlib import Path

import pytest
from pelican import Pelican
from pelican.settings import read_settings

REPO_ROOT = Path(__file__).resolve().parent.parent
PELICANCONF_PATH = REPO_ROOT / "pelicanconf.py"

SHORTCODE_LITERAL = "{% writing_stats %}"
WIDGET_MARKER = '<div class="pelican-stat-widget">'


@pytest.fixture(scope="session")
def writing_stats_output_dir(tmp_path_factory):
    """Build the localized pages once in a temporary output directory."""
    output_path = tmp_path_factory.mktemp("writing_stats_shortcode_output")
    settings = read_settings(
        path=str(PELICANCONF_PATH),
        override={
            "OUTPUT_PATH": str(output_path),
            "ARTICLE_PATHS": [],
            "STATIC_PATHS": [],
        },
    )
    Pelican(settings).run()
    return output_path


@pytest.mark.parametrize(
    "relative_html_path",
    ["pages/about-me.html", "en/pages/about-me.html"],
)
def test_writing_stats_shortcode_is_substituted(
    writing_stats_output_dir, relative_html_path
):
    html_path = writing_stats_output_dir / relative_html_path
    assert html_path.exists(), f"expected build output at {html_path}"
    html = html_path.read_text(encoding="utf-8")

    assert SHORTCODE_LITERAL not in html
    assert WIDGET_MARKER in html
