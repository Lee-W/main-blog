# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

PATH = "content"

# Blog Conf
AUTHOR = "Wei lee"
SITENAME = "Those aren't written down are meant to be forgotten"
SITETITLE = SITENAME
SITEURL = "http://localhost:8000"
SITELOGO = None
BROWSER_COLOR = "#333333"
DEFAULT_DATE_FORMAT = "%Y/%m/%d - %a"

# Locale
TIMEZONE = "Asia/Taipei"
DEFAULT_LANG = "zh-tw"
OG_LOCALE = "zh-tw"

# utterance (comment system)
UTTERANCES_REPO = "Lee-W/main-blog"
UTTERANCES_LABEL = "comment"
COMMENTS_INTRO = (
    "Do you like this article? What do your tink about it? Leave you comment below"
)

# license
SITE_LICENSE = """
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/">
    <img
        alt="Creative Commons License"
        style="border-width:0"
        src="https://i.creativecommons.org/l/by/4.0/88x31.png"
    />
</a>
<br />
This work is licensed under a
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/">
    Creative Commons Attribution 4.0 International License
</a>.
"""

# Page Setting
MAIN_MENU = True
DIRECT_TEMPLATES = ("index", "categories", "tags", "archives", "search")

# Content Setting
DEFAULT_CATEGORY = "Article"
ARTICLE_URL = "posts/{category}/{date:%Y}/{date:%m}/{slug}"
ARTICLE_SAVE_AS = "posts/{category}/{date:%Y}/{date:%m}/{slug}/index.html"
STATIC_PATHS = ["static", "images", "extra"]

# Theme Setting
THEME = "theme/elegant"
JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.i18n"]}
PYGMENTS_STYLE = "default"
APPLAUSE_BUTTON = False
LANDING_PAGE_TITLE = "Hi, I'm Wei Lee"
PROJECTS_TITLE = "Projects"
PROJECTS = [
    {
        "name": "apache-airflow",
        "url": "https://github.com/apache/airflow/",
        "description": "A platform to programmatically author, schedule, and monitor workflows",
    },
    {
        "name": "Commitizen",
        "url": "https://github.com/commitizen-tools/commitizen",
        "description": (
            "Python 3 command-line utility to standardize commit "
            "messages and bump version"
        ),
    },
]

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
    ("Twitter", "https://twitter.com/clleew"),
    ("RSS", "https://blog.wei-lee.me/feeds/all.atom.xml"),
)

# Markdown extension
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.extra": {},
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.nl2br": {},
        "markdown.extensions.toc": {"toc_depth": "1-3"},
        "md_mermaid": {},
        "markdown_del_ins": {},
    },
    "output_format": "html5",
}

# Plugin-setting
PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = [
    "another_read_more_link",
    "i18n_subsites",
    "extract_toc",
    "post_stats",
    "pelican.plugins.webassets",
    "pelican.plugins.tag_cloud",
    "pelican.plugins.render_math",
    "pelican.plugins.share_post",
    "pelican.plugins.seo",
    "series",
]
ANOTHER_READ_MORE_LINK = ""
READERS = {"html": None}
PAGEFIND_ENABLED = True

# pelican-seo settings
SEO_REPORT = True  # SEO report is enabled by default
SEO_ENHANCER = True  # SEO enhancer is disabled by default
SEO_ENHANCER_OPEN_GRAPH = True  # Subfeature of SEO enhancer
SEO_ENHANCER_TWITTER_CARDS = True  # Subfeature of SEO enhancer
