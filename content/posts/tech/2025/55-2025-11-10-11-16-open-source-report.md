Title: 2025/11/10 - 11/16 開源貢獻週報
Subtitle: 這週的 commitizen 是發 PR 的回合
Date: 2025-11-17 09:40 +0800
Category: Tech
Tags: Open Source, 開源貢獻週報
Slug: 2025-11-10-11-16-open-source-report
Authors: Wei Lee

上週主要專注在看 commitizen 的 PRs
這週就順手發了幾隻小 PRs

<!--more-->

## commitizen
* 分類 issues
    1. [[refactor] separate option validation in bump #1643](https://github.com/commitizen-tools/commitizen/issues/1643)
    2. [Not possible to use --get-next when changelog is enabled #1640](https://github.com/commitizen-tools/commitizen/issues/1640)
* 審閱 PRs
    1. [fix(bump): remove NotAllowed related to --get-next option, and other related refactoring #1645](https://github.com/commitizen-tools/commitizen/pull/1645)
    2. [test(changelog): cover incremental_build #1595](https://github.com/commitizen-tools/commitizen/pull/1595)
    3. [fix(bump): extract option validation and new version resolution #1646](https://github.com/commitizen-tools/commitizen/pull/1646)
* 發佈 [v4.10.0](https://github.com/commitizen-tools/commitizen/releases/tag/v4.10.0)
* 開 PRs
    1. [build(pyproject.toml): update dev group spec from poetry style to PEP 735 style #1647](https://github.com/commitizen-tools/commitizen/pull/1647)
    2. [feat: Drop support for Python 3.9 as EOL reached and add Python 3.14 support #1648](https://github.com/commitizen-tools/commitizen/pull/1648)
    3. [ci(github-actions): add python 3.14 to github-actions and tox #1649](https://github.com/commitizen-tools/commitizen/pull/1649)

## commitizen-actions
* 審閱 PR
    * [feat: add more output information #103](https://github.com/commitizen-tools/commitizen-action/pull/103)
        * 看的時候我還不小心以為是 commitizen 本身，這邊實在太少更新了...

## pycon-etl
* 分類 issue
    1. 關閉 [[Bug Report] poetry installing flask-openid (1.2.5): Failed #67](https://github.com/pycontw/pycon-etl/issues/67)
* 開啟 issue [[Feature Request] Auto-Check Dockerfile and pyproject.toml inconsistency #188](https://github.com/pycontw/pycon-etl/issues/188)
* 開 PR [build: upgrade airflow to 3.1.3 #187](https://github.com/pycontw/pycon-etl/pull/187)
    * 週六 Airflow 發佈 3.1.3 ([[ANNOUNCE] Apache Airflow 3.1.3 Released](https://lists.apache.org/thread/mhz6w5gj5o45x0jbm4qpjq34f7h0yy20))，週日就完成 3.1.3 的更新和部署 💪
        * 恩...雖然這個 PR 原本是要升到 3.1.2 ，拖太久一直沒部署，就乾脆直上 3.1.3
