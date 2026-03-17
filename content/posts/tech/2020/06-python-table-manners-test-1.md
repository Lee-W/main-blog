Title: Python Table Manners - 測試 (一)
Date: 2020-02-24 23:33 +0800
Modified: 2020-10-04 15:33 +0800
Category: Tech
Tags: Python, Test
Slug: python-table-manners-test-1
Authors: Wei Lee
Series: Python Table Manners

設定完環境後，接著開始要開發程式的各項功能
要驗證程式正確性時，我們就會撰寫測試案例

<!--more-->

[TOC]

## 為什麼要寫自動化測試
* 如果沒有自動化測試
    * 必須手動去驗證程式的正確性，而且不能確定每次的測試方式都是相同的
     （如果因為很麻煩懶得測試，變成讓客戶去測試，就會造成更多的麻煩了 😱）
    * 增加重構 (refactoring）的風險，因為很難驗證程式的功能有沒有在重構的過程中被改動
    * 加入新的功能不知道會不會動到原本沒問題的功能

最後就會像是這樣

![new-feature-without-test](/images/posts-image/2020-02-22-python-table-manner-series/new-feature.jpg)

**總之，要寫測試！**

## unittest
[unittest](https://docs.python.org/3/library/unittest.html) 是 Python 標準函式庫的測試框架
起源於 jUnit 的做法，所以在函式的命名上和設計上比較不符合 Python 風格
雖然它不會是今天的主角，我也不太建議使用它
不過我們還是可以稍微看一下它的用法

以下取自 [unittest](https://docs.python.org/3/library/unittest.html) 文件中的其中一個範例

```python
import unittest


class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget("The widget")

    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), (50, 50), "incorrect default size")

    def test_widget_resize(self):
        self.widget.resize(100, 150)
        self.assertEqual(self.widget.size(), (100, 150), "wrong size after resize")
```

可以看到幾個特點

* 測試案例必須要繼承 `unittest.TestCase`
* 使用 `setUp` 函式來初始化 `widget` （如果有需要清除資源則會使用 `tearDown`）
* 使用 `assertEqual` 來做正確性的驗證

## pytest
[pytest](https://docs.pytest.org/en/6.1.1/) 是現在 Python 專案建議使用的測試框架，也會是這篇文章的主角

* 為什麼要用 pytest
    * 更符合 Python 程式碼風格 (Pythonic)
    * pytest 支援舊有的 unittest 風格
    * 扁平化（不用繼承）
    * 只需要使用 `assert`，不需要去記 `assert.+` (e.g., `assertEqual`) 等 API
    * 更好的[測試探索 (test discovery)](https://docs.pytest.org/en/6.1.1/goodpractices.html#test-discovery)
    * 更多的進階功能 (e.g., fixture, mark, parameterize and etc.)
    * 強大的套件

以下是取自 [pytest - Create your first test](https://docs.pytest.org/en/6.1.1/getting-started.html#create-your-first-test) 的範例
相比於 unittest 寫法相對簡潔

```python
# content of test_sample.py
def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5
```

## 從 Unittest 到 Pytest
前面的比較其實不太公平，unittest 的範例要測的內容本身就比 pytest 的複雜

所以接下來會用 [pycontw-postevent-report-generator](https://github.com/pycontw/pycontw-postevent-report-generator) 為例子
討論如何從 [v1.0](https://github.com/pycontw/pycontw-postevent-report-generator/tree/v1.0) 的 unittest 風格改成在 [commit 83e4](https://github.com/pycontw/pycontw-postevent-report-generator/commit/83e48c6443303045ed1de2f020297c3110bb1300) 的 pytest 風格

如果想跟著程式碼跑，可以把專案 clone 下來
（當然能貢獻專案就更棒了 XD）

```sh
# clone 專案到本地
git clone https://github.com/pycontw/pycontw-postevent-report-generator

cd pycontw-postevent-report-generator

# 切換到 commit 83e4 的前一個 commit (因為commit 83e4 已經完成修正)
git checkout 83e4~1

# 設定環境
pipenv install --dev
```

### 測試探索 (test discovery)
原本在 `README.md` 中要跑測試的指令相當的冗長
而且還必須要切換到 test 資料夾 (i.e., `cd test`)

```sh
cd test
python -m unittest discover -s ./ -p 'test_*.py'
```

不過這其實是一開始的設計有誤
以下是 test 資料夾的內容

```text
└── test
    …
    ├── test_sponsor.py
    └── test_title.py
```

test (或 tests) 本身也必須是一個套件
所以必須先在 test 內加入 `__init__.py`
（這是我在寫程式初期想開始寫測試遇到一個很大的坎 😢）

```text
└── test
    ├── __init__.py
    ...
    ├── test_sponsor.py
    └── test_title.py
```

做了改變後，就能改用更簡潔的指令跑測試了

```sh
python -m unittest
```

因為 pytest 也支援 unittest 風格
所以也可以直接使用 `pytest` 指令跑測試

```sh
pytest
```

不過在前一篇有提到使用虛擬環境的概念了
所以應該要確保每個專案的指令，都只在虛擬環境中跑
（因為前一篇建議使用 pipenv，之後的範例都會用 pipenv）

```sh
# 將 pytest 安裝到開發環境
pipenv install pytest --dev

# 執行 pytest
pipenv run pytest
```

這時候的測試其實會有許多錯誤
但執行後應該要能看到類似的畫面

```text
===================== test session starts ======================
platform darwin -- Python 3.7.3, pytest-5.3.5, py-1.8.1, pluggy-0.13.1
rootdir: /....../pycontw-postevent-report-generator
plugins: mock-2.0.0, cov-2.8.1
collected 9 items

test/test_sponsor.py FFFFFFFF                            [ 88%]
test/test_title.py F                                     [100%]

=========================== FAILURES ===========================
......
```

`F` 表示測試沒有通過，如果出現 `.` 則表示成功

### Step 0: 追朔程式碼
以 [test/test_sponsor.py::TestSponsor::test_sponsor_number](https://github.com/pycontw/pycontw-postevent-report-generator/blob/v1.0/test/test_sponsor.py#L6) 為例
（在套件以及模組的層級後， pytest 會使用 `::` 來區別不同的層級，試試 `pipenv run pytest -v` 指令）

原本 unittest 風格的程式碼中，做了三件事

1. 使用了 `setUp` 做 `self.sponsors` 的初始化
2. 在 `test_sonpsor_number` 取用 `setUp` 中初始過的 `self.sponsors`
3. 使用 `self.assertEqual` 來看 `self.sponsors` 的長度是否等於 1

```python
import unittest
from atta.partner import sponsor


class TestSponsor(unittest.TestCase):
    def setUp(self):
        sponsors = sponsor.get_all_sponsors("./data/packages.yaml", "./data/sponsors.yaml")
        self.sponsors = sponsors

        ...

    def test_sponsor_number(self):
        self.assertEqual(len(self.sponsors), 1)

        ...
```

### Step 1: 使用 fixture 取代 setUp / tearDown
將 `unittest.TestCase` 移除，改用 pytest 的 [fixture](https://docs.pytest.org/en/6.1.1/fixture.html) 取代 `setUp`
fixture 跟 `setUp / tearDown` 的概念上相近，都是用來 準備 / 清除 資源
但 fixture 更加的輕量且更有彈性

在 `test_sponsor_number` 中加入參數 `sponsors`
pytest 會去找 fixtures 中是否有 `sponsors` 並將之代入

接著將較為冗長的 `assertEqual`，改為 `assert`

```python
import pytest

from report_generator.partner import sponsor


class TestSponsor:
    @pytest.fixture(scope="class")
    def sponsors(self):
        return sponsor.get_all_sponsors("test/data/packages.yaml", "test/data/sponsors.yaml")

        ...

    def test_sponsor_number(self, sponsors):
        assert len(sponsors) == 1

        ...
```

(p.s. 在這裡 `atta` 已經重新命名為 `report_generator`)

### Step 2: 使用 mark.skip 跳過部分測試
原本的測試中有些邏輯錯誤
但我只想先完成風格的轉換，還不打算修正
因此先使用了 [markers](http://doc.pytest.org/en/6.1.1/example/markers.html)
在想跳過的測試案例前面加上 `@pytest.mark.skip`

```python
import pytest

from report_generator.partner import sponsor


class TestSponsor:
    ...

    @pytest.mark.skip("No bronze sponsor in test case")
    def test_sponsor_promotion_web_click_rank_bronze(self):
        answer = sponsor.NA_CONTENT_MESSAGE
        self.assertEqual(self.bronze_sponsor.web_click_rank, answer)
```

執行 `pipenv run pytest` 後，就會發現有部分的測試案例變成了 `s`

```text
========== test session starts ==========
platform darwin -- Python 3.7.3, pytest-5.3.5, py-1.8.1, pluggy-0.13.1
rootdir: /....../pycontw-postevent-report-generator
plugins: mock-2.0.0, cov-2.8.1
collected 9 items

test/test_sponsor.py ....ssss     [ 88%]
test/test_title.py .              [100%]
```

### Step 3: 扁平化 - 移除不必要的 class
從上面的範例可以看到， `self` 其實並不必要
這些測試案例不需要是一個類別
因此可以更近一步，把 `TestSponsor` 類別移除

```python
import pytest

from report_generator.partner import sponsor


@pytest.fixture(scope="function")
def sponsors():
    return sponsor.get_all_sponsors("test/data/packages.yaml", "test/data/sponsors.yaml")


def test_sponsor_number(sponsors):
    assert len(sponsors) == 1
```

不過這並不代表用類別就是錯的
一般我會在模組內測試案例比較多的時候，使用類別來將相似的測試案例歸在同一類

---

因為篇幅的關係，我決定把測試分成兩篇文章
~~絕對不是因為我寫不完了~~
盡請期待明天更深入的 pytest 應用 😄

## Reference
* [Python Testing with pytest](https://pragprog.com/book/bopytest/python-testing-with-pytest)
    * 非常推薦用這本書上手 `pytest`
* [快快樂樂成為 Coding Ninja (by pytest) - PyCon APAC 2015](https://www.youtube.com/watch?time_continue=201&v=pX1_I_sEi8k)
* [Pytest: Rapid Simple Testing -  Swiss Python Summit 2016](https://wei-lee.me/pycon-note/posts/swiss-python-summit-2016/2019/11/pytest-rapid-simple-testing/)
