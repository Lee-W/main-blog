Title: Apache Airflow 3.2.0 發佈！
Subtitle: 大家的 SQLite 資料庫升級守門員，這次失手了 😢
Date: 2026-04-15 12:00
Modified: 2026-04-15 17:30
Category: Tech
Tags: Airflow, Airflow 開發生情報
Slug: apache-airflow-3-2-0-release
Authors: Wei Lee

上次 [Apache Airflow 3.1.8 發佈！]({filename}/posts/tech/2026/11-apche-airflow-3-1-8-release.md) 的時候，我成功測試出 SQLite 升級的錯誤
但這次 3.2.0 的發佈就錯過了 🤦‍♂️

<!--more-->

👉 相關原文：
1. [📢 Apache Airflow 3.2.0beta2 is available for testing! 🎉](https://lists.apache.org/thread/309jtv28po8bsy2rq830w0hj402kbg8n)
2. [[VOTE] Release Airflow 3.2.0 from 3.2.0rc1 & Task SDK 1.2.0 from 1.2.0rc1](https://lists.apache.org/thread/znry5y1p4dn3noj3454pzllr3gf17qph)
3. [[VOTE] Release Airflow 3.2.0 from 3.2.0rc2 & Task SDK 1.2.0 from 1.2.0rc2](https://lists.apache.org/thread/z4l33ydpqzbcxbhno3gm8yf99fswhsrz)
4. [[RESULT] [VOTE] Release Airflow 3.2.0 from 3.2.0rc2 & Task SDK 1.2.0 from 1.2.0rc2](https://lists.apache.org/thread/rorz8rq9dn3myvngotnk2xs1mjngvw2m)
5. [[ANNOUNCE] Apache Airflow 3.2.0 Released](https://lists.apache.org/thread/wqz7v2n5n02lk6khw6nmr3src4467jqs)

## 本文
[Airflow 3.2.0（2026-04-07）](https://airflow.apache.org/docs/apache-airflow/stable/release_notes.html#id182) 是近期 Airflow 較大的一次發佈，上一個次版本（minor version）已經是 [2026-09-25](https://airflow.apache.org/docs/apache-airflow/stable/release_notes.html#airflow-3-1-0-2025-09-25) 的事了

Rahul 寫了 [Apache Airflow 3.2.0: Data-Aware Workflows at Scale](https://airflow.apache.org/blog/airflow-3.2.0/) 簡述此次新增的功能
其中資產分區（Asset Partition）是眾所期待的功能之一（有一部分是我做的！）
PyCon TW 2025 時遇到不少 Airflow 使用者對這個功能很感興趣
（至於我在大港開唱 2026 遇到去年演講的聽眾，就又是另一個故事了……）

總之，3.2.0 歷經了 beta1、beta2、rc1、rc2，終於成功發佈了 🎉

## 我怎麼想
Airflow 3.2.0 的發佈很值得開心，但大家的 SQLite 資料庫升級守門員這次失手了 😢
而且還是我用 [pycon-etl](https://github.com/pycontw/pycon-etl) 測試 rc2 到一半就發佈了 😱

> This email is calling for a vote on the release, which will last at least
> until *07th Apr* and until 3 binding +1 votes have been received.

確實是有三個決定性投票（binding vote），而且也到了 4/7
只是我沒預期是 4/7 的什麼時候……

我記得 rc1 的時候好像有測失敗過一次，但後來就又成功了...
而 rc2 就可以穩定重現失敗了

### 錯誤發生在哪？
這次的錯誤發生在資料庫遷移檔（migration file）[0097](https://github.com/apache/airflow/blob/4a499ad4241876850e4ad93d1db42e3d7b71a634/airflow-core/src/airflow/migrations/versions/0097_3_2_0_enforce_log_event_and_dag_is_stale_not_null.py#L41-L54)
乍看之下，我也沒發現問題在哪，所以問了大家的 AI 好朋友 CC

原因是在同一個資料表已經做了 `UPDATE`，此時已有活躍中的交易（active transaction）
因此 `PRAGMA foreign_keys=off` 會被忽略
遷移檔嘗試關閉外鍵 (FK) 檢查，但因為膠衣已經開始，SQLite 直接忽略這個操作
不過 CC 其實也試了好幾次才找到原因

修正這個錯誤的 PR [fix(migrations): move UPDATEs inside disable_sqlite_fkeys in migration 0097 #64876](https://github.com/apache/airflow/pull/64876) 已經被合併， 3.2.1 就不會有這個問題了

### 如何透過 breeze 重現錯誤並正確測試

以下流程會建立一個有資料的舊版 SQLite 資料庫，並在新版本中測試 升級是否正常

#### 1. 設定想測試的版本，並透過 breeze 啟動 airflow (breeze 外)

```sh
# outside breeze
OLD_VERSION=3.1.8
NEW_VERSION=v3-2-test

breeze start-airflow \
    --backend sqlite \
    --load-example-dags \
    --use-airflow-version "$OLD_VERSION"
```

#### 2. 在 DB 中新增需要的資料，並備份已有資料的 SQLite 資料庫 (breeze 內)

```sh
# inside breeze
airflow dags trigger example_params_trigger_ui
sqlite3 /root/airflow/sqlite/airflow.db "PRAGMA wal_checkpoint(TRUNCATE);"
cp /root/airflow/sqlite/airflow.db /files/seed.db

# Verify at least one Dag run exists in the DB
row_count=$(sqlite3 /files/seed.db "SELECT COUNT(*) FROM dag_run;")
[ "$row_count" -gt 1 ] || { echo "FAIL: expected >1 dag_run rows, got $row_count"; exit 1; }
```

上面透過 airflow cli 跑了範例 Dag `example_params_trigger_ui`
也可以隨便在 Airflow 的 UI 上跑幾個範例 Dag
主要是在 Dag 執行（Dag run）與任務實例（task instance）資料表中要有資料列
其他有透過外鍵（FK）參照 Dag 資料表的資料表也可以

接著將有資料的 SQLite 資料庫備份到 `/files/see.db`
回到 breeze 外， airflow 資料夾下的 `files/` 就會看到這個檔案

下面的指令是驗證，至少要用一個 Dag 執行的資料列存在

#### 3. 切換到遷移檔修正完的版本，並開啟 breeze shell (breeze 外)

```sh
# outside breeze
git checkout "$NEW_VERSION"

breeze shell \
    --backend sqlite \
    --mount-sources selected \
```

#### 5. 使用剛備份的 SQLite 資料庫測試升級、降級、再升級

在 `breeze` 的 shell 中執行：

```sh
# inside breeze
cp /files/seed.db /root/airflow/sqlite/airflow.db

row_count=$(sqlite3 /root/airflow/sqlite/airflow.db "SELECT COUNT(*) FROM dag_run;")
[ "$row_count" -gt 1 ] || { echo "FAIL: expected >1 dag_run rows, got $row_count"; exit 1; }

airflow db migrate
airflow db downgrade --to-revision 937cbd173ca1 -y
airflow db migrate
```

如果中間報錯，至少是升降版都沒有問題
理想上應該要連資料是否會被影響到都去做測試
但這件事要放在整個流程自動化以後了
我本地端有個分支在做這件事，最近應該可以把 PR 發出來
