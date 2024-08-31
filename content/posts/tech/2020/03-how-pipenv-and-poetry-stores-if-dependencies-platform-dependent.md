Title: pipenv 和 poerty 如何處理在不同作業系統下相依套件不同
Date: 2020-02-12 11:45
Category: Tech
Tags: Python, Dependency
Slug: how-pipenv-and-poetry-stores-if-dependencies-platform-dependent
Authors: Wei Lee

[TOC]

## 遇到的問題
用 [twine](https://twine.readthedocs.io/en/latest/) 上傳 Python 套件
在 mac 的本地端測試有成功，但丟上 CI 跑在 Ubuntu 的 image 內會缺少 `jeepney` 套件

## 問題的根源
目前最新版 (3.1.1) 的 twine 相依於套件 [keyring](https://github.com/jaraco/keyring) ([setup.cfg#L44](https://github.com/pypa/twine/blob/3.1.1/setup.cfg#L44))
而 keyring 在不同的作業系統中，相依的套件是不同的 ([setup.cfg#L30](https://github.com/jaraco/keyring/blob/master/setup.cfg#L30))

```toml
install_requires =
    pywin32-ctypes!=0.1.0,!=0.1.1; sys_platform=="win32"
    SecretStorage>=3; sys_platform=="linux"
    jeepney>=0.4.2; sys_platform=="linux"
    importlib_metadata; python_version < "3.8"
```

我缺少的的確就是那幾個 `sys_platform=="linux"` 的套件

## pipenv 怎麼處理
基本上 `pipenv` 不算有解決這個問題， `pipenv` 只會將目前系統的所需套件寫進 **Pipfile.lock**

以 twine 為例，在 macOS 透過 `pipenv` 安裝 ，跑 `pipenv graph`指令
就會發現 keyring 只會直接相依於 importlib-metadata

```text
  - keyring [required: >=15.1, installed: 21.1.0]
    - importlib-metadata [required: Any, installed: 1.5.0]
      - zipp [required: >=0.5, installed: 2.2.0]
```

但換到 Ubuntu 上跑，就會多了 SecretStorage 跟 jeepney

```text
  - keyring [required: >=15.1, installed: 21.1.0]
    - importlib-metadata [required: Any, installed: 1.5.0]
      - zipp [required: >=0.5, installed: 2.2.0]
    - jeepney [required: >=0.4.2, installed: 0.4.2]
    - SecretStorage [required: >=3, installed: 3.1.2]
      - cryptography [required: Any, installed: 2.8]
        - cffi [required: >=1.8,!=1.11.3, installed: 1.14.0]
          - pycparser [required: Any, installed: 2.19]
        - six [required: >=1.4.1, installed: 1.14.0]
      - jeepney [required: >=0.4.2, installed: 0.4.2]
```

這個問題也有其他人提過 ([Cross-platform Pipenv.lock? #3902](https://github.com/pypa/pipenv/issues/3902))

`pipenv` 貢獻者給的建議是使用 `pipenv install --keep-outdated`
但這個指令的說明是 **Keep out-dated dependencies from being updated in Pipfile.lock.**
總覺得好像不是在這個 use case 下使用的

最後我的解決方案是是把那幾個平台相依的套件安裝進去
原因是在 production 的環境就是需要這幾個多安裝的套件，我在 local 多裝幾個套件好像也沒什麼差
但如果今天是相反的狀況，我可能就會傾向 local 跑在 docker 裡

## Poetry 怎麼處理
[poerty](https://python-poetry.org/) 對這個問題則是有比較好的解法

透過 poetry 安裝 twine 後
產生的 **poetry.lock** 會把 `marker = "sys_platform == \"linux\""` 記錄下來
實際 `poetry shell` 進去看，的確也沒多安裝這些套件

```toml
[[package]]
category = "main"
description = "Store and access your passwords safely."
name = "keyring"
optional = false
python-versions = ">=3.6"
version = "21.1.0"

[package.dependencies]
SecretStorage = ">=3"
jeepney = ">=0.4.2"
pywin32-ctypes = "<0.1.0 || >0.1.0,<0.1.1 || >0.1.1"

......

[[package]]
category = "main"
description = "Python bindings to FreeDesktop.org Secret Service API"
marker = "sys_platform == \"linux\""
name = "secretstorage"
optional = false
python-versions = ">=3.5"
version = "3.1.2"
```

## 總結
poetry 在處理不同平台相依套件不同的狀況，處理得比較好
它會把所有需要的資訊記錄下來，在不同的平台進行不同的安裝

如果要用 pipenv 則可以使用 `pipenv install --keep-outdated`
或者就直接多安裝這幾個不是每個平台都需要的套件
