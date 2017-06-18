---
Title: PyCon TW 2017 - Day 3
Date: 2017-06-16 16:07
Category: Python
Tags: PyCon
Slug: PyCon-TW-2017-Day3
Authors: Lee-W
Summary: 
Series: PyCon TW 2017
---

* [[Keynote] From Little Tinhs, Big Things Grow](#1)
* [比美麗的湯更美麗：pyquery](#2)
* enjoy type hinting and its benefits (我很想聽這場，不過還是先跑去聽unconf了xd)
	* [slide](https://www.slideshare.net/masahitojp/the-benefits-of-type-hintss)
	* [共筆](https://hackfoldr.org/pycontw2017/https%253A%252F%252Fhackmd.io%252Fs%252FHkqR2Dvkb)
* Coding test-driven Python package with CI and cloud
* [Unconf](#5)
* [Lighning Talk](#6)

---

<a name='1'></a>
## [Keynote] From Little Things, Big things grow.

![Chinese Intro]({filename}/images/posts-image/2017-06-11-PyCon-TW-2017-Day3/1-Keynote-Chineses.png)

Russell開場就講了一串中文，引來如雷的掌聲xd

他的介紹也很有趣xd
```
他剩下兩洲就能完成 Python 會議基調演講全大洲制霸；
只要企鵝們願意舉辦 PyCon 南極洲，他很樂意提供演說。
```
同時，他也在這次PyCon的Sprint帶來專案跟大家分享
這會在我的下一篇文章提到

不過Russell的英文語速就真的有點快超過我能理解的語速了ＱＱ
所以這場也有點記不了太多東西

- [共筆](https://hackfoldr.org/pycontw2017/https%253A%252F%252Fhackmd.io%252Fs%252FryvqnPv1-)

`Work in Progress`

### Technical issues are often social
- Backward Compatibility matters
	- But it also has a price
		- Hard to introduce new features
- Timing matters
- Messaging matters
- Reading the tea leaves (Trend?)

### Tool and ecosystem
- Community matteres
- Accessibility
- Toxic shock
- Denial is not a river in Egypt
	- Complainting matters
- Codes of Conduct in practice 
- Outreach is important
- The moral high road is littered with the corpses of our allies
- Free software: Theory and practice
- Patches welcome
- Dreaming a bigger dream
- Make it easy to spend mony and recevie money
- Make it easy to do the right things
- Don't assume resources are free
- Enabling Diversity

---

<a name='2'></a>
## 比美麗的湯更美麗：pyquery
- [slide](https://aji.tw/slides/pycon2017/#/)

`Work in Progress`
裝起來的問題，通常是lxml

.html是tag內的內容
.outer_html是包含了tag


pyquery一個打requests + bs4
還能吃selenium，當opener

---

<a name='3'></a>
## Write Elegant Concurrent Code in Python
- [slide](https://speakerdeck.com/mosky/elegant-concurrency)
- [共筆](https://hackfoldr.org/pycontw2017/https%253A%252F%252Fhackmd.io%252Fs%252FHkqR2Dvkb)
- [Sample Code](https://github.com/moskytw/elegant-concurrency-lab)

`Work in Progress`
Concurreny: 一段時間內同時跑
Parallel: 一個時間點同時跑

### Why Concurrency?
- Get the machine into full play! 不要讓CPU空轉！
- Capacity
	- CPU
	- IO 
		- Network

### Concurrency isHard 
- queue (sync queue)
- thread


### Communicating Sequential Process (CSP)
Go採用CSP的機制

Python也不建議用Lock跟Share Memory的方式做Concurrency

### Channel-Basesd Concurrency
Python的thread對os的thread是一對一的

Python的daemon thread並不是unix的thread

### Concurrent Units

不要混用各種Concurrent Units

------
<a name='5'></a>
## Unconf
- [共筆](https://hackfoldr.org/pycontw2017/https%253A%252F%252Fhackmd.io%252Fs%252FrkMXWDTyb)
`Work in Progress`
### 大會遊戲 line chatbot 黑白亂做
[Source Code](https://github.com/adrianliaw/quizbot-2017)

### 懶得答題？寫個 bot 來幫你刷榜
[slide](https://github.com/aweimeow/PyConTW2017-UnConf-Slide)

###  What Steve Jobs Taught Me about Software Development and Life in General
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

就像jserv的slide上說的

```
每年的pycon好像都有其他語言的東西混進來，像是15年有人根本是在講d3.js
只是用python幫忙準備資料;
今年是有人全部都在講Rust，只是我們用Rust寫了個python module XDDD
```

Lightning Talk馬上就出現一個julia了xddd
記得15年的PyCon超多Julia的
連keynote speaker都有


