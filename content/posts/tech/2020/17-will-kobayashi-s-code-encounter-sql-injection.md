Title: 小林的程式會不會遇到 SQL Injection
Date: 2020-09-22 12:50
Category: Tech
Tags: Python, Anime
Slug: will-kobayashi-s-code-encounter-sql-injection
Authors: Wei Lee

其實這篇文章應該一年前就該寫了...
今年為了在 PyCon TW 的 Lightning Talk 想個梗，就拿出來講 ([slide](https://speakerdeck.com/leew/xiao-lin-de-cheng-shi-ma-hui-bu-hui-yu-dao-sql-injection))
沒想到被投影機擺了一道......

<!--more-->

[TOC]

## 前言雜談
去年看了京阿尼的作品[小林家的龍女僕](https://zh.wikipedia.org/wiki/%E5%B0%8F%E6%9E%97%E5%AE%B6%E7%9A%84%E9%BE%8D%E5%A5%B3%E5%83%95)

第一集就發現主角小林也是寫 Python 的工程師，就開心地分享了這個消息
![del](/images/posts-image/2020-will-kobayashi-s-code-encounter-sql-injection/del.jpg)

沒想到馬上就有朋友問我這段程式碼會不會有 SQL injection
![will it encounter sql injection](/images/posts-image/2020-will-kobayashi-s-code-encounter-sql-injection/will it encounter sql injection.png)

單看這一段程式碼其實很難直接下定論
畢竟 key 根本就不會被帶入 `session_id=$key`，誰知道 db 怎麼實作的

當然，早就有人注意到這段程式碼了
它出自 [webpy/web/session.py](https://github.com/webpy/webpy/blob/webpy-0.39/web/session.py#L313)

* [如何评价京都动画2017年1月新作 小林家的龙女仆?](https://www.zhihu.com/question/51933296/answer/143492909)
    * 除了找到程式碼外，它還列出了劇情的其他 Python 程式碼，並討論了京都動畫使用這段程式碼會不會有法律問題
* [小林さんちのメイドラゴンで出てきたコード（小林さんを探せ！）](https://qiita.com/ygkn/items/6b3be1afa31e4092826e)
    * 透過 `git blame` 來找出「到底誰是小林！」
* [Ponkatsu - Tag: sql injection](https://ponkatsu807462913.wordpress.com/tag/sql-injection/)
    * 直接點出這段程式碼會遇到 SQL injection

但身為工程師還是要自己驗證一下到底會不會有 SQL injection

## 什麼是 SQL injection
根據 [SQL注入](https://zh.wikipedia.org/wiki/SQL%E6%B3%A8%E5%85%A5) 維基百科頁面的例子
假設有一段產生 SQL 字串的程式碼是這樣寫的

```python
sql_str = "SELECT * FROM users WHERE (name = '" + username + "') and (pw = '" + password + "');"
```

只要攻擊者輸入了

```python
username = "1' OR '1'='1"
password = "1' OR '1'='1"
```

就會產生

```sql
SELECT * FROM users WHERE (name = '1' OR '1'='1') and (pw = '1' OR '1'='1');
```

因為 1 一定等於 1，這段 SQL 就會產生跟 `SELECT * FROM user;` 一樣的效果
也就是攻擊者在完全不知道帳號密碼的情況下，就可以取得所有 users 的帳號密碼

## web.py 到底會不會有 SQL injection？
因為小林家的龍女僕是在 2017 年的 1 月到 4 月播出
根據 web.py 的 [tags](https://github.com/webpy/webpy/tags) 頁面，在那之後的第一個發佈是 `webpy-0.39`
可以推測，這最有可能是第一個包含小林撰寫程式碼的發佈

![web.py release](/images/posts-image/2020-will-kobayashi-s-code-encounter-sql-injection/webpy tag.jpg)

我們先從安裝 `web.py==0.39` 到虛擬環境中開始
（p.s. web 跟 py 中間的 . 是必要的，因為真的有個套件叫 webpy）

```sh
poetry add web.py==0.39
```

很不幸，如果使用的是 Python 3，會遇到以下的錯誤訊息

```text
Creating virtualenv kobayashi-pwI4Cysh-py3.8 in /Users/weilee/Library/Caches/pypoetry/virtualenvs

Updating dependencies
Resolving dependencies... (0.1s)

Writing lock file


Package operations: 1 install, 0 updates, 0 removals

  - Installing web.py (0.39)

[EnvCommandError]
Command ['/Users/weilee/Library/Caches/pypoetry/virtualenvs/kobayashi-pwI4Cysh-py3.8/bin/pip', 'install', '--no-deps', 'web.py==0.39'] errored with the following return code 1, and output:
Collecting web.py==0.39
  Using cached web.py-0.39.tar.gz (93 kB)
    ERROR: Command errored out with exit status 1:
     command: /Users/weilee/Library/Caches/pypoetry/virtualenvs/kobayashi-pwI4Cysh-py3.8/bin/python -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/.../web.py/setup.py'"'"'; __file__='"'"'/.../web.py/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /...
         cwd: /.../web.py/
    Complete output (7 lines):
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
      File "/.../web.py/setup.py", line 6, in <module>
        from web import __version__
      File "/.../web.py/web/__init__.py", line 14, in <module>
        import utils, db, net, wsgi, http, webapi, httpserver, debugerror
    ModuleNotFoundError: No module named 'utils'
    ----------------------------------------
ERROR: Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
WARNING: You are using pip version 20.1.1; however, version 20.2.3 is available.
You should consider upgrading via the '/Users/weilee/Library/Caches/pypoetry/virtualenvs/kobayashi-pwI4Cysh-py3.8/bin/python -m pip install --upgrade pip' command.
```

web.py 要到 0.40 才支援 Python 3 (Ref: [python3 ImportError: No module named utils #180](https://github.com/webpy/webpy/issues/180))

因為我不太想測試 Python 2，就假設小林的程式碼到 0.40 都沒什麼被改動到好了 😆

### 初始化資料庫
要實驗到底有沒有辦法取得資料庫的資料，總是要先有一個資料庫
這裡做了三件事

1. 用 `sqlite3` 跟 "kobayashi.db" 建立連線
2. 建立 `USER` 資料表
3. 將 "kobayashi", "tohru", "kanna", "elma" 新增到 `USER` 資料表中

```python
import sqlite3


def init_db():
    # connect and create "kobayashi.db"
    conn = sqlite3.connect("kobayashi.db")

    # create USER table
    create_table_sql = """
    CREATE TABLE `USER` (
        `account`   TEXT NOT NULL UNIQUE,
        `password`  TEXT NOT NULL,
        PRIMARY KEY(`account`)
    );
    """

    # insert users into USER table
    insert_user_sql = """
    INSERT INTO
        USER (account, password)
    VALUES
        ('kobayashi', '1'),
        ('tohru', '2'),
        ('kanna', '3'),
        ('elma', '3');
    """

    conn.execute(create_table_sql)
    conn.execute(insert_user_sql)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()
```

### 實作登入功能
`login` 會把使用者輸入的 account 跟 password 帶入 `where`
如果在資料庫找到正確的匹配，就會回傳找到的第一筆 user
如果找不到就回傳 `None`

```python
from typing import Optional, Tuple

import web


def login(account: str, password: str) -> Optional[web.utils.Storage]:
    result_set = db.select("USER", where=f"account ='{account}' AND password='{password}'")
    user = result_set.first()
    if user:
        print("login succeeded")
        return user
    else:
        print("wrong username or password")
        return None
```

這裡用三個案例來測試

1. 錯誤的帳號密碼 → 不應該取得 user
2. 正確的帳號密碼 → 應該取得 user
3. SQL injection → 理想上，也不該取得 user

```python
if __name__ == "__main__":
    db = web.database(dbn="sqlite", db="kobayashi.db")

    print(login("kobayashi", ""))
    print(login("kobayashi", "1"))
    print(login("1' OR '1'='1", "1' OR '1'='1"))
```

但這個世界始終不理想，包含了 SQL injection 的程式成功取得 user
之所以只取到一筆 user，是因為 `login` 只會回傳第一個物件，但這段 SQL 是能取到整個資料庫的 user 的

```text
0.0 (1): SELECT * FROM USER WHERE account ='kobayashi' AND password=''
wrong username or password
None

0.0 (2): SELECT * FROM USER WHERE account ='kobayashi' AND password='1'
login succeeded
<Storage {'account': 'kobayashi', 'password': '1'}>

0.0 (3): SELECT * FROM USER WHERE account ='1' OR '1'='1' AND password='1' OR '1'='1'
login succeeded
<Storage {'account': 'kobayashi', 'password': '1'}>
```

### 該如何修正？
修正的方式很簡單，只要在呼叫 select 的時候用 `vars` 將參數帶進 `where` 即可
其實 web.py 的文件就有寫了 (Ref: [db.query](https://webpy.org/cookbook/query))

```python
def login(account: str, password: str) -> Optional[web.utils.Storage]:
    result_set = db.select(
        "USER",
        where=f"account=$account AND password=$password",
        vars={"account": account, "password": password},
    )
    user = result_set.first()
    if user:
        print("login succeeded")
        return user
    else:
        print("wrong username or password")
        return None
```

這次就算用原本 SQL injetion 的作法，也取不到任何的資料
因為沒有 account 是 `"1' OR '1'='1"`

```text
0.0 (3): SELECT * FROM USER WHERE account ="1' OR '1'='1" AND password="1' OR '1'='1"
wrong username or password
None
```

## 知其然還要知其所以然啊！
除了知道怎麼修正外，我還想知道 web.py 做了什麼
下面冗長的紀錄我追 web.py 原始碼的過程

### pdbpp
寫這篇文章最大的收穫，大概就是大幅的提升了我對 pdb 的熟悉度
剛好聽到廣播 [Python Bytes](https://pythonbytes.fm/) 推薦的 [pdbpp](https://github.com/pdbpp/pdbpp) 就順手玩了一下
pdbpp 在安裝後會取代原生的 pdb
主要有這兩個功能比 pdb 好用

1. syntax highlight
    * 不過需要注意的是，如果要能客製化 highlight 風格，需要直接從 master branch 安裝的版本，目前還沒把這個修正釋出到 PyPI 上
2. sticky mode（在除錯器的上方一直顯示目前追到的程式碼）

![sticky mode example](/images/posts-image/2020-will-kobayashi-s-code-encounter-sql-injection/sticky mode.jpg)

順便記錄一下常用到的 pdbpp 指令

* `n`: 下一行
* `s`: 進到函式
* `p [var]` (e.g., `p locals()`): 印出變數 var
* `args`: 印出參數
* `ll`: 顯示現在在原始碼的哪裡（原本 pdb 的 longlist）

### 追 web.py 原始碼
這部分的紀錄方式會是每進到一次函式 (在 pdb 裡面使用 `s`) 就會加一個四級標題
回到原本的函式，則會在標題後面加一個 back

首先當然是從 `login` 呼叫到 `db.select` 函式開始追回去

#### web/db.py::DB::select
* 位置: [web/db.py#L845](https://github.com/webpy/webpy/blob/0.40/web/db.py#L845)

跑完 874 行的 list comprehension 後，`clauses` 會包含以下四個部分

```pdb
(Pdb++) p clauses
[<sql: 'SELECT *'>, <sql: 'FROM USER'>, <sql: 'WHERE account ="1\' OR \'1\'=\'1" AND password="1\' OR \'1\'=\'1"'>]
```

看起來已經成功將特殊字元跳脫，解決 SQL injection
所以接下來要去追產生 `clause` 的 `gen_clause`

#### web/db.py::DB::gen_clause
* 位置: [web/db.py#L934](https://github.com/webpy/webpy/blob/0.40/web/db.py#L934)

`gen_clause` 會被呼叫三次，當輸入的參數 sql 是 `WHERE` 時，會執行到 948 行的 `nout = reparam(val, vars)`
此時輸入的各個參數如下

```pdb
(Pdb++) p sql
'WHERE'

(Pdb++) p val
'account =$account AND password=$password'

(Pdb++) p vars
{'account': "1' OR '1'='1", 'password': "1' OR '1'='1"}
```

#### web/db.py::reparam
* 位置: [web/db.py#L344](https://github.com/webpy/webpy/blob/0.40/web/db.py#L344)
* 參數:
    * val = `'account =$account AND password=$password'`
    * vars = `{'account': "1' OR '1'='1", 'password': "1' OR '1'='1"}`

一進到 `reparm` ，這些值就會繼續被傳到 `safteval`

#### web/db.py::SafeEval::safeeval
* 位置: [web/db.py#L1699](https://github.com/webpy/webpy/blob/0.40/web/db.py#L1699)
* 帶入參數
    * text = `'account =$account AND password=$password'`
    * mapping = `{'account': "1' OR '1'='1", 'password': "1' OR '1'='1"}`

1700 行的 `Parser` 會將 text 分解成四個 SQL 的部分，並且將 nodes 連同 mapping 一個一個帶入 `eval_node`

```pdb
(Pdb++) p list(nodes)
[Node('text', 'account =', None), Node('param', 'account', None), Node('text', ' AND password=', None), Node('param', 'password', None)]
```

#### web/db.py::SafeEval::eval_node
* 位置: [web/db.py#L1703](https://github.com/webpy/webpy/blob/0.40/web/db.py#L1703)

`self.eval_expr` 的功用是在讓 `node[1]` 能抓到 `"1' OR '1'='1"`
抓到了字串 ``"1' OR '1'='1"`` 後會丟到 `sqlquote`

#### web/db.py::sqlquote
* 位置: [463行](https://github.com/webpy/webpy/blob/0.40/web/db.py#L463)
* 參數:
    * a = `"1' OR '1'='1"`

a 會在 475 行被初始化成 [SQLParam](https://github.com/webpy/webpy/blob/0.40/web/db.py#L93) 物件 ，然後再產生 [SQLQuery](https://github.com/webpy/webpy/blob/0.40/web/db.py#L142) 物件

#### web/db.py::SafeEval::eval_node (back)
* 位置: [web/db.py#L1703](https://github.com/webpy/webpy/blob/0.40/web/db.py#L1703)

回到 `eval_node` ，就會把剛剛的結果 `<sql: '"1\' OR \'1\'=\'1"'>` (`SQLQuery` 物件印出的形式) 回傳

#### web/db.py::SafeEval::safeeval (back)
* 位置: [web/db.py#L1699](https://github.com/webpy/webpy/blob/0.40/web/db.py#L1699)

1701 行的 `[self.eval_node(node, mapping) for node in nodes]` 會產生

<!-- blacken-docs:off -->
```python
>>> self.eval_node(node, mapping) for node in nodes
['account =', <sql: '"1\' OR \'1\'=\'1"'>, ' AND password=', <sql: '"1\' OR \'1\'=\'1"'>]
```
<!-- blacken-docs:on -->

這個 list 會接著被帶入 `SQLQuery.join` 整合成一整個 SQL 的片段

#### web/db.py::SQLQuery::join
* 位置: [web/db.py#L254](https://github.com/webpy/webpy/blob/0.40/web/db.py#L254)

277 ~ 285 行的 for loop 執行完會產生一個新的 target (`SQLQuery` 物件)

```pdb
(Pdb++) p target
<sql: 'account ="1\' OR \'1\'=\'1" AND password="1\' OR \'1\'=\'1"'>

(Pdb++) p target.items
['account =', <param: "1' OR '1'='1">, ' AND password=', <param: "1' OR '1'='1">]

(Pdb++) p target.values()
["1' OR '1'='1", "1' OR '1'='1"]

(Pdb++) p target.query()
'account =%s AND password=%s'
```

可以發現這時候要回傳的 `SQLQuery` 物件已經把查詢時跟要帶入的值分開儲存

#### web/db.py::reparam（back）
* 位置: [web/db.py#L344](https://github.com/webpy/webpy/blob/0.40/web/db.py#L344)

#### web/db.py::DB::gen_clause (back)
* 位置: [web/db.py#L948](https://github.com/webpy/webpy/blob/0.40/web/db.py#L948)

在 956 行，剛剛回傳的 `nout` 會透過 `xjoin` 跟字串 `WHERE` 整合成一個新的 `SQLQuery` 物件
字串跟 `SQLQuery` 相加的行為被定義在 [196 行](https://github.com/webpy/webpy/blob/0.40/web/db.py#L196) 的 `__radd__`
但因為沒有什麼太意料之外的行為，這裡就不繼續追下去了

#### web/db.py::DB::select (back)
* 位置: [web/db.py#L874](https://github.com/webpy/webpy/blob/0.40/web/db.py#L874)

取得了回傳的 `clauses` 後，它會在 879 行的 `SQLQuery.join` 整合成一個 `SQLQuery` 物件
產生 `qout`

```pdb
(Pdb++) p qout
<sql: 'SELECT * FROM USER WHERE account ="1\' OR \'1\'=\'1" AND password="1\' OR \'1\'=\'1"'>
```

最後就要看 884 行的 `self.query(qout, processed=True)` 是不是真的會以參數化的方式執行這段 SQL

#### web/db.py::DB::query
* 位置: [web/db.py#L807](https://github.com/webpy/webpy/blob/0.40/web/db.py#L807)

執行到 831 行 `self._db_execute(db_cursor, sql_query)` 才會用到傳進來的 `sql_query`

#### web/db.py::DB::_db_execute
* 位置: [web/db.py#L750](https://github.com/webpy/webpy/blob/0.40/web/db.py#L750)

在 756 行的 `_process_query` 產生要執行的 SQL query 跟它的參數，回傳的結果分別是

* query = `'SELECT * FROM USER WHERE account =? AND password=?'`
* params = `["1' OR '1'='1", "1' OR '1'='1"])`

再帶到 757 行的`out = cur.execute(query, params)` 直接對資料庫作查詢，所以就不會遇到 SQL injection 了

#### 原本好像是要追 delete 才對
顧著重現維基百科的例子，竟然忘記了原本要追的其實是另一段程式碼
不過我想本質應該還是相同的
有興趣的話，可以拿以下這段 SQL 來測測看 delete 的 SQL injection 是不是真的能清空整個資料表
**disclaimer: 請不要拿它用在會影響到其他人的程式上 (e.g., production 環境)**

```sql
DELETE FROM USER WHERE account = '' OR ''=''
```

![xkcd joke](https://imgs.xkcd.com/comics/exploits_of_a_mom.png)

> 你是不是真的把你的兒子取名為 `Rober'); DROP TABLE Students;`

## 結語
結論是「雖然小林的程式碼可能遇到 SQL injection，但也存在著很簡單的解決方案，只要使用者有讀文件，應該就不會遇到」
我完全不是資訊安全的專家，只是抱持著對京都動畫和 Python 的愛來追這段程式碼
如果有說錯或可以補充的部分，再麻煩留言讓我知道 🙏

其實小林家的龍女僕，還有其他場景也有出現 Python
像是這裡說了小林自從開始寫 Python 後變得開朗了許多呢（誤

![kobayashi becomes hayppier](/images/posts-image/2020-will-kobayashi-s-code-encounter-sql-injection/kobayashi becomes hayppier.png)

我也是自從寫了 Python 後，每次考試都考 100 分呢（並沒有）
所以大家一起來寫 Python 吧 🐍
那寫 Python 的人最好的交流平台是什麼呢 🤔
當然是 [PyCon TW](https://tw.pycon.org/) 啊 🤩
來當 PyCon TW 志工，跟大家交流 Python，變成一個開朗的人吧 💪

## One more thing
去年七月一場不幸的縱火案，大大的重創了京都動畫
PyCon JP 2019 時，我也去了鷲宮神社留下我的祝福
不會日文的我，就只簡單的寫了 **Pray for Kyoani**

![pray for kyoani](/images/posts-image/2020-will-kobayashi-s-code-encounter-sql-injection/pray for kyoani.jpg)

即便如此，京阿尼還是很快就站起來
一年過後的現在宣布「小林家的龍女僕將於 2021 年開播 」🎉

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">TVアニメ第2期「小林さんちのメイドラゴンS」2021年放送決定！SuperでSupremeなSecond lifeがStartします！<br>そして、メイドラゴンS(読み:エス)ティザービジュアル公開！ティザーサイトもぜひチェックお願いします！　<a href="https://t.co/pKOgbEe3sL">https://t.co/pKOgbEe3sL</a> <a href="https://twitter.com/hashtag/meidragon?src=hash&amp;ref_src=twsrc%5Etfw">#meidragon</a> <a href="https://t.co/XoyiBPbnvt">pic.twitter.com/XoyiBPbnvt</a></p>&mdash; TVアニメ「小林さんちのメイドラゴンS」公式 (@maidragon_anime) <a href="https://twitter.com/maidragon_anime/status/1292838380187746305?ref_src=twsrc%5Etfw">August 10, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
