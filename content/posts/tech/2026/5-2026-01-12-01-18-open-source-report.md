Title: 2026/01/12 - 01/18 開源貢獻週報
Subtitle: 3.1.6 釋出當天， pycon-etl 就跟上了！
Date: 2026-01-18 22:45
Category: Tech
Tags: Open Source, 開源貢獻週報
Slug: 2026-01-12-01-18-open-source-report
Authors: Wei Lee

沒錯，這週二[[ANNOUNCE] Apache Airflow 3.1.6 Released](https://lists.apache.org/thread/07wrnk9p4hod0t74cdzmdobmy1dntql6)一發佈
我就發了 PR 給 pycon-etl ，並且第一時間部署上去了！

<!--more-->

之前升 3.1.0 那段時間太忙，有很多 SQLite 的問題沒有發現
之後就不敢怠慢
一有 Release Candidate，我就先丟去 pycon-etl 測試看看
雖然每次都是在本地測試，拖很久才想到要去部署......

## commitizen
* 審閱 PRs
    1. [docs: add commitizen-tools logo to our docs site #1786](https://github.com/commitizen-tools/commitizen/pull/1786)
    2. [feat(tags): enable version schemes with less than 3 components #1705](https://github.com/commitizen-tools/commitizen/pull/1705)
    3. [build: switch configuration file to .cz.toml #1794](https://github.com/commitizen-tools/commitizen/pull/1794)
    4. [docs(README): remove steps about manually setup a configuration file #1793](https://github.com/commitizen-tools/commitizen/pull/1793)
    5. [fix(config): ensure the actually used config file is correct, fix single config file being detected as duplicated, better test coverage #1784](https://github.com/commitizen-tools/commitizen/pull/1784)
    6. [test(cli): shorten no_raise tests #1796](https://github.com/commitizen-tools/commitizen/pull/1796)
    7. [build: fix mkdocs dev server hot reload failure issue #1801](https://github.com/commitizen-tools/commitizen/pull/1801)
    8. [test: remove unreachable code in pytest.raises block, fix some malformed tests, extract fixtures #1800](https://github.com/commitizen-tools/commitizen/pull/1800)
    9. [test(config): shorten config file factory tests #1804](https://github.com/commitizen-tools/commitizen/pull/1804)
    10. [test(version_schemes): replace match with strict string assertions #1805](https://github.com/commitizen-tools/commitizen/pull/1805)
    11. [test(check): shorten tests and dedup logic #1807](https://github.com/commitizen-tools/commitizen/pull/1807)
    12. [test(commit): extract fixtures to dedup logic in tests #1806](https://github.com/commitizen-tools/commitizen/pull/1806)
    13. [feat(prek): supporting prek as an alternative to pre-commit and switching to prek#1799](https://github.com/commitizen-tools/commitizen/pull/1799)
* 分類 Issues
    1. [BREAKING: Add --version back and deprecate cz version --comitizen which is the default for cz version #1785](https://github.com/commitizen-tools/commitizen/issues/1785)
    2. [Discuss what we should do if there are multiple cz.* files #1702](https://github.com/commitizen-tools/commitizen/issues/1702)
    3. [Proposal: Using Prek instead of pre-commit #1797](https://github.com/commitizen-tools/commitizen/issues/1797)
* 開 Issues
    1. [cz command shows ExpectedExit Exception #1789](https://github.com/commitizen-tools/commitizen/issues/1789)
    2. [4.11.0 is missing on PyPI #1790](https://github.com/commitizen-tools/commitizen/issues/1790)

## commitizen-aciton
* 審閱 PR
    1. [feat: add --build-metadata option #107](https://github.com/commitizen-tools/commitizen-action/pull/107)

## setup-cz
* 審閱 PR
    1. [Feat/add git config #11](https://github.com/commitizen-tools/setup-cz/pull/11)

## commitizen_cz_template
* 審閱 PR
    1. [feat: update cz_template #7](https://github.com/commitizen-tools/commitizen_cz_template/pull/7)

## pycon-etl
* 開 PRs
    1. [build: upgrade airflow to 3.1.6 #191](https://github.com/pycontw/pycon-etl/pull/191)
    2. [build: relock dependencies #192](https://github.com/pycontw/pycon-etl/pull/192)
