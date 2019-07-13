Title: [Note] Effective Python
Date: 2019-01-19 16:45
Category: Tech
Tags: Python, Note
Slug: effective-python
Authors: Lee-W
Summary:

![effective python]({static}/images/books/aE00B2o.jpg)

第二次看過終於有辦法把原本看不懂的部分都看懂了
那些看不懂的大多是很抽象化的技巧
但是啊，看懂了這些語法
現在的我還是沒有能力，將這些抽象化應用在我自己的程式中
不過其他大部分比較簡單的在看過一次
還是提醒我在每一個眉眉角角都還要再更注意
上次看過的還沒有全部都應用到我寫程式的習慣中呢

<!--more-->

---

[TOC]

---

## 第一章： Pythonic 思維
### 作法02： 遵循 PEP8 風格指南
[PEP8](https://www.python.org/dev/peps/pep-0008/)
(我只把我認為容易被忽略或特別重要的幾點留下來)

* Whitespace
    * 過長的 expressions 要接續到其他文字行時，除了原本的縮排層次，應再加上額外的**四個空格**來縮排
* Naming
    * protected instance attributes -> _leading_underscore
    * private instance attributes -> __double_leading_underscore
    * Class, exceptions -> CapitalizedWord
    * model-level constant -> ALL_CAPS
* Statements
    * 使用行內否定 (inline negation, e.g., `if a is not b`)，而非否定正向的運算式 (negation of positive expressions, e.g., `if not a is b`)
    * 別用查驗長度的方式 (`if len(somelist) == 0`) 來檢查空值。使用 `if not somelist`
    * 避免單行 `if`, `for`, `while`, `except`，將它們分多行描述以清楚表達
    * import module 永遠用絕對名稱
        * e.g., 用 `from bar import foo` 而不是 `import foo`
    * import 順序
        1. standard library modules
        2. third-party modules
        3. your own modules

* 用 [pylint](https://www.pylint.org) 來檢查風格

### 作法04： 撰寫輔助函式而非複雜的運算式
* 將複雜的運算式移到輔助函式 (helper function) 內，特別是在你需要重複用到同樣的邏輯的時候
* 與其在運算式中使用 `or` 或 `and` ，不如使用 `if/else` 讓程式碼更易讀

```python
my_values = {'red': ['5'], green: [''] }

# or, and
red = int(my_values.get('red', [''])[0] or 0)

# if/else
red = int(red[0]) if red[0] else 0

# even better if/else
if red[0]:
    red = red[0]
else:
    red = 0

# helper function
def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found

red = get_first_int(my_values, 'red')
```

### 作法05: 知道如何切割序列
* 省略 zero index, 最後的索引來降低視覺雜訊
    * 用 `a[:5]`, `a[5:]` 而不是 `a[0:5]`, `a[5:len(a)]`
* copy value v.s. copy reference

```python
# copy value
b = a[:]
assert b == a
assert b is not a

# copy reference
b = a
assert b is a
```

### 作法07: 使用 list comprehension 而非 map 和 filter
* 避免用 `map`, `filter` ，因為使用他們時需要建立一個 `lambda` ，這是種視覺雜訊


```python
a = [1, 2, 3, 4, 5]

# list comprehension
squares = [x ** 2 for x in a]

# map
squares = map(lambda x: x ** 2, a)
```

### 作法09: 考慮使用 generator 取代大型 list comprehension
* 對於大型輸入來說 list comprehension 可能耗用相當大量的記憶體

### 作法11: 使用 zip 來平行處理 iterables

```python
a = [1, 2, 3, 4]
b = ['a', 'b', 'c', 'd']

# without zip
for i, x in enumerate(a):
    print(x, b[i])

# with zip
for x, y in zip(a, b):
    print(x, y)
```

* 如果提供了不同長度的 iterables ， zip 會 truncate 掉較長的 input

### 作法12: 避免在 for 或 while 後面使用 else 區塊

```python
# avoid
for i in range(3):
    ...
else:
    ...
```

### 作法13: 善用 try/except/else/finally 中的每個區塊
* `finally`
    * 即使例外發生，但也想要在例外發生時執行清理用的 cleanup code
* `else`
    * 如果 try 沒有丟出例外， else 區塊就會執行
    * 用來最小化 try 區塊的程式碼量 -> **讓 try 區塊只出現會丟出例外的程式碼**

## 第二章： 函式
### 作法14: 優先選用例外處理而非回傳 None
* 回傳 `None` 帶有特殊意義的函式容易出錯，因為 `None` 與其他的值 (e.g., `0`, `[]`, `''`)，在做條件運算式運算的結果都是 `False`

### 作法20: 使用 None 與 Docstrings 來指定 mutable default arguments
* default arguments 只會被 evaluate 一次：模組載入時、函式定義時。對於動態值 (e.g., `{}`, `[]`) 來說，這可能導致奇怪的行為

```python
from datetime import datetime

def func(default=datetime.now()):
    print(default)

# The two results would be the same but should be different
func()
func()
```

**Fix**

```python
from datetime import datetime

def func(default=None):
    """Demonstration

    Args:
        default: current datetime
    """
    if not default:
        default = datetime.now()
    print(default)
```

### 作法19: 以 keyword argument 提供選擇性的行為 (Related to 作法21)
```python
# original
def flow_rate(weight_diff, time_diff, period):
    return (weight_diff / time_diff) * period

# with default argument
def flow_rate(weight_diff, time_diff, period=1):
    return (weight_diff / time_diff) * period
```

不像「作法21」全面採取 keyword argement的原因是為了達到 backwards compatibility

### 作法21: 強制使用僅限 keyword argument 來讓程式碼更清楚易懂
* 使用 keyword-only arguments 來強制要求呼叫者提供 keyword argument 以避免混淆，特別是在接收多個 Boolean flag 的函式中

```python
# * indicates the end of positional arguments
def safe_division(number, divisor, *,
                  ignore_overflow=False):
    ...
```

## 第三章： 類別與繼承
### 作法22: 優先選用輔助 class 而非使用 dictionary 或 tuple 來管理紀錄
* 如果還不需要用到較有彈性的完整 class，請使用 `namedtuple` 來製作輕量化、不可變的資料容器
    * `namedtuple` 不能指定預設引數值，如果資料有許多 optional properties，則還是適合用 class

### 作法25: 使用 super 來初始化父類別

```python
class Implicit(BaseClass):
    def __init__(self, value):
        super().__init__(value * 2)
```

### 作法27: 優先選用公開屬性而非私有屬性
* 為什麼私有屬性的語法不強制施行嚴格的可見性限制呢？
    * We are all consenting adults here.
* 選擇私有屬性，只會讓子類別的 overrides 或 extensions 動作變得更麻煩更容易出錯
* 一般來說最好選擇使用 protected attributes
* 唯一得認真考慮使用 private attributes 的時機，是擔心子類別會有名稱衝突的時候

## 第四章： 元類別與屬性
### 作法33, 34, 35
* Metaclass 的應用
    * 驗證 subclass 是否有被正確定義
    * 註冊 class 的存在
    * 在一個 class 被實際使用前，修改其特性

## 第五章： 共時與平行處理
* 共時 (concurrency): 作業系統會在單一處理器快速切換多個執行程式
* 平行處理 (parallelism): 真正在同一時間執行許多工作的處理方式


### 作法38: 使用 Lock 來避免執行緒中的 data race

```python
class Count:
    def __init__(self):
        self.count = 0

    def increment(self, offset):
        self.count += offset
```

如果用 thread 去跑 `increment` 會造成 data race
原因是

```python
counter.count += offset
```

實際上執行了三個 operation
等效於以下的程式碼

```python
value = getattr(counter, 'count')
result = value + offset
setattr(counter, 'count', result)
```

這時候必須在 `increment` 加上 `Lock` 避免 data race

```python
class LockingCounter:
    def __init__(self):
        self.lock = Lock()

    def increment(self, offset):
        with self.lock:
            self.count += offset
```

### 作法39: 使用 Queue 來協調執行緒之間的工作

```python
from queue import Queue

queue = Queue()

def consumer():
    print('consumer waiting')
    queue.get()
    print('consumer done')

thread = Thread(target=consumer)
thread.start()

print('Producer putting')
queue.put(object())
thread.join()
print('Producer done')
```

### 作法41: 考慮使用 concurrent.futures 來達成真正的平行處理

* `from concurrent.futures import multiprocessing`
    * 藉由執行額外的直譯器作為 child processes。因為這些 child processes 跟主直譯器是分開的，所以它們的 GIL 也是分開的
* 使用 multiprocessing 的成本很高
    * 因為 main process 和 child processes 的溝通需要透過 serialization 和 deserialization
* multiprocessing 適合
    * isolated: 不必與程式其他部分共用狀態的 function
    * high-leverage: 在 main process 和 child processes 只需要轉移少量的資料，就能進行大量計算的狀況
* multiprocessing 最好只用到 `concurrent.futures` 的 built-in module 和 `ProcessPoolExecutor` class
    * 其他部分過於複雜，建議避免

## 第六章： 內建模組
### 作法34: 考慮使用 contextlib 與 with statement 來建立可重用的 try/finally 行為

```python
from contextlib import contextmanager


@contextmanager
def log_level(level, name):
    logger = logging.getLogger(name)
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)

    try:
        yield logger
    finally:
        logger.setLevel(old)


with log_level(logging.DEBUG, 'mylog') as logger:
    logger.debug('This is my message!')
    logging.debut('This will not print')
```

* `yield` 前是 contextmanager 的 `__enter__` 會執行的部分，之後則是 `__exit__`


### 作法45: 本地時鐘使用 datetime 而非 time
* 搭配 `pytz` module 來使用 `datetime` built-in module 在不同時區的時間之間作轉換
* 處理過程中，永遠用 UTC 來記錄，呈現給使用者前才轉換


## 第七章： 協作
### 作法49: 為每個 function, class, module 撰寫 Docstrings
* General Docstring Guide
    * 用3個 double quotes (`"""`) 開頭
    * 第一行應該是單一句子，來描寫用途
    * 接下來的文字含有使用者應該知道的作業細節

* class
    * 將重要的 public attribute 和 method 在 class level 的 docstring 寫出
* public function / method
    * 寫上 function 的特殊行為, argument 和 return value
    * 如果沒有 argument, return value，單句描述應該就夠了
    * 如果不會回傳任何東西，就不要提到 return value，而不是寫 "return None"
    * 如果有用到數目不定的 argument , keyword-argument，應該用 `*args`, `**kwargs`來描述
    * 如果有 default argument 都應該被提及
    * 如果是一個 generator，應該描述 iterate 時會 yield 什麼
    * 如果是 coroutine，應該描述
        * 會產生什麼
        * 預期從 yield 收到什麼
        * 什麼時候會停止


### 作法50: 使用 package 來組織 module 並提供穩定的 API
* Python 可以透過 module 或 package 的 `__all__` 特殊屬性來限制要暴露給 API 使用者的「表面積」
    * 如此即使重構也不會影響到使用者
    * 這在提供明確、穩定、給外部使用的 API 是個很好的做法
    * 如果只是在建置自己 module 間使用的 API 則是應該避免的做法
* 盡可能使用 `from x import y`，而不是 `import *`
    * `import *` 可能造成變數名稱複寫，而且不容易被 debug

### 作法51: 定義一個 root exception 來隔離呼叫者與 API
* 為什麼要自定義一個 root exception?
    * 讓使用者知道他們以錯誤的用法使用了你的 API
    * 幫助你找出 API 中的 bug → 只要不是提出這些自定義的例外，就很可能是 bug 的所在

### 作法52: 知道如何打破循環依存性
* 最好的做法是重構程式碼
    * 但有時候清楚的劃分相當困難，或 cost 太高了，因此還是需要知道如何打破循環依存性

* 解法一： 重新安排匯入順序
    * 這是一個比較不好的做法，違反了 PEP 8，且容易讓程式碼稍微的修改就造成問題
* 解法二： import, configure and execute
    * 讓 module 只作定義 function, class 和 constant，不做實際執行
    * 每個 module 提供一個 configure 函式，讓所有 module 都完成匯入後才呼叫
    * 許多狀況下都能運作良好，並且讓 dependency injection 變得可能
    * 缺點
        * 很難重新組織程式碼架構
        * 因為物件的定義和 configuration 在不同的地方，造成程式碼更難閱讀
* 解法三： 動態匯入
    * 通常是最簡單的解法
    * 在 function/method 中才使用 import
    * 但一般來說來是最好避免， import 的 cost 並沒有小到可以被忽略


## 第八章： 推出產品

### 作法57: 考慮使用 pdb 來進行互動式除錯

* 在程式碼加入以下這行，就能讓程式執行到這一步時停下，開啟互動式的 python shell
    ```python
    import pdf; pdf.set_trace()
    ```

* 檢視執行中的程式
    * `bt`: 印出目前 call stack 的 traceback
    * `up`: 上移 call stack
    * `down`: 下移 call stack
* 恢復程式的執行
    * `step`: 執行程式，直到下一行
    * `next`: 執行程式，直到遇到目前函式的下一行
    * `return`: 執行程式，直到目前函式回傳
    * `continue`: 執行程式，直到下一個 breakpoint 或 set_trace 再被呼叫

### 作法58: 最佳化之前先進行效能評估
* 使用 `cProfile` module 而非 `profile` module
    * 因為對程式效能的影響較小

```python
from cProfile import Profile
from pstats import Stats

# some program to test
import test

profiler = Profile()
profiler.runcall(test)

stats = Stats(profiler)
stats.strip_dirs()
stats.sort_stats('cumulative')
stats.print_stats()
```


### 作法59: 使用 tracemalloc 來了解記憶體用量或是否有洩漏
* Python 的預設實作 CPython 中，記憶體管理的方式是使用 reference counting
* Python 3.4 以後可以使用 tracemalloc

```python
import tracemalloc
tracemalloc.start(10)

time1 = tracemalloc.take_snapshot()

# some code that waste memory

time2 = tracemallo.take_snapshot()

stats = time2.compare_to(time1, 'lineno')
for stat in stats:
    print(stat)
```
