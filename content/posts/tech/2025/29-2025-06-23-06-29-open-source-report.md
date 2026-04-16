Title: 2025/06/23 - 06/29 開源貢獻週報
Subtitle: 事不宜遲，現在就購票吧
Date: 2025-07-01 10:40 +0800
Category: Tech
Tags: Open Source, 開源貢獻週報
Slug: 2025-06-23-06-29-open-source-report
Authors: Wei Lee
Lang: zh-tw

這是個充滿 PyCon TW 的一週

<!--more-->

## commtizien
* 審閱 PR [refactor(Init): extract _get_config_data for readability #1538](https://github.com/commitizen-tools/commitizen/pull/1538)
    * 這週還是努力看了一個 PR 嗚嗚嗚嗚嗚

## attila
* 審閱 PR [Fix: use correct selector for highlight.js #2](https://github.com/Lee-W/attila/pull/2)
    * 問題終於被解決了！感恩讚嘆

## pycontw-frontend
* 審閱 PR [update(events): change sprint event tag from post-event to warmup #651](https://github.com/pycontw/pycontw-frontend/pull/651)
    * 源來適你的朋友發現 PyCon TW 官網上活動細節有錯  
      馬上就被修正了，不愧是高瓊強尼戴普  
      事不宜遲，現在就[購票](https://tw.pycon.org/2025/registration/tickets)吧

## pycon-etl
* 開 PR
    * [Add airflow triggerer, update config to fit our limited resource and fix bug found in posts_insights dag #163](https://github.com/pycontw/pycon-etl/pull/163)
        * 機器開太小，跑不起兩個 worker  
          但便宜治百病，一個 worker 也是沒問題！
    * ❌[fix: downgrade uvicorn to 0.29.0 #164](https://github.com/pycontw/pycon-etl/pull/164)
        * 這個 PR 什麼也修不了
    * [fix(docker-compose): add missing AIRFLOW__CORE__EXECUTION_API_SERVER_URL #165](https://github.com/pycontw/pycon-etl/pull/165)
        * 明明開發環境就好好的，為什麼到了生產環境就連不上 API 伺服器了！  
          啊...原來是生產環境的 docker-compose 沒改到嗎...那沒事了
    * [Cleanup not used configuration and dag #166](https://github.com/pycontw/pycon-etl/pull/166)
        * 有些 dag 跟設定沒用到就刪一刪
    * [Rewrite documentation and publish it to GitHub Pages using mkdocs #168](https://github.com/pycontw/pycon-etl/pull/168)
        * 回來碰 pycon-etl 的時候，在各環節都遇到很多問題，而且在文件上都找不到答案 🥲  
          還好有 Henry 幫忙，順手就記錄下 Henry 教我的各個細節
    * [Move mypy config from setup.cfg to pyproject.toml #171](https://github.com/pycontw/pycon-etl/pull/171)
        * 沒想到 setup.cfg 這東西還在，該刪了吧  
          把 `AIRFLOW_HOME` 也一起加進 `PYTHON_PATH`，這樣才能正常匯入 repo 的函式庫
    * (草稿) [feat(discord): move all discord message sending to dag "discord_message_notification" and use Asset to trigger #167](https://github.com/pycontw/pycon-etl/pull/167)
        * 將傳送 Discord 訊息的邏輯整合到同一個 dag 執行
          如果其他 dag 有需要傳 Discord 訊息，那麼它們要 yield 一個 outlet event，並把要送給 Discord API 的資訊寫在 extra 中  
          另外也嘗試使用 [AIP-82](https://cwiki.apache.org/confluence/display/AIRFLOW/AIP-82+External+event+driven+scheduling+in+Airflow) 的 `AssetWatcher` 來偵測上游資料有沒有改變  
          其實以我們的情境，也許 [AIP-77](https://cwiki.apache.org/confluence/display/AIRFLOW/%5BWIP%5D+AIP-77+Asset+Validations) 比較適合，但這就要等到它被實作了
          這樣改動的好處是 ~~使用了比較潮的功能~~ ，只留下一個 Discord 訊息的發送點，如果有少發或多發訊息都可以很容易找到原因
* 關閉 issue [Upgrade to Airflow 2+ (or even 3) #154](https://github.com/pycontw/pycon-etl/issues/154)
    * 已經成功升級到 Airflow 3.0.2 並且部署到 GCE 上了 🎉
* 開 issue
    1. [[Feature Request] Check whether git bundle fits our use case #169](https://github.com/pycontw/pycon-etl/issues/169)
        * 還沒研究，但聽起來 git bundle 跟我們的部署方式比較吻合
    2. [[Feature Request] Move our discord role assigning functionality to airflow #170](https://github.com/pycontw/pycon-etl/issues/170)
        * 這是我回來碰 pycon-etl 的起點  
          這些定時跑的東西可以盡量整合進 pycon-etl  
          不然隨著時間推移，志工們會漸漸忘記這些服務到底都在哪
