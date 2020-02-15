Title: PyCon CA 2019
Date: 2019-12-23 17:51
Category: Tech
Tags: Python, PyCon, Conference
Slug: pycon-ca-2019
Authors: Lee-W
Summary:
Series:

隔了一個多月，終於有時間可以來補 PyCon CA 2019 的心得
這是我今年參加的第四場 PyCon
終於是因為當 Regular Talk 的講者參加

<!--more-->

當初會想投稿的原因，就單純的是被 PyCon CA 的 Organizer 在 PyCon US 的閃電秀燒到
「秋天剛好是來加拿大看楓葉的好時間」
好像還沒來過加拿大就來投稿看看吧 XD
雖然這麼說，這個想法也是擱置了好一段時間
之後開始比較認真在構思，則是因為有其他想去北美一趟的理由

想想之後也會協助 PyCon TW 2020 議程組
來當講者看看，好像也會知道大家都在幹嘛（？？？

## 講者宣傳
PyCon CA 每一位講者的議程都會發篇推特宣傳
而且會積極地邀請你一起來宣傳自己的分享
這點還蠻有趣的
![-w375](/images/posts-image/2019-12-23-pycon-ca-2019/15720217074612.jpg)

## 會場
PyCon CA 辦在一個市中心的宴會廳

![Hall way](/images/posts-image/2019-12-23-pycon-ca-2019/15770893363222.jpg)

Keynote Speaker 的演講廳完全是大家可以邊吃飯邊聽議程的 XD
![Keynote](/images/posts-image/2019-12-23-pycon-ca-2019/15770893540925.jpg)

## 議程
提醒議程的方式很好玩
走廊會閃燈，提醒大家議程即將開始
原本以為是劇場的三明三暗，但好像都會閃超過三次
但還是蠻有趣的

第一場我去聽 **Understanding autistic children using BioSensors and Python!**
稍微詳細一點的筆記我都丟在 [note](https://lee-w.github.io/pycon-note/posts/pycon-ca-2019/2019/12/understanding-autistic-children-using-bioSensors-and-python/)
這場主要在講她們如何透過 sensor 來偵測自閉症

再來我去聽 **My Favourite Errors - Tales From The Ops Side** ([note](https://lee-w.github.io/pycon-note/posts/pycon-ca-2019/2019/12/my-favourite-errors/))
主要是講各種可能遇到的 HTTP 錯誤
除了前一場本來就是我非常有興趣的議題外，這場是我覺得 PyCon CA 數一數二精彩的議程
雖然跟 Python 完全沒有直接關係 XD
後來發現講者前一段時間才在 devops day 講過同樣的講題

接下來連三場，我跑去主持人，就沒特別花時間做筆記
畢竟用非母語主持其實還是有些吃力
主持完真的太累，就一口氣休息了幾場

* **Modelling user journeys with Keras and neural networks**
    * 第一場主持的太緊張了，沒有什麼聽到 XD
* **Anomaly detection in the wild**
    * 主要講如何偵測異常值，舉的例子都還蠻有趣的
* **A Pythonista’s intro to Kafka: no, it’s not like Celery**
    * 如果對 Kafka 有興趣，這場很值得聽

第二天早上是閃電秀
登記閃電秀和其他活動的方式是上去改 PyCon CA 的 [wiki](https://github.com/pyconca/2019-wiki)
我也投了一個小小的閃電秀來宣傳一下明年的 PyCon TW ([slide](https://speakerdeck.com/leew/pycon-tw-2020-at-pycon-ca-2019))
迴響還蠻不錯的，尤其是講到台南美食的時候 XD
倒是這天因為太冷了，我有點睡過頭，差點就趕不上閃電秀...

因為我是這天的下午分享，聽的議程就比較少
印象最深刻的是 **Fun with compilers: exploring languages one Python at a time**
[GitHub]([Fun with compilers: exploring languages one Python at a time](https://github.com/pdmccormick/pyconca2019-fun-with-compilers))
之前有人問我 Python 到底是編譯還是直譯
這位講者給的答案是 Python 就只是個語言，要看用哪個 implementation 來跑
![is-python-compiled-or-interpreted](/images/posts-image/2019-12-23-pycon-ca-2019/15770893777395.jpg)

* **PySpark: avoiding common pitfalls and keeping your sanity** ([note](https://lee-w.github.io/pycon-note/posts/pycon-ca-2019/2019/12/pyspark-avoiding-common-pitfalls-and-keeping-your-sanity/))
    * PySpark 跟 Python 語法上一些不同需要注意的地方
* **How to Level Up** ([note](https://lee-w.github.io/pycon-note/posts/pycon-ca-2019/2019/12/how-to-level-up/))
    * 用什麼心態面對學習，才能讓自己的技術更上一層樓

當天因為體力跟時間的關係，還有不少議程沒聽到
這些是之後影片出來我會想要補的議程

* My Favourite Errors
* Fantastic anti-patterns and where to find them: pinpointing performance bottlenecks
* Rust accelerated Pythons
* How to build bulletproof integrations
* Forecasting and observing airfare trends using Python and neural networks
* Operator overloading: you're doing it wrong
* Put Your Data in a Box
* Python is a weirdo
* The blameless post mortem: how embracing failure makes us better
* Pull requests: merging good practices into your project

## Python Table Manners - A Clean Style
我的分享主要是整理了一大堆工具，他們可能能在開發的各個不同環節用上
我把這次的分享定位在「讓你知道有這個工具，我怎麼用它，你如果會用到，可以自己研究細節」
因為介紹了很多工具，所以沒有辦法深入討論
當初也有點擔心這樣的內容會不會太淺
出發 PyCon CA 前，有先到 Taipei.py 分享一下
得到的迴響比我預想的還好些
PyCon CA 當天來聽的人也算不少，我想應該還算成功吧

[slide](https://speakerdeck.com/leew/python-table-manners-a-clean-style-at-pycon-ca-2019)

![myself](/images/posts-image/2019-12-23-pycon-ca-2019/15770893864623.jpg)

一個有趣的小插曲是
我原本介紹了一套 Java Script 的工具 [commitizen](https://github.com/commitizen)
雖然 Python 也有 [commitizen](https://github.com/Woile/commitizen)
但一開始用的時候，遇到了很多的 bug
PyCon CA 前一個禮拜，覺得還是想介紹個 Python 的套件
就想說去貢獻看看，能不能把這些 Bug 修完
認真使用才發現功能大部分都沒問題，只是我剛好亂玩遇到 Bug......
幸運的是 [commitizen](https://github.com/Woile/commitizen) 作者回覆超快
PyCon CA 前，我就把遇到的 Bug 都修完了
既然都修完了，就順便把這段的投影片也更新一下
後來還拿著這個專案去主持一個 Sprint

## Development Sprint
參與的專案還蠻多的
在 PyCon CA 前，幾乎沒有人想填 [wiki](https://github.com/pyconca/2019-wiki)
都是到 PyCon CA 開始後，甚至是 Sprint 開始後才慢慢有專案出現 XD

![Broad](/images/posts-image/2019-12-23-pycon-ca-2019/15770894153368.jpg)

![Sprint](/images/posts-image/2019-12-23-pycon-ca-2019/15770894201423.jpg)

原則上不供餐，鼓勵你和你的夥伴一起出去吃飯
其實我覺得挺好的
雖然第二天還是訂了 Pizza XD

## 雜談
雖然今年參與的 PyCon 都有讓我覺得比起之前跟參與者的交流更多
PyCon CA 給我的感覺是所有參與者之間最沒有隔閡的
大家就是一群來這裡的 Pythonists
不會因為你有不同的身份，而有不同
但也可能是我當了志工才有這樣的感覺

紀念品也還蠻有趣的，是當地很需要的毛帽
有一度想要買，因為真的很冷...
我在加拿大期間最冷的期間就是會期這兩天
-8 度真的很瘋狂，但又不能不出門......
