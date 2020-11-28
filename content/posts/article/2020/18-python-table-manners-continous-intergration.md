Title: Python Table Manners - 持續整合
Date: 2020-03-04 00:00
Category: Tech
Tags: Python. Code Quality
Slug: python-table-manner-continuous-integration
Authors: Lee-W
Status: draft
Series: Python Table Manner

## 持續整合（Continuous integration)
在我使用 [GitHub Actions](https://github.com/actions) 前有用過 [drone](https://github.com/drone/drone)
但既然都是放在 GitHub 上的開源專案了，就來玩玩看 GitHub Action 吧


https://github.com/pycontw/pycontw-postevent-report-generator/tree/ae6b60c8f2aa494217cd0f09fba01d312f737639/.github/workflows

三個 workflow

有人 push
就做檢查
python-check.yaml

merge master 時執行


publish 到 PyPI 上
python-publish.yaml



## Reference
[Python in GitHub Actions](https://hynek.me/articles/python-github-actions/)


---
快速的紀錄一下

在 pypi 上的 pypi-token 需要 ""

e.g. 你的 pypi-thisisrandomestringrepresentingyourapitoken
那你要在 secret 上丟 "pypi-thisisrandomestringrepresentingyourapitoken" 而不是 pypi-thisisrandomestringrepresentingyourapitoken
