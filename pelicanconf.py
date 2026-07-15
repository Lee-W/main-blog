from pelican.themes import attila

HOST = "blog.wei-lee.me"

# ----common between blogs----
PATH = "content"

# Blog Conf
AUTHOR = "Wei Lee"
SITEURL = "http://localhost:8000"
STATIC_SITEURL = SITEURL
SITELOGO = "/images/avatar.jpeg"
BROWSER_COLOR = "#333333"
HEADER_COVER = "images/cover.jpeg"
SITE_DESCRIPTION = "開源、技術、閱讀，以及日常"
SITESUBTITLE = SITE_DESCRIPTION
DEFAULT_DATE_FORMAT = "%Y/%m/%d - %a"
TIMEZONE = "Asia/Taipei"
SHOW_ARTICLE_MODIFIED_TIME = True

FAVICON = "favicon-32.png"
FAVICON_IE = "favicon.ico"
TOUCHICON = "apple-touch-icon.png"

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
)
CATEGORIES_URL = "category"
ARCHIVES_URL = "archives"
ARCHIVES_SAVE_AS = "archives.html"
AUTHORS_URL = "authors"
AUTHORS_SAVE_AS = "authors.html"
CATEGORIES_URL = "categories"
CATEGORIES_SAVE_AS = "categories.html"
TAGS_URL = "tags"
TAGS_SAVE_AS = "tags.html"
SERIES_LIST_URL = "series_list"
SERIES_LIST_SAVE_AS = "series_list.html"

# Content Setting
ARTICLE_URL = "posts/{category}/{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "posts/{category}/{date:%Y}/{date:%m}/{slug}/index.html"
PAGE_URL = "pages/{slug}"
PAGE_SAVE_AS = "pages/{slug}.html"
CATEGORY_URL = "category/{slug}"
CATEGORY_SAVE_AS = "category/{slug}.html"
TAG_URL = "tag/{slug}"
TAG_SAVE_AS = "tag/{slug}.html"
AUTHOR_URL = "author/{slug}"
AUTHOR_SAVE_AS = "author/{slug}.html"
PAGINATION_PATTERNS = (
    (1, "{name}", "{name}{extension}"),
    (2, "{name}{number}", "{name}{number}{extension}"),
)
# Both are required together: STATIC_PATHS makes Pelican copy the directory,
# EXTRA_PATH_METADATA remaps individual files' output path within it.
STATIC_PATHS = ["images", "extra", "static"]
EXTRA_PATH_METADATA = {
    "extra/robots.txt": {"path": "robots.txt"},
    "extra/favicon.ico": {"path": "favicon.ico"},
    "extra/favicon-16.png": {"path": "favicon-16.png"},
    "extra/favicon-32.png": {"path": "favicon-32.png"},
    "extra/favicon-512.png": {"path": "favicon-512.png"},
    "extra/apple-touch-icon.png": {"path": "apple-touch-icon.png"},
}

# License
CC_LICENSE = {
    "name": "創用 CC 姓名標示─相同方式分享",
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
SOCIAL_PROFILE_LABEL = "保持聯繫"
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
        "pymdownx.blocks.caption": {},
        "pymdownx.superfences": {},
        "pymdownx.details": {},
        "pymdownx.snippets": {},
    },
    "output_format": "html5",
}

# Utterance (comment system)
UTTERANCES_LABEL = "blog-comment"
COMMENTS_INTRO = '喜歡這篇文章的話，歡迎在下方留言（需要 GitHub 帳號），或是<a href="mailto:hello+blog@wei-lee.me">寄 Email 找我聊聊！</a>'

# pelican-random-article
RANDOM_ARTICLE_BUTTON = True

# Theme Setting
THEME = attila.get_path()
THEME_TEMPLATES_OVERRIDES = ["templates"]
CSS_OVERRIDE = ("static/rights-notice.css",)

# i18n
JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.i18n"]}
OG_LOCALE = "zh_TW"
DEFAULT_LANG = "zh-tw"
I18N_TEMPLATES_LANG = "en"
LANGUAGES = [("zh-tw", "/"), ("en", "/en/")]
LANGUAGE_NAMES = {
    "zh-tw": "臺灣華語",
    "en": "English",
}
CURRENT_LANG = "zh-tw"
I18N_SUBSITES = {
    "en": {
        "LOCALE": "C",
        "CC_LICENSE": {
            "name": "Creative Commons Attribution-ShareAlike",
            "version": "4.0",
            "slug": "by-sa",
        },
        "SOCIAL_PROFILE_LABEL": "Keep In Touch",
        "SOCIAL": (
            ("Linkedin", "https://tw.linkedin.com/in/clleew"),
            ("GitHub", "https://github.com/Lee-W"),
            ("Twitter", "https://twitter.com/clleew"),
            ("RSS", f"https://{HOST}/en/feeds/all.atom.xml"),
        ),
        "COMMENTS_INTRO": 'If you enjoyed this article, feel free to leave a comment below (GitHub account required), or <a href="mailto:hello+blog@wei-lee.me">drop me an email to chat!</a>',
        "CURRENT_LANG": "en",
        "CSS_OVERRIDE": ("../static/rights-notice.css",),
        "OG_LOCALE": "en_US",
        "SITE_DESCRIPTION": "Open source, technology, books, and everyday life.",
        "SITESUBTITLE": "Open source, technology, books, and everyday life.",
    }
}
I18N_UNTRANSLATED_ARTICLES = "remove"
I18N_UNTRANSLATED_PAGES = "remove"

# Plugin-setting
PLUGINS = [
    "pelican.plugins.i18n_subsites",
    "pelican.plugins.neighbors",
    "pelican.plugins.random_article",
    "pelican.plugins.render_math",
    "pelican.plugins.seo",
    "pelican.plugins.series",
    "pelican.plugins.share_post",
    "pelican.plugins.sitemap",
    "pelican.plugins.statistics",
    "pelican.plugins.summary_link",
    "pelican.plugins.tag_cloud",
    "pelican.plugins.webassets",
    "pelican.plugins.heatmap",
    "pelican.plugins.osm",
    "pelican.plugins.on_this_day",
    "pelican.plugins.tabular",
    "pelican.themes.attila.readtime",
]
PAGEFIND_ENABLED = True
SUMMARY_LINK_FORMAT = ""

# Local plugins
LOCAL_PLUGINS = [
    "image_markup",
]
PLUGIN_PATHS = ["plugins"]
PLUGINS.extend(LOCAL_PLUGINS)
# pelican-tabular settings
TABULAR_COUNT_TEMPLATE = ""  # suppress the row-count line under tables
TABULAR_GROUP_COUNT_TEMPLATE = ""  # suppress per-group counts in group headers

# pelican-sitemap settings
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.7,
        "indexes": 0.5,
        "pages": 0.6,
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "weekly",
        "pages": "monthly",
    },
}

# pelican-seo settings
SEO_REPORT = True  # SEO report is enabled by default
SEO_ENHANCER = False
SEO_ENHANCER_OPEN_GRAPH = False
SEO_ENHANCER_TWITTER_CARDS = False


# ----this blog only----
# Blog Conf
SITENAME = "不寫下來的東西都會被遺忘"
SITETITLE = SITENAME

# Attila refresh: this is the blog variant (brick is the theme default, so no
# brand override needed). Adds body.site-blog for the theme's per-site styling.
SITE_VARIANT = "blog"

# Utterance (comment system)
UTTERANCES_REPO = "Lee-W/main-blog"

# Page Setting
MENUITEMS = (
    ("🏠 首頁", "/"),
    ("👤 關於我", "/pages/about-me"),
    ("🕰️ 近況", "/pages/now"),
    (
        "📂 分類",
        (
            ("👨‍💻 技術", "/category/tech"),
            ("📚 讀書筆記", "/category/book"),
            ("💬 隨筆", "/category/random-thoughts"),
        ),
    ),
    (
        "🧭 探索",
        (
            ("🏷️ 標籤", "/tags"),
            ("🗄️ 歸檔", "/archives"),
            ("📚 系列文章", "/series_list"),
            ("🗺️ 共同工作", "/pages/coworking"),
            ("📜 部落卷", "/pages/blogroll"),
            ("©️ 著作權", "/pages/copyright"),
        ),
    ),
    ("🎲 隨機", "/random/"),
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

# i18n
CATEGORY_TRANSLATIONS = {
    "Tech": "技術",
    "Random Thoughts": "隨筆",
    "Book": "讀書筆記",
}
I18N_SUBSITES["en"].update(
    {
        "CATEGORY_TRANSLATIONS": {
            "Tech": "Tech",
            "Random Thoughts": "Random Thoughts",
            "Book": "Book",
        },
        "MENUITEMS": (
            ("🏠 Home", "/en/"),
            ("👤 About Me", "/en/pages/about-me"),
            ("🕰️ Now", "/en/pages/now"),
            (
                "📂 Categories",
                (
                    ("👨‍💻 Tech", "/en/category/tech"),
                    ("📚 Book Digest", "/en/category/book"),
                    # ("💬 Random Thoughts", "/en/category/random-thoughts"),
                ),
            ),
            (
                "🧭 Explore",
                (
                    ("🏷️ Tags", "/en/tags"),
                    ("🗄️ Archives", "/en/archives"),
                    ("📚 Series", "/en/series_list"),
                    ("🗺️ Coworking", "/en/pages/coworking"),
                    ("📜 Blogroll", "/en/pages/blogroll"),
                    ("©️ Copyright", "/en/pages/copyright"),
                ),
            ),
            ("🎲 Random", "/en/random/"),
        ),
        "SITENAME": "Those aren't written down are meant to be forgotten",
    }
)
