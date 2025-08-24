Title: Remote Python Pizza 🍕 2020
Date: 2020-05-03 16:52
Category: Tech
Tags: Python, PyCon, Python Pizza, commitizen-tools
Slug: remote-python-pizza-2020
Authors: Wei Lee

上週六參加了第一場遠端的 Python 研討會 [Remote Python Pizza](https://remote.python.pizza/)
由於疫情的關係，國外的 PyCon 大多轉往線上或取消
雖然目前還不確定今年台灣的狀況會如何
但先觀摩一下其他社群怎麼做的，對我們也很有幫助

<!--more-->

整體的體驗比我想像的好了不少，我還蠻享受 Remote Python Pizza 的
雖然只是透過螢幕跟文字，還是能感受到整個社群的交流
或許這在疫情趨緩後，也可以作為研討會的另一種標準
雖然少了實體的交流，但不用長途跋涉就可以集結全世界的大大們，其實也很方便
而針對時差這件事，他們也有在議程表上標上 UTC 跟使用者的當地時間，這在遠端研討會上就變得很必要

會眾交流主要是透過 [Discord](https://discordapp.com/)
不管是要回報 CoC 、對講者提問、工作人員休息室...等，都有專屬的頻道
盡可能將實體會議的元素都帶進來，其實還蠻有趣的

演講則是給主辦人先給講者跟主持人 Zoom 的連結
講者演講前的 30 分鐘，就先加入 Zoom 待命，接著把影片串到 Youtube 上讓會眾觀看

Remote Python Pizza 的時間非常緊湊
每一場演講只有十分鐘，演講之間的休息只有兩分鐘
因為也沒有實際換場的必要，所以這段就很考驗主持人的技術了
[pyjokes](https://pyjok.es/) 對於英語系的會議，應該會很有幫助 XD

因為時差的關係，開始的時候已經是下午四點
大概聽到八點就開始覺得有點累了
不過坐在客廳用電視投影演講是真的還蠻爽的 XD

![tv](/images/posts-image/2020-05-03-remote-python-pizza/tv.jpeg)

為了響應 Remote Python Pizza ，我當天的晚餐也是吃 Pizza
而且 Discord 中就有一個 `#cafeteria` 頻道，讓大家曬自己的 Pizza 照
其實還蠻 High 的 XD
我覺得這是線上會議**鼓勵會眾互動非常棒的設計**

![pizza](/images/posts-image/2020-05-03-remote-python-pizza/pizza.jpeg)

第一場 Hynek 的 *On the Meaning of Version Numbers* 就先介紹了 [SemVar](https://semver.org/)
主要說大部分的專案都沒辦法用好 SemVar ，所以 SemVar 可能太難遵守，不見得是一個很好的作法
可以改成使用 [CalVer](https://calver.org/)
在一開始我會提到的 SemVar 就好好的被打臉了一波 XDDD

第二場講者沒來，所以就跳過直接換我，害我錯愕了一下
一場演講只要十分鐘，完全是個適合推廣 [commitizen-tools](https://github.com/commitizen-tools) 的好機會
就毅然決然的投稿了 XD

![my-avatar](/images/posts-image/2020-05-03-remote-python-pizza/my-avatar.jpg)

不過真的沒想到，官網會直接用我 Twitter 的大頭貼＠＠
不過既然都被用了兵長的頭貼，我就順勢穿著調查兵團的披風來給演講了 XD
有點久沒講英文，還是覺得稍微有點卡
倒是我在演講中提到還是 beta 的自動產生變更日誌（changelog）功能
剛好在今天正式釋出了，快點來試試看吧 🤩

```sh
python -m pip install commitizen
```

Disconnect3d 給的 *sudo python is a trap, use isolate mode* 是我印象最深刻的一場
現場 demo 如果你使用了 `sudo python`，駭客多輕鬆就可以駭入你的電腦
所以不要使用 `sudo python` 啊！
![sudo-python-is-a-trap](/images/posts-image/2020-05-03-remote-python-pizza/sudo-python-is-a-trap.jpg)

整體節奏太緊湊，實在沒什麼時間好好做筆記
之後再找個時間把比較有趣的內容補起來

每一場演講結束後
除了在 Zoom 中的主持人會拍手外，大家會在 `#question-answer` 頻道洗一波 👏 的 emoji
其實還蠻可愛 XD
大家也能在這個頻道直接堆剛講完的講者提問
另外也有 `#slide` 頻道，讓大家快速找到講者的投影片
講者也可以在結束後，創一個 `#talk-*.` (e.g., `#talk-commitizen`) 的頻道討論演講相關的內容
以講者的角度來說，我覺得這裡的交流甚至有機會比實體會議更多，是個蠻好的作法

中間倒是有個小插曲，直播到一半就被 Youtube 封鎖了......
最後發現原因是直播時不能開 `Made for Kids`，很容易被封鎖
而且這還是預設值，要自己記得關掉＠＠
這倒是可以作為一個警示，線上會議要多準備幾套備用的方案

大概就是這樣
因為時差的關係，我大概撐到 12 點就差不多了
畢竟整個會議有 50 場演講，延續了 12 個小時
要全部參加完實在太累了
之後再來補帶吧
