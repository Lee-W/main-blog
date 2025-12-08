Title: 2025/12/01 - 12/07 開源貢獻週報
Subtitle: 恭喜熊老師成為 commitizen 維護者
Date: 2025-12-08 21:20
Category: Tech
Tags: Open Source, 開源貢獻週報
Slug: 2025-12-01-12-07-open-source-report
Authors: Wei Lee

總之，先恭喜熊老師成為 commitizen 的維護者
之前在 Sciwork 總是被問，為什麼沒有其他台灣人一起來玩 commmitizen
這不是來了嗎

<!--more-->

雖然不是很重要，但最近也想整理一下我用的 pelican 主題 [attila](https://github.com/Lee-W/attila/)
原作者好像沒在維護了，我剛把 main 分支整理好
之後再把我的功能慢慢的加回到我新的 main 分支，並加上版號

## commitizen
* 審閱 PRs
    1. [feat: add custom validation #1236](https://github.com/commitizen-tools/commitizen/pull/1236)
    2. [test: replace try with pytest.raises #1654](https://github.com/commitizen-tools/commitizen/pull/1654)
    3. [docs(faq): minor updates in FAQ and make features won't add a separate page #1668](https://github.com/commitizen-tools/commitizen/pull/1668)
    4. [docs(pyproject): update maintainers list #1681](https://github.com/commitizen-tools/commitizen/pull/1681)
    5. [ci(deps): bump dawidd6/action-homebrew-bump-formula from 6 to 7 #1689](https://github.com/commitizen-tools/commitizen/pull/1689)
    6. [refactor(cli): separate parser data and main function logic #1670](https://github.com/commitizen-tools/commitizen/pull/1670)
    7. [fix(git): replace lstrip with strip for compatibility issue #1685](https://github.com/commitizen-tools/commitizen/pull/1685)
    8. [perf: add TYPE_CHECKING to CzQuestion imports #1682](https://github.com/commitizen-tools/commitizen/pull/1682)
    9. [docs(contributing): fix broken link#1684](https://github.com/commitizen-tools/commitizen/pull/1684/)
    10. [perf(ruff): enable ruff rules TC001~TC006 #1692](https://github.com/commitizen-tools/commitizen/pull/1692)
    11. [docs(check): rewrite command document #1693](https://github.com/commitizen-tools/commitizen/pull/1693)
* 分類 issues 或加入討論
    1. [Add support for cz version <version_arg> #1679](https://github.com/commitizen-tools/commitizen/issues/1679)
    2. [Introduce --next flag on cz version --project #1678](https://github.com/commitizen-tools/commitizen/issues/1678)
    3. [Add new capabilities to cz version #1677](https://github.com/commitizen-tools/commitizen/issues/1677)
    4. [ease the setup of prepare-commit-msg hook #1355](https://github.com/commitizen-tools/commitizen/issues/1355)
    5. [Deprecate the cz_customize convention and allow for overriding functionality #1385](https://github.com/commitizen-tools/commitizen/issues/1385)
    6. [Add option for body line length #1597](https://github.com/commitizen-tools/commitizen/issues/1597)
    7. [Enable ruff rule TC001~TC005 #1690](https://github.com/commitizen-tools/commitizen/issues/1690)
    8. [Allow package.json to be located in subdirectories by processing paths #1379](https://github.com/commitizen-tools/commitizen/issues/1379)
    9. [Add new capabilities to cz version #1677](https://github.com/commitizen-tools/commitizen/issues/1677)
    10. [Automate check for commitizen document broken links #1691](https://github.com/commitizen-tools/commitizen/issues/1691)
    11. [Skip python package workflow when there is only documentation change #1697](https://github.com/commitizen-tools/commitizen/issues/1697)
    12. [cz bump --yes is not documented #1698](https://github.com/commitizen-tools/commitizen/issues/1698)
* 修正 PR [feat: Drop support for Python 3.9 as EOL reached and add Python 3.14 support #1648](https://github.com/commitizen-tools/commitizen/pull/1648) 上的合併衝突

## infrastructure-asfquart
* 審閱 PR [Use uv as the unified project manager #38](https://github.com/apache/infrastructure-asfquart/pull/38)
    * 在源來適你社群看到有興趣的 issue，雖然被接走了，但還是順手幫忙看一下

## pycon-etl
* 草擬 PR [build: upgrade airflow to 3.1.4 #189](https://github.com/pycontw/pycon-etl/pull/189)
    * 上週 Apache Airflow 準備釋出 3.1.4。順手就拿 3.1.4rc1 測試了一下，之前升到 3.1.3 遇到的錯誤都已經被我修正。但好像權杖 (token) 有點問題，還要再等 3.1.4rc2
