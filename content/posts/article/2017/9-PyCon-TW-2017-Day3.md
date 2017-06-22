Title: PyCon TW 2017 - Day 3
Date: 2017-06-11 09:00
Modified: 2017-06-18 14:08
Category: Python
Tags: PyCon
Slug: PyCon-TW-2017-Day3
Authors: Lee-W
Summary: 
Series: PyCon TW 2017


這天就是PyCon的最後一天了
聽說這是PyCon第一次引入Unconf
今年Unconf都還蠻有趣的，讓我一直猶豫到底要一般議程還是Unconf
不過Unconf那邊聲音就有點糊聽不太清楚
不知道是不是R4場地的關係

<!--more-->

---

## 議程

* [[Keynote] From Little Things, Big Things Grow](#1)
* [比美麗的湯更美麗：pyquery](#2)
* enjoy type hinting and its benefits (我很想聽這場，不過還是先跑去聽unconf了xd)
	* [slide](https://www.slideshare.net/masahitojp/the-benefits-of-type-hintss)
	* [共筆](https://hackfoldr.org/pycontw2017/https%253A%252F%252Fhackmd.io%252Fs%252FHkqR2Dvkb)
* Coding test-driven Python package with CI and cloud
* [Unconf](#5)
* [Lightning Talk](#6)

---

<a name='1'></a>
## [Keynote] From Little Things, Big things grow.

![Chinese Intro]({filename}/images/posts-image/2017-06-11-PyCon-TW-2017-Day3/1-Keynote-Chineses.png)

Russell開場就講了一串中文，引來如雷的掌聲xd

他在PyCon官網的介紹也很有趣xd
```
他剩下兩洲就能完成 Python 會議基調演講全大洲制霸；
只要企鵝們願意舉辦 PyCon 南極洲，他很樂意提供演說。
```
同時，他也在這次PyCon的Sprint帶來專案跟大家分享

不過Russell的英文語速就真的有點快，超過我能好好做筆記的語速了ＱＱ

- [共筆](https://hackfoldr.org/pycontw2017/https%253A%252F%252Fhackmd.io%252Fs%252FryvqnPv1-)


### Technical issues are often social
- Backward Compatibility matters
	- But it also has a price
		- Hard to introduce new features
- Timing matters
- Messaging matters
- Reading the tea leaves (Trend?)
- [The Kick Ass Curve](http://headrush.typepad.com/creating_passionate_users/2005/10/getting_users_p.html)

### Tool and ecosystem
- Community matters

### Accessibility
- Toxic shock
- Denial is not a river in Egypt
	- Complaining matters
- Codes of Conduct in practice
- Outreach is important

### Patches welcome

### Develop a funding culture
- Make it easy to
	- spend money and receive money
	- do the right things
- Don't assume resources are free

### Q & A
這好像是我第一次在R0舉手提問
最後因為時間關係沒被叫到ＱＱ
不過我還是跑到前面去問Russell，如何在Backward Compatibility和New Fatures中取捨
Russell的回答是如果專案已經持續很長的一段時間，並且有一定的使用者
Backward Compatibility就是一件很重要的事
因為我們並不會希望以前的使用者不能在使用
不過如果是新開始的專案，那就從新的開始就好
像他現在的[Bee Ware](https://pybee.org)就是全用Python3

下午Russell會給一場跟Bee Ware有關的Talk - [Stranger in Strange Land](https://hackmd.io/s/HkqR2Dvkb#1300-1345talk-stranger-in-a-strange-land)
不過因為標了很高的難度，想說我應該也聽不懂，也先沒去聽了xd

---

<a name='2'></a>
## 比美麗的湯更美麗：pyquery
- [slide](https://aji.tw/slides/pycon2017/#/)

### [pyquery](https://github.com/gawel/pyquery)
- 用jquery的方式來做parsing
- 可以做crawling (一個lib就做了requests + bs4的事啊！)
- 可以拿selenium當opener

裝不起來的問題，通常是因為lxml沒裝好

感覺是一個很值得期待的library
下次要寫爬蟲，再拿它來試試看

---

<a name='3'></a>
## Write Elegant Concurrent Code in Python
- [slide](https://speakerdeck.com/mosky/elegant-concurrency)
- [共筆](https://hackmd.io/s/HkqR2Dvkb#1115-1200-talk-write-elegant-concurrent-code-in-python)
- [Sample Code](https://github.com/moskytw/elegant-concurrency-lab)


Concurreny: 一段時間內同時跑
Parallel: 一個時間點同時跑

### Why Concurrency?
- Get the machine into full play! 不要讓CPU空轉！
- 通常不會用Python解CPU Bound的問題，而是I/O Bound的問題

聽完這場，感嘆自己真的對Concurrent還是不太懂＠＠
雖然我沒記什麼筆記
不過Slide很清楚，共筆也記了很多
還附上Sample Code了
哪天比較懂Concurrent的時候再回來看應該會比較有感覺吧

------
<a name='5'></a>
## Unconf
- [共筆](https://hackfoldr.org/pycontw2017/https%253A%252F%252Fhackmd.io%252Fs%252FrkMXWDTyb)

### 大會遊戲 line chatbot 黑白亂做
[Source Code](https://github.com/adrianliaw/quizbot-2017)

### 懶得答題？寫個 bot 來幫你刷榜
- [slide](https://github.com/aweimeow/PyConTW2017-UnConf-Slide)
- [Source Code](https://github.com/aweimeow/PyConTW2017-Quiz-Solver)

跟著上面那一個Unconf做的大會chat bot
就有會眾分享如何寫一個bot自動去達大會的題目xdd
覺得很有趣


###  What Steve Jobs Taught Me about Software Development and Life in General
這就是Carosell待過Apple的VP
大致上覺得跟[少，但是更好](http://lee-w.github.io/posts/book/2016/03/essentialism/#essentialism)

Saying, "No!" enables focus, flow, success.

- How to decide when to say "yes"?
	- The one that changes your life would be a good one. 

------

<a name='6'></a>

## Lightning Talk
- [共筆](https://hackfoldr.org/pycontw2017/https%253A%252F%252Fhackmd.io%252Fs%252FHJu2JvTyW)

Lightning Talk大概是PyCon最歡樂的時候了
因為只有5分鐘，不然就要被拔線了
大家都得講得很快

今年的PyCon金句大概就是Hisahiro Ohmura推坑PyCon JP的

![Buy First, Consider Second]({filename}/images/posts-image/2017-06-11-PyCon-TW-2017-Day3/2-buy-first.jpg)

```
聽不懂日文？
沒關係
我也聽不太懂中文
```

另外，就像jserv的slide上說的

```
每年的pycon好像都有其他語言的東西混進來，像是15年有人根本是在講d3.js
只是用python幫忙準備資料;
今年是有人全部都在講Rust，只是我們用Rust寫了個python module XDDD
```

Lightning Talk馬上就出現一個julia了xddd
記得兩年前的PyCon超多Julia的
