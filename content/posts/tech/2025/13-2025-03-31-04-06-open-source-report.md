Title: 2025/03/31 - 04/06 開源貢獻週報
Date: 2025-04-07 09:45 +0800
Category: Tech
Tags: Open Source, 開源貢獻週報
Slug: 2025-03-31-04-06-open-source-report
Authors: Wei Lee

在 Airflow 即將邁入 3.0 之際， PyCon TW 維護的 Airflow 終於有望邁入 2.0 了！（咦？）

<!--more-->

## pycontw/reviewer-guidebook
* Review and merge [Add a brief explanation of the review guidelines #16](https://github.com/pycontw/reviewer-guidebook/pull/16)

## commitizen
* Wrap up and get [fix(commands/init): add missing uv provider to "cz init" #1378](https://github.com/commitizen-tools/commitizen/pull/1378) merged
* Triage issues
    1. [Allow bump calculate the next version from git log #1374](https://github.com/commitizen-tools/commitizen/issues/1374)
    2. [version_files not working #1382](https://github.com/commitizen-tools/commitizen/discussions/1382)
    3. [The --devrelease option in cz bump is not correctly incrementing the version #1367](https://github.com/commitizen-tools/commitizen/issues/1367)
* Review PRs
    1. [feat: filter search for commit change type #1381](https://github.com/commitizen-tools/commitizen/pull/1381)
    2. [fix: display invalid tag information #1375](https://github.com/commitizen-tools/commitizen/pull/1375)
* Close PR [Feature/multi language commitizen #1328](https://github.com/commitizen-tools/commitizen/pull/1328)
    * 這個要做的好感覺得花一點時間研究，但感覺原本送 PR 的人不會回來惹 🥲
* File issue [Make uv.lock optional bump #1383](https://github.com/commitizen-tools/commitizen/issues/1383)

## pycontw/pycon-etl
* 測試完 [Use uv as python, dependencies, virtual environment management tools #155](https://github.com/pycontw/pycon-etl/pull/155) 跟 [Remove default airflow cfg #156](https://github.com/pycontw/pycon-etl/pull/156) 並且 merge 它們
    * 感覺接下來還得花點時間把文件補齊，摸索大家部署的方式也花了我一點時間
