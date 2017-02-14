#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

HOME = os.path.expanduser("~")


PATH = 'content'

# Config
THEME = os.path.join(HOME, "pelican-themes/flex/")
DISQUS_SITENAME = "lee-w-blog"

TIMEZONE = 'Asia/Taipei'
DEFAULT_LANG = 'zh'

AUTHOR = 'Lee-W'
SITENAME = 'Life Lies in Traveling'
SITEURL = 'http://localhost:8000'
SITETITLE = AUTHOR
SITELOGO = '//s.gravatar.com/avatar/3e049ed33195d00a8b745b16c63dce6e?s=120'
BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'monokai'
MAIN_MENU = True

MENUITEMS = (
    ('Archives', '/archives.html'),
    ('Categories', '/categories.html'),
    ('Tags', '/tags.html'),
)

DATE_FORMATS = {
    'zh': '%Y/%m/%d - %a',
}

# Feed generation is usually not desired when developing

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (('linkedin', 'http://tw.linkedin.com/in/clleew'),
          ('github', 'http://github.com/Lee-W'),
          ('facebook', 'http://www.facebook.com/clleew'),
          ('google', 'http://plus.google.com/113295124327840065090'),)

DEFAULT_PAGINATION = 10

ARTICLE_URL = 'posts/{category}/{date:%Y}/{date:%m}/{slug}'
ARTICLE_SAVE_AS = 'posts/{category}/{date:%Y}/{date:%m}/{slug}/index.html'

# Markdown extension
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.extra': {},
        'markdown.extensions.codehilite': {},
        'markdown.extensions.nl2br': {},
    },
    'output_format': 'html5'
}

# Plugin-setting
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['another_read_more_link']
ANOTHER_READ_MORE_LINK = ""
