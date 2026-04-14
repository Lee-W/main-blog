Title: ウォール・ローゼが突破された！
Date: 2025-10-25 11:20 +0800
Category: Tech
Tags: Open Source
Slug: it-matters-revised
Series: IT Matters Awards 2025

哦，不是，是 [IT Matters](https://award.ima.org.tw/) 的初選過了
想說源來適你粉專才發了一篇很多強者報名的貼文
我作為陪跑者的任務應該已經結束了，沒想到有通過

<!--more-->

想當初[2022 年 7 月至今，你到底都做了什麼啊！]({filename}/posts/tech/2025/42-it-matters.md)中的報名之料送出去後
還被通知格式不對

重新看了一次需求

> 請依以下評選構面以及指引填寫實績或規劃。(每個構面下的舉例說明僅為建議填寫方向，不限內容且可自行發揮。請盡量以實績說明。)

原來是每個構面可以自行發揮，不是整個都得要自行發揮
虧我初版可能還比較接近正確的格式
覺得不太喜歡才整理成[2022 年 7 月至今，你到底都做了什麼啊！]({filename}/posts/tech/2025/42-it-matters.md)的樣子
但初版早已不復存在，所以又重新整理了一版

雖然複審還沒有結束，但已經通知大家要準備決審投影片
老實說我也不清楚要準備什麼
就...我也沒辦法憑空生出原本文件沒寫的
有想要追問什麼，用原本的文件就很足夠了吧
直接喚起了，有些文件都寫得又短、又清楚，但還是有人想要找我開會的 PTSD
開會中我能做的什麼呢？
叫對方去看文件...恩...沒了...
我謝謝你 😇

雖然我投影片就是把同樣的內容複製一遍
但倒是有發生個小插曲，讓我再次感到自己身為 Airflow 台灣漢語翻譯負責人是有價值的
避免在台灣的文件中出現開源社區這樣的詞
查了一下，苗栗有個地方叫開元里，也許那裡有開元社區吧
但依然是錯字 🤦‍♂️
不過後來是迅速修正了，給予好評 👍

---

## 1. 創新性與影響力
<!--例如:在參與的專案中，是否為重要貢獻者之一？參與的專案是否具足夠知名度，或被廣泛使用？-->

主要貢獻的中大型開源專案包括 [Apache Airflow](https://github.com/apache/airflow/)、[Ruff](https://github.com/astral-sh/ruff) 以及 [Commitizen](https://github.com/commitizen-tools/commitizen)。

### Apache Airflow

- **個人貢獻**
  - 現任 [Committer](https://github.com/apache/airflow/blob/610b5c0458a835d0e9db0aac4aab8e0caf625002/airflow-core/docs/project.rst?plain=1#L108)，具備直接合併程式碼的權限
  - [台灣漢語程式碼、翻譯負責人](https://github.com/apache/airflow/blob/610b5c0458a835d0e9db0aac4aab8e0caf625002/.github/CODEOWNERS#L48)
  - [貢獻量前 20 名貢獻者](https://github.com/apache/airflow/graphs/contributors)
  - 發起 [350+ 合併 PRs](https://github.com/apache/airflow/pulls?q=sort%3Aupdated-desc+is%3Apr+author%3ALee-W+is%3Amerged+)
  - 主導多項 Airflow Improvement Proposal (AIP)  
    - **[AIP-90 Human in the loop](https://github.com/orgs/apache/projects/508/views/1?query=sort%3Aupdated-desc+is%3Aopen)**（主導人之一）  
    - **[AIP-74 Introducing Data Assets](https://github.com/orgs/apache/projects/412/views/1?query=sort%3Aupdated-desc+is%3Aopen)**（負責主要實作）  
    - **[AIP-75 New Asset-Centric Syntax](https://github.com/orgs/apache/projects/413/views/1?query=sort%3Aupdated-desc+is%3Aopen)**（協助實作）  
- **專案影響力**
  - 被 **[Google Cloud Composer](https://cloud.google.com/composer)、[Amazon MWAA](https://aws.amazon.com/managed-workflows-for-apache-airflow/)、[Astronomer](https://www.astronomer.io/)** 等商業產品直接採用
  - 被開源社群 [PyCon Taiwan](https://tw.pycon.org/) 採用 ([pycon-etl](https://github.com/pycontw/pycon-etl))
  - [約 1,400萬次下載/月](https://pypistats.org/packages/apache-airflow)

### Ruff
- **個人貢獻**
  - [貢獻量前 30 名貢獻者](https://github.com/astral-sh/ruff/graphs/contributors)
  - [發起 62 個合併 PRs](https://github.com/astral-sh/ruff/pulls?q=sort%3Aupdated-desc+is%3Apr+author%3ALee-W+is%3Amerged+)  
  - 主導 **[Airflow 2 → 3 遷移自動化](https://github.com/apache/airflow/issues/41641)**，設計並實作 [Ruff AIR301–312 規則](https://docs.astral.sh/ruff/rules/#airflow-air)
- **專案影響力**
  - [約 7,200萬次下載/月](https://pypistats.org/packages/ruff)
  - 廣泛應用於 [大型開源專案與企業](https://github.com/astral-sh/ruff#whos-using-ruff)

### Commitizen

- **個人貢獻**
  - [專案維護者](https://github.com/commitizen-tools/commitizen/blob/9e6830c97b498d1ffc7a52b66908d82764668c44/pyproject.toml#L7)
  - [貢獻量第 1 名](https://github.com/commitizen-tools/commitizen/graphs/contributors)
- **專案影響力**
  - [約 100萬次下載/月](https://pypistats.org/packages/commitizen)
  - 獲 [Numberly](https://numberly.com/en/) 自 2023/06 起贊助維護

## 2. 可持續性與實踐力
<!--例如:是否積極且持續參與開源專案，並頻繁更新或貢獻？專案是否具實際落地應用與商業可行性？-->

- **長期持續貢獻** (自 2022/07/01 起算)
  - [400+ Airflow 貢獻](https://github.com/apache/airflow/graphs/contributors)
  - [64 Ruff 貢獻](https://github.com/astral-sh/ruff/graphs/contributors)
  - [120+ Commitizen 貢獻](https://github.com/commitizen-tools/commitizen/graphs/contributors)
- **實際落地應用**
  - Airflow: 廣泛應用於 ETL/ML pipeline，並被各大雲端服務整合  
  - Ruff: 已成為 Python 社群主要 linter，亦可協助 Airflow 2 → 3 遷移  
  - Commitizen: 實際應用於企業版本管理流程

## 3. 開源精神與貢獻度
<!--例如:在程式碼、文件撰寫、Issue 回覆、教學內容製作、專案治理等方面是否有具體的貢獻？-->

- **程式碼與設計**
  - 詳述於第一點各中專案個人貢獻
- **文件與翻譯**
  - 擔任 Airflow [台灣漢語程式碼、翻譯負責人](https://github.com/apache/airflow/blob/610b5c0458a835d0e9db0aac4aab8e0caf625002/.github/CODEOWNERS#L48)，負責審閱台灣漢語翻譯相關 PRs
- **專案治理** (自 2022/07/01 起算)
  - 擔任 Airflow Committer
    - [審閱約 1,000 合併 PRs](https://github.com/apache/airflow/pulls?q=sort%3Aupdated-desc+is%3Apr+is%3Aopen+reviewed-by%3ALee-W+-author%3ALee-W)
    - [參與 250+ issue 討論](https://github.com/apache/airflow/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20is%3Aissue%20involves%3ALee-W%20created%3A2022-07-01..2025-08-31)
  - 擔任 Commitizen 維護者
    - [審閱約 500 PRs](https://github.com/commitizen-tools/commitizen/pulls?q=is%3Apr+reviewed-by%3ALee-W+is%3Amerged+merged%3A2022-07-01..2025-08-31+-author%3ALee-W)
    - [參與 150+ issue 討論](https://github.com/commitizen-tools/commitizen/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20is%3Aissue%20involves%3ALee-W%20created%3A2022-07-01..2025-08-31)
- **教學內容**  
  - 持續於 [技術部落格](https://blog.wei-lee.me/) 撰寫文章，分享 Airflow、Ruff、Commitizen 等主題  

## 4. 推廣與傳播力
<!--例如:是否積極參與社群活動，與他人交流互動？是否透過演講、文章、社群媒體等多種管道分享知識、經驗或專案資訊？-->

### 開源技術相關演講 (自 2022/07/01 起算)
1. **2025/10/08** 🇺🇸 - Seamless Migration: Leveraging Ruff for a Smooth Transition from Airflow 2 to Airflow 3 @ [Airflow Summit 2025](https://airflowsummit.org/sessions/2025/seamless-migration-leveraging-ruff-for-a-smooth-transition-from-airflow-2-to-airflow-3/)
2. **2025/09/06** 🇹🇼 - Unlocking the Future of Data Pipelines - Apache Airflow 3 @ [PyCon TW 2025](https://tw.pycon.org/2025/en-us/conference/talk/366)
3. **2025/07/18** 🇨🇿 - Hold on! You have a data team in PyCon Taiwan! @ [EuroPython 2025](https://ep2025.europython.eu/session/hold-on-you-have-a-data-team-in-pycon-taiwan)  
    - [slide](https://speakerdeck.com/leew/hold-on-you-have-a-data-team-in-pycon-taiwan)
4. **2025/03/28** 🇹🇼 - Airflow 3.0 The First Glance @ [黃金流沙饅頭營](https://www.icloud.com/pages/0c6_qp3_RnuCJfcIh8_9xnqLA#2025_%E9%BB%83%E9%87%91%E6%B5%81%E6%B2%99%E9%A5%85%E9%A0%AD%E7%87%9F)  
    - [slide](https://speakerdeck.com/leew/20250328-airflow-3-dot-0-the-first-glance)
5. **2025/03/16** 💻 - 踏入開源的第一步 @ NetDB - Tech Day, Invited Talk  
    - [slide](https://speakerdeck.com/leew/20250316-ta-ru-kai-yuan-de-di-bu)
6. **2025/03/02** 🇵🇭 - Unleash the Chaos: Developing a Linter for Un-Pythonic Code! @ [PyCon APAC 2025](https://pycon-apac.python.ph/)  
    - [slide](https://speakerdeck.com/leew/unleash-the-chaos-developing-a-linter-for-un-pythonic-code-806b2bae-e161-4762-b0d5-d9fb8efdd24a)  
    - [🎬recording](https://www.youtube.com/watch?v=tbSZx0UsWfQ)
7. **2024/09/28** 🇯🇵 - Unlocking Python's Core Magic @ [PyCon JP 2024](https://2024.pycon.jp/en/talk/AQKFHX)  
    - [slide](https://speakerdeck.com/leew/unlocking-pythons-core-magic)  
    - [🎬recording](https://www.youtube.com/watch?v=9jbHA6tE9MM)
8. **2024/09/21** 🇹🇼 - Unleash the Chaos: Developing a Linter for Un-Pythonic Code! @ [PyCon TW 2024](https://tw.pycon.org/2024/conference/talk/311)  
    - [slide](https://speakerdeck.com/leew/unleash-the-chaos-developing-a-linter-for-un-pythonic-code)  
    - [🎬recording](https://www.youtube.com/watch?v=2jUd0o8VuE0)
9. **2024/09/11** 🇺🇸 - What If...? Running Airflow Tasks without the workers @ [Airflow Summit 2024](https://airflowsummit.org/sessions/2024/what-if-running-airflow-tasks-without-the-workers/)  
    - [slide](https://docs.google.com/presentation/d/1XGd7bQg6cGLNbHFiZjX__SmI4FLw6D_iASY9eRSO4mo/edit?usp=sharing)  
    - [🎬recording](https://www.youtube.com/watch?v=WkljjYtqu8Q)
10. *2024/05/08* 💻 - Starts Airflow task execution directly from the triggerer @ Airflow Town Hall  
    - [slide](https://speakerdeck.com/leew/starts-airflow-task-execution-directly-from-the-triggerer)
11. *2024/02/17* 💻 - Intro to Airflow - From Zero to Hero @ [源來適你](https://www.facebook.com/opensource4you)  
    - [slide](https://speakerdeck.com/leew/intro-to-airflow-from-zero-to-hero)
12. **2023/07/29** 🇹🇼 - Atomic Commits: An Easy & Proven Way to Manage & Automate Release Process @ [COSCUP 2023](https://coscup.org/2023/zh-TW/session/TUGLJP)
    - [slide](https://speakerdeck.com/leew/atomic-commits-an-easy-and-proven-way-to-manage-and-automate-release-process)  
    - [🎬recording](https://www.youtube.com/watch?v=IxzN9ClXhs8)

### 其他開源社群活動
- **主導衝刺開發** (Python 研討會中類似黑客松，但專注於開源專案貢獻的活動)  
  - **Apache Airflow**
        1. [EuroPython 2025](https://github.com/EuroPython/website/pull/1437)
        2. [DurianPy](https://www.meetup.com/durianpy/events/308390476/)
        3. PyCon APAC 2025
        4. [PyCon TW 2024](https://hackmd.io/LKLr7XyOR9mK1AEEnvnCuQ#Apache-Airflow)
  - **Commitizen**
        5. [PyCon US 2024](https://us.pycon.org/2024/events/dev-sprints/#sprint-3)
        6. [COSCUP 2024](https://pretalx.coscup.org/coscup-2024/talk/SDR77M/)
        7. [Scisprint Taipei 2024 March](https://sciwork.kktix.cc/events/scisprint-202403-taipei)
        8. [PyCon TW 2023](https://hackmd.io/R98LEB4MSxm4AeExmxuZnA#commitizen-tools)
        9. [Scisprint@Amazon Taipei 2023](https://sciwork.kktix.cc/events/scisprint-202302-taipei)
        10. [PyCon TW 2022](https://hackmd.io/UYumgLy_QxaCSCqrXKDBpw#commitizen-tools)
        11. [PyCon TW 2021](https://hackmd.io/PAgYsu5nSHyERIRaUokWxQ#commitizen-tools)
        12. PyCon TW 2020
        13. PyCon CA 2019
- **導師**: 擔任 [「源來是你」Airflow 與 Commitizen 導師](https://blog.wei-lee.me/)，協助新手開源參與
- **公開分享技術內容**  
  - 投影片（[SpeakerDeck](https://speakerdeck.com/leew)）  
  - 文章 ([部落格](https://blog.wei-lee.me/))  

## 5. 其他開源成就（加分項）
<!--例如:是否有參與或作為主要成員組織國際開源社群活動？近三年 (2022/07/01後) 是否獲得其他開源獎項或成就？-->

- **國際社群志工**
  - [Python Asia Organization](https://pythonasia.org/events/)  
    - EuroPython 2025 攤位志工
  - [PyCon APAC](https://pycon.asia/)  
    - PyCon JP 2024 攤位志工  
    - PyCon US 2024 攤位志工
  - [PyCon CA 2019](https://2019.pycon.ca/) 議程主持人
- **[PyCon Taiwan](https://tw.pycon.org) 志工**  
  - 2025: 到處都看得到他們、審稿委員  
  - 2024: 公關 & 行銷組員、審稿委員  
  - 2023: 行銷組長  
  - 2022: 大會副主席  
  - 2021: 大會主席  
  - 2020: 議程組長  
  - 2019: 議程組員  
- **[源來適你](https://github.com/opensource4you/readme)**  
  - 導師（Airflow / Commitizen）
