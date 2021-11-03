Title: PyCon TW 2017 - Day 3
Date: 2017-06-11 09:00
Modified: 2017-06-18 14:08
Category: Tech
Tags: Python, Conference, PyCon
Slug: PyCon-TW-2017-Day3
Authors: Lee-W
Series: PyCon TW 2017

這天就是 PyCon 的最後一天了
聽說這是 PyCon 第一次引入 Unconference
今年 Unconf 都還蠻有趣的，讓我一直猶豫到底要一般議程還是 Unconference
不過 Unconference 那邊聲音就有點糊聽不太清楚
不知道是不是 R4 場地的關係

<!--more-->

---

## 議程

* [[Keynote] From Little Things, Big Things Grow](#1)
* [比美麗的湯更美麗：pyquery](#2)
* [Write Elegant Concurrent Code in Python](#3)
* enjoy type hinting and its benefits (我很想聽這場，不過還是先跑去聽 Unconference 了 XD)
    * [slide](https://www.slideshare.net/masahitojp/the-benefits-of-type-hintss)
    * [共筆](https://hackfoldr.org/pycontw2017/https%253A%252F%252Fhackmd.io%252Fs%252FHkqR2Dvkb)
* Coding test-driven Python package with CI and cloud
* [Unconference](#5)
* [Lightning Talk](#6)

---

<a name='1'></a>

## [Keynote] From Little Things, Big things grow.

![Chinese Intro](/images/posts-image/2017-06-11-PyCon-TW-2017-Day3/1-Keynote-Chineses.jpg)

Russell 開場就講了一串中文，引來如雷的掌聲 xD
他在 PyCon 官網的介紹也很有趣 xD

```text
他剩下兩洲就能完成 Python 會議基調演講全大洲制霸；
只要企鵝們願意舉辦 PyCon 南極洲，他很樂意提供演說。
```

同時，他也在這次 PyCon 的 Sprint 帶來專案跟大家分享

不過 Russell 的英文語速就真的有點快，超過我能好好做筆記的語速了 QQ

* [共筆](https://hackfoldr.org/pycontw2017/https%253A%252F%252Fhackmd.io%252Fs%252FryvqnPv1-)

### Technical issues are often social

* Backward Compatibility matters
    * But it also has a price
        * Hard to introduce new features
* Timing matters
* Messaging matters
* Reading the tea leaves (Trend?)
* [The Kick Ass Curve](http://headrush.typepad.com/creating_passionate_users/2005/10/getting_users_p.html)

### Tool and ecosystem

* Community matters

### Accessibility

* Toxic shock
* Denial is not a river in Egypt
    * Complaining matters
* Codes of Conduct in practice
* Outreach is important

### Patches welcome

### Develop a funding culture

* Make it easy to
    * spend money and receive money
    * do the right things
* Don't assume resources are free

### Q & A

這好像是我第一次在 R0 舉手提問
最後因為時間關係沒被叫到 QQ
不過我還是跑到前面去問 Russell，如何在 Backward Compatibility 和 New Fatures 中取捨
Russell 的回答是如果專案已經持續很長的一段時間，並且有一定的使用者
Backward Compatibility 就是一件很重要的事
因為我們並不會希望以前的使用者不能在使用
不過如果是新開始的專案，那就從新的開始就好
像他現在的[Bee Ware](https://pybee.org) 就是全用 Python3

下午 Russell 會給一場跟 Bee Ware 有關的 Talk - [Stranger in Strange Land](https://hackmd.io/s/HkqR2Dvkb#1300-1345talk-stranger-in-a-strange-land)
不過因為標了很高的難度，想說我應該也聽不懂，也先沒去聽了 xd

---

<a name='2'></a>

## 比美麗的湯更美麗：pyquery

* [slide](https://aji.tw/slides/pycon2017/#/)

### [pyquery](https://github.com/gawel/pyquery)

* 用 jquery 的方式來做 parsing
* 可以做 crawling ( 一個 lib 就做了 requests + bs4 的事啊！ )
* 可以拿 selenium 當 opener

裝不起來的問題，通常是因為 lxml 沒裝好

感覺是一個很值得期待的 library
下次要寫爬蟲，再拿它來試試看

---

<a name='3'></a>

## Write Elegant Concurrent Code in Python

* [slide](https://speakerdeck.com/mosky/elegant-concurrency)
* [共筆](https://hackmd.io/s/HkqR2Dvkb#1115-1200-talk-write-elegant-concurrent-code-in-python)
* [Sample Code](https://github.com/moskytw/elegant-concurrency-lab)

Concurreny: 一段時間內同時跑
Parallel: 一個時間點同時跑

### Why Concurrency?

* Get the machine into full play! 不要讓 CPU 空轉！
* 通常不會用 Python 解 CPU Bound 的問題，而是 I/O Bound 的問題

聽完這場，感嘆自己真的對 Concurrent 還是不太懂＠＠
雖然我沒記什麼筆記
不過 Slide 很清楚，共筆也記了很多
還附上 Sample Code 了
哪天比較懂 Concurrent 的時候再回來看應該會比較有感覺吧

---

<a name='5'></a>

## Unconference

* [共筆](https://hackfoldr.org/pycontw2017/https%253A%252F%252Fhackmd.io%252Fs%252FrkMXWDTyb)

### 大會遊戲 line chatbot 黑白亂做

[Source Code](https://github.com/adrianliaw/quizbot-2017)

### 懶得答題？寫個 bot 來幫你刷榜

* [slide](https://github.com/aweimeow/PyConTW2017-UnConf-Slide)
* [Source Code](https://github.com/aweimeow/PyConTW2017-Quiz-Solver)

跟著上面那一個 Unconference 做的大會 chat bot
就有會眾分享如何寫一個 bot 自動去達大會的題目 xdd
覺得很有趣

### What Steve Jobs Taught Me about Software Development and Life in General

這就是 Carosell 待過 Apple 的 VP
大致上覺得跟[少，但是更好]({filename}/posts/book/05-essentialism.md#essentialism)

Saying, "No!" enables focus, flow, success.

* How to decide when to say "yes"?
    * The one that changes your life would be a good one.

---

<a name='6'></a>

## Lightning Talk

* [共筆](https://hackfoldr.org/pycontw2017/https%253A%252F%252Fhackmd.io%252Fs%252FHJu2JvTyW)

Lightning Talk 大概是 PyCon 最歡樂的時候了
因為只有 5 分鐘，不然就要被拔線了
大家都得講得很快

今年的 PyCon 金句大概就是 Hisahiro Ohmura 推坑 PyCon JP 的

![Buy First, Consider Second](/images/posts-image/2017-06-11-PyCon-TW-2017-Day3/2-buy-first.jpg)

```text
聽不懂日文？
沒關係
我也聽不太懂中文
```

另外，就像 jserv 的 slide 上說的

```text
每年的 pycon 好像都有其他語言的東西混進來，像是 15 年有人根本是在講 d3.js
只是用 python 幫忙準備資料 ;
今年是有人全部都在講 Rust，只是我們用 Rust 寫了個 python module XDDD
```

Lightning Talk 馬上就出現一個 julia 了 xddd
記得兩年前的 PyCon 超多 Julia 的
