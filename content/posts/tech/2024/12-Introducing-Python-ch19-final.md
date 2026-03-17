Title: Gobby's Python 讀書會 - 「第十九章 成為 Python 鐵粉」決定版
Date: 2024-08-06 19:58 +0800
Modified: 2024-08-06 23:35 +0800
Category: Tech
Tags: Python, Study Session
Slug: Introducing-Python-ch19-final
Authors: Wei Lee

繼上次的[草稿]({filename}/posts/tech/2024/10-Introducing-Python-ch19-draft.md)後該來個決定版了

<!--more-->

[TOC]

這次的內容非常的多，讀書會的一個小時是一定吸收不完的
但先聽過，知道 Python 有這些東西可以用，也許以後會有幫助

我會頻繁參照四年前寫的 [Python Table Manners 系列]({filename}/posts/tech/2020/04-python-table-manners-series.md)
提到的工具稍微有些過期，這篇文章會補充新的工具
但概念本身是互通的

## Where to find Python code
* [PyPI](https://pypi.org/)
    * Python Package Index
        * 讀作 Py-P-I
    * `pip install <package>` 預設會到 PyPI 找套件安裝
    * 遠古以前曾經叫做 "cheese shop"
        * 來自 Monty Python
* [GitHub Trend](https://github.com/trending/python)
    * GitHub 是目前主流的 Git 倉儲，在這可以找到最近流行的 Python 專案
* [Popular Python recipes](https://code.activestate.com/recipes/langs/python/)
    * 這就真的是第一次看到了

## Install package
* [pip](https://pypi.org/project/pip/)
    * e.g., `pip install pip`
* [pipenv](https://pipenv.pypa.io/en/latest/)
    * pip + [virtualenv](https://virtualenv.pypa.io/en/latest/)
* system package management (*Don't. Just Don't. Please*)
    * mac: [brew](https://brew.sh/), [ports](https://www.macports.org/)
    * Linux: apt-get, yum, dpkg, zypper
    * Windows: Windows Installer
* [conda](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html)
* 直接從原始碼建置
* *[poetry](https://python-poetry.org/)*
    * 包含打包並發布函式庫的功能
* *[uv](https://github.com/astral-sh/uv)*
    * 以 [Rust](https://www.rust-lang.org/) 撰寫的套件管理工具
    * `pip` 或 [pip-tools](https://github.com/jazzband/pip-tools)
    * 被大型專案如 [Airflow](https://airflow.apache.org/) 部分採用
* *[pipx](https://github.com/pypa/pipx) (just notice Josix wrote a [blog post](https://josix.tw/post/pipx-deep-dive/) for it)*
    * 主要用於安裝 Python 實作的指令列工具，而不是函示庫

pipenv, poetry 跟 pipx 更多的介紹可以參考 [Python Table Manners - 虛擬環境和套件管理]({filename}/posts/tech/2020/05-python-table-manners-dependency-management.md)

## IDE (*plus interactive shell and editor*)
* IDLE

Python 自帶的編輯器，在終端機輸入 `IDLE` 就能開啟

![IDLE.jpg](/images/posts-image/2024-Introducing-Python-ch19-final/IDLE.jpg)

* [PyCharm](https://www.jetbrains.com/pycharm/)
* [IPython](https://ipython.org/)
    * 這應該是互動式 shell，不算是 IDE 🤔
* [Jupyter Notebook](https://jupyter.org/)
* [Jupyter Lab](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html)
* *[Vim](https://www.vim.org/) / [NeoVim](https://neovim.io/)*
    * 編輯器的神
* *[VsCode](https://code.visualstudio.com/)*

大致上學習曲線如下（PyCharm可以參考 IntelliJ）

![learning-curve](/images/posts-image/2024-Introducing-Python-ch19-final/learning-curve.jpg)

👉 [Python Table Manners 番外 - 編輯器]({filename}/posts/tech/2021/2-python-table-manners-editor.md)

## Documentation and naming
* [PEP8](https://peps.python.org/pep-0008/)
    * Python 的程式碼風格指南
    * 建議演講： [Raymond Hettinger - Beyond PEP 8](https://www.youtube.com/watch?v=wf-BqAjZb8M)
* *建議讀物： [Clean Code]({filename}/posts/tech/2018/05-the-clean-code.md)*
    * 雖然這本主要是用 Java 為範例，但概念本身對寫好程式很有幫助

這章的標題「名稱與文件」，但內容主要在講註解跟命名
很微妙的翻譯
但如果對真的寫文件有興趣，可以參考 [Python Table Manners - 文件]({filename}/posts/tech/2020/13-python-table-manners-documentation.md)

## Type Hinting
* *[mypy](https://github.com/python/mypy)*

👉 [Python Table Manners - 程式碼風格 # 型別檢查 - mypy]({filename}/posts/tech/2020/08-python-table-manners-coding-style.md#-mypy)

除此之外，自從 Python 3.9，型別如 `list, dict, set` 都可以直接被使用
不用再從 typing 函式庫匯入 (i.e., `from typing import List, Dict, Set`)

```python
example_list: list[int] = [1, 2, 3]
```

如果你用的是 Python 3.8 ，你可以在檔案最上方

```python
from __future__ import annotations
```

如果你用的是 3.8 以前的版本，那你應該升級你的 Python
（3.7 在 2023 就已經不支援了）

## Testing (and linting?)
* print
    * **不要在 production 使用 print**
* [pylint](https://github.com/pylint-dev/pylint), [pyflakes](https://github.com/PyCQA/pyflakes), [flake8](https://flake8.pycqa.org/en/latest/), [pep8](https://pypi.org/project/pep8/), *[black](https://github.com/psf/black)*
    * 👉 [Python Table Manners - 程式碼風格]({filename}/posts/tech/2020/08-python-table-manners-coding-style.md)
    * *不過在 4202 年的現在，我推薦使用 [ruff](https://github.com/astral-sh/ruff) 取代以上所有工具*
* testing
    * 為什麼要測試
        * 避免既有的程式，因為新的改動壞掉
        * 👉 [Python Table Manners - 測試 (一)]({filename}/posts/tech/2020/06-python-table-manners-test-1.md)
        * 👉 [Python Table Manners - 測試 (二)]({filename}/posts/tech/2020/07-python-table-manners-test-2.md)
        * 👉 [Python Table Manners - pre-commit: git commit 前做完檢查]({filename}/posts/tech/2020/10-python-table-manners-pre-commit.md)
    * stdlib
        * [unittest](https://docs.python.org/3/library/unittest.html)
        * [doctest](https://docs.python.org/3/library/doctest.html)
    * [nose](https://pypi.org/project/nose/)
    * [tox](https://tox.wiki/)
        * 本身不是測試框架
        * 主要用來做任務管理
        * 特點是可以在多個 Python 版本執行任務（包含測試）
    * [py.test](https://docs.pytest.org/)
        * 目前最主流的 Python 測試框架，一般會建議使用它
    * [green](https://github.com/CleanCut/green)
    * *[hypothesis](https://hypothesis.readthedocs.io/en/latest/)*
        * Property-based testing
        * 相當有趣的概念，但我其實也沒用到很熟
* Continuous Integration (CI)
    * [buildbot](https://buildbot.net/)
    * [jenkins](https://www.jenkins.io/)
    * [travis-ci](https://www.travis-ci.com/)
    * [circleci](https://circleci.com/)
    * *[GitHub Actions](https://github.com/features/actions)*
        * 👉 [Python Table Manners - 持續整合/部署]({filename}/posts/tech/2020/19-python-table-manners-continous-intergration.md)

## Debugging
* print
    * `vars()`: 列出變數的 `__dict__`
    * `locals()`： 列出局部變數
    * `globals()`: 列出全域變數
* decorator

```python
import functools
import logging


def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("before function starts")
        result = func(*args, **kwargs)
        print("after function ends")
        return result

    return wrapper


@debug
def func():
    pass
```

* [pdb](https://docs.python.org/3/library/pdb.html)  
    * 常用 pdb 指令
        * `c`ontinue
        * `s`kip
        * `n`ext
        * `l`ist
        * `p`rint
    * 中斷點
        * 在 Python 檔案中加入 `breakpoint()`，可以在執行時停在那行，並進入 pdb 互動式介面

```shell
# how to use pdb in terminal

## run pdb on file
pdb <file name>

## run pdb on module
pdb -m <module name>
```

## Logging
* [logging](https://docs.python.org/3/howto/logging.html)
    * message: 日誌訊息
    * level: 日誌等級
    * logger
    * handler: 對日誌做額外的處理（e.g., 輸出成檔案）
    * formatter: 日誌格式
    * filter: 過濾特定日誌

```python
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename="example.log", encoding="utf-8", level=logging.DEBUG)
logger.debug("This message should go to the log file")
logger.info("So should this")
logger.warning("And this, too")
logger.error("And non-ASCII stuff, too, like Øresund and Malmö")
```

## Optimization (sounds more like profiling)
* "Python 通常很快"
    * *我不確定，即使身為一個 Python 忠貞的使用者，我認為很多人會認為這句話不成立 lol*
* [time](https://docs.python.org/3/library/time.html), [timeit](https://docs.python.org/3/library/timeit.html)
    * 參考 Debugging decorator 的寫法，可以將它們實作成 decorator 或 context manager，計算函式執行時間，找出瓶頸

## Algorithm and Data Structure
* list comprehension 通常比較快
* *這章也是很微妙，我不能說跟演算法、資料結構無關，但...就這？*

## Python Distributions
* [CPython](https://github.com/python/cpython)
    * 如果沒有特別安裝其他的發佈，這就是大部分人所使用的 Python
    * C extension
        * [NumPy](https://numpy.org/)
* [Cython](https://cython.org/)
* [PyPy](https://www.pypy.org/)
* [Numba](https://numba.pydata.org/)

## Source Control
* [Mercurial](https://www.mercurial-scm.org/)
* [Git](https://git-scm.com/)
    * `init`
    * `add`
    * `status`
    * `commit`
        * *[commitizen](https://github.com/commitizen-tools/commitizen) 可以幫助你寫更好的提交訊息 (commit message)！*
    * 👉 [Basic Git Tutorial]({filename}/posts/tech/2016/11-basic-git-tutorial.md) (雖然已經是 8 年前的文章了，但基礎概念應該是沒變太多吧...)

## Distributing Python Program
* *這章其實沒講什麼...*
* *可以研究看看怎麼將套件上傳到 PyPI*

## Learn more
* books
    * [Learning Python](https://nbviewer.org/github/Lee-W/Learning_Python/tree/master/)
* Websites
    * [Real Python](https://realpython.com/)
* Community
    * PyLadies
    * PyCons
    * local meetups
* Jobs
    * *you'll find your way out*
