import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *
from pelicanconf import HOST, I18N_SUBSITES, LANGUAGES

SITEURL = f"https://{HOST}"
STATIC_SITEURL = SITEURL
RELATIVE_URLS = False

FEED_MAX_ITEMS = 30
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
# Each subsite serves its feeds from its own language root, so the Atom
# self-links have to point there instead of the default site root.
for _language, _language_root in LANGUAGES:
    if _language in I18N_SUBSITES:
        I18N_SUBSITES[_language]["FEED_DOMAIN"] = (
            f"{SITEURL}{_language_root.rstrip('/')}"
        )

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
