Title: 2025/06/30 - 07/06 開源貢獻週報
Subtitle: 下一期八月再見
Date: 2025-07-06 21:55 +0800
Category: Tech
Tags: Open Source, 開源貢獻週報
Slug: 2025-06-30-07-06-open-source-report
Authors: Wei Lee
Cover: /images/meme/jojo-last-hamon.png

下個禮拜就要出發前往 EuroPython 了
這段期間除了上班以外的時間，都會拿來旅遊
大概沒什麼機會貢獻開源，所以就回來再說吧～

<!--more-->

## cargo-dist
* 之前為了 Ruff 開的 PR [feat: update ubuntu version from 20.04 to 22.04 #1766](https://github.com/axodotdev/cargo-dist/issues/1760) 剛好在這幾天被合併了

## commitizen
* 審閱 PRs
    1. [fix(ExitCode): add from_str in ExitCode and replace parse_no_raise with it, warn if the error code is not in range #1545](https://github.com/commitizen-tools/commitizen/pull/1545/files)
    2. [refactor(process_commit_message): better type and early return #1542](https://github.com/commitizen-tools/commitizen/pull/1542)

還是努力看了一兩隻 PR
但這真的就是我回國前最後的波紋了

![jojo-last-hamon](/images/meme/jojo-last-hamon.png)

## pycon-etl
* 開 PRs
    1. [Upgrade to Airflow 3.0.3 #172](https://github.com/pycontw/pycon-etl/pull/172)
        * 最近剛好在 [[VOTE] Release Airflow 3.0.3 from 3.0.3rc3 & Task SDK 1.0.3 from 1.0.3rc3](https://lists.apache.org/thread/n1l14lrf8gwcxwnqt81fj8c63ondy0zy)，就直接拿來測測看，升到這個版本後 pycon-etl 的 patch 檔們就可以刪光光惹
    2. [refactor(dags:airflow_log_cleanup): split the huge bash as separate tasks #173](https://github.com/pycontw/pycon-etl/pull/173)
        * 把那串不知道哪抄來的超長 bash 腳本拆開來，玩了一下 [TaskGroups](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html#taskgroups) 跟 [Params](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/params.html)
        * 很多邏輯應該可以刪掉，但我只先把原本 bash 改成 Python 或是 Airflow 任務
        * 原本一個做這麼多事的任務被我拆成一個個細小的任務  
          (原來可以有巢狀 TaskGroup 🤔)
          ![task-groups](/images/posts-image/2025-06-30-07-06-open-source-report/task-groups.jpg)
* 完成 PR [feat(discord): move all discord message sending to dag "discord_message_notification" and use Asset to trigger #167](https://github.com/pycontw/pycon-etl/pull/167)
    * 延續 [2025/06/23 - 06/29 開源貢獻週報 - 事不宜遲，現在就購票吧]({filename}/posts/tech/2025/29-2025-06-23-06-29-open-source-report.md) 繼續改下去，將 [AIP-75](https://cwiki.apache.org/confluence/display/AIRFLOW/AIP-75+New+Asset-Centric+Syntax) 加入的新語法也用上了，但確實是比較合理
    * 用 [HttpHook](https://airflow.apache.org/docs/apache-airflow-providers-http/stable/_api/airflow/providers/http/hooks/http/index.html#airflow.providers.http.hooks.http.HttpHook) 重新寫過傳送 Discord 訊息的邏輯，並且讓上游的資源（Asset） 在傳送資源事件額外資訊（Asset Event Extra）只傳 Airflow 變數（Variable）的鍵，到了傳送訊息的 Dag 才去取得實際的值，以確保所有的 webhook 都是由 Airflow 變數所管理
    * 現在所有資產跟 Dag 之間的相依大概長這樣 ![assets](/images/posts-image/2025-06-30-07-06-open-source-report/assets.jpg)


---

## Reference
* [JOJO 的奇妙冒險](https://ani.gamer.com.tw/animeVideo.php?sn=6166)
