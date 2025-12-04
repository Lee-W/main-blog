Title: 觸發觸發器的元件，是不是該叫觸發觸發器器
Date: 2025-12-04 22:40
Category: Tech
Tags: Airflow
Slug: airflow-triggerer-trigger-translation
Authors: Wei Lee

最近突然好奇 Apache Airflow 的 Trigger 跟 Trigger**er** 到底是怎麼翻譯的
去看了一下，竟然都翻譯成觸發器
這不對啊
如果 trigger 是`觸發器`，那 trigger**er**應該要是`觸發觸發器器`吧

<!--more-->

trigger 叫觸發器應該是可以
trigger**er** 是管一堆 trigger 的元件
嚴格來說應該也能是一種觸發器吧我想

出於好奇就拿去源來適你的 Airflow 頻道問大家的想法
第一個得到的回答是最一般的

> 觸發器 觸發者？我亂翻的 中文造詣不高

沒想到我中文造詣更差，根本連這句話都沒有看懂
就讓話題繼續下去了
這裡收集了大家有趣的想法們

* 觸發器主管
* 觸發器長
* 觸發總管
* 觸發器人
* 觸發器管理員
* 觸發王
* 觸發強者
* 觸發大師
* 非同步觸發魔法棒
* 板機者

最後想到了觸發者
沒想到又回到了最一開始的提案，再看了一次那句話才看懂

因為原先 Dag 執行的 `triggeredBy` 被翻譯成觸發者，我就把它改為觸發來源了
應該也是比較符合原意一點

👉 [fix(i18n): Translate trigger as 觸發器, triggerer as 觸發者 and dagRun.triggeredBy as 觸發來源 #58988](https://github.com/apache/airflow/pull/58988)

不過我還是蠻喜歡觸發觸發器器跟板機者的
但我實在不敢發 PR 🫢
