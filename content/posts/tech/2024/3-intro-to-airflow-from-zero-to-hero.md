Title: Intro to Airflow - From Zero to Hero
Subtitle: 3/16 有拍抗女神更精彩的分享，敬請期待
Date: 2024-02-20 23:59 +0800
Category: Tech
Tags: 源來適你, Airflow, Talks
Slug: intro-to-airflow-from-zero-to-hero
Authors: Wei Lee

上週六感謝[源來適你](https://www.facebook.com/profile.php?id=100090487996922)邀請我到社群線上分享 Airflow
好久沒有準備超過 10 分鐘的分享了 😱

<!--more-->

上次上台還是帶著無敵星星在 PyCon APAC 2023 [閃電講](https://speakerdeck.com/leew/does-kobayashi-san-write-code-vulnerable-to-sql-injection) 的時候了
當時台下笑得還蠻開心的
這次不知道是因為線上，還是只是我太沒梗了嗚嗚嗚
內容已經不夠充實了，娛樂效果還不足 🥲

![star](/images/posts-image/2024-intro-to-airflow-from-zero-to-hero/star.jpg)

這次的分享主要介紹了 Airflow 的 component
透過 WebUI 觸發 DAG 後， worker, scheduler, metadata database 是怎麼互動？
deferrable operator 是如何在 worker 跟 triggerer 運作的
上次去勇哥的誰來午餐的時候，剛好有跟 TP 討論到就學了一課

記錄了最近用 [Dataset](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/datasets.html) 遇到的小雷
Dataset 目前還沒有辦法自動偵測 data 是否改變
只能作為其他 DAG 的 outlet
如果那個 DAG 被執行了，才去通知相依於 Dataset 的 DAG
雖然雷的可能是我沒有好好 read the **** documentation

去年聖誕節有被 Flyte 嘴了一下 Airflow 的 operator 語法不直覺
這次輪到我用 [Taskflow](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/taskflow.html#taskflow) 反駁一下
其實 Airflow 也是有跟 Python function 接近的語法啊！

除了介紹其他 astronomer 的開源專案外
還是得例行的工商 [commitizen-tools](https://github.com/commitizen-tools/commitizen) 跟 [PyCon Taiwan](https://tw.pycon.org/)
還有讚揚了 PyCon Taiwan 的 Airflow 最初導師 - 博安老師

<iframe class="speakerdeck-iframe" style="border: 0px; background: rgba(0, 0, 0, 0.1) padding-box; margin: 0px; padding: 0px; border-radius: 6px; box-shadow: rgba(0, 0, 0, 0.2) 0px 5px 40px; width: 100%; height: auto; aspect-ratio: 560 / 420;" frameborder="0" src="https://speakerdeck.com/player/37a8ccf607f245dc8430ad414e74ad81" title="Intro to Airflow - From Zero to Hero" allowfullscreen="true" data-ratio="1.3333333333333333"></iframe>

倒是 Q & A 還蠻熱烈、蠻有趣的
討論了不少職涯、公司的商業模式、技術問題
雖然我離公司很商業的部分有點距離，很多問題都只能窩不知道

![i-don't-know](/images/posts-image/2024-intro-to-airflow-from-zero-to-hero/i-don't-know.jpg)

簡單記錄一下這次的分享
不過最重要還是要宣傳**暫定 3/16 Sat 10:00 a.m. 拍抗女神在源來適你的分享**
請鎖定[源來適你](https://www.facebook.com/profile.php?id=100090487996922)的 FB 粉專公告！
看到這的你各位，通通給我去捧場參加啊
