Title: COPCUP 2019
Date: 2019-09-02 14:10
Category: Tech
Tags: Conference, COSCUP
Slug: coscup-2019
Authors: Lee-W
Summary: 

事隔了兩年又再次參加了 COSCUP
上一次好像是還在中研院的時候

現在會議都會有共筆，就不太需要再另外做筆記
所以大概就是聊聊這次去比較喜歡的幾場 talk

[COSCUP 2019 共筆](https://hackmd.io/@coscup/2019/https%3A%2F%2Fhackmd.io%2F%40coscup%2FHJAlwq67H)

<!--more-->

好像前幾年就開始有把每一個軌的主題分得很清楚
也有可能是我以前去的時候沒發現 XD
這次參加最多場的應該是 `開源與職涯` 這一軌
尤其想聽 `海外頭路：憂喜甘苦談`
我明明已經提早過去了，沒想到隊伍從前 10 分鐘就排得很長了......
是大家都想離開台灣了嗎 XD

聽到最有趣的是 talk 是 `如何在两年内从初学者成长为流行开源项目维护者和技术书作者？`
（[共筆](https://hackmd.io/1kfASFqeR1iCEq2Uqf9S_A)附上）
講者分享如何在兩年內成為了 flask 的維護者，還寫了一本技術書
~~最重要的訣竅就是**不要工作**~~
比起提供建議，我覺得這更像是是一個 call to action
用他的故事來告訴我們，要做到這些事並不見得那麼困難
有時候就是需要多一點衝動而已
不知道有沒有錄影，這場真的蠻值得再看一次的 XD

第一天最後是 Rust 核心成員 Steve Klabnik （[共筆](https://hackmd.io/3Euz7maGRLSATDR_X3P7lA)）帶來的 talk
原本還想說再講 Rust ，會不會聽不懂
不過後來講的內容跟開源專案的組織管理比較有關
其實還挺有趣的

第二天一早就被告台科大停電，臨時更換地點
不過還算是蠻順利的，除了換個場地，沒有網路了以外，倒是沒遇到什麼大問題
這天我大概都在會場亂晃，除了下面有筆記的兩場 talk 外，好像就都沒什麼印象了 XD

下面就放了一些我當天有做的筆記
有一些是從共筆補充過來
也有一些時覺得不知道怎麼整理上共筆，就留在這了

[TOC]

---

# Day 1

## Infra / DevOps 的養成之路與開源工具

* [共筆](https://hackmd.io/Yhf8ByscR2-oIifd9c2IBQ)
* [slide - 開源與職涯 - Infra 的養成之路與開源工具](https://docs.google.com/presentation/d/1wF1gA_Q-cZ33nXf1YhqGIWuLy_iMcC_1XllEHEkMgAc/edit#slide=id.i0)
* [slide - 系統工程師的大怪升級之旅](https://speakerdeck.com/chusiang/my-devops-tour-0-dot-1)
    * Ref:[奮鬥吧！系統工程師](https://zh.wikipedia.org/wiki/奮鬥吧！系統工程師)

### 開源與職涯 - Infra 的養成之路與開源工具

* CV 要夠詳細
    * 只有打 Linux 五個字沒有人看得懂 → 細說你會什麼
* 社群
    * 選擇你最舒服的方式參與
    * [開源社群 List](https://docs.google.com/presentation/d/1wF1gA_Q-cZ33nXf1YhqGIWuLy_iMcC_1XllEHEkMgAc/edit#slide=id.g487e56660f_0_14)

### 系統工程師的大怪升級之旅

* DevOps 三步工作法
    1. 由左自右的流動
    2. 從右自左的回饋
    3. 文化
* 推薦讀物
    * 自我成長: [學徒模式](https://www.tenlong.com.tw/products/9789862762561)
    * DevOps: [The Nature of Software Development](https://www.amazon.com/Nature-Software-Development-Simple-Valuable-ebook-dp-B00VDHRFWU/dp/B00VDHRFWU/ref=mt_kindle?_encoding=UTF8&me=&qid=)

### Q & A

* Q1: 撰寫 DevOps 部落格時如何避開機密、公司智財權等？
    * 自己複製出環境、資料等，自己把找到的技術在自己的環境複製一次，執行成功之後才記錄下來

## Learn to test and then test to learn

* Material
    * [slide](https://docs.google.com/presentation/d/185lhxQoS07G1g9Qw7ngT4Z2lQaB7p3HIPky5ERkIWFc/edit)
* Pitfalls of End-to-end Testing
    * High learning curve
    * Hard to build and maintain
    * Not easy to identify defects
    * Slow feedback
    * Not realistic enough
* Test to learn
    * 透過寫測試，紀錄學習歷程，下次回來看就知道怎麼用了
* Wrap Up
    * Unit Testing is the foundation and hard to learn
    * Mock and wrapper help you isolate your system boundaries
    * To make your code unit-testable, you'll learn to write better code.
    * Test to learn

## 海外頭路：憂喜甘苦談

* [共筆](https://hackmd.io/@coscup/rJkQ17l4H)

### 荷蘭
* Why Not The Netherlands
    * 荷蘭文難學
    * 食物難吃
    * 外食很貴
    * 房租很高
    * 稅很重 (up to 51.75%)
* Why The Netherlands
    * 英文可存活
    * 簽證好辦
    * 薪水
    * 多元文化
    * 氣候宜人 (冬天頂多 0 度)
    * 房貸比房租便宜
    * 30% Ruling （高技術外國人的稅務優惠）
* Bonus
    * 在歐洲正中間，方便旅遊
    * 大麻？（其實是非法，但政府明確表明不抓 xD）紅燈區？ 

* 荷蘭對 Work from Home 的政策算蠻鬆的

### 日本
* Mercari Backend Engineer
    * What is Mercari？
        * 主要做二手拍賣
    * 主要使用 Go Lang, php
    * How many leave do you have?
        * 10 days leave + 3 days summer leave + 10 days sick leave
    * Are you usually late for work?
        * 彈性工時 (12:00 ~ 16:00 一定要在公司)
    * How many foreigner in you project?
        * Engineer: 50% foreigners
    * Do you have lots of nomikai（應酬）?
        * 一季一次
        * 一次約 ￥4,000

### Q & A

#### Q: 日本階級制度很重？
是，但因為是外國人，所以可以裝作不知道
  
#### Q: 怎麼找到海外工作的？
LinkedIn, location 換到當地後，就會有收不完的邀約了

#### Q: 不會日文可以去日本工作嗎
* 只會講英文的話，建議去 Line, Rakuten, Mercari ，小公司至少要有 N2 比較順利

#### Q: 日本薪水大概是多少
* New Grade 年收 400 萬日幣， Senior 則要怎麼談

#### Q: 荷蘭 engineer 職缺多嗎？
* 很多，目前最大是 Uber ，另外有很多新創
* 因為英國脫歐，最近荷蘭職缺比較多

#### Q: 荷蘭的永久居留證？
* 荷蘭不能雙重國籍
    * 但因為不承認台灣是個國家，所以申請上會特別容易，不會被刁難

#### Q: 台灣人到歐洲最大的障礙是什麼
自己煮飯，其他都還好

#### Q: 會遇到歧視嗎？
* 日本 - Lilith Peng
    * 女性歧視有點大
    * 排外的社會 → 沒有解法，各憑本事
* 荷蘭 - 呂行
    * 除非到鄉下才會有歧視，但大城市還好

#### Q: 除了薪資以外，為什麼想出國
體驗不同文化、生活方式

#### Q: 為什麼 荷蘭/日本，而不是北美
* 荷蘭 - 呂行
    * 因為北美簽證不好拿，不習慣美國的生活方式
* 日本 - Lilith Peng
    * 日本有高度人才證
    * 會日文，英文不好 XD
    * 日本離台灣近
    * 稅率比歐洲好
    * 房租便宜

#### Q: 日本/荷蘭 的面試文化？
* 荷蘭
    * 會有白板題
    * 一關問架構
    * 一關問經歷
* 日文
    * 履歷表用 Excel 寫，會加分
    * 履歷是一致的格式
    * 面試分兩種
        * 外商派
        * 日本傳統派
            * 西裝外套、打領帶、皮鞋、公事包......
            * 90度鞠躬
            * 他們就是看感覺錄取 ← 他們認為人才是可以被培養的 XD

#### Q: 會不會有天花板
* 日本工程師大概 1,500 萬就是天花板，除非轉管理職
* 荷蘭不算特別明顯

----

# Day 2

## 源碼在哪裡
* grep 可以對二進位檔直接做文字搜尋
* Technical / Development History
    * Firsthand
        * **Mailing lists**, IRC, HipChat, Slack, Issue trackers, Forums, Journals / Papers
    * Summary
        * Wiki, Tech News, Tech Document, White Papers, Blogs, Books, Review papers
    * Mangement
        * Source Hosts
            * Github / Bitbucket and etc., SourceForge, Launchpad
        * Local Deployment
            * FHS, Language-specific path
        * Distributed Deployment
            * Auxiliary servies (e.g., Open Stack, web)
    * Version
        * `Major.Minor.Patch`

## Do you Select PostgreSQL or mysql
* [slide](https://speakerdeck.com/soudai/do-you-select-postgresql-or-mysql)
    
### Difference between MySQL and PostgreSQL
* Server architecture
    * MySQL → multi-thread
    * PostgresSQL → multi-process
* Licence
    * MySQL → GPL v2 or Commercial License
    * PostgresSQL → PostgresSQL License
* The Development Style
    * MySQL → Oracle
    * PostgresSQL → Community

### Advantage of MySQL
* Extensibility
* Good at fetching by **primary key** and **primary key** update
* Flexible replication
    * Multi source replication
    * Group Replication → Multi Master
* Document Store
    * JSON type → schema-less table

### Advantage of PostgreSQL
* Parallel Query
    * but not to increase number of workers beyond number of CPU core
* Materialized View
* Foreign Data Wrapper → an external table handle for your own table (other DBMS)
    * support WHERE, JOIN, GROUP BY, DELETE & UPDATE
    * Any data store is acceptable
* GIN INDEX & Function INDEX + JSON