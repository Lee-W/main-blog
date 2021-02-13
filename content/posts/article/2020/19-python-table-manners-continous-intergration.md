Title: Python Table Manners - 持續整合/部署
Date: 2020-12-31 17:53
Category: Tech
Tags: Python, CI/CD
Slug: python-table-manner-continuous-integration
Authors: Lee-W
Series: Python Table Manners

這篇好像真的拖得很久...
原本預定的發表時間還是 2020-03-04 呢 ......
總之，剛好年假就趁機補一下

<!--more-->

在使用 [GitHub Actions](https://github.com/actions) 前，這篇原本要寫 [drone](https://github.com/drone/drone) 的使用方式
不過既然是放在 GitHub 上的開源專案，好像沒理由不用 GitHub Actions
（但其實只是我當時想玩玩沒碰過的新東西）

同樣會延續之前舉例的專案 [pycontw-postevent-report-generator](https://github.com/pycontw/pycontw-postevent-report-generator) (以下會簡稱 rg-cli）來講為什麼要用、如何使用 GitHub Actions

[TOC]

## 想解決的問題
先從這樣的工具能解決什麼問題開始聊起

假設你是某開源專案的維護者，設定好專案程式碼風格檢查跟自動化測試
有個貢獻者提交了一個 pull request 給你審核
審核完準備要 merge 的時候，才發現他的 pull request 測試跑不過
這可能就會浪費你前面大部分審核的時間

如果能在貢獻者 push 完，自動就做檢查
確認已經通過基本的檢查，才讓人工介入（維護者審核）
那就能省下你很多時間

![pass](/images/posts-image/2020-02-22-python-table-manner-series/pass.jpg)

當這個 pull request 通過所有測試和人工審核，merge 回 master 分支之後
接下來就要讓服務上線或是發佈套件，而這些步驟通常都很重複性且繁瑣
如果自動化這些步驟就能省下人工成本，並減少人為失誤

## 如何套用到 rg-cli ?
簡單先將想做的事分為三個步驟
前一步通過才可以執行下一步

1. 當貢獻者提交 pull request 後，自動執行風格檢查、跑測試
2. 當 pull request 被維護者 merge 回 master 分支之後，根據 git commit 更新版本號並產生 git tag ，最後再將 git tag 推回 master 分支  
  （如果不太知道這段在做什麼，可以參考 [Commitizen: 規格化 commit message]({filename}/posts/article/2020/11-python-table-manners-commitizen.md))
3. 當 master 分支偵測到新的版本號（git tag）產生後，自動將新的套件上傳到 [PyPI](https://pypi.org/project/pycontw-report-generator/)

## GitHub Actions 實例
接下來看 [pycontw-postevent-report-generator/.github/workflows/ @ 3ff174](https://github.com/pycontw/pycontw-postevent-report-generator/tree/3ff174384639c8d6f40c4cd16e59ceba950838e9/.github/workflows) 中的三個檔案，分別對應到前面所提的三個步驟

1. [python-check.yaml](https://github.com/pycontw/pycontw-postevent-report-generator/blob/3ff174384639c8d6f40c4cd16e59ceba950838e9/.github/workflows/python-check.yaml)
2. [merge-into-master.yaml](https://github.com/pycontw/pycontw-postevent-report-generator/blob/3ff174384639c8d6f40c4cd16e59ceba950838e9/.github/workflows/merge-into-master.yaml)
3. [python-publish.yaml](https://github.com/pycontw/pycontw-postevent-report-generator/blob/3ff174384639c8d6f40c4cd16e59ceba950838e9/.github/workflows/python-publish.yaml)

### Python Check
每個 GitHub Actions 的 workflow 都需要有一個名稱

```yml
name: python check
```

這會顯示在 **Actions** > **Workflows** 中

![workflow](/images/posts-image/2020-02-22-python-table-manner-series/workflow.jpg)

接著要指定哪些事件發生時要執行這個 workflow
(See more 👉 [Events that trigger workflows](https://docs.github.com/en/free-pro-team@latest/actions/reference/events-that-trigger-workflows))

```yaml
on: [push, pull_request]
```

再來則是要在哪執行、執行什麼

* `jobs`： workflow 要執行的 job ，可以有超過一個 job。每個 job 都必須給它一個 job id (e.g., check)
    * `run-on`： 要跑在哪種機器上 （More option 👉[jobs.<job_id>.runs-on](https://docs.github.com/en/free-pro-team@latest/actions/reference/workflow-syntax-for-github-actions#jobsjob_idruns-on)）
    * `steps`:  要執行的 step
        * `name`: step 的名稱
        * `use`: step 要使用哪個 action，可以用在 [GitHub Marketplace · Actions](https://github.com/marketplace?type=actions) 找看看有沒有別人已經寫好的 action 不用重造輪子
        * `with`: 輸入 actions 的參數
        * `run`: 要執行的指令（`|` 是 yaml 的斷行）

```yaml
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - name: Check out
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v1
        with:
          python-version: "3.7"

      - name: Install dependencies
        run: |
          python -m pip install pipenv invoke
          inv env.init-dev -w
......
```

當這個 workflow 被執行的時候，可以在 GitHub Actions 看到細節

![step](/images/posts-image/2020-02-22-python-table-manner-series/job.jpg)

### Merge into master
上個 workflow 只要偵測到任何 push 或 pull request 就會執行
而這個 workflow 則是在 master 分支有改動時執行
這時就可以在 `on` 的後面針對特定的事件做判斷

```yaml
on:
  push:
    branches:
      - master  # another branch could be specified here
```

除了 workflow 能偵測事件以外，也能依造不同的事件內容執行不同的 job
下面的狀況是只有「開頭不是 "bump:" 的 commit」 才執行 `bump-version`

```yaml
jobs:
  bump-version:
    if: "!startsWith(github.event.head_commit.message, 'bump:')"
    runs-on: ubuntu-latest
```

因為 commitizen 自動跳版本號的時候，會 push 一個 commit 回 master 分支
所以要給 GitHub Actions 適當的權限
那就需要設定密碼或 token 來做到
因為它們不適合被公開，所以要設定在 secret 裡面
設定 secret 的頁面可以從 **Settings** > **Secrets** > **New repository secret** (右上角) 找到

![secret](/images/posts-image/2020-02-22-python-table-manner-series/secret.jpg)

在 job 取出 secret 的方式則是如下使用 `${{ secrets.secret_id }}` 這樣的語法

```yaml
      - name: Check out
        uses: actions/checkout@v2
        with:
          fetch-depth: 0
          token: '${{ secrets.PERSONAL_ACCESS_TOKEN }}'
```

### Python Publish
跟 GitHub Actions 比較相關的內容，在上面兩個 workflow 都寫得差不多的
那這裡就來聊聊跟 PyPI 相關的

從去年七月起，PyPI 就有支援使用 API token 上傳
（See more 👉 [PyPI now supports uploading via API token](https://pyfound.blogspot.com/2019/07/pypi-now-supports-uploading-via-api.html)）
所以建議使用 API token 而不是個人的 PyPI 帳號密碼
產生 PyPI token 的方式可以在上面的文章找到，我就不贅述
使用的方式則是把原本帳號的欄位改成 `__token__` （就是這個字串，不用代換成任何東西)
密碼改成 PyPI 給你的 token

在串 GitHub Actions 時，我踩到一個很有趣（？）的雷
假設你的取得的 token 是 `pypi-thisisrandomestringrepresentingyourapitoken`
在 workflow 中用 `password: ${{ secrets.pypi_password }}` 取得 secret
那在 secret 就要設定 `"pypi-thisisrandomestringrepresentingyourapitoken"`
而不是 `pypi-thisisrandomestringrepresentingyourapitoken`
不過也許將 workflow 的內容改成 `password: "${{ secrets.pypi_password }}"` 也能解決
總之，要記得加 `""`

## Reference
* [GitHub Actions](https://docs.github.com/en/free-pro-team@latest/actions)
* [Python in GitHub Actions](https://hynek.me/articles/python-github-actions/)
