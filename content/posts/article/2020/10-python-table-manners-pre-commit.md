Title: Python Table Manners - pre-commit: git commit 前做完檢查
Date: 2020-02-28 23:10
Modified: 2020-03-18 10:20
Category: Tech
Tags: Python, Git, Code Quality
Slug: python-table-manners-pre-commit
Authors: Lee-W
Series: Python Table Manners

在前一篇提到了 invoke，透過它可以簡化很多繁瑣的指令
但人類是懶惰的
即使已經更簡便了，沒被督促常常還是會忘了執行
就像這次的系列文，如果沒被寫作松督促，不知道什麼時候才會出現（笑
所以這次要來聊聊 [pre-commit](https://pre-commit.com) 如何強制做檢查

[TOC]

## pre-commit
[pre-commit](https://pre-commit.com/) 主要的用途就是讓我們能方便的加入 [Git Hook](https://git-scm.com/book/zh-tw/v2/Customizing-Git-Git-Hooks)，並在各種 git 的相關操作前進行檢查

正如它的命名，它可以在進行 `git commit` 前執行一些操作
不過並不僅限於 commit 前，也可以在其它 git 的階段進行
之所以要這麼做就是為了讓不符合要求的程式碼，從最一開始就不會進入到版本庫 （pre commit）或 git 伺服器 （pre push）

## 使用 pre-commit 進行檢查

```sh
# 安裝 pre-commit
pipenv install pre-commit --dev
```

之後可以開始寫設定檔 `.pre-commit-config.yaml`，告訴 pre-commit 要做哪些檢查
需要注意的是，專案必須要是一個 git 專案
這些設定都會被寫入 `.git/hooks/` 中

e.g.,

```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v2.5.0
    hooks:
      - id: end-of-file-fixer
      - id: trailing-whitespace
        args: [--markdown-linebreak-ext=md]
```

以上面的例子來說

* `repos` 告訴 pre-commit 要去哪邊找到這些 hook
    * `repo`: 去找專案 [pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks)
    * `rev`: 在專案 pre-commit-hooks 找到 rev [v2.3.0](https://github.com/pre-commit/pre-commit-hooks/tree/v2.3.0)
    * `hooks`: 在 pre-commit-hooks rev v2.3.0 的 [.pre-commit-hooks.yaml](https://github.com/pre-commit/pre-commit-hooks/blob/v2.3.0/.pre-commit-hooks.yaml) 中尋找指定的 hook
        * `id`: hook id
        * `args`: 執行這個 hook 的額外參數

大部分常見的 hook 都被定義在[pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks)
除此之外，如 [black](https://github.com/psf/black) 和 [flake8](https://gitlab.com/pycqa/flake8) 等工具也都有提供 pre commit hook

另外，**建議 rev 不要使用 master，而應該使用版本號等明確的 rev**
原因是預設 pre-commit 會將已知的專案存下來
如果沒有特別設定， pre-commit 不會把最新版 pull 下來
那指到的 master 就只會第一次 pre-commit 抓到時的 master，不會是真正最新版的 master

寫完設定檔後，接著就是把 pre-commit hook 安裝到 git 專案中

```sh
# 將 pre-commit hook 安裝到 git 專案
pipenv run pre-commit install
```

需要注意的是每次重新 clone 之後，都必須要執行一次
雖然可以將 `.pre-commit-config.yaml` 加入版本控制
但 `.git/hook/` 是不能被加入版本控制的

執行完會出現以下訊息

```sh
pre-commit installed at .git/hooks/pre-commit
```

第一次進行 git commit 時，會將 [pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks) clone 到 pre-commit 統一管理的地方
之後就會進行 `Fix End of Files` 跟 `Trim Trailing Whitespace` 的檢查

```sh
[INFO] Initializing environment for https://github.com/pre-commit/pre-commit-hooks.
[INFO] Installing environment for https://github.com/pre-commit/pre-commit-hooks.
[INFO] Once installed this environment will be reused.
[INFO] This may take a few minutes...
Fix End of Files.........................................................Passed
Trim Trailing Whitespace.................................................Passed
```

如果沒有通過， git 會阻止你進行 commit

## 使用自定義的 pre-commit hook
除了使用現成的 pre-commit hook，也可以寫客製化的檢查

下面的例子就是在 commit 前，要進行 pytest 的檢查

```yaml
repos:
  - repo: local
    hooks:
      - id: pytest
        name: pytest
        stages: [commit]
        language: system
        entry: pipenv run pytest
        types: [python]
```

* `repo: local`: 直接在本地資料夾執行
    * `hooks`: 有哪些 hook 要執行
        * `id`, `name`: hook 的 id / name 是 `pytest`
        * `stages`: 在 `commit` 前執行
        * `language`: 直接使用系統執行 `entry` 內的指令
        * `entry`: 這個 hook 要執行的指令是 `pipenv run pytest`
        * `types`: 只有在 python 這種檔案類型才進行檢查

其中 `stages` 總共有六種

* commit
* merge-commit
* push
* prepare-commit-msg
* commit-msg
* manual

這裡需要注意的是當執行 `pipenv run pre-commit commit` 時
預設只會寫入 `.git/hooks/pre-commit`
如果要加入其他階段，則必須要在後面加入參數 `-t [hook-type]`

e.g.,

```sh
pipenv install pre-commit install pre-push
```

* 支援的 6 種 hook-type
    * pre-commit
    * pre-merge-commit
    * pre-push
    * prepare-commit-msg
    * commit-msg

像是 pytest 這種需要執行比較久的
我就不見得會在 commit 這個 stage 做檢查
而是會把 `stages` 改成 `push`
並安裝 pre-push 的 hook (i.e. `pipenv run pre-commit install -t pre-push`)

如果不想要每個 hook 都各自做設定，可以在 `.pre-commit-config.yaml` 加上 `default_stages`

```yaml
default_stages: [push]
```

表示如果沒有特定指定 `stages` 的 hook 都只在 `push` 的階段做檢查

## 為自己的工具加上 pre-commit hook
如果你有寫檢查工具，加上 pre-commit hook 就能讓人更方便使用你的工具
在工具加入 `.pre-commit-hooks.yaml` 讓 pre-commit 知道其他人引入你的工具時要怎麼做檢查
撰寫的方式跟 local 的 repo 的寫法相似

```yaml
repos:
    - repo: local
      hooks:
        - id: ...
          name: ...
          description: ...
          entry: ...
```

## Reference
* [提升程式碼品質：使用 Pre-Commit (Git Hooks)](https://mropengate.blogspot.com/2019/08/pre-commit-git-hooks_4.html)
