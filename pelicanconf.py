# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from functools import partial


PATH = 'content'

# Blog Conf
AUTHOR = 'Lee-W'
SITENAME = 'Laziness makes Great Engineer'
SITEURL = 'http://localhost:8000'
SITETITLE = AUTHOR
SITELOGO = None
TIMEZONE = 'Asia/Taipei'
DEFAULT_LANG = 'zh-tw'
DEFAULT_CATEGORY = 'Article'
BROWSER_COLOR = '#333333'
DISQUS_SITENAME = "lee-w-blog"
MAIN_MENU = True

MENUITEMS = (
    ('Archives', '/archives.html'),
    ('Categories', '/categories.html'),
)

DATE_FORMATS = {
    'zh': '%Y/%m/%d - %a',
}

TYPOGRIFY = False
ARTICLE_URL = 'posts/{category}/{date:%Y}/{date:%m}/{slug}'
ARTICLE_SAVE_AS = 'posts/{category}/{date:%Y}/{date:%m}/{slug}/index.html'
DEFAULT_PAGINATION = 10

STATIC_PATHS = ['extra', 'images', 'static']

# Theme Setting
THEME = 'theme/pelican-themes/pelican-bootstrap3/'
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}
DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'search')
DISPLAY_TAG_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_SERIES_ON_SIDEBAR = True
DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE = True
SHOW_SERIES = True
SHOW_ARTICLE_CATEGORY = True
EXTRA_PATH_METADATA = {
    'images': {'path': 'images'},
}
CSS_OVERRIDE = '/static/custom.css'
PYGMENTS_STYLE = 'default'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (('Linkedin', 'http://tw.linkedin.com/in/clleew'),
          ('GitHub', 'http://github.com/Lee-W'),
          ('Gitlab', 'https://gitlab.com/Lee-W'),
          ('Facebook', 'http://www.facebook.com/clleew'),
          ('RSS', '//lee-w.github.io/feeds/all.atom.xml'),)


# Markdown extension
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.extra': {},
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.nl2br': {},
        'del_ins': {},
        'toc': {},
    },
    'output_format': 'html5'
}

# Plugin-setting
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = [
    'another_read_more_link', 'series', 'render_math',
    'neighbors', 'share_post', 'i18n_subsites', 'tipue_search', 'tag_cloud',
    'extract_toc'
]
ANOTHER_READ_MORE_LINK = ''

# Custom Jinja Filters
JINJA_FILTERS = {
    'sort_by_article_count': partial(
        sorted,
        key=lambda x: len(x[1]),
        reverse=True
    )
}
