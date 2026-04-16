Title: EuroPython 2020
Date: 2020-08-06 15:15 +0800
Category: Tech
Tags: Python, PyCon, EuroPython, EuroPython 2020, commitizen-tools
Slug: europython-2020
Authors: Wei Lee
Lang: zh-tw

好不容易投稿上了 EuroPython
原本打算順便去愛爾蘭的 Skellig Michael
疫情一來就全都去不成了 😭

<!--more-->

[TOC]

## 前言雜談
EuroPython 2020 在 3 月底的時候公佈轉成線上會議
比起 PyCon US，場地跟其他費用都還沒有支出，算是蠻幸運的
倒是今年線上會議要收票的問題，聽說在 Telegram 群組有一番爭論
一張一般票 EUR 95.00 的確不算很便宜
不過講者票今年不用錢就是了 XD

今年有來自 69 個國家的會眾參與，比起 2019 多了 40 個國家
雖然大家抱怨歸抱怨，最後好像還是有 1000 人以上買票啊 XDDDD

線上會議跟真人會議的體驗上會有差是無法避免
但我覺得已經算是盡可能把實體會議的一切搬到線上了
能在這麼短的時間內，完成那麼多規劃真的蠻厲害的
最棒的一點是，留了很多文件給大家參考 🤩

* [EuroPython 2020 Online Conference Tools](https://docs.google.com/document/d/1OAVtZnxVgmkDGvSV1vEzra7m5Nfjr-81kCrustzxAek/edit#)
* [EuroPython 2020 Speaker Guide](https://docs.google.com/document/d/1hno9PgvEViHBkmCXP6BkpAsL8-mTpm6Sb8S6A8lwVPs/edit#heading=h.b0yozxqx8i03)

以往 EuroPython 的演講影片都會公開，並放到 [PyVideo](https://pyvideo.org/) 上
我原本蠻好奇今年打算怎麼在收費和不收費的會眾做出區別
畢竟以往購票參與會議一個很大的價值是跟其他的與會者互動
今年的互動雖然用 Discord 來彌補，但還是會打一些折扣

最後的作法是會先還沒剪的影片傳到私有的 Youtube 頻道供購票會眾觀看，但兩週後就會公開
幾週後弄完就把修剪版放上去

整體參加下來我覺得是很成功的線上會議，我也很享受跟會眾的線上互動
雖然少了實體的互動是可惜了點，但降低參與成本讓更多還自不同地區的人能一起來共襄盛舉
現在也還說不準預期疫情到底什麼時候會結束，不知道線上會議會不會是一個新的標準
又或者之後可以嘗試一下實體/虛擬混合的會議？

## Discord 互動設計
EuroPython 設計了很完整的架構，讓會眾可以更快速的找到各個資訊在 Discord 的哪裡

### Lobby
![lobby](/images/posts-image/2020-07-28-euro-python-2020/lobby.jpg)

Lobby 的 Channel Category 主要是註冊用跟大會公告
進到 `info-desk` 輸入自己的票務資訊後，就會有機器人自動設定正確的權限
而且這個機器人也有開源 👉 [ep-regbot](https://github.com/EuroPython/ep-regbot)

`hallway` 可以想像成大會的走廊，就是讓會眾隨意聊天的地方
好像有人問有沒有人要在 after party 的時段直播表演樂器
有點像是 PyCon TW 的 PyNight
但 after party 的時間，在台灣的凌晨，我就沒有參加到了

### Conference Tracks
![conference tracks](/images/posts-image/2020-07-28-euro-python-2020/conference-track.png)

註冊後最重要的是 Conference Tracks 這個 Channel Category
microsoft / brain/ ni /parrot 可以看成 PyCon TW 的 r0 / r1 /r2，總之就是不同的 track
除了 track 都有自己的討論頻道外，每個 track 還會有一個 `.*-peek` 的頻道
機器人會截圖 track 中現在 Zoom 的畫面
供會眾參考要不要連進去現在的 Zoom 或是看 Youtube
我覺得這個功能真的超酷 XDD

另外，每個 Track 都會有自己的 Channel Category
裡面會有每一個講者的頻道
身為講者，我覺得有一個自己的頻道可以繼續跟會眾互動真的蠻棒的 💯
還有兩個頻道是給 Open Space 用的，這次好像不算特別熱絡
一天大概只有兩、三場

### Sponsor Exhibit
![sponsor exhibit](/images/posts-image/2020-07-28-euro-python-2020/sponsor.jpg)

贊助商也會有各自的頻道
也會有各自的 Zoom ，可以跟跟會眾互動
我有稍微路過一下，但沒參與太多就跑去參加下一個演講了

另外，在每一場演講的間隔，會播放贊助商的廣告影片
我覺得效果蠻不錯的
畢竟就是在等下一場演講，好像就還是得看完 XD

### Attendee Rooms
![attendee rooms](/images/posts-image/2020-07-28-euro-python-2020/attendee-rooms.jpg)

會眾有一整個 Channel Category
好像可以自己創主題式的討論
但這部分我就真的沒什麼參與到了

### Backstage
![backstage](/images/posts-image/2020-07-28-euro-python-2020/speaker-backstage.jpg)

講者後台的設計就真的有點複雜
在線上會議會遇到的一個問題是「怎麼提醒講者時間快到了」，直接在演講中打斷講者好像不太適合
他們的作法是講者會在演講開始前 15 分鐘加入 `.*-greenroom`，讓 session manager 確定講者已經抵達
接著， session manager 會讓講者加入 Zoom 跟 `.*-talkback`
用 Zoom 讓講者做演講並跟主持人做互動
session manager 則是透過 `.*-talkback` 跟講者說剩下的時間

在線上會議也有講者準備/休息室（greenroom）的概念真的蠻有趣的 XD

## 會期
### Day 1
第一天開始時因為技術問題卡了十幾分鐘
倒是有會眾開始詢問，有沒有人有 vga-to-hdmi 轉接線

> It's just like being there in person - "does someone have the correct vga-to-hdmi adaptor?" 🙂

EuroPython 就連實體會議找不到轉接線都模擬了（誤
大家都在等有沒有會眾剛好有帶 HDMI 線現場救援（？？？
有跟上這段討論真的超有趣 😆

開場結束後，馬上又遇到下一個問題
連接線找到了，但找不到講者 😱
第一場 Keynote Speaker 就直接 no show 了，真的有點尷尬 @@

因為時差的關係，大概會有三分之一的演講完全沒機會聽到
晚上我又另外有事，第一天沒聽到什麼演講
這兩場是我還有時間做筆記覺得也蠻不錯的演講

* [Clean Architectures in Python](https://wei-lee.me/pycon-note/posts/europython-2020/2020/07/clean-architectures-in-python/)
* [Practical Optimisations for Pandas](https://wei-lee.me/pycon-note/posts/europython-2020/2020/07/practical-optimisations-for-pandas/)

我超佩服 @ongchinhwee
她每個研討會都能在 twitter 上做超多超快的筆記
今年她在 PyCon Taiwan 演講完，要好好跟她請教怎麼辦到的 XD

### Day 2

#### Community-oriented conference status during COVID-19
Noah 分享了亞太地區 PyCon 的近況
台灣是亞太地區唯一能辦實體 PyCon
搞不好有機會是 2020 疫情開始後，唯一一場能辦實體的 PyCon

#### How to Avoid Becoming a 10x Engineer
這場演講頻道的討論超熱鬧
看來大家應該都遇過了 10x Engineer
寫 code 是一般人的時倍快，製造的 bug 是十倍快

#### Live-coding a music synthesizer
原本應該要去聽 Advanced Infrastructure Management in Kubernetes using Python
但這場從 `ni-peek` 看到的截圖實在太有趣了，就來看 Ram Rachum 如何現場完成合音器

![music](/images/posts-image/2020-07-28-euro-python-2020/music.png)

#### Python Table Manners: Cut the Cookie Gracefully
這場是我自己的演講 XD
雖然講過幾次了，而且又是線上的
但老實說還是稍微會有點緊張

不過在我的頻道中，討論算是還蠻熱烈的
也被問了蠻多問題的
其中一個問題是「為什麼要使用 invoke ，而不用可以跟 poetry 整合的 [taskipy](https://github.com/illBeRoy/taskipy)」
恩...
就只是單純因為我不知道有這個東西 XD

就會眾的反應來看，大致上這場演講是成功的
一開始構思這場演講的時候，也會擔心內容會不會不夠深入
但介紹了這麼多工具，總會有一兩個是會眾不知道吧！
不然帶走我的 [cookiecutter template](https://github.com/Lee-W/cookiecutter-python-template) 還是能省下一些重造輪子的時間

### Running EuroPython 2020 as an online conference
這場演講外，大會主席還給了 **EuroPython 2021: Help us build the next edition!** 的演講
除了講今年線上會議遇到的困難，還招募了明年有意願來籌備會議的會眾

[slide](https://ep2020.europython.eu/media/conference/slides/7tiTuRY-running-europython-2020-as-an-online-conference.pdf)

其中有提到為什麼 2020 還是要收錢
因為如果今年不收錢了，以後如果突然要收錢就會變得很困難
大概就跟調降健保費就漲不回去的概念是一樣的
對於一個組織跟研討會的存續其實是不好的

> If you can handle free, that's fine, I still believe that the free for all is going in the wrong direction. It's likely that we will stay in this situation for a longer while and unless you plan for it longer term, running free events is going to create too much loss for the orgs behind the conference to stay alive.

另外，還有一個問題很有趣
如果開啟 Zoom 會議的主持人電腦當機怎麼辦？
這時候會不會講者的演講就突然中斷了
這還真的是我完全沒想過的問題
他們的解法是直接用雲端服務開 VM 來開 Zoom 的會議避免掉這樣的問題

#### Making Pandas Fly
講者 Ian Ozsvald 同時也是 High Performance Python 的作者
這場主要談如何讓 Pandas 更有效率，大多都是蠻泛用的技巧，算是蠻有收穫的
筆記我放在 [Making Pandas Fly](https://wei-lee.me/pycon-note/posts/europython-2020/2020/07/making-pandas-fly/)

如果覺得這場演講對你有幫助，可以寄明信片給 Ian
Ian 很喜歡收明信片 XD

#### Lightning Talk
除了演講外，我也報名了 Lightning Talk
在一天開始的某一個時段，開放一個 Google Sheet 讓大家填，先搶先贏

我的內容當然是繼續宣傳 [commitizen-tools](https://github.com/commitizen-tools) XD
不過用英文演講又要 Live Demo 果然還是需要準備一下
即興上場還是會有點卡

#### Guido van Rossum Q&A
![guido](/images/posts-image/2020-07-28-euro-python-2020/guido.png)

Guido 的訪談算是第二天的重頭戲，稍微紀錄一下我比較有印象的內容

* Python will always be dynamic language. Type needs to be optional.
* 對於新進的軟體工程師，推薦可以看 [King's Day Speech](http://neopythonic.blogspot.com/2016/04/kings-day-speech.html)
* Q: 你能想到你最不喜歡 Python 哪嗎?
    * A: 目前沒想法，抱歉

### Developments Sprint
報名的方式很容易，只要到 [EuroPython 2020 Sprints](https://wiki.python.org/moin/EuroPython2020/Sprints) 上面自己改文件就好
順帶一提，今年 PyCon TW 的 Sprint 也是採用相似的形式 👉 [PyCon TW 2020 衝刺開發 Development Sprints](https://hackmd.io/w5hh0hUNQr65k4ayG2128Q?view)

第一天的開始會請各個專案的主辦人介紹自己的專案是什麼
除了專案以外，還有人帶初學者 session ，讓第一次參加的人可以更容易進入狀況
算是蠻好的設計，也許我們可以來學一下 🤔

![sprint](/images/posts-image/2020-07-28-euro-python-2020/sprint.jpeg)

今年線上的 Sprint 好像沒有很多人參與
也可能是 commitizen 的 Sprint 真的太邊緣了.....
從頭到尾就只有我跟作者 Santi 兩個人在寫
中間會有人突然跳進來，但他們都一語不發就又跳出去了 0.0

雖然我們邊緣，我們還是解決了超多 issue！
這兩天把 [commitizen](https://github.com/commitizen-tools/commitizen) 1/3 的 open issue 解掉
而且釋出 2.0
邊緣歸邊緣，我們還是很有產出的！
![commitizen result](/images/posts-image/2020-07-28-euro-python-2020/commitizen result.png)

Sprint 的中間還有個有趣的小插曲
因為大家很好奇怎麼做 [mate](https://zh.wikipedia.org/wiki/%E7%91%AA%E9%BB%9B%E8%8C%B6)
第二天的晚上，就突然開了一個做瑪黛茶的 Open Space XD

![mate annonucement](/images/posts-image/2020-07-28-euro-python-2020/mate annonucement.png)

![mate open space](/images/posts-image/2020-07-28-euro-python-2020/mate open space.png)
