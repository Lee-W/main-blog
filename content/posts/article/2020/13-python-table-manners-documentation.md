Title: Python Table Manners - 文件
Date: 2020-04-15 19:13
Modified: 2020-10-04 16:49
Category: Tech
Tags: Python, Documentation
Slug: python-table-manners-documentation
Authors: Wei Lee
Series: Python Table Manners

Python 開源專案中，[Sphinx](https://www.sphinx-doc.org/en/master/) 是很常見的文件產生工具
它能將 [reStructuredText](https://docutils.sourceforge.io/rst.html) 寫成的文件轉成網頁
[Read the Docs](https://readthedocs.org/) 也直接支援 Sphinx 產生的網頁

<!--more-->

但我今天要介紹的工具是 [mkdocs](https://www.mkdocs.org/)
最簡單的原因就是，我只會寫 Markdown 不會寫 reStructuredText XD
Guido 也說簡單一點的文件可以使用 Markdown 而不需使用 Shpinx
（我又要搬同一張截圖出來救援了 XD）

![because-guido-say-so](/images/posts-image/2020-02-22-python-table-manner-series/because-guido-say-so.png)

[TOC]

## 安裝

```sh
pipenv install mkdocs --dev
```

## 使用
這次依然是以將 mkdocs 運用到 [pycontw-postevent-report-generator](https://github.com/pycontw/pycontw-postevent-report-generator) 為例子
在 [commit 3fab5b](https://github.com/pycontw/pycontw-postevent-report-generator/commit/3fab5b9e7171d8302b012ad40ec1292d99c297a0) 版之後產生將文件從 `README.md` 移動到 `docs` 並產生 GitHub Page

### 初始化
首先進到專案資料夾中，初始化 mkdocs 需要的檔案

```sh
pipenv run mkdir new .
```

執行後，資料夾會多出以下兩個檔案

* `mkdocs.yml`: mkdocs 的設定檔
* `doc/index.md`: 空白的範例文件

透過這個指令在本機將伺服器跑起來

```sh
pipenv run mkdocs serve
```

打開瀏覽器，進入 `http://127.0.0.1:8000/` 就能看到最初始的頁面

![initial document](/images/posts-image/2020-02-22-python-table-manner-series/initial document.jpg)

### 修改網站名稱
初始的 `mkdocs.yml` 預設只會有這一行

```yaml
site_name: My Docs
```

指的是文件的頁面名稱，先把它改成專案的名稱

```yaml
site_name: PyCon TW post-event report generator (rg-cli)
```

### 增加頁面
因為 GitHub 也會讀 `docs/READMD.md` 作為進入專案時看到的文件
為了減少維護文件的時間，可以將 `README.md` 移動到 `docs` ，並取代掉 `index.md` 做為首頁

因為原先在 [pycontw-postevent-report-generator](https://github.com/pycontw/pycontw-postevent-report-generator) 中的 `README.md` 有點長
我將 **How to contribute** 的內容拆出來放到 `contributing.md`
將檔案命名成 `contributing.md` 在 GitHub 開 issue 時自動出現這個頁面的連結（See more 👉 [Setting guidelines for repository contributors](https://help.github.com/en/github/building-a-strong-community/setting-guidelines-for-repository-contributors)）
至於要怎麼寫好 `contributing.md` 則可以參考 [Wrangling Web Contributions: How to Build a CONTRIBUTING.md](https://mozillascience.github.io/working-open-workshop/contributing/)

```text
├── docs
│   ├── README.md
│   └── contributing.md
```

接著在 `mkdocs.yml` 加入 `nav` 參數，指定不同頁面對應的檔案

```yaml
site_name: PyCon TW post-event report generator (rg-cli)
nav:
    - Home: index.md
    - Contributing: contributing.md
```

位置是透過參數 `docs_dir` 來決定相對路徑
如果沒有設定，預設是相對於 `docs`

![separate page](/images/posts-image/2020-02-22-python-table-manner-series/separate page.jpg)

### 內部連結
撰寫文件時，為了讓使用者更容易找到其他頁面，會使用到內部連結
這時只要在文件中使用跟 `mkdocs.yml` 一樣的相對路徑即可

e.g., 在 `README.md` 連結到 `contributing.md`

```md
Please see the [Contributing](contributing.md) for further details.
```

### 更改主題
mkdocs 預設有 `mkdocs`, `readthedocs` 兩種主題
如果想嘗試其他主題則可以在 [MkDocs Themes](https://github.com/mkdocs/mkdocs/wiki/MkDocs-Themes) 找到
以主題 [mkdocs-material](https://github.com/squidfunk/mkdocs-material) 為例

首先先將主題安裝到開發環境內

```sh
pipenv install mkdocs-material --dev
```

在 `mkdocs.yml` 加上 `theme` 參數
需要注意的是這裡的 `name` 不需要加上前綴的 `mkdocs-`

```yaml
site_name: rg-cli
nav:
    - Home: index.md
    - Contributing: contributing.md
theme:
  name: 'material'
```

![material theme](/images/posts-image/2020-02-22-python-table-manner-series/material theme.jpg)

### 輸出靜態網頁
為了要能部署到其他服務 (e.g., GitHub Page）上，要先在本地將 Markdown 寫成的文件輸出成網頁

```sh
pipenv run mkdocs build
```

接著就可以在資料夾 `site` 找到輸出的網頁
因為 `site` 的內容都會跟著 `docs` 改變，專案中只需要留有原始的 Markdown 文件就好
可以在 `.gitignore` 加入 `site/`

```sh
echo "site/" >> .gitignore
```

下次輸出時，在指令後面加上 `--clean` 就可以清空上次的內容，重新輸出

```sh
pipenv run mkdocs build --clean
```

### 部署至 GitHub Page
在開源專案中，將文件部署到 GitHub Page 上是相當常見的
mkdocs 也為我們考慮到這點

只要在 `mkdocs.yml` 加入專案的 remote 相關設定

```yaml
repo_url: https://github.com/pycontw/pycontw-postevent-report-generator
remote_branch: gh-pages
remote_name: origin
```

並執行 `pipenv run mkdocs gh-deploy` 就會自動將文件部署到 GitHub Page 上

如果想更近一步透過 GitHub Action 來達到 push 原始碼，就自動產生 GitHub Page
可以參考我之前寫的 [透過 GitHub Action 自動發佈 Pelican 部落格文章]({filename}/posts/article/2020/02-automate-publishing-pelican-post-through-github-action.md)
雖然裡面使用的例子是 Pelican ，但只要把建置頁面的指令換掉就可以了

### 其他 mkdocs.yml 常用設定
* site_description, site_author, copyright
* google_analytics
* markdown_extensions
    * mkdocs 解析 Markdown 文件時要使用 [Python Markdown](https://python-markdown.github.io/) 的 [extension](https://python-markdown.github.io/extensions/) 和其設定
* plugins
    * 預設會使用 [search](https://github.com/mkdocs/mkdocs/wiki/MkDocs-Plugins#search--tables-of-content) 套件，如果想使用其它套件可以在 [MkDocs-Plugins](https://github.com/mkdocs/mkdocs/wiki/MkDocs-Plugins) 找到

## Bonus: 徽章
在開源專案中，常常可以見到一些有趣的徽章
它們很可能就是用 [shields.io](https://shields.io/) 產生的
除了常見的徽章外，也可以透過修改 url 製作客製化的徽章

像是在 markdown 文件加入

```markdown
![shields badge](https://img.shields.io/badge/<LABEL>-<MESSAGE>-<COLOR>)
```

就會出現

![shields badge](https://img.shields.io/badge/<LABEL>-<MESSAGE>-<COLOR>)

### 自製測試覆蓋率徽章
最近發現另一個有趣的小工具 - [coverage-badge](https://github.com/dbrgn/coverage-badge)
它可以不透過 [codecov](https://codecov.io/) 直接去讀 [pytest-cov](https://github.com/pytest-dev/pytest-cov) 產生的 `.coverage`  產生測試覆蓋率徽章

```sh
pipenv install coverage-badge --dev
pipenv run coverage-badge -o docs/coverage.svg
```

## Reference
* [Publish a (Perfect) Python Package on PyPI](https://wei-lee.me/pycon-note/posts/europython-2019/2020/03/publish-a-perfetc-python-package-on-pypi/)
* [MkDocs](https://www.mkdocs.org/)
* [mkdocs-material](https://github.com/squidfunk/mkdocs-material)
* [shield.io](https://shields.io/)
