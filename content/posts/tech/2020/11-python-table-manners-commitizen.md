Title: Python Table Manners - Commitizen: 規格化 commit message
Date: 2020-03-01 00:45 +0800
Modified: 2020-07-19 16:47 +0800
Category: Tech
Tags: Python, Git, commitizen-tools
Slug: python-table-manners-commitizen
Series: Python Table Manners
Authors: Wei Lee
Lang: zh-tw

接續著前一篇的 pre-commit ，繼續談 git 相關的工具
這篇來聊聊如何透過 [commitizen](https://github.com/commitizen-tools/commitizen) 規範 commit message
還有規範過的 commit message 能拿來做什麼

<!--more-->

[TOC]

## 為什麼要好好寫 commit message
![no-good-commit](/images/posts-image/2020-02-22-python-table-manner-series/no-good-commit.jpg)

如果不好好寫有意義的 commit message，每次都只用 "update" 當訊息
當你下了 `git log` 指令，就會看到一堆 "update"
然後哪天系統出錯的時候，你也會不知道要回朔到哪一個版本

![bad-commit](/images/posts-image/2020-02-22-python-table-manner-series/bad-commit.jpg)
(from [hackjutsu/bad-commit-example](https://github.com/hackjutsu/bad-commit-example/commits/master))

撰寫好的 commit message，除了讓未來的自己知道自己在幹嘛
也能讓團隊之間的溝通更順利

* 送 Pull Request / Merge Request 時，審核者能更快速地知道增加了哪些功能
* 新進人員可以從過往的 commit message 找到整個專案發展的脈絡，更容易上手專案

## Commitizen
除了提供的 commit message 撰寫建議和規範 （👉 [Writing commits](https://commitizen-tools.github.io/commitizen/tutorials/writing_commits/)）
[commitizen](https://commitizen-tools.github.io/commitizen/) 更進一步提供互動式介面，讓使用者可以夠輕鬆地產生符合規範的 commit message
同時也整合了前一篇所提到的 pre-commit hook，避免使用者將不符合規範的 commit message 寫入
除了採用來自 Angular 社群的 [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) (約定式提交) 外， commitizen 提供了高度的客製化，讓每個團隊或專案都可以依照自己的需求，撰寫相對應的規範
規範了 commit message 後，除了增加可讀性增加外，也讓訊息有可以被解析做其他運用
e.g., 提升版本號, 產生更新日誌

## 安裝與設定 Commitizen
跟 invoke 一樣，我會把 commitizen 同時安裝在系統和虛擬環境
安裝在虛擬環境主要是為了能在 CI/CD 伺服器上自動升版

```sh
# 安裝 commitizen 到系統
pipx install commitizen

# 安裝 commitizen 到虛擬環境中
pipenv install commitizen --dev
```

在專案中第一次使用 commitizen 可以使用初始化指令來完成基本的設定

```sh
cz init
```

一開始會先問想使用哪種設定檔

![cz-init-1](/images/posts-image/2020-02-22-python-table-manner-series/cz-init-1.png)

接著要選擇一套 commit 規範，預設有三種
如果有安裝其他的 commit 規範，它們也會出現在選項中（See more 👉 [Third-Party Commitizen Templates](https://commitizen-tools.github.io/commitizen/third-party-commitizen/)）

![cz-init-2](/images/posts-image/2020-02-22-python-table-manner-series/cz-init-2.png)

再來會問最新的 git tag 是否為最新的版本號
如果不是，就會列出 `git tag` 所有的結果
如果完全沒有用過 git tag，預設會是 `0.0.1`

![cz-init-3](/images/posts-image/2020-02-22-python-table-manner-series/cz-init-3.jpg)

之後會詢問版本的格式要是如何
常用的格式有 `$version` (e.g., `1.0.0`) 或 `v$version` (e.g., `v1.0.0`)

![cz-init-4](/images/posts-image/2020-02-22-python-table-manner-series/cz-init-4.jpg)

最後會確認要不要將驗證 commit message 的 pre-commit hook 設定好

![cz-init-5.jpg](/images/posts-image/2020-02-22-python-table-manner-series/cz-init-5.jpg)

完成後就會看到以下畫面

![cz-init-6.jpg](/images/posts-image/2020-02-22-python-table-manner-series/cz-init-6.jpg)

相對應的設定也會加入到設定檔 `pyproject.toml` (或 `.cz.toml`)

```toml
[tool.commitizen]
name = "cz_conventional_commits"
version = "1.0.2"
tag_format = "$version"
```

## 使用 Commitizen

```sh
# 使用 commitizen 做 commit
# (也可以用簡短版的 cz c)
cz commit
```

以 `cz_conventional_commits` 這套規則為例
會先詢問這次的 commit 做了哪一種改動

![commitizen-1](/images/posts-image/2020-02-22-python-table-manner-series/commitizen-1.jpg)

接著會要求輸入這次改動各項細節

* Scope： 改動範圍
* Subject： 簡短敘述這次的改動
* Body： 詳細敘述這次的改動
* Is this a BREAKING CHANGE？： 這是否是一個重大改動
* Footer： 其他參考資訊，通常可以將 Issue 的編號寫在這

![commitizen-2-w1024](/images/posts-image/2020-02-22-python-table-manner-series/commitizen-2.jpg)

回答完，就會產生 commit message **feat(blog-post): update python table manners series**
最下方則是 pre-commit hook 的 commit message 格式檢查通過

## 強制檢查 commit message
剛開始引入 commitizen 時，可能會常常忘記要使用它來做 commit
這時候就能使用到前一篇提到的 [pre-commit](https://pre-commit.com/)
雖然在 2.0.0 後可以透過 `cz init` 初始設定好，但還是說明如果事後才想設定要怎麼做

我在 [commitizen](https://github.com/commitizen-tools/commitizen) 中有加入 [.pre-commit-hooks.yaml](https://github.com/commitizen-tools/commitizen/blob/master/.pre-commit-hooks.yaml)
因此只要在專案的 `.pre-commit-config.yaml` 加入以下這段

```yaml
- repos
  - repo: https://github.com/commitizen-tools/commitizen
    rev: v1.23.1
    hooks:
      - id: commitizen
        stages: [commit-msg]
```

並透過 pre-commit 設定 commit-msg 階段的 git hook

```sh
pipenv run pre-commit install -t commit-msg
```

在 commit 執行完，要進訊息寫入前
git 會執行 `cz check` 來確認輸入的訊息是否符合規範
如果不符合規範就會拒絕這次的 commit

需要注意的是檢查會在產生 commit message 後才能執行
因此要設定 commit-msg 階段的 git hook （i.e., `.git/hooks/commit-msg`）
如果只下 `pipenv run pre-commit install` 是不會成功的

接著可以開始聊勞，這些 commit message 能做什麼應用了

## 自動提升版本號
與 commit message 規範可以做客製化不同
commitizen 目前並沒有提供不同版本表示方式的客製化
一律都會遵守 [Semantic Version](https://semver.org/) （語意化版本）
這種版本號採用 `MAJOR.MINOR.PATCH` (e.g., `1.10.20`) 的格式

* `MAJOR`： 重大改動，不向後相容
* `MINOR`： 新增功能，必須向後相容
* `PATCH`： 修正功能，必須向後相容

以 commitizen 預設使用的 `cz_conventional_commits` 來說，相對應的 commit 種類和應該提升的版本號如下

* `MAJOR`: BREAKING CHANGE (每次 commit 都會問的，這次是否為重大改動)
* `MINOR`: feat
* `PATCH`: fix, refactor, perf

p.s. conventional commit 可以有很多種延伸，這裡指的只是 commitizen 採用的版本

每次提升版本號只會提升 1 ，而且以最前面的為主
e.g., 要 merge 回 master 的改動中出現 BREAKING CHANGE，不管其他有多少 feat 或 fix ，都只會讓 `MAJOR` 提升 1

目前只有 `cz_conventional_commits` 有預設的版本對應
如果為 `cz_jira`, `cz_customize` 或自己客製化規則加上提升版本的功能，可以參考commitizen 文件中 [customization](https://commitizen-tools.github.io/commitizen/customization/) ，並加上 `bump_pattern`（比對 commit 是哪個種類） 和 `bump_map` （哪個種類的 commit 要提升哪個版本號）

稍微解釋了一下提升版本的規則，接下來要來講該如何使用了

```sh
cz bump
```

第一次提升版本的時候，會先確認目前在設定檔 (e.g., `pyproject.toml`）中的版本是否已經有相對應的 git tag

如果沒有則會確認這是否是第一次為這個專案加上 git tag

```text
Tag v0.0.1 could not be found.
Possible causes:
- version in configuration is not the current version
- tag_format is missing, check them using 'git tag --list'

? Is this the first tag created?  (Y/n)
```

如果想跳過這個確認可以在後面加上參數 `--yes`

```sh
cz bump --yes
```

接著 commitizen 就會新增一個相對應的 git tag 和更新設定檔中的版本號
因為要將設定檔中的改動儲存， commitizen 這時會再新增一個 commit
(e.g., `bump: version 0.0.1 → 0.0.2`)

除了設定檔中的版本號外，有時候專案本身也有其他地方會使用到版本號
如果每次透過 commitizen 提升版本號後，還要手動更新其他部分，就失去了自動的好處了
所以 commitizen 另外提供了 `version_files` 這個設定，將需要改動的檔案也寫進來
commitizen 提升版本號時，就會一併更新檔案的內容
（Read More 👉 [bump](https://commitizen-tools.github.io/commitizen/bump/) ）

透過 `cz bump` 指令雖然可以省下很多步驟
但更好的做法是將自動升版加入到加入到持續整合（Continuous Integration）
在 git repo 上將分支 merge 到 master 時，自動提升版本號
因為會牽涉到各個不同平台的做法，不會敘述太多
這裡附上 commitizen 文件中 [Github Actions](https://commitizen-tools.github.io/commitizen/tutorials/github_actions/), [Gitlab CI](https://commitizen-tools.github.io/commitizen/tutorials/gitlab_ci/) 還有 [Jenkins Pipeline](https://commitizen-tools.github.io/commitizen/tutorials/jenkins_pipeline/) 的做法

## 客製化 commit 規範
目前 commitizen 提供兩種方式

1. 直接在設定檔設定 → 適合只需要改動問題，不需要使用到複雜的功能
2. 將 commit 規範寫成 Python 套件發佈 → 適合需要加入複雜的驗證

### 直接在設定檔設定
首先必須先將 name 指定到 `cz_customize` 這套 commit 規範

```toml
[tool.commitizen]
name = "cz_customize"
```

再來要設定下面的欄位
其中最重要的是 `message_template`（支援[Jinja](https://jinja.palletsprojects.com/en/2.11.x/)）
以 `"{{change_type}}:{% if show_message %} {{message}}{% endif %}"` 這個例子來說
需要 `change_type`, `show_message`, `message` 三個變數來產生 commit message

（p.s. 如果想要使用驗證 commit message 的功能，則要更新 `schema_pattern`）

```toml
[tool.commitizen.customize]
message_template = "{{change_type}}:{% if show_message %} {{message}}{% endif %}"
example = "feature: this feature enable customize through config file"
schema = "<type>: <body>"
schema_pattern = "(feature|bug fix):(\\s.*)"
bump_pattern = "^(break|new|fix|hotfix)"
bump_map = {"break" = "MAJOR", "new" = "MINOR", "fix" = "PATCH", "hotfix" = "PATCH"}
info_path = "cz_customize_info.txt"
info = """
This is customized info
"""
```

變數要在 `[[tool.commitizen.customize.questions]]` 的區段作定義
背後所使用的套件是 [questionary](https://github.com/tmbo/questionary)

* `name`： 必須跟前面 `message_template` 定義的一模一樣，而且裡面用到的變數都要有對應的問題能取得值
* `message`： 顯示給使用者的問題
* `type`： [questionary](https://github.com/tmbo/questionary) 中的問題型態
* 其他欄位 (e.g., `choice`) 則是靠 `type` 來決定是否需要

```toml
[[tool.commitizen.customize.questions]]
type = "list"
name = "change_type"
choices = ["feature", "bug fix"]
message = "Select the type of change you are committing"

[[tool.commitizen.customize.questions]]
type = "input"
name = "message"
message = "Body."

[[tool.commitizen.customize.questions]]
type = "confirm"
name = "show_message"
message = "Do you want to add body message in commit?"
```

設定完之後，再使用 `cz commit` 就可以看到客製化過後的問題了
![customize](/images/posts-image/2020-02-22-python-table-manner-series/customize.jpg)

### 將客製化的 commit 規範寫成 Python 套件發佈
這個做法比較複雜，也比較不常會用到，所以我只會概略地講
（Read More 👉 [Customization](https://commitizen-tools.github.io/commitizen/customization/)）

我已經先將套件的架構驟寫成一個 [cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.0/) 範本
透過以下指令，可以進入 cookiecutter 的互動式介面，並初始化專案

```sh
cookiecutter gh:Lee-W/commitizen_cz_template
```

最主要需要實作的函式有 `questions`, `message`
實作完成後，必須在要使用這個 commit 規範的環境安裝這個套件
安裝之後會在 `cz ls` 看到這個新的 commit 規範
在設定檔中設定 `name` 或在指令列加上參數 `-n name` (e.g., `cz -n cz_test commit`) 就可以開始使用

## 自動產生更新日誌（Changelog）
commitizen 可以透過過往的 commit message 產生 [keep a changelog](https://keepachangelog.com/en/1.1.0/) 格式的更新日誌

透過以下指令，就能從最舊到最新的 commit message 產生更新日誌（預設是 `CHANGELOG.md`）

```sh
cz changelog
```

如果已經有現成的 `CHANGELOG.md`， 則可以使用 `cz changelog --incremental` 指令

commitizen 會試著找出文件中最新釋出版本 (e.g., `1.0.5`) 的位置，將最新釋出版本以後的 commit 加入到更新日誌的最頂端

例如目前有一個專案，最新的版本是 1.0.5，之後有 2 個 commit

* feat: cool new features
* ci: update jenkins file

原本的更新日誌

```markdown
## 1.0.5
### Feat
- old features
```

則 commitizen 在釋出 1.1.0 時，就會產生如下的更新日誌

```markdown
## 1.1.0 (2020-07-19)

### Feat

- new cool new features

## 1.0.5
### Feat
- some old features
```

因為產生更新日誌，通常適合在升版後執行
在 `cz bump` 加上 `--changelog` 參數就可以提升版本的同時，產生更新日誌

## 其他 commitizen 指令和常用參數
* `cz bump`： 提升版本號
    * `--dry-run`： 將提升版本號的訊息輸出到終端機，不會實際產生 tag 和改變檔案
    * `--increment {MAJOR,MINOR,PATCH}`： 提升特定版本號
* `cz changelog`: 產生更新日誌
    * `--dry-run`: 將產生的更新日誌書處到終端機，不產生或更新 `CHANGELOG.md`
* `cz -n NAME [command]`： 使用不同的 commit 規則 （e.g., `cz -n cz_jira commit`）
* `cz version`： 顯示版本
    * `-p`（`--project`）： 顯示專案版本
    * `-c`（`--commitizen`）： 顯示 commitizen 版本（預設）

## 關於 commitizen 的雜談
我在 Taipei.py 第一次試講 Python Table Manners 時
有一頁就提到了，雖然 Python 也有 commitizen 這個工具，但還不太成熟

![commitizen is not mature](/images/posts-image/2020-02-22-python-table-manner-series/not-mature-1.jpg)

沒想到在 PyCon CA 的前一個禮拜我認真測試時
才發現其實 commitizen 已經很夠用了，該有的功能都有
只是我剛好都用一些奇怪的測試方式，測到一些 edge case
這時就覺得信奉 Python （？？？）的我，好像應該好好的介紹 Python 的工具
而不是 JavaScript 的 [commitizen](https://github.com/commitizen)

![i am the one who's not mature](/images/posts-image/2020-02-22-python-table-manner-series/not-mature-2.jpg)

於是我就在 PyCon CA 前一個禮拜，開始貢獻起 [commitizen](https://github.com/commitizen-tools/commitizen)
把我遇到的 issues 都修了，就順便把投影片中相關的內容一起翻新了

貢獻的過程中也發現了很多還能再增加的新功能，於是就在 PyCon CA 2019 帶了這個專案去 Develop Sprint
第一次當 Sprint Leader 還蠻好玩的，也蠻有成就感的
（Read More 👉 [PyCon CA 2019]({filename}/posts/tech/2019/07-pycon-ca-2019.md)）

### 為什麼不用 Java Script 的 commitizen 就好了
~~因為我是 Python 的開發者啊！！！~~

起初我也是從 JavaScript 的版本開始使用 （畢竟兩個專案 star 的數量差了一百倍）
原本我就有寫好 commit message 的習慣
能有工具幫助我把這件事做得更好，當然就再好不過了

用了一段時間後，我開始覺得我明明都已經認真寫好 commit message 了
為什麼每次 Pull Request / Merge Request 還是花那麼多時間寫
是不是有什麼工具可以自動透過寫好的 commit 產生一些訊息？
再來就找到了 [cz-conventional-changelog](https://github.com/commitizen/cz-conventional-changelog)

但 [cz-conventional-changelog](https://github.com/commitizen/cz-conventional-changelog) 不能跟 [cz-customizable](https://github.com/leonardoanalista/cz-customizable) 同時使用
（Read More 👉 [Possible to use multiple adapters? #434](https://github.com/commitizen/cz-cli/issues/434)）

而且這些擴充常常要用到 `package.json` 來做設定
可是我就不是 Java Script 的專案，就不想加入這個檔案來設定啊 🤷‍♂️
所以才開始來找是不是有 Python 版本的替代方案
（Python 的 [commitizen](https://github.com/commitizen-tools/commitizen) 支援的 toml （`.cz.toml`）是通用的格式，裡面 Python 相關的內容，適用於各語言）

### 持續貢獻
整體來說， commitizen 是一個讓我貢獻得很有成就感的專案
最主要的原因之一就是這是我想用的工具

貢獻的過程，也會很快就收到作者 [Woile](https://github.com/Woile) 的回饋
它也會用很友善的文字，讓我覺得貢獻 commitizen 所花的時間，是有受到重視的

![friendly-response-1](/images/posts-image/2020-02-22-python-table-manner-series/friendly-response-1.jpg)

![friendly-response-2](/images/posts-image/2020-02-22-python-table-manner-series/friendly-response-2.jpg)

除此之外， commitizen 測試覆蓋率很高，比較不需要怕改錯了會不會弄壞舊有的功能
程式碼風格上，透過 black 跟 flake8 來規範，讓程式碼閱讀起來輕鬆很多
在貢獻的過程中，也學到了不少很實用的工具（e.g., pre-commit, cookiecutter）

所以**一起來貢獻 [commitizen](https://github.com/commitizen-tools/commitizen) 吧 💪**

## Reference
* [how to create a good commit message](https://medium.com/@klauskpm/how-to-create-good-commit-messages-67943d30cced)
* [How to Write Good Commit Messages: A Practical Git Guide](https://www.freecodecamp.org/news/writing-good-commit-messages-a-practical-guide/)
* [Conventional Commit](https://www.conventionalcommits.org/en/v1.0.0/)
* [Semantic Version](https://semver.org/)
