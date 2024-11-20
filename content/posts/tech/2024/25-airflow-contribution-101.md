Title: 貢獻 Airflow 101
Subtitle: 姑且算是個 mentor(?)...吧？
Date: 2024-11-19 22:45
Category: Tech
Tags: Python, Airflow, 源來適你
Slug: airflow-contribution-101
Authors: Wei Lee

至少在[源來適你的名單]上是有我的名字
雖然 `#airflow-技術討論` 這個頻道偏死寂
但我就是佛系投入、佛系經營

<!--more-->

## 先進入正題，再來聊天

想一起開發 Airflow 的第一步就是把 [breeze] 跑起來
breeze 是 Airflow 專屬的開發工具
用來協助設定本地開發環境跟 CI 環境的設置
文件積極的被維護，應該還算完整
整份文件跟著走完，會對 Airflow 的環境設定有基本的概念
中間有遇到什麼問題或覺得哪裡寫得不清楚的話
可以透過 [Community] 加入 Airflow 的 slack，到 `#airflow-breeze` 或 `#new-contributor` 頻道發問
當然直接開 issue 或 pull request 也沒問題
說不定修正這個問題就是你的第一個貢獻 😉

環境設定好之後，可以先找有 [good first issue] label 的 issues 解解看
除此之外，也可以找有 [area:providers] label 的 issues
因為不會直接碰到 Airflow 的核心，所以有機會比較簡單
從這裡開始了解 Airflow ，也會慢慢了接觸到核心
issue 解完就開 pull requests
開發的流程大致就是如此

### 除了開發以外
#### 1. 幫忙 review [pull requests] (PR)

很多人以為要是 committer 或是 maintainer 才能 review PRs，但其實所有人都可以
即便還不懂 Airflow 的運作，也可以單就 Python 的開發給建議
review 的過程也會更加熟悉 Airflow

#### 2. 幫忙看有 [needs-triage] label 的 issues

這些 issues 通常是還需要驗證或討論的
最簡單可以做的就是幫忙驗證使用者回報的 issue 是不是能重現的，提供的資訊是否足夠
當 committers 看到時，就能很快地進行分類

如果做得夠多，之後就有機會被加入 triage team 成為 [collaborators]
有興趣成為 Airflow 的 committer 的話，這會是很好的第一步
成為 collaborator 後，就會有權限更改 issue 的 label
可以幫忙尚未分類的 issue 做正確的分類

#### 3. 加入 Airflow 的 Slack 討論或回答問題

[Community] 👈 由此加入

以下是幾個我常用的頻道

* `#new-contributors`
    * 新貢獻者發問的地方
* `#airflow-breeze`
    * 跟 breeze 有關的任何問題都可以來這問
* `#user-troubleshooting`
    * 使用者遇到問題會來這邊發問
* `#contributors`
    * 貢獻者們的討論頻道
* `#blogposts`
    * 如果寫了 Airflow 相關的文章，可以來這裡分享
* `#airflow-3-dev`
    * 最近在進行 airflow-3 的開發
* `#users-taiwan`
    * 雖然最近有點死寂，但還是想說一下，這裡是有台灣使用者的頻道啦 🥲
* `#townhall`:
    * 每月一次的線上聚會
    * 自從日光不節約後，變成台灣時間 00:00 開會
    * 真的太太太太太晚了，老了沒辦法熬夜，不參加，抱歉
* `#random`
    * 什麼有的沒的都有可能丟到這
* `#airflow-astronomer`
    * 算是同場加映，畢竟之前有加入開發 [ask-astro]
    * 裡面有個 Ask Astro 的機器人是專門回答 airflow 跟 [Astronomer] 相關問題

其他的頻道如果你需要用到，大概也已經是你在社群夠久的時候了我想？ 🤔

#### 4. 加入 Airflow dev list 的討論

[Community] 👈 由此加入

裡面的話題通常適合至少開發 Airflow 一小段時間的人加入
不過先加入看看大家都在聊什麼也蠻好的
之後會比較容易加入討論

#### 5. 幫忙測試 Release candidates

Airflow 的 Release 都會開 GitHub issue 來紀錄，會以 "Status of testing" 開頭
同時在 Dev list 發起投票，讓大家驗證功能，並決定是否 release
像 [Status of testing Providers that were prepared on November 14, 2024 #44041] 就是上一波的 provider 的 release candidates 測試
如果恰好有貢獻到這次要 release 的內容，就會直接在 issue 中被 tag
這時候可以去 PyPI (e.g., `apache-airflow==2.10.3rc1`) 上安裝 release candidate 測試
並且回去 GitHub issues 和 Dev list 回報測試結果

## 源來適你
[源來適你 / opensource4you]是我大學修分散式系統的助教帥哥嘉平創的社群
~~因為裡面很多人在戰 Airflow，我就加進去潛水了~~
另外，我研究所學長，傳說中三個月成為 committer
人稱開源渣男的辣個男人
最近正積極貢獻 Kafka ，好像已經連續贏得兩週的開源積分戰了
太強，完全看不到車尾燈的強悍

之前不知道哪根筋不對，說了 Airflow 也可以佛系來帶一下
所以就多出 `#airflow-技術討論` 的頻道
不過這佛系是真佛系，佛系帶專案的三大原則就是

1. 不要找我開會
2. 絕對不要找我開會
3. **再說一次，絕對不要找我開會**

Kafka 還能每週開周會，真的是有夠拼的
我無法
真的無法
真的是不要開會
但有問題丟上來頻道，我都很樂意在我心力足夠的情況下跟大家討論
避免 direct message 我，因爲大家可能有同樣的問題
一直回同樣的問題，會煩

最近姑且是佛系經營下，渡到有緣人
上個月還被提名 PR of the month，雖然沒入選
之前還有另一個朋有也有被提名
雖然也是沒入選，但有被找去 Airflow 每月的 Townhall 分享
為了支持有小小晚睡一下去聽他講
不然當初他的 PR 好像吃是我 review 的好像不需要再聽一次 😆
整體來說這件事是還蠻令人開心的

這篇文章之後就會直接放在源來適你的 `#airflow-技術討論`
讓大家知道可以怎麼開始貢獻 Airflow 跟可以預期從我這得到什麼幫助
（恩，對，可能太多幫助）

[源來適你的名單]: https://github.com/opensource4you/readme/blob/24bc45fb88e6ebc38deb5e20533f3eef2752ba96/README.md?plain=1#L51-L55
[breeze]: https://github.com/apache/airflow/tree/main/dev/breeze/doc
[Community]: https://airflow.apache.org/community/
[good first issue]: https://github.com/apache/airflow/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22
[area:providers]: https://github.com/apache/airflow/issues?q=is%3Aopen+is%3Aissue+label%3Aarea%3Aproviders+
[pull requests]: https://github.com/apache/airflow/pulls
[needs-triage]: https://github.com/apache/airflow/issues?q=is%3Aissue+is%3Aopen+label%3Aneeds-triage
[collaborators]: https://github.com/apache/airflow/blob/24811f729f0e20dfff1be9afa8bf4a60b44fe628/.asf.yaml#L121
[ask-astro]: https://github.com/astronomer/ask-astro
[Astronomer]: https://www.astronomer.io/
[Status of testing Providers that were prepared on November 14, 2024 #44041]: https://github.com/apache/airflow/issues/44041
[源來適你 / opensource4you]: https://www.facebook.com/opensource4you
