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
)
CATEGORIES_URL = "category"
TAGS_URL = "tags.html"
TAGS_SAVE_AS = "tags.html"
SERIES_LIST_URL = "series_list.html"
SERIES_LIST_SAVE_AS = "series_list.html"

# Content Setting
ARTICLE_URL = "posts/{category}/{date:%Y}/{date:%m}/{slug}"
ARTICLE_SAVE_AS = "posts/{category}/{date:%Y}/{date:%m}/{slug}/index.html"
STATIC_PATHS = ["images", "extra", "static"]

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
LANGUAGE_NAMES = {
    "zh-tw": "台灣漢語",
    "en": "English",
}
CURRENT_LANG = "zh-tw"
I18N_SUBSITES = {
    "en": {
        "CC_LICENSE": {
            "name": "Creative Commons Attribution-ShareAlike",
            "version": "4.0",
            "slug": "by-sa",
        },
        "SOCIAL_PROFILE_LABEL": "Keep In Touch",
        "COMMENTS_INTRO": "Do you like this article? What do you think about it? Leave your comment below",
        "CURRENT_LANG": "en",
    }
}

# Plugin-setting
PLUGINS = [
    "pelican.plugins.i18n_subsites",
    "pelican.plugins.neighbors",
    "pelican.plugins.random_article",
    "pelican.plugins.render_math",
    "pelican.plugins.seo",
    "pelican.plugins.series",
    "pelican.plugins.share_post",
    "pelican.plugins.statistics",
    "pelican.plugins.summary_link",
    "pelican.plugins.tag_cloud",
    "pelican.plugins.webassets",
    "pelican.plugins.heatmap",
    "pelican.plugins.osm",
]
PAGEFIND_ENABLED = True
SUMMARY_LINK_FORMAT = ""

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
    ("👤 關於我", "/pages/about-me.html"),
    ("🕰️ 近況", "/pages/now.html"),
    ("👨‍💻 技術", "/category/tech.html"),
    ("📚 讀書筆記", "/category/book.html"),
    ("💬 隨筆", "/category/random-thoughts.html"),
    ("🗺️ 共同工作", "/pages/coworking.html"),
    ("🏷️ 標籤", "/tags.html"),
    ("🗄️ 歸檔", "/archives.html"),
    ("📚 系列文章", "/series_list.html"),
    ("🎲 隨機", "/random/index.html"),
)

# Content Setting
DEFAULT_CATEGORY = "Random Thoughts"
ARTICLE_EXCLUDES = ["static"]

# Theme Setting
PYGMENTS_STYLE = "monokai"
AUTHOR_META = {
    # TODO: need a fix in attila
    "wei lee": {
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
            ("👤 About Me", "/en/pages/about-me.html"),
            ("🕰️ Now", "/en/pages/now.html"),
            ("👨‍💻 Tech", "/en/category/tech.html"),
            ("📚 Book Digest", "/en/category/book.html"),
            # ("💬 Random Thoughts", "/en/category/random-thoughts.html"),
            ("🗺️ Coworking", "/en/pages/coworking.html"),
            ("🏷️ Tags", "/en/tags.html"),
            ("🗄️ Archives", "/en/archives.html"),
            ("📚 Series", "/en/series_list.html"),
            ("🎲 Random", "/en/random/index.html"),
        ),
        "SITENAME": "Those aren't written down are meant to be forgotten",
    }
)
