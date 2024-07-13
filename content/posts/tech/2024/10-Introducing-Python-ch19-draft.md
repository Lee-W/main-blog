Title: Gobby's Python 讀書會 - 「第十九章 成為 Python 鐵粉」的草稿
Date: 2024-07-13 12:20
Category: Tech
Tags: Python, Study Session
Slug: Introducing-Python-ch19-draft
Authors: Wei Lee

最近半年 Gobby 為了學 Python 籌備了 Python 的讀書會
找了各路的人來導讀這本[ 精通 Python｜運用簡單的套件進行現代運算](https://www.tenlong.com.tw/products/9789865024864)

<!--more-->

原本我是推薦了[Learning Python, 5th Edition](https://www.oreilly.com/library/view/learning-python-5th/9781449355722/)，但因為它是英文的沒被採用
"Learning Python" 算是奠定了我 Python 基礎最重要的一本書
有些基本概念忘記了，我還是會翻[以前的筆記](https://nbviewer.org/github/Lee-W/Learning_Python/tree/master/)
不過沒想到這已經是 10 年以前的書啦😲

回到「精通 Python」這本書
雖然只看了一章，但有稍微找一下大家對這本書的想法
[《精通 Python 第二版》心得：給入門者的 Python 學習藍圖 ](https://blog.kyomind.tw/introducing-python/)寫的跟我的想法還蠻接近的
尤其是重新定義了 "Introducing Python" 為「精通 Python」 
實在**精闢**到一個不行
恩，肯定沒錯，一定是如此
不可能不是如此

為了我要導讀的「第十九章 成為 Python 鐵粉」
上週花了點時間看完，並寫下了筆記
好久沒有這樣全神貫注地看書，感覺是還蠻不錯的
書本身是中文的，但我寫中文太慢了，筆記當初就是用英文寫的
有些翻譯我真的不確定他對回去的原文是什麼，就寫了我猜的

這篇文的重點是在「草稿」
所以下面就只是當天我寫下的筆記簡單整理過的版本
*斜線的部分是我自己的補充或想法*


[TOC]

## Where to find Python code
* [PyPI](https://pypi.org/)
    * used to be "cheese shop" from Monty Python
* [GitHub Trend](https://github.com/trending/python)
* [Popular Python recipes](https://code.activestate.com/recipes/langs/python/)

## Install package
* [pip](https://pypi.org/project/pip/)
* [pipenv](https://pipenv.pypa.io/en/latest/) = pip + [virtualenv](https://virtualenv.pypa.io/en/latest/)
* system package management (*Don't. Just Don't. Please*)
    * mac: [brew](https://brew.sh/), [ports](https://www.macports.org/)
    * Linux: apt-get, yum, dpkg, zypper
    * Windows: Windows Installer
* [conda](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html)
* build from source
* *[poetry](https://python-poetry.org/)*
* *[uv](https://github.com/astral-sh/uv)*
* *[pipx](https://github.com/pypa/pipx) (just notice Josix wrote a [blog post](https://josix.tw/post/pipx-deep-dive/) for it)*

## IDE (*plus interactive shell and editor*)
* IDLE
* [PyCharm](https://www.jetbrains.com/pycharm/)
* [IPython](https://ipython.org/)
* [Jupyter Notebook](https://jupyter.org/)
* [Jupyter Lab](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html)
* *[Vim](https://www.vim.org/) / [NeoVim](https://neovim.io/)*
* *[VsCode](https://code.visualstudio.com/)*

## Documentation and naming
* [PEP8](https://peps.python.org/pep-0008/)
* *As a programmer, I would suggest reading [Clean Code]({filename}/posts/article/2018/06-the-clean-code.md)*

## Type Hinting
* *[mypy](https://github.com/python/mypy)*

## Testing (and linting?)
* print
    * no print in production
* [pylint](https://github.com/pylint-dev/pylint), [pyflakes](https://github.com/PyCQA/pyflakes), [flake8](https://flake8.pycqa.org/en/latest/), [pep8](https://pypi.org/project/pep8/)
    * *for most cases, I would say just use [ruff](https://github.com/astral-sh/ruff)*
* testing
    * why testing
        * avoid regression
            * what is a regresion
                * break something that used to work fine
    * stdlib
        * [unittest](https://docs.python.org/3/library/unittest.html)
        * [doctest](https://docs.python.org/3/library/doctest.html)
    * [nose](https://pypi.org/project/nose/)
    * [tox](https://tox.wiki/) - *run tests in different Python versions*
    * [py.test](https://docs.pytest.org/) - *for most cases, I would suggest just use py.test*
    * [green](https://github.com/CleanCut/green)
    * *[hypothesis](https://github.com/CleanCut/green)*
* Continuous Integration (CI)
    * [buildbot](https://buildbot.net/)
    * [jenkins](https://www.jenkins.io/)
    * [travis-ci](https://www.travis-ci.com/)
    * [circleci](https://circleci.com/)
    * *[GitHub Actions](https://github.com/features/actions)*

## Debugging
* print
    * `vars()`, `locals()`, `globals()`
* decorator
* [pdb](https://docs.python.org/3/library/pdb.html)
    * `pdb -i`
    * `pdb -m`
    * commands
        * `c`
        * `s`
        * `n`
        * `l`
        * `p`
        * `b`
    * `breakpoint()`

## Logging
* message
* level
* logger
* handler
* formatter
* filter

## Optimization (sounds more like profiling)
* "Python 通常很快"
    * *Idk, even though I'm a Pythonista, I feel many might argue it.*
* [time](https://docs.python.org/3/library/time.html), [timeit](https://docs.python.org/3/library/timeit.html) → use them as a decorator, context manager

## Algorithm and Data Structure
* list comprehension is faster
* *"Algorithm and Data Structure" hmm... 🤔 I can't say you're wrong.*

## Python Distributions
* [CPython](https://github.com/python/cpython)
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
    * `commit` *[commitizen](https://github.com/commitizen-tools/commitizen) rocks*

## Distributing Python Program
* *nothing insightful in this section*
* *upload to PyPI*

## Learn more
* books
    * *Learning Python*
* Websites
    * [Real Python](https://realpython.com/)
* Community
    * PyLadies
    * PyCons
    * local meetups
* Jobs
    * *you'll find your way out*