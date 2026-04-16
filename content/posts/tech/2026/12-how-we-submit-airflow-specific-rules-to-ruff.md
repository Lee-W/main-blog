Title: 如何把 Airflow 規則貢獻進 Ruff？
Date: 2026-03-17 17:05 +0800
Modified: 2026-03-17 21:40 +0800
Category: Tech
Tags: Airflow, Airflow 開發生情報
Slug: how-we-submit-airflow-specific-rules-to-ruff
Authors: Wei Lee
Lang: zh-tw

現在最新的規則長這樣 👉 [Proposing Airflow Best Practices and Ruff AIR Rules](https://github.com/apache/airflow/blob/10ccbd0295f48431cd40c7949ed9c3f1deb22396/contributing-docs/24_proposing_best_practices_and_air_rules.rst#L18)

總之，想貢獻 Ruff AIR 規則，先在 [Airflow 開發者討論群](https://lists.apache.org/list.html?dev@airflow.apache.org)（airflow dev mailing list）發起討論

<!--more-->

👉 相關原文:
1. [[Discuss] How we submit Airflow-Specific Rules to Ruff](https://lists.apache.org/thread/wfqvzk58p352460ydfhlohjb8fddqb9h)
2. [[LAZY CONSENSUS] How we submit Airflow-Specific Rules to Ruff](https://lists.apache.org/thread/156gm0op0bn5frfp12npx1tbd3v508l8)

## 本文

在 Airflow 從 2 升到 3 的期間，我們在 Ruff 加入了不少跟升版相關的 [AIR](https://docs.astral.sh/ruff/rules/) 規則
也因此讓 [Explore and add static checks for DAGs for early detection of common issues #43176] 重新搬上檯面一陣子
（順帶一提 `DAG` 已經是歷史詞彙，請使用 `Dag`，我現在是 `Dag` 警察 👮）

最近 Illya 送了以下 4 支 PRs 到 Ruff

- <https://github.com/astral-sh/ruff/pull/23584>
- <https://github.com/astral-sh/ruff/pull/23631>
- <https://github.com/astral-sh/ruff/pull/23579>
- <https://github.com/astral-sh/ruff/pull/23583>

其中一支做的事已經列在 Airflow 的最佳實踐文件中
另外一支是 3.1.x 中 Airflow 核心就能偵測的問題
最後兩支則是新的最佳實踐建議
~~雖然我也很想便宜行事，想送就送啦，但身為 PMC 成員不能這樣~~
雖然這些在 [Explore and add static checks for DAGs for early detection of common issues #43176] 都討論過，但能有更廣泛的討論還是比較好

所以我提出的做法是：

1. 在 [Airflow 開發者討論群] 發起討論或默認共識（Lazy Consensus）
2. 通過後對 Airflow 開一支文件追加的 PR，同時開始準備對 Ruff 發起追加 AIR 規則的 PR
3. 如果 Ruff 的 AIR 規則 PR 被合併，再發一支 PR 到 Airflow 文件將規則連結補充上去

Illya 在後續扮演了惡魔，預想了各種壞壞狀況（其實我覺得蠻有趣的）
如果有人沒有遵從這個指南行事，那會怎樣嗎？
Airflow 社群就沒人看他 PR？
我原本以為我們對 Ruff 沒有控制權（雖然有一定合作默契），所以也不能怎樣
但 Jarek 補充了許多法律相關的討論
其實關於 Ruff 的 AIR 規則，Airflow 的 PMC 是有一定的控制權的
因為商標屬於 ASF

## 我怎麼想
恩...這原本就是我提的討論
倒是提醒我現在要幫 Illya 開 2 個討論來確認那些是否為 Airflow 社群想要的最佳實踐

更新： 在我發完這篇文沒多久 Illya 就發了這 2 個討論
1. [[VOTE] New DAG Authorship Best Practice: Use `.output` Instead of `xcom_pull` Template Strings](https://lists.apache.org/thread/1oh64pgco8bcbsxyyyflm7ccg1x3frol)
2. [[VOTE] New DAG Authorship Best Practice: Prefer `@task.short_circuit` over trivial `@task.branch`](https://lists.apache.org/thread/odmymy6kn5rqx17x44ydq43c1vfqh511)

[Airflow 開發者討論群]: https://lists.apache.org/list.html?<dev@airflow.apache.org>
[Explore and add static checks for DAGs for early detection of common issues #43176]: https://github.com/apache/airflow/issues/43176
