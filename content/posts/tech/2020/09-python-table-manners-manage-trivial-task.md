Title: Python Table Manners - 管理繁瑣任務
Date: 2020-02-27 20:04 +0800
Modified: 2022-02-03 16:12 +0800
Category: Tech
Tags: Python, Task
Slug: python-table-manners-manage-trivial-tasks
Series: Python Table Manners
Authors: Wei Lee
Lang: zh-tw

前面幾篇從套件管理、虛擬環境、測試、風格檢查到自動排版，提到了很多的工具
每一個工具又有各自的參數和設定
這麼多指令怎麼可能記得起來 😱

![too-many-commands](/images/posts-image/2020-02-22-python-table-manner-series/too-many-commands.jpg)

<!--more-->

所以在這篇要介紹如何用 [invoke](http://www.pyinvoke.org/) 管理這些指令

[TOC]

## invoke 是什麼
invoke 是一套任務執行工具 (task execution tool)，主要用來是統一管理各種指令
有點像是 Python 的 `Makefile`

## 安裝 invoke
不同於 pytest, flake8 等套件，我會同時將 invoke 安裝在系統和虛擬環境中

```sh
# 安裝 invoke 到系統
pipx install invoke

# 安裝 invoke 到虛擬環境中
pipenv install invoke --dev
```

裝在系統的原因是想把它當成類似 `make` 的指令來使用

在虛擬環境還需要裝的原因是，部署時系統通常不會預裝 invoke
如果想在部署時也能使用 invoke 的功能，最方便的方法透過 pipenv 安裝

## 如何使用 invoke
再回到 [pycontw-postevent-report-generator](https://github.com/pycontw/pycontw-postevent-report-generator) 的例子
checkout 到 [commit 83e4](https://github.com/pycontw/pycontw-postevent-report-generator/tree/83e48c6443303045ed1de2f020297c3110bb1300)，回到使用 invoke 管理指令前
從當時的文件可以看到，還需要使用相對冗長的指令

![before-invoke](/images/posts-image/2020-02-22-python-table-manner-series/before-invoke.jpg)

到了 [commit 72ad](https://github.com/pycontw/pycontw-postevent-report-generator/tree/72ad956fd200867dc292a156c97a99a09ebe0104) (實作已經在 [commit bc98](https://github.com/pycontw/pycontw-postevent-report-generator/commit/bc98eec28037a9bed5063fef0f0f564893fce3ac) 完成，只是在 commit 72ad 才更新文件)，已經可以使用較短且較為統一的指令 (以 `inv` 作為開頭)

![after-invoke](/images/posts-image/2020-02-22-python-table-manner-series/after-invoke.jpg)

除此之外，引入 invoke 後，也不用每次都去翻文件
`invoke --list` 可以列出所有可用的指令

```sh
# 列出可用的 invoke 指令
# p.s. invoke 指令可以縮寫為 inv
$ inv --list

Available tasks:

  clean      Remove all the tmp files in .gitignore
  develop    Install script in pipenv environment in development mode
  init-dev   Install development dependencies
  install    Install script in pipenv environment
  test       Run testcase
```

執行的方式則是在 invoke 後面直接加上任務名稱

e.g.,

```sh
inv clean
```

## 實作 invoke 任務
我們先試著將前面的 `python setup.py develop` 改成 invoke 的任務

預設 invoke 會去找目錄下的 `tasks.py`
所以第一步要先在專案最上層建立 `tasks.py`
接著撰寫一個函式叫 `develop` ，這就會是之後的任務名稱 (i.e., 透過 `inv develop` 執行)
在函式前加上裝飾器 (decorator) `@task`
invoke 會傳入一個 context 做為第一個參數 (Read More 👉 [what exactly is this ‘context’ arg anyway?](http://docs.pyinvoke.org/en/stable/getting-started.html#aside-what-exactly-is-this-context-arg-anyway))
(p.s. 原本的程式碼中是使用 `cmd` ，那是錯誤的用法)
最後就可以用這個 context （參數 `ctx`） 執行指令

```python
from invoke import task


@task
def develop(ctx):
    ctx.run("python setup.py develop")
```

如同先前所提到的，操作都應該在虛擬環境內被完成
所以我將 `pipenv run` 的前綴提出來
這樣就能確保之後的操作一定都會在虛擬環境內執行
如果之後更換了管理虛擬環境的工具（e.g. `poetry run`），也可以更輕易的改動 `tasks.py`

```python
from invoke import task

PIPENV_PREFIX = "pipenv run"


@task
def develop(ctx):
    ctx.run(f"{PIPENV_PREFIX} python setup.py develop")
```

## 任務相依
如果任務之間有相依性，可以在 `@task` 後加入 `pre` 或 `post`
表示任務執行前或後還要執行其他任務

e.g., 在初始環境 (`init`) 前，常會先清除不必要的檔案 (`clean`)

```python
from invoke import task


@task
def clean():
    print("clean up")


@task(pre=[clean])
def init():
    print("initial")
```

## 任務模組化
當任務便多時，為了方便維護，就會傾向將相似的任務模組化
這時候就可以使用到 `namespace` 的概念
(Read More 👉 [Constructing namespaces](http://docs.pyinvoke.org/en/stable/concepts/namespaces.html))

不過我不會在這篇文章深入探討要怎麼說
一般來說，除非任務真的非常多，這是不太必要的

如果有興趣看我怎麼把 [pycontw-postevent-report-generator](https://github.com/pycontw/pycontw-postevent-report-generator) 的任務模組化
可以參考 [commit f105](https://github.com/pycontw/pycontw-postevent-report-generator/commit/f1050eabf44a8b8e662370bd97b2a79ad57723c2)

最後修改後 `tasks` 套件中有這些模組

```text
├── tasks
│   ├── __init__.py
│   ├── build.py
│   ├── common.py
│   ├── env.py
│   ├── style.py
│   └── test.py
```

和各個模組下的指令

```sh
$ inv --list

Available tasks:

  secure              Check package security
  build.clean         Remove all the tmp files in .gitignore
  build.develop       Install script in pipenv environment in development mode
  build.install       Install script in pipenv environment
  build.test-cli      Test whether the cli is runnable
  env.clean           Remove virtual environment
  env.init            Install production dependencies
  env.init-dev        Install development dependencies
  style.flake8        Check style through flake8
  style.mypy          Check style through mypy
  style.pylint        Check style through pylint
  style.reformat      Reformat python files through black
  style.run (style)   Check style through linter (Note that pylint is not included)
  test.cov            Run test coverage check
  test.run (test)     Run test cases
```

## 自動補完 （Auto-completion）
工程師是很懶惰的
這種指令列工具沒有自動補完怎麼行
invoke 當然也想到了
透過參數 `--print-completion-script=[shell]` 就能取得 invoke 預先寫好的自動補完腳步
目前支援 bash, zsh, fish 三種 shell

e.g., 將 invoke 產生的 zsh 自動補完腳本寫入 `~/.zsh`

```sh
inv --print-completion-script=zsh >> ~/.zshrc
```

## 為什麼不用 Makefile 就好？
因為有些 shell script 並不見得那麼好寫
（也可能只是我不熟...）

e.g.,

```python
from invoke import task


PIPENV_PREFIX = "pipenv run"


@task
def clean(cmd):
    """Remove all the tmp files in .gitignore"""
    files_to_remove = []
    with open(".gitignore") as input_file:
        for line in input_file.readlines():
            if not line.startswith("#"):
                files_to_remove.append(line.strip())

    cmd.run(f"rm -rf {' '.join(files_to_remove)}")
```

（雖然後來發現上面的一串，可以用 `git clean -Xdf` 取代...）

除此之外，invoke 也可以讓 shell script 的結果，直接跟 Python 互動
更容易實作出想要的功能

另外，推薦閱讀 [Building a CLI for Firmware Projects using Invoke](https://interrupt.memfault.com/blog/building-a-cli-for-firmware-projects)

## 其他進階應用
* 如何在任務加上參數？
    * 任務的函式後面加上除了 context 意外的參數
    * 👉 [Task parameters](http://docs.pyinvoke.org/en/stable/getting-started.html#task-parameters)
* 為什麼用 invoke 的結果跟指令列上的執行結果不完全相同？
    * 在 `run` 函式中加上 `pty=True` 參數通常能解決，但建議可以看看 invoke 為什麼不將這設定為預設行為
    * 👉 [Why is my command behaving differently under Invoke versus being run by hand?](http://www.pyinvoke.org/faq.html#why-is-my-command-behaving-differently-under-invoke-versus-being-run-by-hand)
* 如何在任務執行失敗時，只做警告，不要跳錯
    * 在 `run` 函式加上 `warn=True` (預設是 `False`)
    * 👉 [invoke.runners.Runner.run](http://docs.pyinvoke.org/en/1.2/api/runners.html#invoke.runners.Runner.run)

## Reference
* [Break the Cycle: Three excellent Python tools to automate repetitive tasks - PyCon US 2019](https://wei-lee.me/pycon-note/posts/pycon-us-2019/2019/08/break-the-cycle-three-excellent-python-tools-to-automate-repetitive-tasks/)
