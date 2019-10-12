Title: PyCon JP 2019
Date: 2019-10-12 22:30
Category: Tech
Tags: Conference, PyCon JP
Slug: pycon-jp-2019
Authors: Lee-W
Summary:
Series:

當初在 PyCon US 看到 PyCon JP 上去介紹他們自己
不知道哪根筋不對，就覺得不然就來投稿一下吧
雖然後來投稿並沒有上，但突然發現 PyCon TW 想揪團一起去

![visiting-group-post]({static}/images/posts-image/2019-10-12-pycon-jp-2019/visiting-group-post.png)

想說這次不去，說不定就不會再有這樣的揪團了
就衝動的報名下去了 XD

[TOC]

## Development Sprint
sprint 的報名有分 Leader 跟 Attendee
現場到的人大概 100 人
雖然不用錢，但就是要統計一下人數
而且他們還有不斷寄信提醒「如果無法出席，請釋出位置給想參加的人」
感覺人好像蠻多的
雖然他們的 sprint 辦在假日，這樣比好像不太公平
但感覺上比之前在台灣參加的 sprint 熱絡了不少

一開始會公佈有哪些專案可以參與
到結束前，大家各自分組討論和開發
最後來個 demo，分享大家一天的成果

總共十來個專案中，只有三個是英文的
有兩個就是台灣人 Host 的
所以就來試試看剩下的 [awaitwhat](https://github.com/dimaqq/awaitwhat) XD

awaitwhat 的目標是想挖到 async 更深的 traceback，讓 async 的除錯更方便
但我實在還沒有對 async 太熟
最後就是花了點時間對專案做了一些 refactor
雖然看起來改動很大，但其實貢獻真的很還好（笑

![sprint-demo]({static}/images/posts-image/2019-10-12-pycon-jp-2019/15700839086070.jpg)

晚餐倒是很有趣，他們好像想把餐點排成一隻蛇 xD

![sprint-dinner-snake]({static}/images/posts-image/2019-10-12-pycon-jp-2019/15700839118735.jpg)

## Welcome Party
只有上台 5 分鐘的 Lightning Talk 講者也能來參加講者晚宴（笑

場地沒有座位，只有圓桌
這樣的安排應該是方便大家隨意移動，就能促進更多人的交流
認真想想這樣的設計還蠻不錯的

然後每一個圓桌上都有啤酒 XD

![welcome-beer]({static}/images/posts-image/2019-10-12-pycon-jp-2019/15700839787175.jpg)

## PyCon JP - Day 1
如果想看每場 talk 的細節的話，筆記都整理 PyCon TW Visiting Group 的[共筆](https://hackmd.io/pYYzA4hLROGFKbXR0QMTMA?view)上了
我就不聊每一場的細節了

一開始有點不習慣他們的場地
Keynote 演講的空間後面馬上就是海報，在更後面就是贊助商
有時候聲音就會蠻發散的
不過後來聽前輩們說好像大部分的場地都是這樣
中研院真的是場地太好
倒是 Keynote 會有英日互轉的即時口譯，覺得還挺不錯的

海報的部分則是要感謝 Ohmura-san 幫 PyCon TW 做了精美海報 🙏
![poster]({static}/images/posts-image/2019-10-12-pycon-jp-2019/15700840034582.jpg)

整天下來我最喜歡的 talk 是 Takanori-san 的 [Automate the Boring Stuff with Slackbot](https://www.youtube.com/watch?v=rbNI2LzwaqE)
雖然只是被一些有趣的點打到了（笑
今年他總共參加了 8 場 PyCon
而且大多都是講者，就算不是講者也有帶海報過去
雖然 Noah 好像今年參加了 11 場？
後來跟一些外國講者聊到 Noah，他們說不管到哪場 PyCon 都會遇到他 XD

![pycon-tour]({static}/images/posts-image/2019-10-12-pycon-jp-2019/15700840070533.jpg)

![programmer-is-lazy]({static}/images/posts-image/2019-10-12-pycon-jp-2019/15700840091662.jpg)

因為明年是 Python 2 的 End of Life
![262688.art]({static}/images/posts-image/2019-10-12-pycon-jp-2019/262688.art.jp2){: style="height:150px;width:150px"}
<small>Designed by [Lisa Roach](https://twitter.com/lisroach)</small>

有好幾場 Talk 都跟 Python 2 to 3 相關，像是 ["It’s 2019 and I’m still using Python 2. Should I be worried?"](https://www.youtube.com/watch?v=8a_TEjCl8NQ) 跟 Kir 大大的 ["SupportingPython3 in Large Scale Project"](https://www.youtube.com/watch?v=BS-HyV3V7GI)

對於議程安排覺得還蠻不錯的一點是「同一個時段至少會有一場英文的 talk」
外國來的會眾不會在任何一個時段因為聽不懂日文就完全沒有能聽的 talk
後來跟他們聊到，這好像也是他們近期在努力的目標之一

### Peer Reviewed Lightning Talk
最後想提到我的 Lightning Talk

![lightning]({static}/images/posts-image/2019-10-12-pycon-jp-2019/15700840162587.jpg)

[slide](https://docs.google.com/presentation/d/1buthYkXvgjbrvb3CT9eXUKklRZOTPc4aN3RgH1PZayk/edit#slide=id.g5cf8cd871b_0_9) 跟 [video](https://www.youtube.com/watch?v=7U2D5tcMZb4&t=1110s) 都已經釋出了

PyCon JP 的 Lightning Talk 還蠻特別的
分為 **Peer Reviewed** 跟 **Same Day**
**Peer Reviewed** 必須先投稿，也需要經過審稿
(PyCon TW Visiting Group 包下了所有英文的 Peer Reviewed Lightning Talk XD)
**Same Day** 則是當天投稿，當場抽籤決定誰是講者

我的 Lightning Talk 主要是要介紹 PyCon TW
我用「與人交流」作為 "How to get more than PyCon in a PyCon" 的核心
每一個點再帶到 PyCon TW 在做的一些努力之類的
但其實到了日本才發現，這邊的會眾超積極在跟人交流的啊 XDDD
果然只是我以前都待在舒適圈太開心，都只跟原本的朋友聊聊天

有一個小插曲是
大家湧入主會場的時候，網路就開始不穩定了......
因為我到當天都還有再改 slide，還沒來得及抓最新的離線版本，讓我著實抖了一下
Peter 說得對 "Never live Demo. Never Internet......"
還好在我上台前，網路有稍微恢復，才沒有出包

雖然只有 5 分鐘，但第一次上台給全英文的 talk 還是挺緊張的
![down-stair]({static}/images/posts-image/2019-10-12-pycon-jp-2019/15700840143063.jpg)

原本 PyCon JP 的 party 結束後
Takanori-san 很熱情的帶我們去續攤
![beer]({static}/images/posts-image/2019-10-12-pycon-jp-2019/15700840215951.jpg)

## PyCon JP - Day 2
這天的 Keynote [Pythonで切り開く新しい農業](https://www.youtube.com/watch?v=0bTPOsVvG7g) 主要是在講他透過 Python 來分辨小黃瓜的故事
我很喜歡他對 AI 的註解
> 現在越來越少人要當農夫了
> 如果不做些什麼，農業的知識就會流失
> 而 AI 正好可以作為一種知識儲存和傳遞的工具

Dustin 的 [Modern development environments for Pythonistas](https://www.youtube.com/watch?v=d3cj4f63u-A) 也讓我印象蠻深刻的
主要是因為跟我要去 PyCon CA 講的內容相關
再加上，結束後我們一群 PyCon TW 圍著他問問題 XD
btw Dustin 在 PyCon TW / US / ... 給的 talks "PEP 572"，真的非常精彩
錯過的話，非常推薦可以補帶

當然還有 KK 大的 [When AI meets 3000-year-old Chinese Palmistry](https://www.youtube.com/watch?v=NLLhYKscuMk) 
其實我這次來比較少聽 AI 相關的 talk，但分析手相實在太有趣了

最後我有嘗試去聽一場日文的 talk
憑著我 50 音都背不齊的日文程度，果然還是太挑戰了 XD
當我以為我至少能看投影片的時候，他的投影片也是日文的
後來發現好像是台灣才是比較特例
即使是用中文給的 talk ，還是習慣用英文做投影片

最後閉幕的時候聽到 Python 這個商標在日本被[ARK](http://www.gigamall.ne.jp/ark/ai/python.html)註冊走
PSF 要著手處理這件事了

![drone]({static}/images/posts-image/2019-10-12-pycon-jp-2019/15700840284965.jpg)
<small>最後大合照的無人機</small>

![coffee]({static}/images/posts-image/2019-10-12-pycon-jp-2019/15700840254045.jpg)
<small>某人把還沒打開的奶精加入咖啡</small>

![after-party]({static}/images/posts-image/2019-10-12-pycon-jp-2019/15700840345989.jpg)
<small>離開日本前， Visiting Group 小聚</small>

## Speaker Tour
會議結束後的一天，PyCon JP 還有帶講者們到淺草寺等有名的景點走走
可惜那天下著大雨 QQ

![speaker-tour]({static}/images/posts-image/2019-10-12-pycon-jp-2019/15700840364273.jpg)

## Final Words
整體來說，我覺得 PyCon JP 辦得比我想像的來得更好
能跟著 PyCon TW 來，也讓我覺得跟人交流有比較容易一些
如果下次還有揪團，我應該也還會再來

恩對，大概就是這樣
![me-with-badge]({static}/images/posts-image/2019-10-12-pycon-jp-2019/15700840325586.jpg){: style="width:80%"}

在找一些東西的時候，發現同行的前輩 Kir 也發了一篇 PyCon JP 的文
[My journey of PyCon JP/TW 2019](https://medium.com/@Kir.Chou/my-journey-of-pycon-jp-tw-2019-220555e8e3b1)

另外，這是發在 PyCon TW Blog 的參訪報告 - [Visiting Group in PyCon JP 2019](https://pycontw.blogspot.com/2019/10/visiting-group-in-pycon-jp-2019.html)
整理了我們整團的所見所聞

如果喜歡這篇文章的話，你雖然沒辦法拍手 50 下
但可以在下面按一個 response，或留個 comment 跟我聊聊天
如果能在順手填一下 2020 年的 [PyCon Taiwan 志工招募](https://docs.google.com/forms/d/e/1FAIpQLSe6whkZAEZD10LlPQuSWRYsshySoNR_pux8grGZ0OgmOIkQ3g/viewform?fbclid=IwAR2mPycJxD2HCVm_mIX4v7ChEGwNEgo5-HP_QGA4503dD9E2kCP3M5OihT8) 就能給我更大的支持了 😄