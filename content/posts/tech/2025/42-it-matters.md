Title: 2022 年 7 月至今，你到底都做了什麼啊！
Date: 2025-08-24 17:55
Category: Tech
Tags: Open Source
Slug: what-have-you-done-since-2022-07
Authors: Wei Lee

這聽起來像是動畫作品中
反派角色做了什麼很瘋狂的事
被至親或隊友反問的話
但一時還真的舉不出一部作品

<!--more-->

原本想用喬納森跟迪奧初見面的片段，但又覺得味道不對

不過說了這麼多
其實這是 [IT Matters](https://award.ima.org.tw/) 開源社群貢獻獎的報名資料
條件是 2022/07/01 後的開源貢獻
一開始還興趣普普，忘記看到什麼就覺得好像可以來報名一下

整理完我的貢獻，再看了一輪身旁的人們
如果以現在當紅 meta 來說，我大概就是鬼滅初登場的佛堂鬼
身旁都是一群牛鬼蛇神
雖然這也是主要我會待在社群打滾的原因
到處抱大腿、到處學習

反正報名表寫都寫了，就拿它來水一篇文章
記錄一下 2022/07/01 ~ 2025/08/31 我還想得起來的開源參與

[TOC]

## 主要開源專案貢獻

### Apache Airflow
- **專案影響力**
    - 商業應用： 被 **[Google Cloud Composer](https://cloud.google.com/composer)、[Amazon MWAA](https://aws.amazon.com/managed-workflows-for-apache-airflow/)、[Astronomer](https://www.astronomer.io/)** 等商業產品直接採用  
    - 社群應用： PyCon Taiwan 的 [pycon-etl](https://github.com/pycontw/pycon-etl) 以 Airflow 為核心管理社群內資料
    - [月下載量約 1,400 萬](https://pypistats.org/packages/apache-airflow)
- **個人身份與影響力**
    - 現任 [Committer](https://airflow.apache.org/community/#committers)，具備直接合併程式碼權限
    - [台灣漢語程式碼負責人、翻譯負責人](https://github.com/apache/airflow/blob/eae6578ca53b3a8b29755ebb00d1059d2d409ee8/.github/CODEOWNERS#L48)
- **技術與專案貢獻（2023 至今）**
    - 專案[前 20 名貢獻者](https://github.com/apache/airflow/graphs/contributors)
    - [400+ 個貢獻](https://github.com/apache/airflow/graphs/contributors)
    - [發起 350+ 合併 PRs](https://github.com/apache/airflow/pulls?q=sort%3Aupdated-desc+is%3Apr+author%3ALee-W+is%3Amerged+)
    - [審閱約 1,000 合併 PRs](https://github.com/apache/airflow/pulls?q=sort%3Aupdated-desc+is%3Apr+is%3Aopen+reviewed-by%3ALee-W+-author%3ALee-W)
    - [參與 250+ issue 討論](https://github.com/apache/airflow/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20is%3Aissue%20involves%3ALee-W%20created%3A2022-07-01..2025-08-31)
    - 主導多項 Airflow Improvement Proposal (AIP) 設計與實作
        - **[AIP-90 Human in the loop](https://cwiki.apache.org/confluence/display/AIRFLOW/AIP-90+Human+in+the+loop)**（主導人之一）  
        - **[AIP-74 Introducing Data Assets](https://cwiki.apache.org/confluence/display/AIRFLOW/AIP-74+Introducing+Data+Assets)**（協助實作）  
        - **[AIP-75 New Asset-Centric Syntax](https://cwiki.apache.org/confluence/display/AIRFLOW/AIP-75+New+Asset-Centric+Syntax)**（協助實作）  
    - 主導 Airflow 2 → 3 [遷移自動化](https://github.com/apache/airflow/issues/41641)，包括 **Ruff AIR 規則設計與實作**
- **相關社群參與**
    - 擔任 [源來是你 Airflow Mentor](https://github.com/opensource4you/readme?tab=readme-ov-file#%E7%9B%AE%E5%89%8D%E6%9C%89-mentor-%E5%B8%B6%E7%9A%84%E5%B0%88%E6%A1%88)，協助新手開發者
    - 帶領衝刺開發 (Python 研討會中，類似黑客松，但專注於開源專案開發的活動)
        1. [EuroPython 2025](https://github.com/EuroPython/website/pull/1437)
        2. [DurianPy](https://www.meetup.com/durianpy/events/308390476/)
        3. PyCon APAC 2025
        4. [PyCon TW 2024](https://hackmd.io/LKLr7XyOR9mK1AEEnvnCuQ#Apache-Airflow)
- **相關技術演講**
    - **2025/10/08** 🇺🇸 [Airflow Summit 2025](https://airflowsummit.org/sessions/2025/seamless-migration-leveraging-ruff-for-a-smooth-transition-from-airflow-2-to-airflow-3/)  
        * 主題：Seamless Migration: Leveraging Ruff for a Smooth Transition from Airflow 2 to Airflow 3
    - **2025/09/06** 🇹🇼 [PyCon TW 2025](https://tw.pycon.org/2025/en-us/conference/talk/366)  
        * 主題：Unlocking the Future of Data Pipelines - Apache Airflow 3
    - **2025/07/18** 🇨🇿 [EuroPython 2025](https://ep2025.europython.eu/session/hold-on-you-have-a-data-team-in-pycon-taiwan)  
        * 主題：Hold on! You have a data team in PyCon Taiwan!  
        * [Slide](https://speakerdeck.com/leew/hold-on-you-have-a-data-team-in-pycon-taiwan)
    - **2025/03/28** 🇹🇼 [黃金流沙饅頭營](https://www.icloud.com/pages/0c6_qp3_RnuCJfcIh8_9xnqLA#2025_%E9%BB%83%E9%87%91%E6%B5%81%E6%B2%99%E9%A5%85%E9%A0%AD%E7%87%9F)  
        * 主題：Airflow 3.0 The First Glance  
        * [Slide](https://speakerdeck.com/leew/20250328-airflow-3-dot-0-the-first-glance)
    - **2025/03/02** 🇵🇭 [PyCon APAC 2025](https://pycon-apac.python.ph/)  
        * 主題：Unleash the Chaos: Developing a Linter for Un-Pythonic Code  
        * [Slide](https://speakerdeck.com/leew/unleash-the-chaos-developing-a-linter-for-un-pythonic-code-806b2bae-e161-4762-b0d5-d9fb8efdd24a) | [🎬recording](https://www.youtube.com/watch?v=tbSZx0UsWfQ)
    - **2024/09/28** 🇯🇵 [PyCon JP 2024](https://2024.pycon.jp/en/talk/AQKFHX)  
        * 主題：Unlocking Python's Core Magic  
        * [Slide](https://speakerdeck.com/leew/unlocking-pythons-core-magic) | [🎬Recording](https://www.youtube.com/watch?v=9jbHA6tE9MM)
    - **2024/09/21** 🇹🇼 [PyCon TW 2024](https://tw.pycon.org/2024/conference/talk/311)  
        * 主題：Unleash the Chaos: Developing a Linter for Un-Pythonic Code  
        * [Slide](https://speakerdeck.com/leew/unleash-the-chaos-developing-a-linter-for-un-pythonic-code) | [🎬Recording](https://www.youtube.com/watch?v=2jUd0o8VuE0)
    - **2024/09/11** 🇺🇸 [Airflow Summit 2024](https://airflowsummit.org/sessions/2024/what-if-running-airflow-tasks-without-the-workers/)  
        * 主題：What If...? Running Airflow Tasks without the workers  
        * [Slide](https://docs.google.com/presentation/d/1XGd7bQg6cGLNbHFiZjX__SmI4FLw6D_iASY9eRSO4mo/edit?usp=sharing) | [🎬Recording](https://www.youtube.com/watch?v=WkljjYtqu8Q)
    - **2024/05/08** 💻 Airflow Town Hall  
        * 主題：Starts Airflow task execution directly from the triggerer  
        * [Slide](https://speakerdeck.com/leew/starts-airflow-task-execution-directly-from-the-triggerer)
    - **2024/02/17** 💻 [源來適你](https://www.facebook.com/opensource4you)  
        * 主題：Intro to Airflow - From Zero to Hero  
        * [Slide](https://speakerdeck.com/leew/intro-to-airflow-from-zero-to-hero)
- **[相關技術文章](https://blog.wei-lee.me/tag/airflow.html)**

### Ruff (主要貢獻部分與 Airflow 遷移相關)
- **專案實際應用**
    - 雖非商業應用，但[廣泛應用於大開源專案和企業](https://github.com/astral-sh/ruff#whos-using-ruff)
    - [月下載量約 7,500 萬](https://pypistats.org/packages/ruff)
- **個人技術貢獻**
    - 專案[前 30 名貢獻者](https://github.com/astral-sh/ruff/graphs/contributors)
    - [發起 62 隻合併 PRs](https://github.com/astral-sh/ruff/pulls?q=sort%3Aupdated-desc+is%3Apr+author%3ALee-W+is%3Amerged+)
    - 完成 [Ruff AIR301-AIR302](https://docs.astral.sh/ruff/rules/#airflow-air) 大部分實作
- **相關技術演講**
    - **2025/10/08** 🇺🇸 [Airflow Summit 2025](https://airflowsummit.org/sessions/2025/seamless-migration-leveraging-ruff-for-a-smooth-transition-from-airflow-2-to-airflow-3/)  
        * 主題：Seamless Migration: Leveraging Ruff for a Smooth Transition from Airflow 2 to Airflow 3

### Commitizen-tools
- **實際應用**
    - 雖非商業應用，但被數家商業公司贊助維護。 [numberly](https://numberly.com/en/) 自 2023/06 贊助自今
    - [月下載量約 100 萬](https://pypistats.org/packages/commitizen)
- **核心身份與影響**
    - 專案維護者
- **技術與專案貢獻 (2022/07/01 起)**
    - 專案[第 1 名貢獻者](https://github.com/commitizen-tools/commitizen/graphs/contributors)
    - [發起 44 隻合併 PRs](https://github.com/commitizen-tools/commitizen/pulls?q=is%3Apr+is%3Amerged+merged%3A2022-07-01..2025-08-31+author%3ALee-W+)
    - [審閱近 500 PRs](https://github.com/commitizen-tools/commitizen/pulls?q=is%3Apr+reviewed-by%3ALee-W+is%3Amerged+merged%3A2022-07-01..2025-08-31+-author%3ALee-W)
    - [參與 150+ issue 討論](https://github.com/commitizen-tools/commitizen/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20is%3Aissue%20involves%3ALee-W%20created%3A2022-07-01..2025-08-31)
- **相關社群參與**
    - 擔任 [源來是你 commitizen Mentor](https://github.com/opensource4you/readme?tab=readme-ov-file#%E7%9B%AE%E5%89%8D%E6%9C%89-mentor-%E5%B8%B6%E7%9A%84%E5%B0%88%E6%A1%88)，協助新手開發者
    - 帶領衝刺開發
        1. [PyCon US 2024](https://us.pycon.org/2024/events/dev-sprints/#sprint-3)
        2. [COSCUP 2024](https://pretalx.coscup.org/coscup-2024/talk/SDR77M/)
        3. [scisprint Taipei 2024 March](https://sciwork.kktix.cc/events/scisprint-202403-taipei)
        4. [PyCon TW 2023](https://hackmd.io/R98LEB4MSxm4AeExmxuZnA#commitizen-tools)
        5. [Scisprint@Amazon Taipei 2023](https://sciwork.kktix.cc/events/scisprint-202302-taipei)
        6. [PyCon TW 2022](https://hackmd.io/UYumgLy_QxaCSCqrXKDBpw#commitizen-tools)
        7. [PyCon TW 2021](https://hackmd.io/PAgYsu5nSHyERIRaUokWxQ#commitizen-tools)
        8. PyCon TW 2020
        9. PyCon CA 2019
* **相關技術演講**
    - **2023/07/29** 🇹🇼 [COSCUP 2023](https://coscup.org/2023/zh-TW/session/TUGLJP)  
        * 主題：Atomic Commits: An Easy & Proven Way to Manage & Automate Release Process  
        * [Slide](https://speakerdeck.com/leew/atomic-commits-an-easy-and-proven-way-to-manage-and-automate-release-process) | [🎬Recording](https://www.youtube.com/watch?v=IxzN9ClXhs8)
* [相關技術文章](https://blog.wei-lee.me/tag/commitizen-tools.html)

## 社群與志工經驗
- **國際社群志工經驗**
    - Python Asia Org
        - EuroPython 2025 攤位志工
    - PyCon APAC
        - PyCon US 2024 攤位志工
    - PyCon CA 2019 主持人
- **國內社群志工經驗**
    - **PyCon Taiwan**
        - 2025：到處都看得到他們、審稿委員
        - 2024：志工、審稿委員
        - 2023：行銷組長
        - 2022：大會副主席
        - 2021：大會主席
        - 2020：議程組長
        - 2019：議程組員
    - **源來適你**
        - Apache Airflow Mentor
        - Commitizen Mentor
