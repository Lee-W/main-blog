Title: 黃金流沙饅頭營 Airflow 3.0 宣傳影片 幕後花絮
Subtitle: 拋頭露面實在不是 I 人如我做的來的
Date: 2025-03-29 11:50 +0800
Category: Tech
Tags: Airflow, Airflow 3.0, 源來適你
Slug: opensource4you-airflow-3-0-event-promotion
Authors: Wei Lee

這實在是嘔心瀝血之作啊
除了腳本反覆雕琢，錄影更是錄了 127 次才成功
這實在是太挑戰 I 人我了

<!--more-->

> 你會介意拍個一分鐘的宣傳短片嗎？
> 大概20秒自我介紹 40秒講一下你對 airflow 大版最期待的功德是啥

當初就是收到了一個這樣的訊息
到現在寫這篇文章的時候才發現嘉平打錯字了

## 腳本
大家好，我是李唯。目前是 Apache Airflow 的 committer，平時在幾個開源社群間走跳。在源來適你，姑且算是 airflow 組的 mentor 。在今年九月即將於台北舉辦的 PyCon Taiwan 也擔任了 5 ~ 6 年的志工，最常像現在這樣，宣傳大會以及目前絕贊徵稿中的資訊。現在正是投稿的時刻。

回到 Airflow。爲什麼要使用 Airflow? 因為 Airflow 是一個好工具。它可以幫助你輕鬆完成各種任務的排程。而三月底 Airflow 將迎來它睽違 5 年的大更新。
最令人期待的功能想必就是大家敲碗許久的的 Dag versioning ，讓使用者方便比對過去 Dag 執行時的邏輯。
除此之外，Airflow 3 加強了 Data asset 的概念。讓使用者可以直接定義一個 top level 的 asset，並讓 dag 相依於 asset 進行排程。如果能串起這一個又一個的 asset 和 dag ，也許就能產出更 data centric 的 use cases。
除了功能更強更厲害，就在今天早上，過去過時的UI已經死了。我們想讓UI重新開始，因此用 React 重新寫過介面，為了帶給使用者嶄新的體驗。
功能很多是很棒，但升版是一件很累的事啊。如果你從來不覺得升版開心過，除了 Airflow 本身自帶的升版工具外，我們這次跟 ruff 進行合作，加入了許多 airflow 2 to 3 的規則，讓你能更快速的將 Dag 搬到 Airflow 3。聽到這裡，我想你心裡多少也有些想法吧，希望你務必加入我們社群，一起讓台灣的工程師在世界的舞臺上被看到。

## 腳本撰寫
我其實也不確定最後的影片是不是完全照著腳本念
但實在太羞恥了，我也不敢自己看一遍

不過看完腳本你也發現了吧
沒錯！
除了 Airflow 外，我還偷渡了 [PyCon Taiwan 的徵稿資訊](https://tw.pycon.org/2025/en-us/speaking/cfp)
都看到這了，擇日不如撞日，現在就去投稿吧 💪

自我介紹大概還是抓在 20 秒左右
簡單帶到我在源來適你幹嘛，還得切到推廣 PyCon Taiwan 的徵稿資訊
就沒有機會提到 [commitizen-tools](https://github.com/commitizen-tools/) 了

Airflow 的介紹則是分為幾個部分

* [AIP-63 DAG Versioning]： 畢竟是大家敲碗數年的功能
* [AIP-73 Expanded Data Awareness]： 裡面有一部分是我貢獻的，當然要自肥一下
* [AIP-38 Modern Web Application]： 剛好錄影當天早上 [Remove old UI and webserver #46942] 被 merge 了，也算是比較好理解的概念，就提一下
* [Airflow 2 to 3 auto migration rules #41641]： 現在這也算是我在 own 的功能，也能減輕大家升版到 Airflow 3 的壓力

光是提到這幾點，大概就要 1 分 40 秒了
原本好像還有想提到另一個什麼功能，但最後砍掉了

## 錄影
之所以要錄這麼多次，主要還是希望不要離腳本太遠
尤其是重要的台詞，那個味道還是要在
不然應該可以輕鬆錄錄就結束了

雖然好像錄了很多次，但有幾次錄了 3 秒就咖掉了
不過相機裡面有這麼多影片數，我就堆上去充數了

背景的設計則是我自豪的工作空間
調了幾個角度沒辦法再拍到更多周邊
右後方放了一些搖曳露營的，左後方則是放了燈
升降桌調整到適當的高度，讓他們能正常入鏡
說背景要扣分的
我看你是完全不懂哦

## MyGO 在哪裡，絕對難不倒你

![mygo-restore-right](/images/meme/mygo-restore-right.jpg)

![mygo-why-harahikage](/images/meme/mygo-why-harahikage.jpg)

![mygo-harahikage-is-agood-song](/images/meme/mygo-harahikage-is-agood-song.jpg)

![mygo-accumulate](/images/meme/mygo-accumulate.jpg)

![mygo-accumulate-2](/images/meme/mygo-accumulate-2.jpg)

![mygo-weak-self](/images/meme/mygo-weak-self.jpg)

![mygo-crychic-restart](/images/meme/mygo-crychic-restart.jpg)

![mygo-never-happy](/images/meme/mygo-never-happy.jpg)

![mygo-thoughts](/images/meme/mygo-thoughts.jpg)

![mygo-join-my-band](/images/meme/mygo-join-my-band.jpg)

> 要偷渡幾次 MyGo 😂

沒想到我的宣傳文發出來後，2 分鐘內就被抓包

> 啊，竟然一發佈就被抓到
>
> 不過是 10 次，我的腳本偷渡了 10 次
> 如果不算影片右邊的小燈立牌

恩，對，是 10 次

[AIP-63 DAG Versioning]: https://cwiki.apache.org/confluence/display/AIRFLOW/AIP-63%3A+DAG+Versioning
[AIP-73 Expanded Data Awareness]: https://cwiki.apache.org/confluence/display/AIRFLOW/AIP-73+Expanded+Data+Awareness
[AIP-38 Modern Web Application]: https://cwiki.apache.org/confluence/display/AIRFLOW/AIP-38+Modern+Web+Application
[Remove old UI and webserver #46942]: https://github.com/apache/airflow/pull/46942
[Airflow 2 to 3 auto migration rules #41641]: https://github.com/apache/airflow/issues/41641
