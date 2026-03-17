Title: 要不要用 uv.lock 取代 airflow 開發環境用的 constraints 檔
Date: 2025-08-21 10:05 +0800
Category: Tech
Tags: Airflow, Airflow 開發生情報
Slug: replace-constraints-with-uv-lock-mechanisms-for-dev-env-freeze
Authors: Wei Lee

我以為有了 [PEP 751] 一切的 lock 問題就會解決 😢
但它好像只是讓 `requirements.txt` 更好了很多
細節還是交給個工具去解決

<!--more-->

👉 原文： [[DISCUSS] Replace constraints with uv.lock mechanisms for dev env freeze](https://lists.apache.org/thread/mhq987wq78cmkgjf2ql55rkmkmdd1h5t)

## 本文

**TL;DR: 要不要改用 uv.lock 鎖定開發環境的相依套件**

### 現行 constraints file 用來幹嘛？
1. 記錄最新不會壞掉的相依套件版本
2. 讓 PRs 不會因為相依套件更新壞掉
3. 讓使用者安裝已釋出的 Airflow 不會因為其他套件版本壞掉

### 改用 uv.lock 後？
1. constraints 還是可以透過 `uv.lock` 產生
2. 金絲雀版本 (main 分支上) 中還是可以用 `--resolution-highest` 去看最新版本的相依套件會不會把 Airflow 炸掉
3. 呈 2， PRs 會用 `uv.lock` 而不是最新版本，所以 CI 因為相依套件壞掉的機會降低

### 改用的問題
**誰在什麼時候要去更新 `uv.lock` 並且提交到 repo 中**

* 可能的解法
    * 加個 `upgrade-important-versions` prek hook，在 main 分支的 CI 跑

### 改用的好處
* breeze 建立映像檔比較方便
* 同步本地端環境更方便
* 相依套件比較不會讓 PR 的 CI 炸掉

### 改用的壞處
* 要有人時不時去看 `upgrade-important-versions` hook
* 有的 PR 會有很大的 `uv.lock` 改動

## 我怎麼想
原本想說 [PEP 751] 的 `pylock.toml` 會不會比較好
感覺比較「官方」一點
但 uv 對 [pylock.toml](https://docs.astral.sh/uv/concepts/projects/layout/#pylocktoml) 的支援還是比較像是以前的 `requirements.txt`
而沒有辦法取代 `uv.lock`
那在流程簡化上好像就沒什麼幫助

[PEP 751]: https://peps.python.org/pep-0751
