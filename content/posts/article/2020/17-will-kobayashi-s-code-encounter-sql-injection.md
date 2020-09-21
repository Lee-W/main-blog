Title: 小林的程式會不會遇到 SQL Injection
Date: 2020-09-22 11:00
Category: Tech
Tags: Python, Animate
Slug: will-kobayashi-s-code-encounter-sql-injection
Authors: Lee-W
Status: draft

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
sql_str = "SELECT * FROM users WHERE (name = '" + username + "') and (pw = '"+ password +"');"
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
（p.s. web 跟 py 中間的`.` 是必要的，因為真的有個套件叫 webpy......）

```sh
poetry add web.py==0.39
```

很不幸的，如果你使用的是 Python 3，會遇到以下的錯誤訊息

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
這裏主要做了三件事

1. 用 `sqlite3` 跟 "kobayashi.db" 建立連線
2. 建立 `USER` 資料表
3. 將 kobayashi, tohru, kanna, elma 新增到 `USER` 資料表中

```python
import sqlite3


def init_db():
    # connect and create "kobayashi.db"
    conn = sqlite3.connect("kobayashi.db")

    # create USER table
    create_table_sql = """
    CREATE TABLE `USER` (
        `account`	TEXT NOT NULL UNIQUE,
        `password`	TEXT NOT NULL,
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
這裡實作的 `login` 函式會把使用者輸入的 account 跟 password 直接帶入 `where`
如果在資料庫找到正確的匹配，就會回傳找到的第一筆 user，否則回傳 `None`

```python
from typing import Optional, Tuple

import web


def login(account: str, password: str) -> Optional[web.utils.Storage]:
    result_set = db.select(
        "USER", where=f"account ='{account}' AND password='{password}'"
    )
    user = result_set.first()
    if user:
        print("login succeeded")
        return user
    else:
        print("wrong username or password")
        return None
```

接著使用三個案例來做測試

1. 錯誤的帳號密碼 -> 不應該取得 user
2. 正確的帳號密碼 -> 應該取得 user
3. SQL injection -> 理想上，也不該取得 user

```python
if __name__ == "__main__":
    db = web.database(dbn="sqlite", db="kobayashi.db")

    print(login("kobayashi", ""))
    print(login("kobayashi", "1"))
    print(login("1' OR '1'='1", "1' OR '1'='1"))
```

但這個世界始終不理想，包含了 SQL injection 的程式還是成功取得 user
之所以只取到一筆 user，單純只是因為我只回傳一個物件，但這段 SQL 是能取到整個資料庫的 user 的

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
修正的方式也很簡單，只要在呼叫 select 的時候用 `vars` 將參數帶進 `where` 即可
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
接下來就是冗長的紀錄我追 web.py 原始碼的過程

### pdbpp
為了寫這篇文章，大幅的提升我對 pdb 的熟悉度
剛好聽到廣播 [Python Bytes](https://pythonbytes.fm/) 推薦的 [pdbpp](https://github.com/pdbpp/pdbpp) 就順手玩了一下
安裝 `pdbpp`後，它會取代原生的 `pdb`
主要有這兩個功能比 `pdb` 好用

1. syntax highlight (其實 `ipdb` 也做得到)
2. sticky mode（在除錯器的上方一直顯示目前追到的程式碼）

順便記錄一下常用到的 pdbpp 指令

* `n`: 下一行
* `s`: 進到函式內
* `p [var]` (e.g., `p locals()`): 印出 var
* `args`: 印出參數
* `ll`: 顯示現在在原始碼的哪裡（原本 pdb 的 longlist）

### 追 web.py 原始碼
首先，從 `login` 呼叫的 `db.select` 函式開始，它在 [web/db.py#L845](https://github.com/webpy/webpy/blob/0.40/web/db.py#L845)

跑完 874 行的 list comprehension 後，`clauses` 看起來已經將 SQL injection 的問題解決

```pdb
(Pdb++) p clauses
[<sql: 'SELECT *'>, <sql: 'FROM USER'>, <sql: 'WHERE account ="1\' OR \'1\'=\'1" AND password="1\' OR \'1\'=\'1"'>]
```

所以接著要去追 [934行](https://github.com/webpy/webpy/blob/0.40/web/db.py#L934) 的`gen_clause`
當輸入的參數 sql 是 `WHERE` 時，會執行到 948 行的 `nout = reparam(val, vars)`

```pdb
(Pdb++) p sql
'WHERE'

(Pdb++) p val
'account =$account AND password=$password'

(Pdb++) p vars
{'account': "1' OR '1'='1", 'password': "1' OR '1'='1"}
```

再來看 [344行](https://github.com/webpy/webpy/blob/0.40/web/db.py#L344) 的 `reparam`
因為只會跑到 `safteval`
所以又要跳到 [1699行](https://github.com/webpy/webpy/blob/0.40/web/db.py#L1699)
此時帶入的參數會是

* text = `'account =$account AND password=$password'`
* mapping = `{'account': "1' OR '1'='1", 'password': "1' OR '1'='1"}`

1700 行的 `Parser` 解析出的 node 則是長這樣

```pdb
(Pdb++) p list(nodes)
[Node('text', 'account =', None), Node('param', 'account', None), Node('text', ' AND password=', None), Node('param', 'password', None)]
```

1701行會執行到 [1703行](https://github.com/webpy/webpy/blob/0.40/web/db.py#L1703) 的 `eval_node`
`self.eval_expr` 主要的功用只是讓 `node[1]` 才能抓到 `"1' OR '1'='1"` ，重點在 `sqlquote`
所以就要再去追 [463行](https://github.com/webpy/webpy/blob/0.40/web/db.py#L463)
在 475 行， `"1' OR '1'='1"` 會被初始成一個 `SQLParam` ，然後再產生一個 `SQLQuery` 物件
這時 `eval_node` 就會回傳 `<sql: '"1\' OR \'1\'=\'1"'>` (`SQLQuery` 物件)

回到 `safeeval`
透過 `[self.eval_node(node, mapping) for node in nodes]` 所產生，進到 `SQLQuery.join` 的值會是 `['account =', <sql: '"1\' OR \'1\'=\'1"'>, ' AND password=', <sql: '"1\' OR \'1\'=\'1"'>]`

那就繼續回去追 [254行](https://github.com/webpy/webpy/blob/0.40/web/db.py#L254) 的 `join`
277 ~ 285 行的 for loop 執行完會產生一個新的 target (`SQLQuery` 物件)
裡面的內容如下

```pdb
(Pdb++) p target.items
['account =', <param: "1' OR '1'='1">, ' AND password=', <param: "1' OR '1'='1">]

(Pdb++) p target
<sql: 'account ="1\' OR \'1\'=\'1" AND password="1\' OR \'1\'=\'1"'>

(Pdb++) p target.values()
["1' OR '1'='1", "1' OR '1'='1"]

(Pdb++) p target.query()
'account =%s AND password=%s'
```

這時候回傳的 `SQLQuery` 物件已經把 query 跟要帶入的值分開儲存
回傳回 948 行後，會在 956 行透過 `xjoin` 跟字串 `WHERE` 整合
字串跟 `SQLQuery` 相加的行為被定義在 [196 行](https://github.com/webpy/webpy/blob/0.40/web/db.py#L196) 的 `__radd__`

再來就可以回到最原本的 [874行](https://github.com/webpy/webpy/blob/0.40/web/db.py#L874) 的 `clauses`
在 879行會 `clauses` 的三個 `SQLQuery`物件 變成一個 `SQLQuery` 物件

最後產生的 qout 會是

```pdb
(Pdb++) p qout
<sql: 'SELECT * FROM USER WHERE account ="1\' OR \'1\'=\'1" AND password="1\' OR \'1\'=\'1"'>
```

最後就要看 884 行的 `self.query(qout, processed=True)` 是不是真的會以參數化的方式執行這段 SQL
接下來要看[807 行](https://github.com/webpy/webpy/blob/0.40/web/db.py#L807)中 `query` 函式的實作
執行到 831 行 `self._db_execute(db_cursor, sql_query)` 才會用到傳進來的 `sql_query`
在 [750行](https://github.com/webpy/webpy/blob/0.40/web/db.py#L750) `_db_execute`
會先在 756 行的 `_process_query` 產生要執行的 SQL query
而它會在[775行](https://github.com/webpy/webpy/blob/0.40/web/db.py#L775)將 `query`, `params` 分別取出，他們分別的回傳值會是

* query = `'SELECT * FROM USER WHERE account =? AND password=?'`
* params = `["1' OR '1'='1", "1' OR '1'='1"])`

757 行的`out = cur.execute(query, params)` 就會拿他們做 SQL 查詢，所以就不會遇到 SQL injection 了

### hmm... 原本好像是要追 delete 才對
顧著重現維基百科的例子，跟找到為什麼，竟然忘記了原本的目的
不過我想本質應該還是相同的
有興趣的話，可以拿以下這段 SQL 來測測看 delete 的 SQL injection 是不是真的能清空整個資料表
**disclaimer: 請不要拿它用在任何的 production 環境**

```sql
DELETE FROM USER WHERE account = '' OR ''=''
```

![xkcd joke](https://imgs.xkcd.com/comics/exploits_of_a_mom.png)

> 你是不是真的把你的兒子取名為 `Rober'); DROP TABLE Students;`

## 結語
我完全不是資訊安全的專家，只是抱持著對京都動畫和 Python 的喜愛來追這段程式碼
如果有說錯或可以補充的部分，再麻煩留言讓我知道 🙏

其實小林家的龍女僕，還有其他場景也有出現 Python
像是這段說小林自從開始寫 Python 後變得開朗了許多呢（誤

![kobayashi becomes hayppier](/images/posts-image/2020-will-kobayashi-s-code-encounter-sql-injection/kobayashi becomes hayppier.png)

所以大家一起來寫 Python 吧
那寫 Python 的人最好的交流平台是什麼呢？
當然是 [PyCon TW](https://tw.pycon.org/) 啊！
來當 PyCon TW 志工，跟大家交流學 Python，變成一個開朗的人吧 💪

## One more thing
小林家的龍女僕宣佈將於 2021 年開播 🤩

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">TVアニメ第2期「小林さんちのメイドラゴンS」2021年放送決定！SuperでSupremeなSecond lifeがStartします！<br>そして、メイドラゴンS(読み:エス)ティザービジュアル公開！ティザーサイトもぜひチェックお願いします！　<a href="https://t.co/pKOgbEe3sL">https://t.co/pKOgbEe3sL</a> <a href="https://twitter.com/hashtag/meidragon?src=hash&amp;ref_src=twsrc%5Etfw">#meidragon</a> <a href="https://t.co/XoyiBPbnvt">pic.twitter.com/XoyiBPbnvt</a></p>&mdash; TVアニメ「小林さんちのメイドラゴンS」公式 (@maidragon_anime) <a href="https://twitter.com/maidragon_anime/status/1292838380187746305?ref_src=twsrc%5Etfw">August 10, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
