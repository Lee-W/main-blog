Title: 黃金流沙饅頭營 Airflow 3.0 The First Glance
Subtitle: ✅ 30 張梗圖
Date: 2025-05-29 21:55
Category: Tech
Tags: 源來適你, Airflow 3.0
Slug: airflow-3-0-the-first-glance
Authors: Wei Lee
Cover:/images/meme/mygo-it-s-mygo.jpg

今天聽 Python Bytes [#433] 提到 Airflow 3 才提醒我
兩個月前的黃金流沙饅頭營，我還沒寫篇文章記錄一下

<!--more-->

投影片先上

<iframe class="speakerdeck-iframe" style="border: 0px; background: rgba(0, 0, 0, 0.1) padding-box; margin: 0px; padding: 0px; border-radius: 6px; box-shadow: rgba(0, 0, 0, 0.2) 0px 5px 40px; width: 100%; height: auto; aspect-ratio: 560 / 315;" frameborder="0" src="https://speakerdeck.com/player/dac2c29511774834b0e24d0e624b1575" title="20250328 Airflow 3.0 The First Glance" allowfullscreen="true" data-ratio="1.7777777777777777"></iframe>

原本以為跟[黃金流沙饅頭營 Airflow 3.0 宣傳影片 幕後花絮]({filename}/posts/tech/2025/10-opensource4you-airflow-3-0-event-promotion.md)簡介的差不多
重新翻過投影片其實比預期的講得還多一點
還好時隔兩個月， Airflow 3.0 並沒有跟我當初講的差太多

1. 什麼是 Airflow
2. 為什麼要用 Aiflow
3. AIP-63 - Dag Versioning
4. AIP-38 - Modern Web Design
5. AIP-72 - TaskSDK
    * 提到的比較少，當時對使用者來說也不太重要（這裡記住，待會會考）
7. AIR-73 - Expanded Data Awareness
8. AIP-82 - External Event Driven Scheduling
9. Migration tool - (`airflow conflg lint`, `ruff`)
10. 一起來貢獻 Airflow 叭

倒是 AIP-82 我也是為了這場分享才第一次使用
雖然在之前有大概知道在幹嘛

準備這場分享比較挑戰的大概是這個吧

![30-meme](/images/posts-image/2025-airflow-3-0-the-first-glance/30-meme.jpg)

雖然很麻煩，但又覺得不能在這裡退縮（這種事可能還是退縮一下比較好...）
不過最後我還是達成了！
如果仔細看投影片，梗圖頁的左上角有一個淡淡的數字
那是用來數幾張梗圖的，到最後剛好是 30 張
倒是重數才發現， MyGO!!!!! 跟 Ave Mujica 的梗圖只用了 9 張...
彷彿聽到教主的聲音「是不是假粉」
尤其是前一段時間聽了 [SITCON 2025 R1｜如何演奏春日影？初探影音格式原理與壓縮｜講者 James Kuo-Ping Lo (Misawai)][haruhikage]
這才是真正的 GO 廚啊！！！！！
我得好好向他學習

## 上機實作
除了早上的分享外，下午還有上機實作的環節
雖然沒有網路，還要大家下載 docker image 是有點尷尬
但還有更尷尬的
早上到現場才發現，我也沒辦法把 Airflow 3.0b4 裝起來
不知道是什麼東西壞掉了...
alpha 2 不是好好的嗎
不然回去用 a2 好了，但也不行
被移掉了......

最後就讓大家直接開 breeze 玩玩看 main branch 的 Airflow 了

## TaskSDK
那到底是為什麽三月的時候提 TaskSDK ，使用者可能也無感
就要回到 [AIP-72 - Task Execution Interface aka Task SDK][AIP-72] 提到的 Airflow 的 task 要支援 Python 以外的語言了
可是那時候除了 Python 以外並沒有實作其他的 SDK
你可以用其他語言的 SDK ，但並沒有所謂其他語言的 SDK

![mygo-it-is-but-it-is-not](/images/meme/mygo-it-is-but-it-is-not.jpg)


然而！
最近已經要開始撰寫 GO 的 SDK 了
現在就點擊 <https://apache-airflow.slack.com/archives/C07813CNKA8/p1748434643593459> 一起 GO 起來吧！

![it's mygo](/images/meme/mygo-it-s-mygo.jpg)

[#433]: https://open.spotify.com/show/5o8820UB982QGwS4GYMGx9
[haruhikage]: https://www.youtube.com/watch?v=ZkxE6nLq19s
[AIP-72]: {filename}/posts/tech/2024/22-aip-72.md
