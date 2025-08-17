Title: 2025/08/11 - 08/17 開源貢獻週報
Subtitle: 難得準時
Date: 2025-08-17 14:50
Category: Tech
Tags: Open Source, 開源貢獻週報
Slug: 2025-08-11-08-17-open-source-report
Authors: Wei Lee

晚上要去電影院當鬼滅 Kids 了
出門前先來記錄一下

<!--more-->

## commitizen
* 審閱 PRs
    1. [refactor(Init): fix unbounded variable in _ask_tag_format #1529](https://github.com/commitizen-tools/commitizen/pull/1529)
    2. [fix(Init): fix a typo in _ask_version_provider options and remove unnecessary filter #1528](https://github.com/commitizen-tools/commitizen/pull/1528)
    3. [fix(ExitCode): add from_str in ExitCode and replace parse_no_raise with it, warn if the error code is not in range #1545](https://github.com/commitizen-tools/commitizen/pull/1545)
    4. [docs(config.md): fix format issue, add period and add title to example config code blocks #1534](https://github.com/commitizen-tools/commitizen/pull/1534)
    5. [fix(init): make welcome message easier to read #1524](https://github.com/commitizen-tools/commitizen/pull/1524)
    6. [refactor(Init): remove unnecessary methods from ProjectInfo and refactor _ask_tag, improve test coverage #1526](https://github.com/commitizen-tools/commitizen/pull/1526)
    7. [refactor(changelog): shorten generate_tree_from_commits and use set to check used tags #1540](https://github.com/commitizen-tools/commitizen/pull/1540)
    8. [refactor(Init): remove the variable values_to_add and the _update_config_file function for readability #1537](https://github.com/commitizen-tools/commitizen/pull/1537)
    9. [feat: add check against default branch #1519](https://github.com/commitizen-tools/commitizen/pull/1519)
    10. [Fix deprecated precommit #1569](https://github.com/commitizen-tools/commitizen/pull/1569)
* 分類 issues
    1. [Update tomlkit to allow empty keys in pyproject.toml #1573](https://github.com/commitizen-tools/commitizen/issues/1573)

## pycon-etl
* 開草稿 PR [build: upgrade airflow to 3.0.5rc2 #184](https://github.com/pycontw/pycon-etl/pull/184)
    * 3.0.4 的 PR 都還沒合併， 3.0.5rc 就釋出了，嚇得我快點 merge，然後開 3.0.5 的 PR，剛好測一下 [[VOTE] Release Airflow 3.0.5 from 3.0.5rc2 & Task SDK 1.0.5 from 1.0.5rc2](https://lists.apache.org/thread/f2g9nmgvwb0vodd3my756pbvl7741b90)
