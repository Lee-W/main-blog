Title: PyCon TW 2017 - Sprint
Date: 2017-06-17 16:07
Category: Tech
Tags: Python, Conference, PyCon
Slug: PyCon-TW-2017-Sprint
Authors: Lee-W
Summary:
Series: PyCon TW 2017

這天的 Sprint 是由今年的 Keynote Speaker - Russell Keith-Magee 帶來他的開源專案[BeeWare](https://pybee.org)
讓大家一起來貢獻
這個專案還蠻有趣的
主要就是要讓 Python 能在各平台上跑 (i.e. web, mobile)

<!--more-->

而且這個專案對新手還蠻友善的，文件中就有提供[First Time Contributor](https://pybee.org/contributing/how/first-time/what/)
第一次貢獻的人建議貢獻的專案是[voc](https://github.com/pybee/voc)(Android) 和[batavia](https://github.com/pybee/batavia)(JavaScript)
而且在裡面的 issue 還會標注 first timer only
![first-timer-only]({static}/images/posts-image/2017-06-12-PyCon-TW-2017-Sprint/1-new-comer.png)

雖然我其實對 Java 跟 JavaScript 都不熟
但比起來還是對 JavaScript 多了一點愛
所以我就來貢獻 batavia 了

雖然其實我的貢獻大多就是文件上少寫跟一些錯誤
最後還有幫 Python 的 list 轉成 js 加了幾個小 method
原本想解決 args 跟 kwargs 的 issue，但果然還是對 JS 太不熟了ＱＱ
不過覺得整體來說是蠻好玩的

Russell 都會很友善地回答問題
像我一開始採的雷就是 batavia 還沒支援到 Python3.6，他也很熱心幫我解決
我問了好幾個專案的小問題，Russell 都會說 "That's can be a pull request"
只要送了 PR 就可以得到[Challenge Coins](https://pybee.org/contributing/challenge-coins/)
拿到這個 challenge coin 其實還蠻開心的 xd

![Challenge Coin]({static}/images/posts-image/2017-06-12-PyCon-TW-2017-Sprint/2-challenge-coin.jpg){: style="width:30%"}

最後再附上在 twitter 上，這次參與 spinrt 的大合照
![all]({static}/images/posts-image/2017-06-12-PyCon-TW-2017-Sprint/3-all.jpg){: style="width:50%"}

2017/6/22
折騰了許久，我的[PR](https://github.com/pybee/batavia/pull/569) 終於被 merge 回 batavia 了 XD

---

這次的 PyCon 2017 大致就到這裡結束了
這幾篇文章大概先整理了，當時做的筆記
也許之後有時間，再好好看一次影片跟 Slide，重新整理一下所有的內容
