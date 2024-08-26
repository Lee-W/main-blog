# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

HOST = "blog.wei-lee.me"

# ----common between blogs----
PATH = "content"

# Blog Conf
AUTHOR = "Wei Lee"
SITEURL = "http://localhost:8000"
SITELOGO = "/images/avatar.jpg"
BROWSER_COLOR = "#333333"
HEADER_COVER = "/images/cover.jpeg"
DEFAULT_DATE_FORMAT = "%Y/%m/%d - %a"

# Locale
TIMEZONE = "Asia/Taipei"
DEFAULT_LANG = "zh-tw"
OG_LOCALE = "zh-tw"

# Utterance (comment system)
UTTERANCES_LABEL = "blog-comment"
COMMENTS_INTRO = (
    "Do you like this article? What do your tink about it? Leave you comment below"
)

# Page Setting
MAIN_MENU = True
DEFAULT_PAGINATION = 10
SHOW_PAGES_ON_MENU = False
SHOW_TAGS_IN_ARTICLE_SUMMARY = True
DIRECT_TEMPLATES = (
    "index",
    "categories",
    "authors",
    "archives",
    "tags",
    "series_list",
    "search",
)

# Content Setting
ARTICLE_URL = "posts/{category}/{date:%Y}/{date:%m}/{slug}"
ARTICLE_SAVE_AS = "posts/{category}/{date:%Y}/{date:%m}/{slug}/index.html"
STATIC_PATHS = ["images", "extra", "static"]

# Theme Setting
THEME = "theme/attila"
JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.i18n"]}
SHOW_ARTICLE_MODIFIED_TIME = True
CATEGORIES_URL = "category"
TAGS_URL = "tag"

# License
CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike",
    "version": "4.0",
    "slug": "by-sa",
}

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
    ("RSS", f"https://{HOST}/feeds/all.atom.xml"),
)

# Markdown extension
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.extra": {},
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.nl2br": {},
        "markdown.extensions.toc": {"toc_depth": "1-3"},
        "markdown_del_ins": {},
    },
    "output_format": "html5",
}

# Plugin-setting
PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = [
    "another_read_more_link",
    "post_stats",
    "series",
    "pelican.plugins.render_math",
    "pelican.plugins.share_post",
    "pelican.plugins.seo",
]
ANOTHER_READ_MORE_LINK = ""
PAGEFIND_ENABLED = True

# pelican-seo settings
SEO_REPORT = True  # SEO report is enabled by default
SEO_ENHANCER = True  # SEO enhancer is disabled by default
SEO_ENHANCER_OPEN_GRAPH = True  # Subfeature of SEO enhancer
SEO_ENHANCER_TWITTER_CARDS = True  # Subfeature of SEO enhancer


# ----this blog only----
# Blog Conf
SITENAME = "Those aren't written down are meant to be forgotten"
SITETITLE = SITENAME

# Utterance (comment system)
UTTERANCES_REPO = "Lee-W/main-blog"

# Page Setting
MENUITEMS = (
    ("🏠 Home", "/"),
    ("About Me", "/pages/about-me.html"),
    ("🗄️ Archives", "/archives.html"),
    ("📚 Series", "/series_list.html"),
    ("🔍 Search", "/search.html"),
)
SHOW_CATEGORIES_ON_MENU = True

# Content Setting
DEFAULT_CATEGORY = "Article"
ARTICLE_EXCLUDES = ["static"]

# Theme Setting
PYGMENTS_STYLE = "monokai"
AUTHOR_META = {
    "wei lee": {
        "image": "/images/avatar.jpeg",
    }
}

# Markdown extension
MARKDOWN["extension_configs"]["markdown_mermaidjs"] = {}

# Plugin-setting
EXTRA_PLUGINS = [
    "extract_toc",
    "i18n_subsites",
    "pelican.plugins.webassets",
    "pelican.plugins.tag_cloud",
]
PLUGIN_PATHS.extend(EXTRA_PLUGINS)
