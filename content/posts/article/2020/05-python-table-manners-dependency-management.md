Title: Python Table Manners - 虛擬環境和套件管理
Date: 2020-02-23 12:24
Modified: 2020-10-04 15:22
Category: Tech
Tags: Python, Dependency
Slug: python-table-manners-dependency-mangement
Authors: Lee-W
Series: Python Table Manners

開始 Python 專案時，第一步都是建立一個專屬於專案的虛擬環境
會需要這麼做是為了避免不同的 Python 專案需要使用到不同版本的套件
假設專案 A 需要 `lib==2.3.5` 而專案 B 需要 `lib==1.0.0`
如果 `lib` 都被安裝在本機中，就會有其中一個專案跑不起來
所以只要兩個專案都有建立虛擬環境，它們就都能在自己的虛擬環境中安裝所需的 `lib` 版本
理想上，本機的環境是不需要安裝套件的
因為每一個專案都會在個字的虛擬環境內執行，並安裝各自的套件

<!--more-->

[TOC]

## venv
建立虛擬環境，最基本作法是使用 [venv](https://docs.python.org/3/library/venv.html)
透過以下幾個指令建立，並把需要的套件寫入 `requirements.txt`

```sh
# 建立 Python 虛擬環境到 ./venv
python -m venv ./venv

# 啟動 Python 虛擬環境 (for Unix like)
source venv/bin/activate

# 將虛擬環境用到的套件寫入 requirements.txt
pip freeze >> requirements.txt
```

p.s. 基本上這個系列文會以 Unix 系統（macOS, Linux）為主

但這個做法會遇到幾個問題

1. 忘記開啟/關閉虛擬環境
2. 忘記把新安裝的套件寫入 requirements.txt
3. `pip freeze` 安裝一些不必要的套件

一開始我會使用 [pipreqs](https://github.com/bndr/pipreqs) 來解決 `pip freeze` 所造成的雜亂
但是忘記更新 requirements.txt 跟開關虛擬環境的問題還是存在
常常我在本地測試成功，push 到遠端的時候又告訴我少了套件
只好再送一個 Pull Request 修正......

## pipenv
[pipenv](https://pipenv.readthedocs.io/en/latest/) 可以用來同時管理虛擬環境跟套件
pipenv 不使用 `requriements.txt`，而是使用自定義的 `Pipfile` 跟 `Pipfile.lock` 管理套件
它的好處是能透過單一指令將套件安裝到虛擬環境中，並且更新到 `Pipfile` 以及 `Pipfile.lock`

### 安裝 pipenv
根據不同的系統，可以在 [Installing Pipenv](https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv) 找到安裝 pipenv 的方式

不過最簡單的做法還是透過 `pip` 安裝

```sh
python -m pip install --user pipenv
```

### 初始化環境

```sh
# 初始化虛擬環境
# 如果 Pipfile 跟 Pipfile.lock 還不存在，則會產生
pipenv install

# 指定用特定版本的 Python 來產生虛擬環境
pipenv install --python 3.6.4

# 移除虛擬環境
pipenv --rm

# 列出虛擬環境的所在位置
pipenv --where
```

初始化虛擬環境後，會產生 `Pipfile` 跟 `Pipfile.lock`

* `Pipfile` 是 [toml](https://github.com/toml-lang/toml) 格式的檔案
    * **source**: 指定要去找套件的倉儲，預設是 [PyPI](https://pypi.org/) ，也可以再加上私有的 PyPI
    * **dev-package**: 開發環境所需套件
    * **packages**: 預設安裝套件（通常是 Production 用）

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

* `Pipfile.lock` 是 JSON 格式的檔案
    * 同樣是記錄安裝的套件，但會同時記錄下套件相依的其他套件（假設安裝了 `requests` 套件，而 `requests` 相依於 `urllib3` ，則 `requests` 跟 `urllibs` 都會列在這）

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
交給 `pipenv` 管理就好

### 安裝套件
pipenv 的另一個好處是，它的 API 基本上跟 [pip](https://pip.pypa.io/en/stable/) 是一樣的

```sh
# 安裝套件
pipenv install <package>==<version>

# 解除安裝套件
pipenv uninstall <package>

# 更新套件
pipenv update <package>
```

以安裝 [requests](https://requests.readthedocs.io/en/master/) 為例
會更新在 Pipfile 的 **packages** 區段

```toml
[packages]
requests = "*"
```

Pipfile.lock 中除了 `requests` 外，還會列出 `requests` 的相依套件 `urllib3` (Ref: [setup.py#L47](https://github.com/psf/requests/blob/v2.22.0/setup.py#L47))

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

可以注意到每個安裝的套件會有三個欄位 **index**, **version** 和 **hashes**

* **index**: 套件從哪裡裝的
* **version**: 安裝的版本
* **hashes**: 下載這個套件時產生的雜湊值 (hashing)  
  只要套件內容有改變，就會產生不同的雜湊值  
  可以用於驗證下次安裝時，這個套件的內容是否跟這次相同
  有些套件雖然改了內容，但沒有更新版本號  
  雜湊值可以用來避免使用者在沒注意到的情況下安裝了不同的套件

下面兩個指令就會運用到 **hashes**

```sh
# 安裝時同時確認 Pipfile.lock ，如果 lock 檔跟實際安裝的有衝突，則會取消安裝
pipenv install --deploy

# 直接使用 Pipfile.lock 安裝套件
pipenv install --ignore-pipfile
```

### 安裝開發環境套件
有些套件（e.g., 測試工具）不需要在 Production 的環境上安裝
以往會將不同的套件用不同的 `requirements.txt` 來管理 (e.g.,  `requirments/dev.txt`, `requirements/prod.txt`)
pipenv 則是將開發環境才需要的套件寫在 Pipfile 的 **dev-packages** 內
只要在安裝時後面加上選項 `--dev`

e.g.,

```sh
# 安裝開發環境套件
pipenv install <package>==<version> --dev
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
然後就沒被 Pipfile 給記錄到...

### 其他功能
* `pipenv check`: 檢查安裝的套件是否有已知的安全性問題
* `pipenv graph`: 檢視整個相依套件的相依圖
* `pipenv open <package>`: 開啟安裝的套件（不知道什麼時候養成了「懶得看文件，直接 trace code」的習慣...）

## Poetry
[poetry](https://python-poetry.org/) 是目前很多人說可以取代 pipenv 的工具
除了 pipenv 包含的功能外，它還能用來初始化專案、上傳套件

* pipenv 被抱怨的原因
    * 之前有相隔快兩年沒有新的版本釋出（2020 年倒是更新了幾次）
    * lock 太慢
    * 不會自動跟 setup.py 中的 `install_rquires`

poetry 使用下來體驗還算不錯
而且它採用 pyproject.toml 來做配置設定，這點我就蠻喜歡的

我會建議如果要寫 Python 函式庫的話，可以使用 poetry
至於 Python 應用，使用 pipenv 還是 poetry 就看個人的喜好了

### 基本使用

```sh
# 初始化 poetry 專案
poetry init

# 安裝套件
poetry install

# 加入新的套件
poetry add <package>

# 移除套件
poetry remove <package>
```

## 其他工具
### pip-tools
[pip-tools](https://github.com/jazzband/pip-tools) 主要的功能是產生 hashes ，並不能用來管理虛擬環境
這套工具比較適合習慣使用 pip 跟 virtualenv ，但又想要有 Pipfile.lock 的功能的情況

### dephell
[dephell](https://github.com/dephell/dephell) 是個 all-in-one 的工具
當初看到覺得很有趣，但還沒有時間好好研究
目前使用到對我最有幫助的功能是它能在轉換不同的格式 (e.g., Pipfile → pyproject.toml)

### 自動偵測套件版本並適當升級的服務
* [pyup.io](https://pyup.io)
* [dependabot](https://dependabot.com)

## Bouns: pipx - 在系統安裝 Python 工具
雖然建議 Python 的套件都裝在虛擬環境，但如果平時要使用的工具 (e.g., [invoke](http://www.pyinvoke.org/), [awscli](https://pypi.org/project/awscli/)) 都裝在虛擬環境
每次使用這些工具都得進入虛擬環境就太麻煩了
[pipx](https://pipxproject.github.io/pipx/) 會為每個工具創建一個專屬的虛擬環境，並且設定好 PATH

* 安裝 pipx，並設定 PATH

```sh
python -m pip install --user pipx
python -m pipx ensurepath
```

* 安裝工具

```sh
pipx install [package]
```

## Reference
* [這樣的開發環境沒問題嗎？ - PyCon TW 2018](https://lee-w.github.io/pycon-note/posts/pycon-tw-2018/2019/10/is-your-dev-env-alright/)
* [Pipenv: The Future of Python Dependency Management - PyCon US 2018](https://lee-w.github.io/pycon-note/posts/pycon-us-2018/2019/11/pipenv-the-future-of-python-dependency-management/)
* [Python Dependency Management - PyCon DE 2018](https://lee-w.github.io/pycon-note/posts/pycon-de-2018/2019/12/python-dependency-management/)
