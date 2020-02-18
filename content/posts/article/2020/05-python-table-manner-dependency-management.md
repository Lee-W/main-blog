Title: Python Table Manner - 虛擬環境和套件管理
Date: 2020-02-23 00:00
Category: Tech
Tags: Python, Dependency
Slug: python-table-manner-dependency-mangement
Authors: Lee-W
Status: draft
Series: Python Table Manner

為了避免不同 Python 專案使用的套件版本不同
開始一個 Python 專案時，第一步就是要先建立虛擬環境
理想上，本機的環境是不用安裝套件的
因為每一個專案都會在虛擬環境內執行，並且在裡面安裝各自的套件

<!--more-->

如果要在本機安裝 Python 的工具的話，我建議使用 [pipx](https://pipxproject.github.io/pipx/)

```sh
python -m pip install --user pipx
python -m pipx ensurepath
pipx install [PACKAGE]
```

[TOC]

## virutalenv
創建虛擬環境，最基本就是使用 [virtualenv](https://virtualenv.pypa.io/en/latest/)
透過以下幾個指令建立一個，並把相關的套件寫入 `requirements.txt`

```sh
# 創建 Python 虛擬環境
python -m venv ./venv

# 啟動 Python 虛擬環境
source venv/bin/activate

# 將虛擬環境用到的套件寫入 requirements.txt
pip freeze >> requirements.txt
```

### 遇到的問題
1. 忘記開啟/關閉虛擬環境
2. 忘記把新安裝的套件寫入 `requirements.txt`
3. `pip freeze` 會安裝過多不必要的套件

一開始我會使用 [pipreqs](https://github.com/bndr/pipreqs) 來解決 `pip freeze` 所造成的雜亂

但是忘記寫入套件跟忘記開關虛擬環境的問題還是存在
造成我常常在本地測試成功，送上去 CI 就出錯，只好再送一個 Pull Request 上去

## pipenv
[pipenv](https://pipenv.readthedocs.io/en/latest/) 可以用來同時管理虛擬環境跟套件
`pipenv` 不使用 `requriements.txt`，而是使用自定義的 `Pipfile` 跟 `Pipfile.lock` 來管理套件
只要一個指令就能將套件安裝到虛擬環境中，並且更新到 `Pipfile` 以及 `Pipfile.lock`

### 安裝 pipenv
根據不同的系統，可以在 [Installing Pipenv](https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv) 找到安裝 pipenv 的方式

```sh
pipx install pipenv
```

### 初始化環境

```sh
# 初始化虛擬環境
# 如果 Pipfile 跟 Pipfile.lock 還不存在，則會產生
pipenv install

# 指定不同版本的 Python
pipenv install --python 3.6.4

# 移除虛擬環境
pipenv --rm

# 列出虛擬環境的所在位置
pipenv --where
```

初始化虛擬環境後，會產生 `Pipfile` 跟 `Pipfile.lock`

* `Pipfile` 是一個 [toml](https://github.com/toml-lang/toml) 格式的檔案
    * source: 指定要去找套件的 pypi ，比較常見的 use case 是換到私有的 pypi
    * dev-package: 開發環境所需套件
    * packages: 預設安裝套件（通常是 Production 用）
    * requires: 是否需要限定在某個版本的 Python

```toml
[[source]]
name = "pypi"
url = "https://pypi.org/simple"
verify_ssl = true

[dev-packages]

[packages]

[requires]
python_version = "3.7"
```

* `Pipfile.lock` 則是 JSON 格式的檔案
    * 記錄下安裝的套件，以及其相依的套件（假設安裝了 A 套件，而它相依於 B 套件，則 A 跟 B 套件都會列在這）

```json
{
    "_meta": {
        "hash": {
            "sha256": "..."
        },
        "pipfile-spec": 6,
        "requires": {
            "python_version": "3.7"
        },
        "sources": [
            {
                "name": "pypi",
                "url": "https://pypi.org/simple",
                "verify_ssl": true
            }
        ]
    },
    "default": {},
    "develop": {}
}
```

通常沒有什麼特別的理由，可以不用動到 `Pipfile` 跟 `Pipfile.lock`
交給 `pipenv` 去管理就好

### 安裝套件
`pipenv` 另一個好處是，它的 API 基本上跟 [pip](https://pip.pypa.io/en/stable/) 是一樣的

```sh
# 安裝套件
pipenv install <package>==<version>

# 解除安裝套件
pipenv uninstall <package>

# 更新套件
pipenv update <package>
```

以安裝 [requests](https://requests.readthedocs.io/en/master/) 為例，
會更新在 `Pipfile` 中的 **packages**

```toml
[packages]
requests = "*"
```

`Pipfile.lock` 中除了 `requests` 外，還會安裝他的相依套件 urllib3 (Ref: [setup.py#L47](https://github.com/psf/requests/blob/v2.22.0/setup.py#L47))

```json
{
    ......
    "default": {
        ......

        "requests": {
            "hashes": [
                "sha256:11e007a8a2aa0323f5a921e9e6a2d7e4e67d9877e85773fba9ba6419025cbeb4",
                "sha256:9cf5292fcd0f598c671cfc1e0d7d1a7f13bb8085e9a590f48c010551dc6c4b31"
            ],
            "index": "pypi",
            "version": "==2.22.0"
        },
        "urllib3": {
            "hashes": [
                "sha256:3de946ffbed6e6746608990594d08faac602528ac7015ac28d33cee6a45b7398",
                "sha256:9a107b99a5393caf59c7aa3c1249c16e6879447533d0887f4336dde834c7be86"
            ],
            "version": "==1.25.6"
        }
    },
    ......
}
```

**hashes** 欄位會記錄下，安裝套件時產生的 hash 值
只要套件內容有改變，就會產生不同的 hash 值
主要可以用於驗證下次安裝時，這個套件是否跟這次是一樣的
能解決的問題是有些套件雖然改了內容，卻沒有升版
下面兩個指令就會運用到這個欄位

```sh
# 直接使用 Pipfile.lock 安裝套件
pipenv install --ignore-pipfile

# 安裝時同時確認 Pipfile.lock ，如果 lock 檔跟實際安裝的有衝突，則會跳出
pipenv install --deploy
```

`pipenv` 另外還可以做到將開發時才需要的到的套件分開來
取代以往在不同的環境下，使用不同的 `requirements.txt` (e.g.,  `requirments/dev.txt`, `requirements/prod.txt`)

```sh
# Install dev only package
pipenv install <package>==<version> --dev
```

以安裝 [pytest](https://docs.pytest.org/en/latest/) 為例
就會更新到 `Pipfile` 的 **dev-packages**

```toml
[dev-packages]
pytest = "*"
```

### 在虛擬環境中執行指令

```sh
# 在虛擬環境中執行 [command]
pipenv run <command>

# e.g.,
pipenv run python your_program.py
```

雖然可以透過 `pipenv shell` 進入到虛擬環境，但我不太建議使用
原因是我常常會進入虛擬環境後，亂下 `pip install <package>` 的指令
然後就沒被 `Pipfile` 給記錄到了...

### 其他功能
* `pipenv check`: 檢查安裝的套件是否有已知的安全性問題
* `pipenv graph`: 檢視整個相依套件的相依圖
* `pipenv open <package>`: 直接安裝的套件 （不知道什麼時候養成了「懶得看文件，直接 trace code」的習慣...）

### pipenv 已經很久沒更新了，還要使用嗎？
雖然我的確遇過一些小問題 (e.g., [pipenv 和 poerty 如何處理在不同作業系統下相依套件不同](https://lee-w.github.io/posts/tech/2020/02/how-pipenv-and-poetry-stores-if-dependencies-platform-dependent/))
但就我的使用上，我也不認為 `poetry` 有到完美
目前也還沒找到其他足夠好的工具
而且大部分的狀況下， `pipenv` 也足夠解決我的問題
所以沒什麼意外我大概還是會繼續使用 `pipenv`

## 其他工具

### poetry
[poetry](https://python-poetry.org/) 是目前最多人說可以取代 `pipenv` 的工具
除了 `pipenv` 包含的功能外，它還能用來初始化專案、上傳套件

但我比較不喜歡的一點是，它採用的 API 跟版本標示方式都跟 `pip` 不同
就會再增加學習成本

不過它採用 `pyproject.toml` 來做 configuration 我倒是蠻喜歡的

### pip-tools
[pip-tools](https://github.com/jazzband/pip-tools) 只做產生 lock 檔的部分，不能用來管理虛擬環境
這套工具比較適合習慣使用 `pip` 跟 `virtualenv` ，但又想要有 lock 檔的狀況

### dephell
[dephell](https://github.com/dephell/dephell) 是一個 all-in-one 的工具
當初看到覺得很有趣，但還沒有時間好好研究
目前使用到對我最有幫助的功能是它能在轉換不同的格式 (e.g., `Pipfile` → `pyproject.toml`)

## 自動將舊版套件升級
* [pyup.io](https://pyup.io)
* [dependabot](https://dependabot.com)

## Reference
* [這樣的開發環境沒問題嗎？ - PyCon TW 2018](https://lee-w.github.io/pycon-note/posts/pycon-tw-2018/2019/10/is-your-dev-env-alright/)
* [Pipenv: The Future of Python Dependency Management - PyCon US 2018](https://lee-w.github.io/pycon-note/posts/pycon-us-2018/2019/11/pipenv-the-future-of-python-dependency-management/)
* [Python Dependency Management - PyCon DE 2018](https://lee-w.github.io/pycon-note/posts/pycon-de-2018/2019/12/python-dependency-management/)
