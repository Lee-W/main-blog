# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

PATH = "content"

# Blog Conf
AUTHOR = "Lee-W"
SITENAME = "Laziness makes Great Engineer"
SITEURL = "http://localhost:8000"
SITETITLE = AUTHOR
SITELOGO = None
BROWSER_COLOR = "#333333"
LANDING_PAGE_TITLE = "Hi, I'm Wei Lee"
PROJECTS_TITLE = "Projects"
PROJECTS = [
    {
        "name": "Commitizen",
        "url": "https://github.com/commitizen-tools/commitizen",
        "description": "Python 3 command-line utility to standardize commit messages and bump version",
    }
]
DISQUS_SITENAME = "lee-w-blog"
DISQUS_FILTER = False
COMMENTS_INTRO = (
    "Do you like this article? What do your tink about it? Leave you comment below"
)
SITE_LICENSE = """
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/">
<img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" />
</a>
<br />
This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
"""

# Locale
TIMEZONE = "Asia/Taipei"
DEFAULT_LANG = "zh-tw"
DEFAULT_DATE_FORMAT = "%Y/%m/%d - %a"

# Page Setting
MAIN_MENU = True
DIRECT_TEMPLATES = ("index", "categories", "tags", "archives", "search")

# Content Setting
DEFAULT_CATEGORY = "Article"
ARTICLE_URL = "posts/{category}/{date:%Y}/{date:%m}/{slug}"
ARTICLE_SAVE_AS = "posts/{category}/{date:%Y}/{date:%m}/{slug}/index.html"
STATIC_PATHS = ["static", "images"]

# Theme Setting
THEME = "theme/elegant"
JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.i18n"]}
PYGMENTS_STYLE = "default"
APPLAUSE_BUTTON = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL_PROFILE_LABEL = "Keep In Touch"
SOCIAL = (
    ("Linkedin", "https://tw.linkedin.com/in/clleew"),
    ("GitHub", "https://github.com/Lee-W"),
    ("Gitlab", "https://gitlab.com/Lee-W"),
    ("Twitter", "https://twitter.com/clleew"),
    ("RSS", "https://lee-w.github.io/feeds/all.atom.xml"),
)

# Markdown extension
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.extra": {},
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.nl2br": {},
        "markdown.extensions.toc": {"toc_depth": "1-3"},
        "mdx_del_ins": {},
    },
    "output_format": "html5",
}

# Plugin-setting
PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = [
    "another_read_more_link",
    "share_post",
    "i18n_subsites",
    "tipue_search",
    "tag_cloud",
    "extract_toc",
    "post_stats",
    "assets",
    "series",
]
ANOTHER_READ_MORE_LINK = ""
READERS = {"html": None}
