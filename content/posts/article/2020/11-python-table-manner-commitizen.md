Title: Python Table Manners - Commitizen: 規格化 commit message
Date: 2020-03-01 00:45
Category: Tech
Tags: Python
Slug: python-table-manners-commitizen
Authors: Lee-W
Series: Python Table Manners

接續著前一篇的 pre-commit ，這篇來聊聊如何透過 [commitizen](https://github.com/Woile/commitizen) 規範 commit message

## 為什麼要好好寫 commit message
![no-good-commit](/images/posts-image/2020-02-22-python-table-manner-series/no-good-commit.jpg)

如果不寫好 commit message，哪天系統出錯時，必須回朔到某個版本就會變得相對困難

![bad-commit](/images/posts-image/2020-02-22-python-table-manner-series/bad-commit.jpg)
(from [hackjutsu/bad-commit-example](https://github.com/hackjutsu/bad-commit-example/commits/master))

撰寫好的 commit message 能讓團隊間的溝通更順利

* 送 Pull Request / Merge Request 時，reviewers 能更快速地知道這次增加了哪些功能，也能找到其脈絡
* 新進人員可以從過往的 commit message 找到整個專案發展的脈絡，更容易上手專案

## Commitizen
比起通泛的 commit message 撰寫建議，[commitizen](https://woile.github.io/commitizen/) 更進一步規範 commit message 如何被撰寫
過互動式介面，讓使用者能夠輕鬆地產生符合規範的 commit message

同時也整合了前一篇所提到的 pre-commit hook，避免使用者將不符合規範的 commit message 寫入

除了採用來自 Angular 社群的 [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) (約定式提交) 外， commitizen 提供了高度的客製化，讓每個團隊或專案都可以依照自己的需求，撰寫相對應的規範

規範了 commit message 後，除了增加可讀性增加外，也讓這些訊息有可以被解析做其他運用 （e.g., 升版, 產生更新日誌）

## 安裝與設定 Commitizen
跟 invoke 一樣，我會把 commitizen 同時安裝在系統和虛擬環境

安裝在虛擬環境主要是為了能在 CI/CD 伺服器上自動升版

```sh
# 安裝 commitizen 到系統
pipx install commitizen

# 安裝 commitizen 到虛擬環境中
pipenv install commitizen --dev
```

在專案中第一次使用 commitizen 可以使用初始化指令來完成基本的設定

```sh
cz init
```

一開始會問要將設定寫在哪個檔案內
ini 格式的設定（i.e., `.cz`, `setup.cfg`, `.cz.cfg`） 在 2.0 之後將不再支援
因此建議選擇 `pyproject.toml`

![cz-init-1](/images/posts-image/2020-02-22-python-table-manner-series/cz-init-1.jpg)

接著會選擇一套 commit message 規範
預設有三種，我最常使用的是 `cz_conventional_commits`

![cz-init-2](/images/posts-image/2020-02-22-python-table-manner-series/cz-init-2.jpg)

再來回詢問抓最新的 git tag 來確認是否為目前的版本號
如果選擇否，就會列出 `git tag` 所有的結果
如果 `git tag` 沒有結果，就會預設為 0.0.1

![cz-init-3](/images/posts-image/2020-02-22-python-table-manner-series/cz-init-3.jpg)

最後會詢問版本的格式要是如何
常用的格式有 `$version` (e.g., `1.0.0`) 或 `v$version` (e.g., `v1.0.0`)

![cz-init-4](/images/posts-image/2020-02-22-python-table-manner-series/cz-init-4.jpg)

完成後就會產生對應的 `pyproject.toml`

```toml
[tool.commitizen]
name = "cz_conventional_commits"
version = "1.0.2"
tag_format = "$version"
```

## 使用 Commitizen

```sh
# 也可以使用簡短版 cz c
cz commit
```

以 `cz_conventional_commits` 為例
使用 commitizen 來做 commit 時，會先詢問這次的 commit 做了哪一種改動

![commitizen-1](/images/posts-image/2020-02-22-python-table-manner-series/commitizen-1.jpg)

接著會要求輸入這次改動的細節

![commitizen-2-w1024](/images/posts-image/2020-02-22-python-table-manner-series/commitizen-2.jpg)

以上面的例子來說，產生出的 commit message 就會是 **feat(tasks): add \`inv git.commit\`**

當一個專案一直都是使用 commitizen 來做 commit ，就能產生如同下圖那樣清楚的紀錄

![commitizen-log](/images/posts-image/2020-02-22-python-table-manner-series/commitizen-log.jpg)

## 強制檢查 commit message
剛開始引入 commitizen 時，可能會常常忘記要使用它來做 commit
這時候就能使用到前一篇提到的 [pre-commit](https://pre-commit.com/)
我在 [commitizen](https://github.com/Woile/commitizen) 中有加入 [.pre-commit-hooks.yaml](https://github.com/Woile/commitizen/blob/master/.pre-commit-hooks.yaml)

因此只要在專案的 `.pre-commit-config.yaml` 加入以下這段

```yaml
- repos
  - repo: https://github.com/Woile/commitizen
    rev: master
    hooks:
      - id: commitizen
        stages: [commit-msg]
```

並將 pre-commit 設定到 commit-msg

```sh
pipenv run pre-commit install -t commit-msg
```

在 commit 執行完，要進訊息寫入前
commitizen 會執行 `cz check` 來確認輸入的訊息是否符合規範
如果不符合規範就會拒絕這次的 commit

需要注意到的是檢查在產生 commit message 後才能執行，因此要設定要將 stage 設定成 commit-msg，並要將 pre-commit hook 設定到 commit-msg (i.e., `.git/hooks/commit-msg`)

## Reference
* [How to Write Good Commit Messages: A Practical Git Guide](https://www.freecodecamp.org/news/writing-good-commit-messages-a-practical-guide/)
