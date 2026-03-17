Title: Apache Airflow 3.1.8 發佈！
Subtitle: pycon-etl 再次拯救 SQLite 使用者
Date: 2026-03-17 16:25 +0800
Category: Tech
Tags: Airflow, Airflow 開發生情報
Slug: apache-airflow-3-1-8-release
Authors: Wei Lee

Apache Airflow 3.1.8 於上週發佈
[pycon-etl](https://github.com/pycontw/pycon-etl)又又又又又再一次成為了 SQLite 使用者的救星
找到 SQLite 才會遇到的問題

<!--more-->

👉 相關原文:
1. [[VOTE] Release Airflow 3.1.8 from 3.1.8rc1 & Task SDK 1.1.8 from 1.1.8rc1](https://lists.apache.org/thread/8h0hj9dm3jlobytwnnjs51mfn7wprrkv)
2. [[ACCELERATED VOTE] Release Airflow 3.1.8 from 3.1.8rc2 & Task SDK 1.1.8 from 1.1.8rc2](https://lists.apache.org/thread/c2ff8yhyqps5hxrtnm7bq5gy58rs1fzg)
3. [[RESULT][ACCELERATED VOTE] Release Airflow 3.1.8 from 3.1.8rc2 & Task SDK 1.1.8 from 1.1.8rc2](https://lists.apache.org/thread/k2pmyynlzz7jznw8fxkcqqb3mcnqo4mh)
4. [[ANNOUNCE] Apache Airflow 3.1.8 Released](https://lists.apache.org/thread/wnqv4mfzv32zbjvzpcvsm7sfc1g1lz66)

## 本文
rc1 遇到了 SQLite 資料庫遷移 (migration) 的問題，而且這是個回歸錯誤（regression error）
我在投下 -1 票的同時，也發了 PR [fix(migration): disable disable_sqlite_fkeys for migration 0087#63256](https://github.com/apache/airflow/pull/63256) 修正問題
在 rc2 開測試前，我就先上一個修補（patch）到 [pycon-etl] 測試過了
rc2 順利測試通過，並且成功發佈

## 我怎麼想
自從 3.1.0 那幾個版本，我忘了提前測試 [pycon-etl]
導致我必須要上一堆修補才能讓 [pycon-etl] 升到 3.1.x
只要精力允許，我都會盡可能在第一時間測試 [pycon-etl] 在最新版的資料庫搬遷
理論上如果 Airflow 只是發佈修補版本（patch version），是不太會動到資料庫
但這次就是剛好動到了...我還特別忙...差點就要沒測試到
還好我壓線最後一刻測試了
順便複習一下 PMC 成員要怎麼驗證發行候選版 (release candidate) → [Verify the release candidate by PMC members](https://github.com/apache/airflow/blob/main/dev/README_RELEASE_AIRFLOW.md#verify-the-release-candidate-by-pmc-members)

[pycon-etl]: https://github.com/pycontw/pycon-etl
