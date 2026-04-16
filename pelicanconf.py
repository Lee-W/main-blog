# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

from pelican.themes import attila

HOST = "blog.wei-lee.me"

# ----common between blogs----
PATH = "content"

# Blog Conf
AUTHOR = "Wei Lee"
SITEURL = "http://localhost:8000"
STATIC_SITEURL = SITEURL
SITELOGO = "/images/avatar.jpg"
BROWSER_COLOR = "#333333"
HEADER_COVER = "/images/cover.jpeg"
DEFAULT_DATE_FORMAT = "%Y/%m/%d - %a"
TIMEZONE = "Asia/Taipei"
SHOW_ARTICLE_MODIFIED_TIME = True

# Page Setting
MAIN_MENU = True
DEFAULT_PAGINATION = 10
SHOW_PAGES_ON_MENU = False
SHOW_CATEGORIES_ON_MENU = False
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
CATEGORIES_URL = "category"
TAGS_URL = "tag"

# Content Setting
ARTICLE_URL = "posts/{category}/{date:%Y}/{date:%m}/{slug}"
ARTICLE_SAVE_AS = "posts/{category}/{date:%Y}/{date:%m}/{slug}/index.html"
STATIC_PATHS = ["images", "extra", "static"]

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
JINJA_GLOBALS = {"POST_SHARE_MASTODON_DOMAIN": "g0v.social"}

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

# Utterance (comment system)
UTTERANCES_LABEL = "blog-comment"
COMMENTS_INTRO = "你喜歡這篇文章嗎？你覺得怎麼樣？歡迎在下方留言。"

# Theme Setting
THEME = attila.get_path()

# i18n
JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.i18n"]}
OG_LOCALE = "zh-tw"
DEFAULT_LANG = "zh-tw"
I18N_TEMPLATES_LANG = "en"
LANGUAGES = [("zh-tw", "/"), ("en", "/en/")]
CURRENT_LANG = "zh-tw"
CATEGORY_TRANSLATIONS = {
    "Tech": "技術",
    "Random Thoughts": "隨筆",
    "Book": "讀書筆記",
}
I18N_SUBSITES = {
    "en": {
        "SITENAME": "Those aren't written down are meant to be forgotten",
        "COMMENTS_INTRO": "Do you like this article? What do your tink about it? Leave you comment below",
        "CURRENT_LANG": "EN",
        "CATEGORY_TRANSLATIONS": {},
        "MENUITEMS": (
            ("🏠 Home", "/en/"),
            ("About Me", "/en/pages/about-me.html"),
            ("👨‍💻 Tech", "/en/category/tech.html"),
            ("📚 Book Digest", "/en/category/book.html"),
            ("💬 Random Thoughts", "/en/category/random-thoughts.html"),
            ("🏷️ Tags", "/en/tags.html"),
            ("🗄️ Archives", "/en/archives.html"),
            ("📚 Series", "/en/series_list.html"),
            ("🔍 Search", "/en/search.html"),
            ("🎲 Random", "/en/random/index.html"),
        ),
    },
}

# Plugin-setting
PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = [
    "another_read_more_link",
    "pelican.plugins.i18n_subsites",
    "pelican.plugins.neighbors",
    "pelican.plugins.random_article",
    "pelican.plugins.render_math",
    "pelican.plugins.seo",
    "pelican.plugins.series",
    "pelican.plugins.share_post",
    "pelican.plugins.statistics",
    "pelican.plugins.tag_cloud",
    "pelican.plugins.webassets",
    "pelican.plugins.heatmap",
    "pelican.plugins.osm",
]
ANOTHER_READ_MORE_LINK = ""
PAGEFIND_ENABLED = True

# Local plugins
LOCAL_PLUGINS = [
    "pelican.plugins.deadlinks",
]
PLUGINS.extend(LOCAL_PLUGINS)
DEADLINKS_VALIDATION = False

# pelican-seo settings
SEO_REPORT = True  # SEO report is enabled by default
SEO_ENHANCER = True  # SEO enhancer is disabled by default
SEO_ENHANCER_OPEN_GRAPH = True  # Subfeature of SEO enhancer
SEO_ENHANCER_TWITTER_CARDS = True  # Subfeature of SEO enhancer


# ----this blog only----
# Blog Conf
SITENAME = "不寫下來的東西都會被遺忘"
SITETITLE = SITENAME

# Utterance (comment system)
UTTERANCES_REPO = "Lee-W/main-blog"

# Page Setting
MENUITEMS = (
    ("🏠 首頁", "/"),
    ("關於我", "/pages/about-me.html"),
    ("👨‍💻 技術", "/category/tech.html"),
    ("📚 讀書筆記", "/category/book.html"),
    ("💬 隨筆", "/category/random-thoughts.html"),
    ("🏷️ 標籤", "/tags.html"),
    ("🗄️ 歸檔", "/archives.html"),
    ("📚 系列文章", "/series_list.html"),
    ("🔍 搜尋", "/search.html"),
    ("🎲 隨機", "/random/index.html"),
)

# Content Setting
DEFAULT_CATEGORY = "Random Thoughts"
ARTICLE_EXCLUDES = ["static"]

# Theme Setting
PYGMENTS_STYLE = "monokai"
AUTHOR_META = {
    "Wei Lee": {
        "image": "/images/avatar.jpeg",
    }
}

# Markdown extension
MARKDOWN["extension_configs"]["markdown_mermaidjs"] = {}
