Title: 更新到 pytest 9.0.0 了，大家記得更新環境
Date: 2025-11-12 10:30
Category: Tech
Tags: Airflow, Airflow 開發生情報
Slug: pytest-9-upgrade
Authors: Wei Lee

寫這篇文的時候，[9.0.1](https://github.com/pytest-dev/pytest/releases/tag/9.0.1) 剛好出來...
<!--more-->

👉 原文： [[ANNOUNCE] Pytest 9 upgrade - do your environment(s) upgrade](https://lists.apache.org/thread/ngwdontq5kvvbwkxwos8hx6jh739f9h4)

## 本文
Airflow 的測試相依套件 pytest 更新到 9.0.0 了
有些外掛有因此要小改寫，但這些 Jarek 都處理好了
所以你各位如果本地開發遇到問題
先試試看下面的指令

```shell
uv sync

breeze ci-image build [--python X.Y]
```

啊對，這次 pytest 的錯誤訊息超越了 Jarek 訊息的長度

## 我怎麼想
恩，蠻好的啊
pytest 竟然更新到 [9.0.0](https://github.com/pytest-dev/pytest/releases/tag/9.0.0)
來看一下有什麼改動，紀錄幾個我比較在乎的

### subtests
* 類似 `pytest.mark.parametrize`，但更適用於參數在測試收集階段還無法知道確切值的時候

e.g.,

```python
def test_py_files_contain_docstring(subtests: pytest.Subtests) -> None:
    for path in Path.cwd().glob("*.py"):
        with subtests.test(path=str(path)):
            assert contains_docstring(path)
```

### 原生 TOML 設定檔

終於可以直接用 `[tool.pytest]` ，而不是 `[tool.pytest.ini_options]` 了

反正 pytest 都升上去了，就順手發了這個 [Update pyproject.toml files with pytest>=9.0.0 TOML syntax #58182](https://github.com/apache/airflow/pull/58182) 用用看新的設定方式
`pythonpath` 跟 `addopts` 會需要一點小改動
大致上是讓型別更清楚，還蠻好的
中間有遇到 [inconsistent parsing of addopts in toml #13903](https://github.com/pytest-dev/pytest/issues/13903)，但我認為 TOML 這邊如此設計蠻合理的

之後 commitizen 也來發一下

### 增加設定 strict_parametrization_ids
避免重複的參數化 id，也就是避免無謂重複的測試案例

因為 airflow 有開啟 Ruff 的 [PT014](https://docs.astral.sh/ruff/rules/pytest-duplicate-parametrize-test-cases/) ，應該已經遇不到了
但 pytest 有原生支援還是蠻不錯的

### 停止支援 Python 3.9
畢竟 Python 3.9 的生命週期已經走到盡頭
