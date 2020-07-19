Title: Python Table Manners - 安全性檢查
Date: 2020-03-22 13:10
Modified: 2020-07-19 17:23
Category: Tech
Tags: Python, Security
Slug: python-table-manners-security
Authors: Lee-W
Series: Python Table Manners

果然在沒有寫作松的督促下，馬上就拖稿了 XD
接下來要介紹在 Python 專案中做安全性檢查的工具

<!--more-->

[TOC]

## Safety - 檢查相依套件

![depbot](/images/posts-image/2020-02-22-python-table-manner-series/depbot.jpg)

不知道大家有沒有在 GitHub 上看過這樣的畫面
這個訊息告訴我們，專案的相依套件中可能有安全漏洞

透過 [Safety](https://github.com/pyupio/safety)，就能像這樣在本地做相依套件安全漏洞的檢查
它會到 [safety-db](https://github.com/pyupio/safety-db) 去查找已知的安全性漏洞
這個資料庫則是從 [CVE](https://cve.mitre.org/) (Common Vulnerabilities and Exposures) 整理出來的
如果是免費版，一個月會更新一次資料庫
付費版則可以達到即時更新

### 安裝

```sh
pipenv install safety --dev
```

### 執行

```sh
pipenv run safety check
```

![safety-not-found](/images/posts-image/2020-02-22-python-table-manner-series/safety-not-found.jpg)

在 [pycontw-postevent-report-generator commit 128d](https://github.com/pycontw/pycontw-postevent-report-generator/commit/128d271942099b94faca3693d6c146c879e3b414) ，透過 safety 不會找到任何安全漏洞

如果想要測試 safety 的功能可以安裝套件 [insecure-package](https://pypi.org/project/insecure-package/) (**這個套件是真的存在的，而且是不安全的，僅作為測試用途**)

```sh
pipenv install insecure-package --dev
```

再試一次就能看到 safety 將 insecure-package 列為不安全的套件

![safety-found-insecure](/images/posts-image/2020-02-22-python-table-manner-series/safety-found-insecure.jpg)

另外需要注意的是 `safety check` 是對當前環境做檢查
務必確定已經有進入專案的虛擬環境，不然 safety 只會檢查到本機使用的套件有沒有漏洞

如果想要對 `requriements.txt` 做檢查，則可以加上參數 `-r`

```sh
# 因為這個 case 不是針對 pipenv ，所以前面沒有加上 pipenv run
safety check -r requirements.txt
```

雖然 safety 並不支援對 Pipfile 進行檢查 (Ref: [Add Pipfile support #47](https://github.com/pyupio/safety/issues/47))

但 pipenv 就內建有安全性檢查的指令

```sh
pipenv check
```

雖然 safety 跟 pipenv 都是去查找 [CVE](https://cve.mitre.org/)，但有時候結果會有些不同

以下是 `pipenv check` 針對 [pycontw-postevent-report-generator 1.1.0](https://github.com/pycontw/pycontw-postevent-report-generator/tree/1.1.0) 的執行結果
![pipenv-check-pillow](/images/posts-image/2020-02-22-python-table-manner-series/pipenv-check-pillow.jpg)

## bandit - 程式碼靜態分析
確認完相依套件的安全性後，接著可以透過 [bandit](https://github.com/PyCQA/bandit) 來對自己的程式碼做靜態分析找出常見的漏洞

### 安裝

```sh
pipenv install bandit --dev
```

### 使用

```sh
pipenv run bandit -r <package>
```

![bandit-result](/images/posts-image/2020-02-22-python-table-manner-series/bandit-result.jpg)

執行後就會看到一個列表，整理出專案中可能有的安全性漏洞
每一個項目中會有以下五個欄位

* Issue: 問題
* Severity: 嚴重性
* Confidence: 可信度
* Location: 位置（在程式碼的哪一行）
* More Info: 詳細的原因和可能的解決方案 （也可以從 [Complete Test Plugin Listing](https://bandit.readthedocs.io/en/latest/plugins/#complete-test-plugin-listing) 找到全部的列表）


加上參數 `-i` (可信度) 和 `-l` （嚴重性），就可以讓 bandit 只回報特定程度的漏洞
越多的 i / l 代表程度越高
以下指令就是讓 bandit 只回報高嚴重性 (`-lll`)、高可信度 (`-iii`)的漏洞

```sh
pipenv run bandit -iii -lll -r <package>
```

### 局部跳過檢查
有時候 bandit 給的警告不會在所有狀況都適用
以 [B101: assert_used](https://bandit.readthedocs.io/en/latest/plugins/b101_assert_used.html#module-bandit.plugins.asserts) 為例
警告不該使用 `assert`
在使用 `python -o` 指令產生優化過的 byte code 時，會跳過 `assert`
如果系統使用 `assert` 來進行登入的檢查，就會讓使用者在完全沒驗證的情況下成功登入
但大部分的時候，我們不太會這麼實作
而 `assert` 也是在測試中很常使用到的語法

這時候就可以在專案的最上層加入設定檔 `.bandit`
而它的格式會長這樣

```text
[bandit]
# 要執行 bandit 檢查的檔案或資料夾（逗號分隔）
targets:
# 跳過 bandit 檢查的檔案或資料夾（逗號分隔）
exclude:
# 要跳過的檢查種類 （逗號分隔）
skips:
# 要執行的檢查種類 （逗號分隔）
tests:
```

執行 bandit 時要加上 `--ini .bandit` 讓 bandit 知道要找這份設定檔

```sh
bandit --ini .bandit
```

如果不是整個檔案或種類要跳過，則可以在程式碼後面加上 `# nosec`

## Reference
* [Python Security Tool - PyCon US 2019](https://lee-w.github.io/pycon-note/posts/pycon-us-2019/2019/10/python-security-tool/)
* [Watch out for Safety Bandits! - PyCon AU 2018](https://lee-w.github.io/pycon-note/posts/pycon-au-2018/2019/08/watch-out-for-safety-bandits/)
* [用 Bandit 靜態掃描工具，掃描 Python 專案中的安全性問題](https://myapollo.com.tw/zh-tw/secure-your-python-code-with-bandit/)
