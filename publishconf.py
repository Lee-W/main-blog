#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.


sys.path.append(os.curdir)
from pelicanconf import *  # noqa: F401, E402, F403

SITEURL = "https://blog.wei-lee.me"
RELATIVE_URLS = False

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

DELETE_OUTPUT_DIRECTORY = False

EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
}
PAGEFIND_ENABLED = True
# Following items are often useful when publishing
MODERN_GOOGLE_ANALYTICS = os.environ.get("GOOGLE_ANALYTICS")
