Title: Airflow 的前世今生
Date: 2026-09-26 14:38 +0800
Category: Tech
Tags: Airflow, Open Source, PyCon TW
Slug: happy-birthday-airflow
Authors: Wei Lee
Lang: zh-tw
Status: draft

上週受到 [Software Freedom Day Bukidnon](https://www.facebook.com/sfd.bukidnon.ph) 的邀請去分享 Airflow

<!--more-->

因為邀請來得有點突然，再加上我最近搬家真的太累了......
最後準備的內容，大致上就是上次 COMPUTEX 2026 [Your AI Is Only As Good As Your Data Pipeline](https://speakerdeck.com/leew/youral-is-only-as-good-as-your-data-pipeline) 的加強版

除了追加一點 [Common AI](https://airflow.apache.org/docs/apache-airflow-providers-common-ai/stable/index.html) 整合套件（provider）的介紹
剩下就是稍微談了一下接下來跟 AI workflow 有關的一些 AIP，例如：

* [AIP-111: Task Loops](https://cwiki.apache.org/confluence/spaces/AIRFLOW/pages/440303747/AIP-111+Task+Loops)
* [AIP-115: On-Demand Task Sections](https://cwiki.apache.org/confluence/spaces/AIRFLOW/pages/440305022/AIP-115+On-Demand+Task+Sections)

不過這些其實都不是這篇文章的重點，其他細節就去翻投影片吧 😆

→ [Orchestration Still Matters: Apache Airflow in the Age of AI](https://speakerdeck.com/leew/orchestration-still-matters-apache-airflow-in-the-age-of-ai)

這篇真正想記錄的，是我在做投影片時意外考古到的東西：

**Airflow 到底是哪一天出生的？**

## 是 Airflow 沒錯，但不是 Airflow

![it is, but it is not](/images/meme/avemujica-it-is-but-it-is-not.jpg)
/// caption
© BanG Dream! Project | 出自 [BanG Dream! Ave Mujica](https://ani.gamer.com.tw/animeVideo.php?sn=41638)
///

Airflow 官方把它的起點放在 2014 年 10 月
GitHub 上可以找到的第一個提交，是 2014/10/07 的 [First official commit](https://github.com/apache/airflow/commit/1047940ca4363b04044c4963b9c88f7632746407)

不過如果你真的點進去考古一下，就會發現一件有趣的事情：
**那時候其實還沒有 Airflow**，只有 **Flux**

直到八天後的 2014/10/15，才出現這個 [Renaming project from Flux to Airflow](https://github.com/apache/airflow/commit/88c99624f33880c4ea3dae0a9db767f84b36d79e)

所以如果把第一個 official commit 當成生日，那 Airflow 的生日確實是 10 月 7 日
但如果堅持要說「Airflow」這個名字是哪一天出現的，那其實是 10 月 15 日

不過想想，人類改名也不會說改名的那天才是生日
所以說 2014/10/07 好像還是比較合理 🤔

## Airflow → Apache Airflow

那又是什麼時候從 Airflow 變成 Apache Airflow 的呢？

Airflow 在 2015 年 6 月正式被移到 Airbnb 的 GitHub 並公開發表
接著在 2016 年 3 月加入 Apache Incubator，開始了成為 Apache 專案的旅程

到了 2017/04/17，則可以找到 [[AIRFLOW-1000] Rebrand distribution to Apache Airflow](https://github.com/apache/airflow/commit/4fb05d8cc7)
Python distribution 也從原本的 `airflow` rebrand 成現在熟悉的 `apache-airflow`

而這趟旅程最後在 2019 年 1 月，Apache Airflow 從 Incubator 畢業，正式成為 Apache Software Foundation 的 Top-Level Project，告一個段落

透過 AI 幫我整理了一下時間線：

* **2014/10/07** — First official commit，當時專案還叫 Flux
* **2014/10/15** — Flux 改名為 Airflow
* **2015/06** — 正式移到 Airbnb GitHub 並公開發表
* **2016/03** — 加入 Apache Incubator
* **2016/04** — 開始遷移到 Apache 的基礎設施
* **2017/04/17** — Python distribution rebrand 為 Apache Airflow
* **2019/01** — 從 Incubator 畢業，成為 Apache Top-Level Project

## 那就來過生日吧 🎂

Apache Airflow Korea User Group 將在今年 10/7，也就是 First official commit 的十二週年，幫 Airflow 舉辦生日派對：

[Apache Airflow Birthday Party](https://www.meetup.com/korea-apache-airflow-user-group/events/316548871/)

剛好幾天後的 [PyCon TW 2026](https://tw.pycon.org/2026/) 又離 10/15，也就是 Flux 正式改名為 Airflow 的日子非常近
那既然韓國都過了，台灣也來過一下吧 🎂

在 [PyCon TW 2026](https://tw.pycon.org/2026/en-us) 第一天，Apache Airflow Taiwan User Group 將跟韓國社群的朋友一起慶祝：

→ [Airflow Community Open Space & Birthday Celebration @ PyCon TW 2026 🎂](https://www.meetup.com/taipei_py/events/316661146/)
第二天也還會有 [Airflow Community Open Space @ PyCon TW 2026 🇰🇷 🇹🇼](https://www.meetup.com/taipei_py/events/316661171/)
總之就是大家隨興聊聊 Airflow 的小空間

距離 Apache Airflow Taiwan User Group 上次有活動已經是好久以前
後來寄生的 Taipei.py 消滅後，就跟著一起消滅了

最近 [Taipei.py](https://www.meetup.com/taipei_py/) 復活了
那 Apache Airflow Taiwan User Group 就一起復活吧

![mygo-restore-right](/images/meme/mygo-restore-right.jpg)

而且 PyCon TW 2026 結束後還有加碼的 [PyCon TW 2026 After-Sprint](https://www.meetup.com/taipei_py/events/316510887/)

目前只有 Apache Airflow 一個專案
所以此刻我們還是可以把它視為一個 Airflow 的活動 😆

歡迎大家一起來玩！
