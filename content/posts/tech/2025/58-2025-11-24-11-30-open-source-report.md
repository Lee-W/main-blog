Title: 2025/11/24 - 11/30 開源貢獻週報
Subtitle: 這週是開源音樂的回合
Date: 2025-11-30 16:30
Category: Tech
Tags: Open Source, 開源貢獻週報
Slug: 2025-11-24-11-30-open-source-report
Authors: Wei Lee

準備要出門去聽 OCF 舉辦的 [Mong Tong × XTRUX《明日音》專場](https://ocf.tw/story/epaper/2025/202510news/main/)

<!--more-->

雖然不是很懂，但畢竟是 OCF 舉辦的，就來支持一下

昨天去聽 [BanG Cover！夢想連彈](https://go.fansi.me/events/170086) 真的很快樂
姑且也算是跟開源相關（？）
畢竟是在聽強者我朋友的演講 [從 User 到 Contributor，如何開啟你的第一個 Open Source PR](https://www.youtube.com/watch?v=dEEF86opHiY) 被推坑的

## commitizen

* 審閱 PRs
    1. [docs(exit-codes): general update and add docstring to exceptions.py#1662](https://github.com/commitizen-tools/commitizen/pull/1662)
    2. [docs(third-party): separate providers and template docs#1664](https://github.com/commitizen-tools/commitizen/pull/1664)
    3. [test: replace try with pytest.raises #1654](https://github.com/commitizen-tools/commitizen/pull/1654)
    4. [docs(faq): minor updates in FAQ and make features won't add a separate page #1668](https://github.com/commitizen-tools/commitizen/pull/1668)
    5. [feat: add custom validation#1236](https://github.com/commitizen-tools/commitizen/pull/1236)
    6. [fix(version): fix the behavior of cz version --major #1673](https://github.com/commitizen-tools/commitizen/pull/1673)
    7. [refactor(cargo_provider): cleanup and get rid of potential type errors #1599](https://github.com/commitizen-tools/commitizen/pull/1599)
    8. [docs: add more issue forms #1671](https://github.com/commitizen-tools/commitizen/pull/1657)
    9. [docs(bump): add missing --allow-no-commit behaviors and other minor d… #1656](https://github.com/commitizen-tools/commitizen/pull/1656)
    10. [docs(config): split the configuration documentation into pages #1657](https://github.com/commitizen-tools/commitizen/pull/1657)
* 分類 issues
    1. [reorg customize.md #1663](https://github.com/commitizen-tools/commitizen/issues/1663)
    2. [--config is not documented explicitly #1669](https://github.com/commitizen-tools/commitizen/issues/1669)
    3. [Use ChainMap to rewrite the cmd options <- configuration file <- default configuration chain #1672](https://github.com/commitizen-tools/commitizen/issues/1672)
    4. [Not possible to use --get-next when changelog is enabled #1640](https://github.com/commitizen-tools/commitizen/issues/1640)
    5. [Shared cross-repository configuration for commitizen #434](https://github.com/commitizen-tools/commitizen/issues/434)
    6. [Bumping rule is wrongly documented  #515](https://github.com/commitizen-tools/commitizen/issues/515)
* 開啟 issue
    1. [Separate version providers from core #1676](https://github.com/commitizen-tools/commitizen/issues/1676)
* 加入 issues 討論
    1. [Check unknown config in configuration file #300](https://github.com/commitizen-tools/commitizen/issues/300)
    2. [Deprecate the cz_customize convention and allow for overriding functionality #1385](https://github.com/commitizen-tools/commitizen/issues/1385)
* 加入 GitHub Discussions 討論
    1. [Clarify when ExpectedExit should be used #1675](https://github.com/commitizen-tools/commitizen/discussions/1675)
* 修正 PR [feat: Drop support for Python 3.9 as EOL reached and add Python 3.14 support #1648](https://github.com/commitizen-tools/commitizen/pull/1648) 上的合併衝突
