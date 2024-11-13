Title: Python Table Manners
Subtitle: 2024/25 edition 製作確定
Date: 2024-11-13 23:00
Category: Tech
Tags: Python
Slug: python-table-manners-series-2024-2025-edition
Authors: Wei Lee
Series: Python Table Manners 2024/25 edition

雖然也是有動畫作品 2017 宣布劇場版製作確定
到了 2024 年就確定不製作了 🤔

<!--more-->

之前就有想重新整理一下
畢竟很多在 2020 年 [Python Table Manners 系列]({filename}/posts/tech/2020/04-python-table-manners-series.md) 寫的工具
有些我也沒在用了，不然就是用的方式不同了

最近有朋友不知道去哪翻到我的舊文
發了一篇推薦
稍微給了我一點想要重新整理的動力

![share](/images/posts-image/2024-python-table-manners/share.png)

另外就是發現 cookicutter 在我沒注意的期間也加了不少酷酷的功能
看到新功能就想玩一下

整個系列還是會圍繞在我的 Python 專案模板 [cookiecutter-python-template](https://github.com/Lee-W/cookiecutter-python-template/) 用到的工具
最大的改動可能是 [uv](https://docs.astral.sh/uv/) 跟 [ruff](https://docs.astral.sh/ruff/) 吧
其它大概就是從 Airflow ~~抄~~ 學來的一些 best practices

目前已經有兩個完成的 PRs

* [Replace project root poetry with uv #229](https://github.com/Lee-W/cookiecutter-python-template/pull/229)
* [Add markdownlint and spell check #230](https://github.com/Lee-W/cookiecutter-python-template/pull/230)

還開了一個 GitHub project [cookiecutter-python-template v2](https://github.com/users/Lee-W/projects/1/views/1?layout=board) 跟幾個初期的 issues

* [Investigate cookiecutter nested configuration #233](https://github.com/Lee-W/cookiecutter-python-template/issues/233)
* [Add Dependency Group Support #231](https://github.com/Lee-W/cookiecutter-python-template/issues/231)
* [Add uv support for managing dependency and virtual env #232](https://github.com/Lee-W/cookiecutter-python-template/issues/232)
* [Enhance prompt through Human readable prompts #234](https://github.com/Lee-W/cookiecutter-python-template/issues/234)

希望我不會做著做著就確定不製作了
