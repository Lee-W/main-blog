Title: 2026/02/02 - 02/08 開源貢獻週報
Subtitle: pycon-etl 又一次即時更新到最新版 Airflow
Date: 2026-02-08 22:20
Category: Tech
Tags: Open Source, 開源貢獻週報
Slug: 2026-02-02-02-08-open-source-report
Authors: Wei Lee

上週沒特別發一篇週報，但整週的貢獻都寫在 [scisprint Taipei 2026 January]({filename}/posts/tech/2026/7-scisprint-taipei-2026-january.md) 了

<!--more-->

## commitizen
上週 scisprint 才發佈 [v4.13.0](https://github.com/commitizen-tools/commitizen/releases/tag/v4.13.0)，這週就已經有 [v4.13.6](https://github.com/commitizen-tools/commitizen/releases/tag/v4.13.6)

* 審閱 PRs
    1. [refactor(init): replace self.config.settings with DEFAULT_SETTINGS #1832](https://github.com/commitizen-tools/commitizen/pull/1832)
    2. [test(changelog): add forgotten f in f-strings #1834](https://github.com/commitizen-tools/commitizen/pull/1834)
    3. [test: enable ruff rule PT #1837](https://github.com/commitizen-tools/commitizen/pull/1837)
    4. [test(test_cmd): minor refactoring tests #1833](https://github.com/commitizen-tools/commitizen/pull/1833)
    5. [test(init): cover cz without descriptions #1829](https://github.com/commitizen-tools/commitizen/pull/1829)
    6. [test: remove duplicated chdir fixture #1844](https://github.com/commitizen-tools/commitizen/pull/1844)
    7. [ci(gen_cli_help_screenshots): refactor the script and add some TODOs #1845](https://github.com/commitizen-tools/commitizen/pull/1845)
    8. [test: use pathlib utilities in tests #1843](https://github.com/commitizen-tools/commitizen/pull/1843)
    9. [fix(pre-commit-hooks): correct rev-range syntax in commitizen-branch #1841](https://github.com/commitizen-tools/commitizen/pull/1841)
    10. [fix(cargo_provider): support workspace virtual manifests #1733](https://github.com/commitizen-tools/commitizen/pull/1733)
    11. [fix(changelog): add incremental parameter to changelog generation #1808](https://github.com/commitizen-tools/commitizen/pull/1808)
    12. [test(test_deprecated): use pytest.mark.parametrize #1851](https://github.com/commitizen-tools/commitizen/pull/1851)
    13. [test: add deprecated test back #1852](https://github.com/commitizen-tools/commitizen/pull/1852)
    14. [fix(commands/bump): prevent using incremental changelog when it is set to false in config#996](https://github.com/commitizen-tools/commitizen/pull/996)
* 參與 issue 討論
    1. [Add option for body line length #1597](https://github.com/commitizen-tools/commitizen/issues/1597)
    2. [Discuss cz init self.config #1831](https://github.com/commitizen-tools/commitizen/issues/1831)
    3. [Make BaseConfig an abstract class #1847](https://github.com/commitizen-tools/commitizen/issues/1847)

## pycon-etl
* 審閱 PR
    1. [build: replace Makefile with poe #193](https://github.com/pycontw/pycon-etl/pull/193)
* 開 PR [build: upgrade airflow to 3.1.7 #194](https://github.com/pycontw/pycon-etl/pull/194) 並部署

這次一樣是 Ephraim 一發佈完，當晚我就直接更新到 3.1.7 了
[[ACCELERATED VOTE] Release Airflow 3.1.7 from 3.1.7rc2 & Task SDK 1.1.7 from 1.1.7rc2](https://lists.apache.org/thread/qbv53ol7pj5t19o6c16mwq7ovxlcsdbm)
