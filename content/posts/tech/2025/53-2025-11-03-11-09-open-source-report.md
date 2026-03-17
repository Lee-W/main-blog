Title: 2025/11/03 - 11/09 開源貢獻週報
Subtitle: commitizen v4.10.0 即將發佈！
Date: 2025-11-08 22:55 +0800
Category: Tech
Tags: Open Source, 開源貢獻週報
Slug: 2025-11-03-11-09-open-source-report
Authors: Wei Lee

下週一準備來發佈 commitizen `v4.10.0`
有興趣的可以 git checkout 到 `v4-10-0` 的分支玩玩看

<!--more-->

因為明天要出門聽音樂會，大概不會有貢獻了
就先提早發這次的週報
一口氣看這麼多 commitizen 的 PRs 真的好吃力 😫
但我把現存 PR 的數量減少了一半 💪

## commitizen-tools
* 審閱 PRs
    1. [test(cz_customize): add missing YAML configuration file tests #1516](https://github.com/commitizen-tools/commitizen/pull/1516)
    2. [feat(conventional_commits): Add exclamation on commit title for breaking change #1576](https://github.com/commitizen-tools/commitizen/pull/1576)
    3. [feat: add config option for line length warning #1574](https://github.com/commitizen-tools/commitizen/pull/1574)
    4. [refactor(bump): cleanup related to update_version_file #1594](https://github.com/commitizen-tools/commitizen/pull/1594)
    5. [refactor(cargo_provider): cleanup and get rid of potential type errors #1599](https://github.com/commitizen-tools/commitizen/pull/1599)
    6. [refactor(BaseConfig): update set_key comments and type annotation, remove duplicated docstring #1600](https://github.com/commitizen-tools/commitizen/pull/1600)
    7. [refactor(BaseConfig): update docstring, extract factory method and remove unnecessary variable assignment #1601](https://github.com/commitizen-tools/commitizen/pull/1601)
    8. [refactor(RestructuredTest): rename variable, fix typo and remove unnecessary string copy #1609](https://github.com/commitizen-tools/commitizen/pull/1609)
    9. [docs(Check): add missing raise exception in __call__ #1616](https://github.com/commitizen-tools/commitizen/pull/1616)
    10. [refactor: remove unnecessary class member tag_format #1617](https://github.com/commitizen-tools/commitizen/pull/1617)
    11. [refactor: remove self.encoding for better maintainability #1618](https://github.com/commitizen-tools/commitizen/pull/1618)
    12. [test: rename the fixture config to mock_config for better code search #1619](https://github.com/commitizen-tools/commitizen/pull/1619)
    13. [refactor(BaseFormat): merge ChangelogFormat into BaseFormat #1612](https://github.com/commitizen-tools/commitizen/pull/1612)
    14. [refactor(utils): make get_backup_file_path to return a path for semantic correctness #1634](https://github.com/commitizen-tools/commitizen/pull/1634)
    15. [refactor(hooks): refactor to improve readability #1633](https://github.com/commitizen-tools/commitizen/pull/1633)
    16. [refactor(Commit): refactor _prompt_commit_questions and fix some type hint #1632](https://github.com/commitizen-tools/commitizen/pull/1632)
    17. [refactor(Bump): remove use of getattr #1622](https://github.com/commitizen-tools/commitizen/pull/1622)
    18. [Feat/version info #1639](https://github.com/commitizen-tools/commitizen/pull/1639)
    19. [test(SemVer): refine tests and remove unnecessary tests which test the behavior of library #1598](https://github.com/commitizen-tools/commitizen/pull/1598)
* 開 PRs
    1. [4.10.0 release #1641](https://github.com/commitizen-tools/commitizen/pull/1641)： 準備 `v4.10.0` 的發佈，下週一就來發佈吧！
    2. [Enable Ruff S101 - Checks for uses of the assert keyword. #1642](https://github.com/commitizen-tools/commitizen/pull/1642)： 沒想到我們生產環境竟然有 assert ，嚇壞我了

## pycon-etl
* 開草稿 PR [build: upgrade airflow to 3.1.2 #187](https://github.com/pycontw/pycon-etl/pull/187)
    * 資料庫升級又遇到問題了，看起來又是 sqlite 的外鍵問題 😭
