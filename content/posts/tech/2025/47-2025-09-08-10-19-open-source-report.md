Title: 2025/09/08 - 10/19 開源貢獻週報
Subtitle: 時差爆擊
Date: 2025-10-22 21:10
Category: Tech
Tags: Open Source, 開源貢獻週報
Slug: 2025-09-08-10-19-open-source-report
Authors: Wei Lee

因為諸多研討會跟出差，中間出門了一陣子
加減還是有看一些 PR

<!--more-->

原本想說回來可以再看一些，但這次時差的影響真的比想像中的大
光是要抓回生活的節奏就花了不少時間
開始煮飯跟開始打拳真的是抓回節奏的第一步

除此之外也因為一些事，更理解了資深開源貢獻者們在各種事情的處理態度
不過我實在是沒體力寫小論文，所以就走了另一條
畢竟這是場馬拉松（至少我是這麼希望的）
自身的身心健康還是更為重要，這樣才能走得長久

## commitizen-tools
* 分類 issues
    1. [Allow amend! prefix #1586](https://github.com/commitizen-tools/commitizen/issues/1586)
    2. [Add issue forms of performance improvement, test, refactoring, etc. #1628](https://github.com/commitizen-tools/commitizen/issues/1628)
    3. 合併 [Allow partial customization of Conventional Commits: add/remove change types and extend configuration options #1588](https://github.com/commitizen-tools/commitizen/issues/1588) 到 [Deprecate cz_customize #1385](https://github.com/commitizen-tools/commitizen/issues/1385)
* 發布
    * 開 [Release 4.9.0 #1589](https://github.com/commitizen-tools/commitizen/pull/1589) 以發佈 [4.9.0](https://github.com/commitizen-tools/commitizen/releases/tag/v4.9.0) 然後撤銷（因為少了一個相依套件）
    * 修復 [Tag: Diverging master history breaking 4.9.1 detection with 'pre-commit autoupdate' #1602](https://github.com/commitizen-tools/commitizen/issues/1602)，並且發佈 [4.9.1](https://github.com/commitizen-tools/commitizen/releases/tag/v4.9.1)
* 審閱 PRs
    1. [test(Init): add type hint and rename variable #1603](https://github.com/commitizen-tools/commitizen/pull/1603)
    2. [refactor(BaseCommitizen): construct Style object directly to get rid … #1607](https://github.com/commitizen-tools/commitizen/pull/1607)
    3. [refactor(BaseCommitizen): remove NotImplementedError and make them ab… #1608](https://github.com/commitizen-tools/commitizen/pull/1608)
    4. [refactor(Init): make project_info a module and remove self.project_info #1605](https://github.com/commitizen-tools/commitizen/pull/1605)
    5. [style(UvProvider): fix typo in comment #1611](https://github.com/commitizen-tools/commitizen/pull/1611)
    6. [feat: allow amend! prefix as created by git --fixup=reword:<commit> #1587](https://github.com/commitizen-tools/commitizen/pull/1587)
    7. [fix(Init): raise InitFailedError on keyboard interrupt on pre-commit … #1604](https://github.com/commitizen-tools/commitizen/pull/1604)
    8. [docs: enable blank issue and add url to contact links #1627](https://github.com/commitizen-tools/commitizen/pull/1627)
    9. [refactor(ConventionalCommitsCz): rewrite message method to make the p… #1626](github.com/commitizen-tools/commitizen/pull/1626)
    10. [test: rename the fixture config to mock_config for better code search #1619](https://github.com/commitizen-tools/commitizen/pull/1619)
    11. [test(utils): do not create file for simplicity #1621](https://github.com/commitizen-tools/commitizen/pull/1621)
    12. [test(changelog): remove unused timer fixture #1624](https://github.com/commitizen-tools/commitizen/pull/1624)
    13. [refactor(Bump): remove use of getattr #1622](https://github.com/commitizen-tools/commitizen/pull/1622)
    14. [refactor(cmd): unnest try except #1629](https://github.com/commitizen-tools/commitizen/pull/1629)

## jordanbaird/Ice
* 加入 [[Bug]: \<MacOS Tahoe app crashes\> #647](https://github.com/jordanbaird/Ice/issues/647) 討論
