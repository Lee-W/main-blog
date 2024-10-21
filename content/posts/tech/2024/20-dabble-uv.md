Title: 淺嚐 uv
Subtitle: 先從部落格開始
Date: 2024-10-21 18:50
Category: Tech
Tags: Python, Blog
Slug: dabble-uv
Authors: Wei Lee

隨著快速又強大的 linter [ruff][ruff] 被大量採用
志在取代 pip （？）的 [uv][uv] 也隨之問世
大專案如 [Apache Airflow®][airflow] 也採用了這個工具

<!--more-->

剛釋出的時候並不如現在有強大的功能
先支援了 pip 跟 pip-compile 的基本功能
並不符合我希望能取代 [pipenv][pipenv] 或 [poetry][poetry] 的需求
大概一兩個月前又有一個很大的更新，似乎是可以取代 [poetry][poetry] 了
但我還是想單純的用它來管 app 啊

然而前段時間刷推特看到 PyCon JP 朋友寫了 [さらなる進化を遂げた「uv」の新機能][uv-intro-jp]
裡面有提到

```sh
uv init --app
```

我才發現，原來 [uv][uv] 已經可以拿來管理 app 的相依套件了嗎！
那我還不趕快來試試
順便來試試前幾天在[Python Bytes Episode 405][python-bytes] 聽到的 [setup-uv][setup-uv]

於是就發了[Replace pipenv with uv #38][main-blog-pr] 跟 [dependency: replace pipenv with uv #11][travelog-pr]兩個更新部落格套件管理工具的 PRs

目標有兩個

1. 把 [pipenv][pipenv] 換成 [uv][uv]
2. 把 setup-python 換成 [setup-uv][setup-uv]

意外的還蠻順利的，幾乎沒有遇到什麼困難
首先要先把相依套件從 `Pipfile` 跟 `Pipfile.lock` 移到 `pyproject.toml` 跟 `uv.lock`

但因為專案中已經有 `pyproject.toml`，我先把原本檔案名改掉
透過以下指令產生 [uv][uv] 管理 app 相依套件用的欄位到 `pyproject.toml`

```sh
uv init --app
```

再手動進行合併
也可以看 [uv][uv] 如何初始化在 `pyproject.toml` 的 section
但是我懶，交給 `uv init` 處理就好

再來要把 Pipfile 中的套件加入 [uv][uv]

```sh
uv add [dep1] [dep2] ...
```

要加入開發用套件，則是要加上 `--dev` 的 flag

```sh
uv add [dev-dep-1] [dev-dep-2] ... --dev
```

建立虛擬環境的部分，我則是使用 `uv sync` 來取代

| | pipenv | uv |
| --- | --- | --- |
| prod | `pipenv install` | `uv sync --no-dev` |
| dev | `pipenv install --dev` | `uv sync`|

最後就剩下匯出 requirements.txt 給 `pip-audit` 來檢查的指令需要改成

```sh
uv pip compile pyproject.toml -o requirements.txt
```

剩下都是只要把 [pipenv][pipenv] 改成 [uv][uv]
setup-python 改成 [setup-uv][setup-uv] 也是相當的直覺

雖然原本相依套件本來就不多不會安裝太久
但現在 [uv][uv] 實在快到「你真的有裝嗎，不要騙我沒讀書耶」的程度 😆

<!--references-->

[ruff]: https://github.com/astral-sh/ruff
[uv]: https://github.com/astral-sh/uv
[airflow]: https://airflow.apache.org/
[pipenv]: https://pipenv.pypa.io/en/latest/
[poetry]: https://python-poetry.org/
[python-bytes]: https://pythonbytes.fm/episodes/show/405/oh-really
[setup-uv]: https://github.com/astral-sh/setup-uv
[uv-intro-jp]: https://gihyo.jp/article/2024/09/monthly-python-2409
[main-blog-pr]: https://github.com/Lee-W/main-blog/pull/38
[travelog-pr]: https://github.com/Lee-W/travlog/pull/11
