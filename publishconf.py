import os
import sys

from pelican.plugins.i18n_feeds import feed_settings

sys.path.append(os.curdir)
from pelicanconf import *
from pelicanconf import HOST, I18N_SUBSITES, LANGUAGE_NAMES, SITENAME, SOCIAL

SITEURL = f"https://{HOST}"
STATIC_SITEURL = SITEURL
RELATIVE_URLS = False

FEED_MAX_ITEMS = 30
# feeds/ holds every language (pelican-i18n-feeds); each site's own language
# lives under its language prefix (zh-tw/feeds/, en/feeds/, ja/feeds/). The
# helper also fixes each subsite's FEED_DOMAIN (so the Atom self-links carry
# the /<lang>/ prefix), sets attila's <head> feed link titles and points each
# site's RSS icon at its own language feed.
globals().update(
    feed_settings(
        siteurl=SITEURL,
        sitename=SITENAME,
        default_lang=DEFAULT_LANG,
        subsites=I18N_SUBSITES,
        language_names=LANGUAGE_NAMES,
        all_languages_labels={
            "zh-tw": "全部語言 / All languages",
            "ja": "すべての言語 / All languages",
            "en": "All languages",
        },
        social=SOCIAL,
    )
)
# Feeds under /zh-tw/ get their own URL as <id>; feeds/, en/feeds/ and
# ja/feeds/ keep Pelican's id, because subscribers already hold those URLs.
I18N_FEEDS_URL_AS_ID = True
I18N_FEEDS_KEEP_ID_PREFIXES = ["feeds/", "en/feeds/", "ja/feeds/"]

DELETE_OUTPUT_DIRECTORY = True
DRAFT_SAVE_AS = ""
DRAFT_URL = ""
DRAFT_LANG_SAVE_AS = ""
DRAFT_LANG_URL = ""
DRAFT_PAGE_SAVE_AS = ""
DRAFT_PAGE_URL = ""
DRAFT_PAGE_LANG_SAVE_AS = ""
DRAFT_PAGE_LANG_URL = ""

UMAMI_WEBSITE_ID = os.environ.get("UMAMI_WEBSITE_ID")
