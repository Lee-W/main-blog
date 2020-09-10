Title: 小林的程式會不會遇到 SQL Injection
Date: 2019-09-30 00:00
Category: Tech
Tags: Python, Animate
Slug: will-kobayashi-s-code-encounter-sql-injection
Authors: Lee-W
Status: draft

## 前言

最近開始看了京阿尼的作品[小林家的龍女僕](https://zh.wikipedia.org/wiki/%E5%B0%8F%E6%9E%97%E5%AE%B6%E7%9A%84%E9%BE%8D%E5%A5%B3%E5%83%95)

第一集就看到小林寫的也是 Python 就很開心的分享了
![-w560](/images/posts-image/will-kobayashi-s-code-encounter-sql-injection/15723300258537.jpg)

然後就有強大的 CTO 來問我會不會有 SQL injection，才讓我開始了這一串奇怪的追程式碼的過程
![IMG_4508](/images/posts-image/will-kobayashi-s-code-encounter-sql-injection/IMG_4508.png)

## 看看其他人怎麼做

單看程式碼其實很難直接下定論
畢竟那段的 key 根本就不會被帶入 `session_id=$key`，誰知道 db 怎麼實作的 xD

---

恩，真的有人知道了
在我搜尋的過程中，就有找到兩篇文在探討
看來後面還有很多 Python 的程式碼呢

[如何评价京都动画2017年1月新作 小林家的龙女仆?](https://www.zhihu.com/question/51933296/answer/143492909)

這篇有稍微討論到，京阿尼用這段程式碼會不會有授權問題

[小林さんちのメイドラゴンで出てきたコード（小林さんを探せ！）](https://qiita.com/ygkn/items/6b3be1afa31e4092826e)

這篇則是想直接找到小林到底是誰 X

[Ponkatsu - Tag: sql injection](https://ponkatsu807462913.wordpress.com/tag/sql-injection/)

另外有找到這則回覆是說會有 SQL injection
但身為 Python 工程師還是要眼見為憑啊，所以來看程式碼吧

[webpy - web/session.py](https://github.com/webpy/webpy/blob/master/web/session.py)

## 2019

[session.py#L336](https://github.com/webpy/webpy/blob/master/web/session.py#L336)
[db.py#L859](https://github.com/webpy/webpy/blob/master/web/db.py#L859)
[db.py#L948](https://github.com/webpy/webpy/blob/master/web/db.py#L948)

```sql
CREATE TABLE `USER` (
	`account`	TEXT NOT NULL UNIQUE,
	`password`	TEXT NOT NULL,
	PRIMARY KEY(`account`)
);
```


```sql
INSERT INTO USER (account, password) VALUES ('pycontw', 'testpassword')
```

## delete

```sql
DELETE FROM USER WHERE account = '' OR ''=''
```


## Select
[SQL Injection 常見的駭客攻擊方式](https://www.puritys.me/docs-blog/article-11-SQL-Injection-%E5%B8%B8%E8%A6%8B%E7%9A%84%E9%A7%AD%E5%AE%A2%E6%94%BB%E6%93%8A%E6%96%B9%E5%BC%8F.html)

```sql
SELECT * FROM user WHERE account ='' or 1=1--' and password='';
```

完了

```python
import web
db = web.database(dbn="sqlite", db="kobayashi.db")
result_set = db.select('USER', where="account ='' or 1=1--' and password=''")
```

應該這麼做

```python
import web
db = web.database(dbn="sqlite", db="kobayashi.db")
account = "' or 1=1--"
password = "anyway"
db.select('user', where='account=$key and password=$password', vars=locals())
```

```ipython
In [9]: db.select('user', where='account=$key and password=$password', vars=locals())
0.0 (1): SELECT * FROM user WHERE account="' or 1=1--" and password='anyway'
Out[9]: <web.db.SqliteResultSet at 0x113521780>

In [10]: key = '" or 1=1--'

In [11]: db.select('user', where='account=$key and password=$password', vars=locals())
0.0 (2): SELECT * FROM user WHERE account='" or 1=1--' and password='anyway'
Out[11]: <web.db.SqliteResultSet at 0x1139148d0>
```

## 2017

但這樣其實不對
因為這是 2017 年 1 月的動畫
（我沒追漫畫，所以就不）

2014年5月10日

[git - Find commit where file was added](https://stackoverflow.com/questions/11533199/git-find-commit-where-file-was-added)

```sh
git log --diff-filter=A -- foo.js
```

fd1d69523e126cc88506ac61e504e2684fedeb0a
Sep 20, 2007

改名到 web/session.py

原本是 `trunk/web/session.py`

看來還得追下去

來自
05c8b7c743ea7d5dd6a01f091aef6f40332fd15f
Aug 23, 2007

還是看 0f2b0019e7802768aaf6178e10939934d81b265a
Fri Dec 30
![Screen Shot 2019-10-30 at 12.38.24 P](/images/posts-image/will-kobayashi-s-code-encounter-sql-injection/Screen%20Shot%202019-10-30%20at%2012.38.24%20PM.png)![Screen Shot 2019-11-10 at 10.01.35 P](/images/posts-image/will-kobayashi-s-code-encounter-sql-injection/Screen%20Shot%202019-11-10%20at%2010.01.35%20PM.png)

---


```python
import web
db = web.database(dbn="sqlite", db="kobayashi.db")

result_set = db.select('USER', where="account ='' or 1=1--' and password=''")
print(result_set.first())

# ---
db.delete('user', where="account = '' OR ''=''")

# ---
result_set = db.select('USER', where="account ='' or 1=1--' and password=''")
print(result_set.first())

# ---
db.insert('USER', account='pycontw-r1', password='testpassword')
db.insert('USER', account='pycontw-r2', password='testpassword')

# ---
account = 'pycontw-r1'
db.delete('user', where="account=$account", vars=locals())

#---

account = "'' OR ''=''"
db.delete('user', where="account=$account", vars=locals())
```
