Title: How was PyCon US 2019
Date: 2019-06-22 21:49
Modified: 2020-02-04 18:43
Category: Tech
Tags: Python, PyCon, Conference
Slug: how-was-pycon-us-2019
Authors: Lee-W

既然自稱 Python 的信徒
總是要來世界最大的 PyCon 朝聖一下 XD

![IMG_3010](/images/posts-image/2019-06-22-how-was-pycon-us-2019/IMG_3010.jpg)

（我還因為寫了 GitHub ，被以為是 GitHub 的員工 XD）

<!--more-->

[TOC]

## 簡介一下 PyCon US

PyCon 總共跨了 9 天
除了主會議外，還有各種不同的活動跟討論

* 5/1 ~ 5/2: Tutorial
* 5/3 ~ 5/5: 主會議
* 5/6 ~ 5/9: Development Sprint

今年辦在 Cleveland 的 Huntington Convention Center
會眾大概有 3000 人
會議期間除了同時會有 6 個軌的 talk 以外，還會有好幾間的 Open Space

最大的會議廳長這樣
![IMG_3033](/images/posts-image/2019-06-22-how-was-pycon-us-2019/IMG_3033.jpg)
![IMG_3035](/images/posts-image/2019-06-22-how-was-pycon-us-2019/IMG_3035.jpg)

參加前，我有看了這篇 "[How to have a great first PyCon](https://treyhunner.com/2018/04/how-to-make-the-most-of-your-first-pycon/)"
對我這次去參加 PyCon 很有幫助

## Tutorial
我參加了兩場 Tutorial

* [Getting started with Kubernetes and container orchestration](https://www.youtube.com/watch?v=J08MrW2NC1Y&list=PLPbTDk1hBo3xof51R8pk3kP1BVBuMYP9c&index=18&t=0s)
    * Kubernetes 的使用介紹的蠻清楚的，我覺得對入門 Kubernete 很有幫助
* [Building Evolutionary API with GraphQL and Python](https://www.youtube.com/watch?v=DWgD5iloSHs&list=PLPbTDk1hBo3xof51R8pk3kP1BVBuMYP9c&index=15&t=0s)
    * 主要是在講 GraphQL 的概念，我覺得偏簡單，原本希望可以多聽到一些設計上的想法

一場 Tutorial 大概是三個小時
一天參加一場，我的體力上比較負荷的來
但中午吃飯跟其他會眾聊天的時候，遇到了好幾個人都是兩天參加滿四場 Tutorial ...

好幾個會眾都推薦了 David Beazley 的 [Lambda Calculus from the Ground Up](https://www.youtube.com/watch?v=pkCLMl0e_0k)
這場 Tutorial 的介紹開宗明義就說了

> You will learn nothing practically useful in this tutorial.

但大家還是都很推薦這場
聽說 David Beazley 是很有名的 Speaker（請原諒我的孤陋寡聞 QQ）
我甚至遇到一位會眾說看到名字就報名了，也不用看是什麼主題

## Talks
稍微簡介幾場我還有印象的 talk
也許之後有時間會把筆記好好整理一下分享出來

### Day 1
* **Keynote - Russell Keith-Magee**
    * Python's Black Swan
        * 你現在覺得 Python 的存在很自然，但 10 年後 Python 還會在嗎？
        * 我們要怎麼做些什麼才能讓 Python 在 10 年後還存在
    * 5 Calls to Action
        1. Start thinking about Black swans (before it's too late)
        2. Improve resourcing of maintenance and R&D efforts
        3. Value contributors and their contributions
        4. Get out your wallet
        5. Contribute
* **API Evolution the Right Way**
    * 更新 API 並且淘汰舊的版本，你需要注意的幾個設計細節
    * 如果想直接看文字不要補影片的話，可以直接看講者的文章 [API Evolution the Right Way](https://emptysqua.re/blog/api-evolution-the-right-way/)
* **Programmatic Notebooks with papermill**
    * Netflix 推銷自己的開源工具 [papermill](https://github.com/nteract/papermill)
    * 用一個 jupyter notebook 當作範本，由外部輸入幾組不同的參數，一次產生多個相對應 jupyter notebooks（為什麼我在弄碩論的時候沒發現有這樣的工具 QQ）
* **Everything at Once: Python's Many Concurrency Models**
    * 介紹跟比較 5 種 Python 的 Concurrency Model (asyncio, Python threads, GIL-released thread, multiprocessing, distributed tasks)
* **Supporting Engineers with Mental Health Issues**
    * Enginner 常常因為壓力太大造成一些心理的狀況，該如何正視自己的狀況並試著調適或尋求幫助
* [Lightening Talk - Overthinking T-Shirts with Scipy](https://www.youtube.com/watch?v=yFcCuinRVnU&list=PLPbTDk1hBo3x9H3_WOWv_p6wD01B5eBvn&index=1&t=16m35s)
    * 這是他們用自己公司的產品 Demo 他們計算要帶多少 T-Shirts 來發，並且快速的視覺化
    * 其實講題蠻瞎的，但講者講的真的很有趣很精彩 XD

### Day 2
* **Keynote - Shadeed "Sha" Wallace-Stepter**
    * "How many people here are on probation or parole?" （這個開頭害我以為我是不是英文真的太差誤會了什麼...... ）
    * Sha 訴說自己如何一個從犯人變成創業家的故事，如何在獄中學習 Python，並在出獄後重新融入社會
* **Keynote - Jessica McKellar**
    * 上一場像是實例的現身說法，這場則是在同一個主題下的 call to action
    * Jessica 想做的是改變美國的監獄系統
        * 如果出獄的人並不能融入社會，社會也不願意接受他們，那他們就會很容易再犯再回到監獄，而這會產生很大的社會成本
        * 如果能讓他們在獄中學習技能，並說服一些公司慢慢接受這群人，我們就能讓這些人重新融入社會，並成為社會的生產力
    * 工程師的工作不就是該修復系統嗎？
    * 這兩場 keynote 非常的精采，是整場 PyCon 最多人起立鼓掌最久的 Talk
        * 很不幸的這兩場的影片剛好消失了，目前只能從 [Jessica 的 twitter](https://twitter.com/jessicamckellar/status/1127639822640660482) 看到文字版的內容
* **The Zen of Python Teams**
    * 將 Zen of Python 應用到建造更好的團隊
* **Does remote work really work?**
    * 怎樣的人適合 remote work？ (Remote work is not for everyone.)
    * 你要注意些什麼才能成為一個好的 remote worker
* **Python Security Tool**
    * 這場很實際地提了幾個跟 Python 有關的 Security Tool  
      ![IMG_3063](/images/posts-image/2019-06-22-how-was-pycon-us-2019/IMG_3063.jpg)
* [Lightening Talk - Writing Selfless Python](https://www.youtube.com/watch?v=sRwHWPDJBnk&list=PLPbTDk1hBo3x9H3_WOWv_p6wD01B5eBvn&index=2&t=39m35s)
    * 無私的 Python： 有了 [selfless](https://pypi.org/project/selfless/) 我們不用在 Python 中寫自私的 (**self**fish) class 也能有同樣的功能
* [Lightening Talk - One Weird Trick for people to see your name in lunch](https://www.youtube.com/watch?v=sRwHWPDJBnk&list=PLPbTDk1hBo3x9H3_WOWv_p6wD01B5eBvn&index=2&t=8m45s)
    * 因為 badge 太長了，吃午餐的時候其他人會看不到你的名字
        * 那就在 badge 後面打個結，讓帶子短一點，大家就能看到你的名字了
    * 恩對，這場 Lightening Talk 就真的是這樣而已 XD
* [Lightening Talk - 3 Quick Tips for Software Blogging](https://www.youtube.com/watch?v=sRwHWPDJBnk&list=PLPbTDk1hBo3x9H3_WOWv_p6wD01B5eBvn&index=2&t=5m19s)
    1. Set a Purpose
        * Why do you want to blog?
            * Publish info, guides, help
            * Personal journalling /notes
            * connect with others
            * electronic biz card
            * be self-motivated
        * Don't
            * ~~become famous~~
            * ~~make money from ads~~
    2. Write new, helpful content
        * Don't repeat existing content. Make something new!
    3. Tools and Platforms Don't Matter (Content matters)

### Day 3
* **Keynote - Python Steering Council**
    * 現在的 Python 政府討論 Python的過去與未來
        * Python Governance
        * PEP 8000
        * PEP 13
    * Q: Where to start to become a core dev?
        * [Python Developer’s Guide](https://devguide.python.org)

* **Keynote - Nina Zakharenko - Light up you life with Python & LEDS!**
    * 現場 Demo [MicroPython](https://micropython.org)，如何用 Python 操控硬體
    * 我想這場主要是想展示用 Python 能很簡單地做到一些原本想像中可能會比較困難的事

### Watch List

我跟在 PyCon 認識的朋友整理了一些之後會想補帶的 talk

* [API Evolution the Right Way](https://www.youtube.com/watch?v=dqDnB6jKzcE)
* [The Zen of Python Teams](https://www.youtube.com/watch?v=WZ8FEB4J8-c)
* [Releasing the World's Largest Python Site Every 7 Minutes](https://www.youtube.com/watch?v=2mevf60qm60)
* [Time to take out the rubbish: garbage collector](https://www.youtube.com/watch?v=CLW5Lyc1FN8)
* [Getting Started Testing in Data Science](https://www.youtube.com/watch?v=0ysyWk-ox-8)
* [Escape from auto-manual testing with Hypothesis!](https://www.youtube.com/watch?v=KcyGUVzL7HA)
* [Ace Your Technical Interview Using Python](https://www.youtube.com/watch?v=NltGUUi23zc)
* [Migrating Pinterest from Python2 to Python3](https://www.youtube.com/watch?v=e1vqfBEAkNA)
* [Scraping a Million Pokemon Battles: Distributed Systems By Example](https://www.youtube.com/watch?v=QvZqttX9uXc)
* [Practical decorators](https://www.youtube.com/watch?v=MjHpMCIvwsY)
* [Break the Cycle: Three excellent Python tools to automate repetitive tasks](https://www.youtube.com/watch?v=-BHverY7IwU)

## Open Space

畢竟 talk 都會錄影，而且很快就上傳了（大概結束後兩天就會上傳）
所以後來我就越來越常去 Open Space
而且相較之下 Open Space 會比較有跟人互動的機會

![IMG_3042](/images/posts-image/2019-06-22-how-was-pycon-us-2019/IMG_3042.jpg)
![IMG_3060](/images/posts-image/2019-06-22-how-was-pycon-us-2019/IMG_3060.jpg)
![IMG_3064](/images/posts-image/2019-06-22-how-was-pycon-us-2019/IMG_3064.jpg)

除了一些比較技術性的討論外
也會有不少娛樂性的 Open Space（通常在晚上）
像這個就是揪團要一起看 Game of Throne XD

![IMG_3062](/images/posts-image/2019-06-22-how-was-pycon-us-2019/IMG_3062.jpg)

大部分討論性質的 Open Space 會像這樣圍成一圈

![open-space](/images/posts-image/2019-06-22-how-was-pycon-us-2019/15611957026963.jpg)

這是我去參加 Vim 討論會的照片
當天就有人分享了討論的筆記 ([Vim BoF @PyCon2019](https://gist.github.com/pwlandoll/dcb252686ae3c2e2486fd6425eb00d91))

我還有參加到一場幫忙做履歷健檢的跟討論 Tech Interview

## Job Fair / Poster

Job Fair 主要就是跟各個公司聊天，看看他們的工作性質跟開了什麼缺
有聽到幾間 remote 的公司還蠻有趣的
不過其實也不用等到 Job Fair 才問
Job Fair 的公司反而比較少，不過應該就是專注在有開缺的公司
前幾天的攤位反而更有機會聊聊
![IMG_3025](/images/posts-image/2019-06-22-how-was-pycon-us-2019/IMG_3025.jpg)

Poster 也是一個能跟人互動蠻好的機會
不過那些比較有趣的，通常旁邊都會圍著一群人 XD
[Hypothesis](https://hypothesis.readthedocs.io) 好像整個 session 人都沒少過
（話說 Hypothesis 還真的從 talk, tutorial, sprint 到 poster 每個場合都出現了）
![IMG_3070](/images/posts-image/2019-06-22-how-was-pycon-us-2019/IMG_3070.jpg)

## Development Sprint

自從上次在 PyCon TW 參加了 PyBee 的 Sprint ，就覺得這樣一群人協作開源專案很有趣
所以這也是我這次 PyCon 幾乎最期待的活動

在 Development Sprint ，開源專案的作者會帶自己的專案找大家一起來協作
沒有帶專案來的人就可以看自己對哪個有興趣加入貢獻
參加 Development Sprint 是貢獻開源專案還蠻好的入門方式
畢竟原作者跟 core contributor 就在旁邊
有遇到什麼問題想問馬上就可以問

我這次參加了 [pallets](https://github.com/pallets), [cpython](https://github.com/python/cpython), [pybee](https://github.com/pybee), [OpenEdx](https://github.com/edx) 的 Sprint
每一個專案，我在最後都有提交至少一個小 PR
這次最有成就感的大概就是成功提交了一個 flask 跟 cpython 的 PR
（雖然 cpython 的其實還在 review 中）

這幾個專案之中，我覺得 [pybee](https://github.com/pybee), [OpenEdx](https://github.com/edx) 算是最新手友善的

![IMG_3195](/images/posts-image/2019-06-22-how-was-pycon-us-2019/IMG_3195.jpg)

Sprint 的這幾天還蠻常看到 Guido 在走廊走來走去
也蠻多人去找他搭話跟拍照的
不過害羞的我就有點不敢過去了 QQ

記錄一下這四天丟了哪些 PR

* [pallets](https://github.com/pallets)
    * Pull Request
        * [Fix MethodView inheritance Error (#3138) #3179](https://github.com/pallets/flask/pull/3179)
* [Beeware](https://beeware.org)
    * Pull Request
        * [Fix the CAPSLOCK typo in toga_cocoa #679](https://github.com/beeware/toga/pull/679)
        * [Fix open file not working when using open command and double click files #686](https://github.com/beeware/toga/pull/686)
        * [Fix the error that UP arrow won't go the previous page #28](https://github.com/beeware/podium/pull/28)
* CPython
    * Project
        * [Python Developer’s Guide](https://devguide.python.org)
        * [The Ultimate Guide to the CPython Source Code](https://realpython.com/cpython-source-code-guide/?preview=cpython-sprints)
    * Pull Request (not yet merged)
        * [bpo-36841: Supporting customization of float encoding in JSON](https://github.com/python/cpython/pull/13233)
* OpenEdx
    * Project
        * [Contributing to Open edX](https://contributing-to-open-edx.readthedocs.io/en/latest/)
        * [open edx slack](https://openedx.slack.com)
            * openedx-slack-invite.herokuapp.com
        * [Sites powered by Open edX](https://openedx.atlassian.net/wiki/spaces/COMM/pages/162245773/Sites+powered+by+Open+edX)
    * Pull Request
        * [Add pull upstream reminder in contribute](https://github.com/edx/edx-documentation/pull/1825)
        * [INCR-236](https://github.com/edx/edx-platform/pull/20502)


## 給自己下次去的建議

### 多跟人交流、多跟人交流、多跟人交流

這是我感受到跟在台灣參加研討會最不一樣的地方
（也可能是我在台灣的研討會都在舒適圈中...）
只要你願意，在會場中幾乎每個人都很樂於跟你交流
可能你只是站在一個桌子上吃早餐，就會有人過來跟你聊聊
這個體驗真的蠻有趣的

### 練好英文口說

原本覺得自己英文程度雖然稱不上好，但應該也沒到太差吧
至少在旅行上是沒遇過什麼問題
但這種程度跟要跟人討論或聊天還是差太多了
當然要說點話是沒什麼問題，但要流暢表達自己就還是蠻困難的
一對一的聊天還算勉強有辦法
到了團體討論就真的很吃力
光在聽力上要跟上大家在討論的就有點辛苦
就更不用說要加入討論了
剛到 PyCon 的前幾天對於這件事還真的蠻挫折的

### 準備好一段短的招呼語跟自我介紹

一開始有人來找我聊天，還是會有些緊張，不知道要說什麼
畢竟在台灣真的也沒什麼這樣練習英文口說的機會
後來多跟幾個人聊過後
自然而然就形成了一套跟人開頭的招呼語跟自我介紹
之後話題就能比較順利地一直接下去

### 留點緩衝時間給調時差

這次到美國的隔天就已經要開始 PyCon 了
一到了傍晚就會開始想睡
所以前幾天的 After Party 我參加一下就走了
後來也沒去參加 Facebook
一來是我也有點不知道怎麼在這種場合應對
二來是真的太累了...

### 保留體力 - 不用每個活動都參與到

剛來的時候會覺得，都花了這麼多錢特地跑來，一定要把握時間每
就會勉強自己盡可能每個時段都要塞滿
但 PyCon 的 talk, open space and etc. 實在太多了
真的要塞滿，體力就有點負荷不來，後來就都是邊睡邊聽......
中間可以留一些時間在 Quiet Room 稍微休息

![IMG_3187](/images/posts-image/2019-06-22-how-was-pycon-us-2019/IMG_3187.jpg)

與其多衝一些場數，不如專注地把幾場真正想聽的專心聽完

### 多去 Open Space

相較於 talk ， Open Space 除了沒有錄影可以補帶以外
也是一個跟人們可以更有互動的機會
有時候說不定也能聽到一些不能在 talk 說的事（笑
而且我覺得在這應該是蠻有機會交到一些朋友的場合
（雖然我後來認識的大多是在走廊上或吃飯遇到的 XD）

### 事前對有興趣的 talk 準備好想問的問題

雖然說看現場的感受跟看影片還是不一樣
但既然都去聽了，如果能跟講者討論自己遇到的問題，應該會更有收穫

### 將當下的熱情紀錄下來，並列出 action items

參加的當下的感受還蠻強烈的，但回來台灣好一段時間後
當初的熱情跟想法，就會慢慢被生活給磨光
所以立刻把明確的 action items 記錄下來，也許會讓這些事情成真的機會高一點

寫下這篇文章，某種程度上也是想記錄下這次參加的感受呢

## 食物 （20190703 update）

![food](/images/posts-image/2019-06-22-how-was-pycon-us-2019/food.png)

既然有人問了，就來補充一下吧 XD

首先是從 Tutorial 開始到 Sprint 結束的九天
每天都有星巴克可以喝
雖然到 Sprint 的時候好像已經把經費花光
臨時又有廠商在贊助才能撐到結束

![IMG_3011](/images/posts-image/2019-06-22-how-was-pycon-us-2019/IMG_3011.jpg)

議程以外那幾天大多是自助式
大概都是這樣的沙拉

![IMG_3024](/images/posts-image/2019-06-22-how-was-pycon-us-2019/IMG_3024.jpg)

議程那幾天就有點像是餐盒
有豬、牛、素、水果幾種可以選
像這個就是牛排，吃起來就還不錯
![IMG_3045](/images/posts-image/2019-06-22-how-was-pycon-us-2019/IMG_3045.jpg)

這個也是牛排
但吃起來很可怕......
上面那個餅皮我真的努力要吃過了，但我失敗了＠＠
這是我待在美國這一個月最難吃的食物......

![IMG_3061](/images/posts-image/2019-06-22-how-was-pycon-us-2019/IMG_3061.jpg)

恩，大概就只有這樣xD

## 雜談

一開始對於要不要飛一趟去美國還蠻猶豫的
畢竟 PyCon 的 talk 網路上都看得到，花這一大筆錢真的值得嗎？
而且自己一個跑到一個人生地不熟的地方也是挺可怕的

其實這些問題我到最後也沒給自己一個好的答覆
反正就覺得現在如果不衝動地做這件事，也許就不會有下次了
就毅然決然的買了機票跟門票
逼得自己沒有退路，一定得要去

以結論來說，我覺得非常值得
而且如果有可能，我明年還是會想去 PyCon 2020 in Pittsburgh
在 PyCon 體驗到一些我在台灣比較不會接觸到的事
平常也許可以看看文章，聽別人說說這些故事
但這跟實際現場的體會真的太不一樣了
最大的感受是「那些原先覺得做不到的事，似乎變得不再那麼遙遠」

當然我在美國其實待了一個多月，也是去了不少地方
說不定哪天有空也會寫篇遊記

這篇快速整理了一下我現在想到的，也許之後還會再補點內容
