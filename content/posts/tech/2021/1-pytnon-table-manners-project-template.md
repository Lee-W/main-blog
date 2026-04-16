Title: Python Table Manners - Cookiecutter 專案模板
Date: 2021-01-01 13:30 +0800
Category: Tech
Tags: Python
Slug: python-table-manners-cookiecutter
Series: Python Table Manners
Authors: Wei Lee
Lang: zh-tw

[Python Table Manners 系列]({filename}/posts/tech/2020/04-python-table-manners-series.md) 整理了各種開發 Python 專案能用到的工具們
如果每次重新開啟新專案都得重複設定的步驟就很浪費時間
所以我將它們整理成專案模板 [cookiecutter-python-template](https://github.com/Lee-W/cookiecutter-python-template)
下次創立新專案的時候，只要透過這個模板就能快速產生已經設定好的空白專案
這篇文章會跟大家聊聊如何使用這個專案模板和如何建立自己的專案模板

<!--more-->

[TOC]

## 什麼是 Cookiecutter？
[Cookiecutter](https://github.com/cookiecutter/cookiecutter) 是以 Python 撰寫，透過已有的專案模板產生新專案的工具
雖然是用 Python 撰寫，但不限於只能使用在 Python 專案
甚至也不太需要會寫 Python，就能製作屬於自己的專案模板
目前在 Github 上，已經有超過 5,000 個已經製作好的 cookiecutter 模板

相較於每次都從前一個專案或空專案複製設定的做法
Cookiecutter 能確保我們不會少代換掉舊的設定（e.g., 舊專案名稱）
並減少需要代換這些內容的人力

## 如何使用 Cookiecutter 模板？
以我製作的模板 [cookiecutter-python-template](https://github.com/Lee-W/cookiecutter-python-template) 為例

首先要安裝 cookiecutter ，建議使用 pipx

```sh
pipx install cookiecutter
```

再來要指定產生新專案要用的模板

```sh
cookiecutter https://github.com/Lee-W/cookiecutter-python-template
```

接著會進入互動式介面，詢問專案相關的設定
每個問題依序會以 `值 [預設值]: 使用者輸入` 的形式出現
有的`值`會因為前面的回答不同，而產生對應的預設值
`值` (e.g., python_table_manners) 會被帶回專案模板去取代模板中的變數 (e.g., project_slug)

```txt
project_name [Python Project]: python table manners
project_slug [python_table_manners]:
project_description [Short Description for Python Project]: example for cookiecutter template
github_username [Lee-W]:
github_url [http://github.com/Lee-W/python_table_manners]:
author_name [Wei Lee]:
author_email [weilee.rx@gmail.com]: test@test.com
python_version [3.7]: 3.9
Select dependency_management_tool:
1 - pipenv
2 - poetry
Choose from 1, 2 [1]: 2
use_strict_mypy_config [n]: n
Select open_source_license:
1 - MIT license
2 - BSD license
3 - ISC license
4 - Apache Software License 2.0
5 - GNU General Public License v3
6 - Not open source
Choose from 1, 2, 3, 4, 5, 6 [1]: 1
```

所有問題都回答完之後就會出現新的資料夾 python_table_manners
（模板以 project_slug 作為產生的資料夾名稱）
可以看到資料夾裡面已經有前幾篇提到會用到的相關檔案

```sh
$ tree python_table_manners

.
├── CHANGELOG.md
├── LICENSE
├── docs
│   ├── README.md
│   └── contributing.md
├── mkdocs.yml
├── pyproject.toml
├── python_table_manners
│   ├── __init__.py
│   └── python_table_manners.py
├── setup.cfg
├── tasks
│   ├── __init__.py
│   ├── build.py
│   ├── common.py
│   ├── doc.py
│   ├── env.py
│   ├── git.py
│   ├── secure.py
│   ├── style.py
│   └── test.py
└── tests
    ├── __init__.py
    └── test_python_table_manners.py

4 directories, 20 files
```

## 如何製作 Cookiecutter 模板？
在新的專案內，先開個名稱為 `{{ cookiecutter.project_slug }}` 的資料夾
所有模板的內容都將放在這裡
e.g., [cookiecutter-python-template/{{ cookiecutter.project_slug }}](https://github.com/Lee-W/cookiecutter-python-template/tree/0.6.1/%7B%7Bcookiecutter.project_slug%7D%7D)

接著將想問使用者的問題寫進 `cookiecutter.json`
可以參考 [cookiecutter-python-template/cookiecutter.json](https://github.com/Lee-W/cookiecutter-python-template/blob/0.6.1/cookiecutter.json)
key 就是詢問使用者的問題，value 就是預設值

對 [jinja2](https://jinja.palletsprojects.com/en/2.11.x/) 熟悉的讀者，可能看到 `{{ }}` 就發現了
cookiecutter 背後是透過 jinja2 來取代這些值
模板中所有 `{{ cookiecutter.key_from_cookiecutter_json }}` 都會被代換成 cookiecutter.json 裡面的值
因為是使用 jinja2 ，當然也能運用它方便的語法
並且不限定於模板內才能使用，甚至在 cookiecutter.json 裡面都能使用

e.g.,

```json
{
    "project_name": "Python Project",
    "project_slug": "{{ cookiecutter.project_name.lower().replace(' ', '_').replace('-', '_') }}",
    ...,
    "_template_version": "0.6.1"
}
```

（from [cookiecutter-python-template/cookiecutter.json @ 0.6.1](https://github.com/Lee-W/cookiecutter-python-template/blob/0.6.1/cookiecutter.json)）

如果有一些值不想問使用者，可以在 key 的最前面加上 `_`
(e.g., `_template_version`)

當然也能使用 jinja2 的 if/else 語法，針對使用者的回答產生不同的模板內容
以下的範例就是使用者選擇不同的 dependency_management_tool 時，env.py 的指令內容會跟著改變

<!-- blacken-docs:off -->

```python
@task
def init(ctx):
    """Install production dependencies"""
    {% if cookiecutter.dependency_management_tool == 'pipenv' -%}
    ctx.run("pipenv install --deploy")
    {%- elif cookiecutter.dependency_management_tool == 'poetry' -%}
    ctx.run("poetry install --no-dev")
    {%- endif %}
```

（from [cookiecutter-python-template/{{cookiecutter.project_slug}}/tasks/env.py @ 0.6.1](https://github.com/Lee-W/cookiecutter-python-template/blob/0.6.1/%7B%7Bcookiecutter.project_slug%7D%7D/tasks/env.py#L18)）
<!-- blacken-docs:on -->

除了預設基本的 jinja2 語法外， cookiecutter 還提供了常用的 jinja2 extensions
這些可以在 [Template Extensions](https://cookiecutter.readthedocs.io/en/latest/advanced/hooks.html) 找到

比較可惜的是 Cookiecutter 並不支援追加問答
假設你想在使用者回答 dependency_management_tool 後
因為使用者選擇了 poetry，接續問要用哪個 poetry 版本
但當使用者選 pipenv 則不問這個問題
這樣的設計在 cookiecutter 是做不到的
（Read the discussion 👉 [Conditional follow-up questions based on prior answers #913](https://github.com/cookiecutter/cookiecutter/issues/913#issuecomment-286571701)）

### hook
如果有嘗試用我的專案模板產生專案，並且選擇不同的 dependency_management_tool
你會發現在選擇 pipenv 的時候會有 Pipfile，但選 poetry 的時候不會有
這就是透過 post_gen_project.py 做到的

[cookiecutter-python-template/hooks/](https://github.com/Lee-W/cookiecutter-python-template/tree/0.6.1/hooks)中，可以看到以下兩個檔案

* `pre_gen_project.py`: 建立專案前要執行的內容
* `post_gen_project.py`: 建立專案後要執行的內容

在 post_gen_project.py 中會做判斷，只要使用者不是選 pipenv ，就會把 Pipfile 刪除

```python
def main():
    if "{{ cookiecutter.dependency_management_tool }}" != "pipenv":
        remove_pipfile()
```

（from [cookiecutter-python-template/hooks/post_gen_project.py](https://github.com/Lee-W/cookiecutter-python-template/blob/0.6.1/hooks/post_gen_project.py#L8)）

（Read more 👉 [Using Pre/Post-Generate Hooks (0.7.0+)](https://cookiecutter.readthedocs.io/en/latest/advanced/hooks.html)）

## Reference
* [Python Application Layouts: A Reference](https://realpython.com/python-application-layouts/)
* [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage)
* [wemake-services/wemake-python-package](https://github.com/wemake-services/wemake-python-package)
* [How to set up a perfect Python project](https://sourcery.ai/blog/python-best-practices/)
* [Understanding Best Practice Python Tooling by Comparing Popular Project Templates](https://medium.com/better-programming/understanding-best-practice-python-tooling-by-comparing-popular-project-templates-6eba49229106)
