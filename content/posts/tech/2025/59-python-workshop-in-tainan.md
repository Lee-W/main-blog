Title: 開源菜雞的隨意雜談
Subtitle: 這天，台灣多了 5 位 Airflow 貢獻者
Date: 2025-12-03 23:05 +0800
Category: Tech
Tags: Airflow, Development Sprint
Slug: some-random-guy-talk-about-airflow
Cover: /images/posts-image/2025-python-workshop-in-tainan/seigaku.jpeg
Authors: Wei Lee
Lang: zh-tw

三月邦邦找我回實驗室分享的時候，老師說我畢業後都沒回去台南找他
依稀又有印象嘉平好像在某次跟大家說，每次都他上來台北，總是要換我們去台南吧吧
恩，好吧，那這次我就台南吧

<!--more-->

不過如果去一趟什麼都沒做的話，就有點沒意思
車錢很貴，我很窮，所以要讓效用最大化
看準了[南臺灣技術社群大聚 2025](https://gdg-kaohsiung.kktix.cc/events/devfest2025scs2025)的時間就出發了
聽 Denny 跟 Mac 分享了不同研討會所遇到的困難和各種心法
有點想起以前 tai 常說的「最後正確的方式，可能就還是那幾種」

去成大的話就順便辦場 PyCon TW 的衝刺開發
反正我的形式都很隨興，負擔不會太大

至於標題的[開源菜雞的隨意雜談](https://speakerdeck.com/leew/20251127-kai-yuan-cai-ji-de-sui-yi-za-tan)
就...很突然，被說這次要給個分享
痾...好吧？那我拿三月的改一下講好了
倒是我還以為這個標題會被唸，但過關了，也蠻好的
分享內容應該還行，但講的有點軟爛
不過我花了點時間更新了我想要引用的作品們
除此之外因為今年成為 Apache Airflow 台灣漢語的負責人
總覺得要多用一點中文，而不是都用英文
所以也有翻修了一次
但分享過程還是一直在卡詞

![bad-eng-mandarin](/images/meme/bad-eng-mandarin.jpg)

## Python 開源實戰工作坊

記錄這次的成果

* 來自現場貢獻者
    * 已合併
        1. [Fix formatting error in Breeze setup instructions #58748](https://github.com/apache/airflow/pull/58748)
        2. [Fix link format for installation guide in documentation #58751](https://github.com/apache/airflow/pull/58751)
        3. [feat: add OpenFaaS connection type and documentation #58759](https://github.com/apache/airflow/pull/58759)
        4. [fix Preserve variable value formatting in edit dialog #58757](https://github.com/apache/airflow/pull/58757)
        5. [docs: Fix broken permalink icon #58763](https://github.com/apache/airflow/pull/58763)
    * 已關閉（剛好跟前面的 PRs 重複 😢）
        6. [Fix format error in quick start documentation #58755](https://github.com/apache/airflow/pull/58755)
        7. [Fix broken link of docker installation full guide #58758](https://github.com/apache/airflow/pull/58758)
* 來自我
    * 發出 PR [build: update uv to 0.9.13, prek to 0.2.19, hatch to 1.16.0 #58754](https://github.com/apache/airflow/pull/58754) 並且關掉它 😢
    * 根據審查建議，修正 [feat(param): add source to Param #58615](https://github.com/apache/airflow/pull/58615)，現已被合併
    * 審閱 PRs
        1. [Fix CloudwatchTaskHandler display error #54054](https://github.com/apache/airflow/pull/54054)
        2. [fix mypy error in airflow-core/src/airflow/models/trigger.py #58753](https://github.com/apache/airflow/pull/58753)
        3. [Fix: Make dynamically created assets with AssetAlias visible in UI #58087](https://github.com/apache/airflow/pull/58087)
        4. [Revert "Increase scheduler loop sleep in dag.test for executors (#587… #58745](https://github.com/apache/airflow/pull/58745)
        5. [Fix mypy errors in models #58728](https://github.com/apache/airflow/pull/58728)
        6. [[main] Upgrade important CI environment #58732](https://github.com/apache/airflow/pull/58732)
        7. [Catch and log pandas import errors #58744](https://github.com/apache/airflow/pull/58744)
        8. [fix airflowignore negation does not work in subfolders #58740](https://github.com/apache/airflow/pull/58740)

偷偷辦活動還被發現（笑

![message](/images/posts-image/2025-python-workshop-in-tainan/message.jpg)

但我可是有認真在工作的！
我基本上只是等看看有沒有貢獻者有問題，沒有就繼續做我的事

這樣的形式對我來說比較輕鬆
某種程度上也能篩選出適合繼續貢獻開源的人
畢竟在貢獻開源，很難找到有人能一直像直升機那般關照，大家都很忙
最後還是得要自己找到問題，然後找到對的人去問

對於這樣的活動，我都是抱持著「如果有一人能持續，那就算是很成功的活動惹」的心態
倒是聊天的過程也會感受到，大家做事情的方式很不同
有些朋友喜歡成為偉い人、做大事
但我就比較軟爛，喜歡慢慢小小地推進就好
不過也許是不同的人們用各自不同的方式一起幫忙，這些事情才真的能 💪慢慢被推動起來吧

## 台南的愛店
這次托大家的福，吃了很多不錯的食物
不過也還有好幾家想吃的店沒有吃到 😢
但我還是最喜歡我在台南一直喜歡的這兩家愛店們

[性格せいかく](https://www.instagram.com/tainan_singlebrunch/)的拉花真的很棒，食物也很好吃

看啊，燈笑得多開心
![seigaku](/images/posts-image/2025-python-workshop-in-tainan/seigaku.jpeg)
而且，獨 GOGO ，不如眾 GOGO
照片中右邊的小扭蛋，是這次坐旁邊的客人的
一開始還想說我放這麼多娃娃是不是太怪了
餐點上完，我速速拍完就可以收起來
沒想到後來他把他的燈一起放過來，就多聊了一兩個小時
因為 MyGO!!!!! 又認識了一個很酷的新朋友！

再來是[小巷裡的拾壹號](https://www.instagram.com/thealleyno.11/)
他的咖啡就是苦，就是好喝
然而我依然還是沒辦法買到一整盒 10 包的**拾壹號經典配方**的濾掛包
可能太搶手了
除了咖啡好喝外，他的食物也超好吃
我的天啊，那個香蒜醬，真的是太香了

![11](/images/posts-image/2025-python-workshop-in-tainan/11.jpeg)
他有跟我說滿一千也可以免運幫我寄咖啡來北部
希望我都寫下來了，這次喝完要記得可以跟他們訂
