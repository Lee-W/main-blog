Title: 2025/11/17 - 11/23 開源貢獻週報
Subtitle: commitizen-tools 的新子專案 setup-cz!
Date: 2025-11-24 08:50
Category: Tech
Tags: Open Source, 開源貢獻週報
Slug: 2025-11-17-11-23-open-source-report
Authors: Wei Lee

commitizen 作者 Santi 強勢回歸
推出 commitizen 的新 GitHub Action [setup-cz](https://github.com/commitizen-tools/setup-cz/)
讓大家可以更有彈性的使用 commitizen!

<!--more-->

其實順手有修了幾個部落格們的 [action/checkout](https://github.com/actions/checkout) 跟 submodules 相關的問題
但太細了，有點懶得謝進來

## commitizen
* 審閱 PRs
    1. [fix(bump): extract option validation and new version resolution #1646](https://github.com/commitizen-tools/commitizen/pull/1646)
    2. [docs(Bump): wording consistency #1650](https://github.com/commitizen-tools/commitizen/pull/1646)
    3. [docs(bump): add example to version file #1651](https://github.com/commitizen-tools/commitizen/pull/1651)
    4. [refactor(bump): rename parameter and variables #1652](https://github.com/commitizen-tools/commitizen/pull/1652)
    5. [docs(bump): general documentation update #1653](https://github.com/commitizen-tools/commitizen/pull/1653)
    6. [fix(bump): remove NotAllowed related to --get-next option, and other related refactoring#1645](https://github.com/commitizen-tools/commitizen/pull/1645#pullrequestreview-3480554629)
    7. [feat: add custom validation #1236](https://github.com/commitizen-tools/commitizen/pull/1236)
    8. [test: replace try with pytest.raises #1654](https://github.com/commitizen-tools/commitizen/pull/1654)
    9. [docs(bump): check consistency warning minor update#1655](https://github.com/commitizen-tools/commitizen/pull/1655/)
    10. [docs(bump): add missing --allow-no-commit behaviors and other minor d… #1656](https://github.com/commitizen-tools/commitizen/pull/1656)
    11. [docs(config): split the configuration documentation into pages #1657](https://github.com/commitizen-tools/commitizen/pull/1657)
    12. [feat(bump): add --version-files-only and deprecate --files-only #1659](https://github.com/commitizen-tools/commitizen/pull/1659)
    13. [docs(third-party): separate providers and template docs #1664](https://github.com/commitizen-tools/commitizen/pull/1664)
    14. [ci(deps): bump dawidd6/action-homebrew-bump-formula from 5 to 6#1665](https://github.com/commitizen-tools/commitizen/pull/1665)
    15. [ci(deps): bump actions/checkout from 5 to 6 #1666](https://github.com/commitizen-tools/commitizen/pull/1666)
    16. [docs: add more issue forms#1671](https://github.com/commitizen-tools/commitizen/pull/1671)
* 分類 issue
    1. [Not possible to use --get-next when changelog is enabled #1640](https://github.com/commitizen-tools/commitizen/issues/1640)
    2. [[refactor] separate option validation in bump #1643](https://github.com/commitizen-tools/commitizen/issues/1643)
    3. [Rename the option cz bump --files-only to --version-files-only #1658](https://github.com/commitizen-tools/commitizen/issues/1658)
    4. [Review Exit codes before v5 release (if possible) #1661](https://github.com/commitizen-tools/commitizen/issues/1661)
    5. [change_type_order is not documented #1663](https://github.com/commitizen-tools/commitizen/issues/1663)
    6. [docs(exit-codes): general update and add docstring to exceptions.py #1662](https://github.com/commitizen-tools/commitizen/pull/1662)
    7. [Use ChainMap to rewrite the cmd options <- configuration file <- default configuration chain #1672](https://github.com/commitizen-tools/commitizen/issues/1672)
* 開 PR [docs(external_links): fix outdated link and add links to another commitizen talk #1667](https://github.com/commitizen-tools/commitizen/pull/1667)

## setup-cz
* [feat(ci): introduce new setup-cz action #1](https://github.com/commitizen-tools/setup-cz/pull/1)
