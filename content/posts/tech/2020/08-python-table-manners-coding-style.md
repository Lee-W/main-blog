Title: Python Table Manners - 程式碼風格
Date: 2020-02-26 18:39 +0800
Modified: 2020-10-04 15:57 +0800
Category: Tech
Tags: Python, Code Quality
Slug: python-table-manners-coding-style
Authors: Wei Lee
Series: Python Table Manners

接下來要介紹的是 linters
它們是用來檢查程式是否符合特定程式碼風格的一類工具
以 Python 來說，則可能是判斷有沒有遵守 [PEP 8](https://www.python.org/dev/peps/pep-0008/)
linter 除了能檢查是否不符風格，通常也能用來檢查語法錯誤

<!--more-->

[TOC]

## 風格檢查 - flake8
[flake8](https://flake8.pycqa.org/en/latest/) 是 Python 最常被使用的 linter 之一
幾乎是所有 Python 開源專案的標準配備

### 使用
以下面這段程式碼為例

<!-- blacken-docs:off -->

```python
# bad_code.py
import os

os =  "My Operating system"
```

<!-- blacken-docs:on -->

這段程式碼出現了兩個問題

* 把模組 `os` 指派成一個字串，會導致無法使用 `os` 模組內的函式（因為 `os` 已經變成一個字串）
* `os` 的 `=` 後面加上兩個空白是不必要的，不符合 PEP 8 的規範

```sh
# 安裝 flake8
pipenv install flake8 --dev

# 執行 flake8
pipenv run flake8
```

flake8 預設對當前目錄下所有 Python 的檔案做檢查

執行後，`flake8` 會將這些錯誤找出來

```text
./bad_code.py:4:1: F811 redefinition of unused 'os' from line 1
./bad_code.py:4:5: E222 multiple spaces after operator
```

透過錯誤碼（e.g., `F811`）可以在 [flake8 rules](https://www.flake8rules.com/) 找到為什麼這是個錯誤和怎麼修正比較好

### 設定
某些狀況下，我們會不完全依照 flake8 的風格
例如 [PEP 8](https://www.python.org/dev/peps/pep-0008/) 的每行只能有 79 個字元，已經越來越不被使用

除了可以直接在 `flake8` 指令後面加上參數
也可以直接寫入設定檔 `setup.cfg` (或 `.flake8`, `tox.ini`）
以下是我所使用的設定

```ini
[flake8]
ignore =
    # F632: use ==/!= to compare str, bytes, and int literals
    F632,
    # W503: Line break occurred before a binary operator
    W503,
    # E501: Line too long
    E501,
    # E203: Whitespace before ':' (for black)
    E203
exclude =
    .git,
    __pycache__,
    build,
    dist

max-line-length = 88
```

* `ignore`: 指定要忽略的錯誤類型（可以從 [flake8 rules](https://www.flake8rules.com/) 找到這些錯誤碼）
* `exclude`: 不用被檢查的檔案
* `max-line-length`: 每行最長長度（這裡設定的 88，是後面會介紹到的 [black](https://black.readthedocs.io/en/stable/) 的預設值）

Read More 👉 [Configuring Flake8](https://flake8.pycqa.org/en/latest/user/configuration.html)

### 局部跳過檢查
另一種狀況是，我們只想在讓一兩行程式碼跳過 flake8 的檢查
但這份檔案的其他地方還是希望能被檢查
這時候可以在那行程式碼加上 `# noqa: [error]`

e.g.,

```python
example = lambda: "example"  # noqa: E731
```

## 風格檢查 - pylint
[pylint](https://www.pylint.org/) 同樣是相當常見的 Python linter
一般來說，比 `flake8` 檢查的更加嚴格

### 使用
與 flake8 不同， `pylint` 指令需要指定模組或套件名稱才能進行檢查

```sh
# 安裝 pylint
pipenv install pylint --dev

# 執行 pylint
pipenv run pylint <package> ......
```

### 設定
原本我建議使用 `pipenv run pylint --generate-rcfile >> .pylintrc` 來產生設定檔
但現在我更傾向在 pyproject.toml 中只寫入想要客製化的設定
原先的做法會在設定檔 .pylintrc 中有著大量的預設值，不容易找到哪些是修改過的設定，造成維護上的困難
不過需要注意的是在某些版本的 pylint 這個設定方式會出錯，所以建議安裝版本 2.6.0 以上的 pylint

```toml
[tool.pylint]
    [tool.pylint.messages_control]
    disable = [
        "bad-continuation",
        "missing-function-docstring",
        "missing-module-docstring",
        "invalid-name"
    ]

    [tool.pylint.format]
    max-line-length = 88
```

其中 disable 的錯誤可以在 [pylint-messages](http://pylint-messages.wikidot.com/all-codes) 找到

### 局部跳過檢查
只要在要忽略的程式碼前面一行加上 `# pylint: disable=[error]`
但需要注意的是，這行以後全部的檢查都會被關閉
所以要記得在需要開啟檢查的地方再加上 `# pylint: enable=[error]`

```python
# pylint: disable=line-too-long
print("Imagine this is a really long line!")
# pylint: enable=line-too-long
```

## flake8 v.s. pylint
除了相關的檢查外， pylint 會比 flake8 做更嚴格的檢查
也可以做更多的設定，但在執行上也會比較慢

在 PyCon US 2018 的 [Automating Code Quality](https://wei-lee.me/pycon-note/posts/pycon-us-2018/2019/09/automating-code-quality/)，Kyle Knapp 很詳細的比較了這兩個工具

我的使用上會把 flake8 作為強制檢查程式碼風格的一環
只要沒有通過 flake8 的檢查，就應該做修正
而 pylint 的警告則是只作為參考

flake8 在大多數狀況已經足夠
花時間去修改成符合某些 pylint 過於嚴格的檢查，或設定 `.pylint`，對我來說並不值得
而且 Guido 也是這麼說的 XD

![because-guido-say-so](/images/posts-image/2020-02-22-python-table-manner-series/because-guido-say-so.png)

## 型別檢查 - mypy
[mypy](http://mypy-lang.org/) 是 Python 做靜態型別檢查的工具
Python 是一個動態型別的語言，所以可以隨意地不同型別的值指派給同一個變數
e.g.,

```python
str_var = "This is a string"

str_var = 1
```

但這麼做有時候會造成邏輯上的錯誤
例如 `import csv` 時，如果使用了 `csv` 作為其他的變數名稱
就會將變數的值取代掉原本引入的模組

除此之外，型別標記的程式碼也會增加可讀性
因此近幾年越來越多人注意 Python 的型別標記

PyCon US 2017 中 Lisa Guo 和 Hui Ding 的 Keynote Session [Python@Instagram]({filename}/posts/tech/2017/13-Python@Instagram.md) 講了 Instagram 是為什麼要和如何將龐大的程式庫加上型別標示
[Static Typing in Python](https://wei-lee.me/pycon-note/posts/pycon-us-2020/2020/05/static-typing-in-python/) 則是 PyCon US 2020 年 Dustin 對型別標示和檢查的詳細介紹
而 Vita Smid 在 EuroPython 2019 的 [Static typing: beyond the basics of def foo(x: int) -str:](https://wei-lee.me/pycon-note/posts/europython-2019/2020/03/static-typing-beyond-the-basics-of-def-foo-x-int-str/) 則講到了型別檢查更進階一點的應用
這幾場演講都非常推薦可以觀看！

### 使用
以下列的程式碼為例

```python
# wrong_type_hint.py
from typing import List


def func(val: List[str]):
    print(val)


func([1, 2, 3])
```

`func` 的參數 `val` 標記為 `List[str]`
但在呼叫的時候卻傳入整數陣列

```sh
# 安裝 mypy
pipenv install --dev

# 執行 mypy
pipenv run mypy [files] --ignore-missing-imports
```

執行 `mypy` 後，它就會告訴跳出型別錯誤的警告

```sh
wrong_type_hint.py:8: error: List item 0 has incompatible type "int"; expected "str"

wrong_type_hint.py:8: error: List item 1 has incompatible type "int"; expected "str"

wrong_type_hint.py:8: error: List item 2 has incompatible type "int"; expected "str"
```

mypy 預設會去找所有引入的函式庫是否也有做好型別標記
所以一般使用上都會加上參數 `--ignore-missing-imports`
只要確保我們撰寫的部分都是正確的

### 設定
以下是我用來設定 mypy 的 `setup.cfg`

```ini
[mypy]
files=[your files]
ignore_missing_imports=true
```

## 自動排版 - black
比起 flake8, pylint 只做風格檢查
[black](https://github.com/psf/black) 會更進一步的直接修正不符合風格的程式碼
原本我不太喜歡使用這種的工具
原因是每次執行的結果不一定相同，修正的結果不見得符合我的需求，這時就要再去做設定

black 某種程度上的解決了這些問題
black 每次執行的結果都會是相同的，而且大致上修正結果我還算滿意
它最特別的地方是，不太能做客製化設定，也不能只做局部程式碼修正

引述自 black 的文件

> The Black code style
>
> Black reformats entire files in place. It is not configurable. It doesn't take previous formatting into account. It doesn't reformat blocks that start with # fmt: off and end with # fmt: on. # fmt: on/off have to be on the same level of indentation. It also recognizes YAPF's block comments to the same effect, as a courtesy for straddling code.

為什麼這可能是件好事？
因為這能讓大家更專注於程式碼的功能本身
而不是這裡要不要加逗號？要不要斷行？如何去調教設定檔？

> “There should be one-- and preferably only one --obvious way to do it.”
> –The Zen of Python, by Tim Peters

### 使用
因為 black 還是 beta 版
透過 pipenv 安裝時還要加上 `--pre` 參數

```sh
# 安裝 black
pipenv install black --dev --pre

# 執行 black 修正程式碼風格
pipenv run black <package>
```

因為 black 是直接重新排版程式碼
我節錄了部分我在 pycontw-postevent-report-generator [commit e64a](https://github.com/pycontw/pycontw-postevent-report-generator/tree/e64a1202c2af08fe9ca5a44b1e52fdafeac2098d) 修正風格的結果
上面紅色的部分是原本的程式碼，下面綠色是修正過的結果
(p.s. 當時設定的長度是 119)

![black-fix-1](/images/posts-image/2020-02-22-python-table-manner-series/black-fix-1.jpg)

![black-fix-2](/images/posts-image/2020-02-22-python-table-manner-series/black-fix-2.jpg)

![black-fix-3](/images/posts-image/2020-02-22-python-table-manner-series/black-fix-3.jpg)

如果只想要檢查程式碼是否符合 black 的風格
而不要直接做修正，可以在指令後面加入 `--check` 參數

```sh
pipenv run black <package> --check
```

### 設定
雖然說 black 不能對風格做太多的設定
我們還是能先指定哪些檔案是要修正，哪些是不用的
以下是我放在 `pyproject.toml` 的設定
（p.s. `line-length = 88` 是 black 的預設值）

```toml
[tool.black]
line-length = 88
include = '\.pyi?$'
exclude = '''
/(
    \.eggs
  | \.git
  | \.hg
  | \.mypy_cache
  | \.tox
  | \.venv
  | _build
  | buck-out
  | build
  | dist
)/
'''
```

## 排序函式庫 - isort
[isort](https://github.com/timothycrosley/isort) 是自動排列函式庫引入順序的的工具
PEP 8 建議將引入的函式庫分為三類做排序

1. 標準函式庫
2. 第三方函式庫
3. 本地的函式庫

並在每一個種類間空一行
e.g.,

```python
import os

import flask

import models
```

使用 isort 的原因跟 black 差不多
就是讓程式來決定比較枝微末節的事，專注在開發本身上面

### 執行

```sh
# 安裝 isort
pipenv install isort --dev

# 執行 isort 修正函式庫排序
pipenv run isort --atomic .
```

* `--atomic`: 只有重新排序後的結果沒有語法錯誤，才會儲存

### 設定
自從 5.0.0 後， isort 直接把常見的設定寫成 [profile](https://pycqa.github.io/isort/docs/configuration/profiles/)
只要指定 profile 就能直接套用相容的設定

```toml
[tool.isort]
profile = "black"
```

不過有一個相關的 bug 到 5.0.5 後才修正 (Ref: [Black profile not compatible with Black (ensure_newline_before_comments not working) #1295](https://github.com/PyCQA/isort/issues/1295))
所以還是建議安裝最新的版本

## 其他工具
* [check-manifest](https://github.com/mgedmin/check-manifest): 檢查有沒有少放入 `MANIFEST.in` 的檔案
* [seed-isort-config](https://github.com/asottile/seed-isort-config)

## Bonus: 設定檔的選用
從前面的測試篇到現在有提到很多設定檔的格式
通常每個工具都會有自己的設定檔 (e.g., `.coveragerc`, `.flake8`) 或者用 Python 比較通用的格式 (e.g., `pyproject.toml`, `setup.cfg`)
其中 `pyproject.toml` 是在 [PEP 518](https://www.python.org/dev/peps/pep-0518/) 提出的設定檔格式
不過還沒有被所有的工具支援
[awesome-pyproject](https://github.com/carlosperate/awesome-pyproject) 整理了目前已經支援或討論是否要支援 `proproject.toml` 的工具

比起讓多個工具的設定散落在各個設定檔
我傾向統一管理在 `pyproject.toml` 或 `setup.cfg`

* `pyproject.toml`
    * black
    * isort
    * pylint
    * coverage
    * pytest
    * commitizen (之後才會介紹到)
* setup.cfg
    * flake8
    * mypy

## Reference
* [Automating Code Quality - PyCon US 2018](https://wei-lee.me/pycon-note/posts/pycon-us-2018/2019/09/automating-code-quality/)
* [Life Is Better Painted Black, or: How to Stop Worrying and Embrace Auto-Formatting - PyCon US 2019](https://wei-lee.me/pycon-note/posts/pycon-us-2019/2019/11/life-is-better-painted-black-or-how-to-stop-worrying-and-embrace-auto-formatting/)
* [Beyond PEP 8 -- Best practices for beautiful intelligible code - PyCon 2015](https://www.youtube.com/watch?v=wf-BqAjZb8M&feature=youtu.be)
