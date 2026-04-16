Title: 2025/05/19 - 05/25 開源貢獻週報
Subtitle: 你跟得上嗎？
Date: 2025-05-25 23:15 +0800
Category: Tech
Tags: Open Source, 開源貢獻週報
Slug: 2025-05-19-05-25-open-source-report
Cover: /images/meme/fate-emiya-can-you-keep-up.png
Authors: Wei Lee
Lang: zh-tw

你問我跟得上嗎？你才得給我跟上！

<!--more-->

本想這麼說的，然後這時候 BGM 在下一首 Emiya

<iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/6GKxOE9OBLLnaLF1uQP29V?utm_source=generator" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>

但 Tim 大大的 PR 實在太多了
真的跟不上 🥲

## Commitizen
* Review
    1. [docs: improve clarity of docs and fix typo/grammar issues #1404](https://github.com/commitizen-tools/commitizen/pull/1404)
        * 我沒辦法 merge ， Axel 有要求改動
    2. [refactor(customize): improve code readability #1412](https://github.com/commitizen-tools/commitizen/pull/1412)
    3. [refactor(git): code cleanup and test coverage #1417](https://github.com/commitizen-tools/commitizen/pull/1417)
    4. [refactor(bump): code cleanup and better test coverage #1422](https://github.com/commitizen-tools/commitizen/pull/1422)
    5. [test(changelog): code cleanup and better type #1423](https://github.com/commitizen-tools/commitizen/pull/1423)
    6. [refactor(commit): simplify call #1426](https://github.com/commitizen-tools/commitizen/pull/1426)
    7. [refactor(check): code cleanup #1427](https://github.com/commitizen-tools/commitizen/pull/1427)
    8. [refactor(bump): add type for out, replace function with re escape #1429](https://github.com/commitizen-tools/commitizen/pull/1429)
    9. [refactor(version_scheme): cleanup #1430](https://github.com/commitizen-tools/commitizen/pull/1430)
    10. [docs(ISSUE_TEMPLATE): correct labels #1436](https://github.com/commitizen-tools/commitizen/pull/1436)
    11. [docs(label_issues): add logics for adding os related labels #1437](https://github.com/commitizen-tools/commitizen/pull/1437)
    12. [docs(bug_report): add fallback command if cz version --report is not available #1438](https://github.com/commitizen-tools/commitizen/pull/1438)
    13. [refactor(git): extract _create_commit_cmd_string, better test coverage #1442](https://github.com/commitizen-tools/commitizen/pull/1442)
    14. [refactor(changelog): minor cleanup #1443](https://github.com/commitizen-tools/commitizen/pull/1443)
    15. [refactor(BaseConfig): update function name, upgrade mypy version #1444](https://github.com/commitizen-tools/commitizen/pull/1444)
    16. [fix(defaults): add non-capitalized default constants back and deprecated warning #1447](https://github.com/commitizen-tools/commitizen/pull/1447)
    17. [docs(label_pr.yml): add labels based on new PR title #1448](https://github.com/commitizen-tools/commitizen/pull/1448)
    18. [build(termcolor): remove termcolor <3 restriction](https://github.com/commitizen-tools/commitizen/pull/1450)
    19. [refactor(changelog): better typing, yield #1453](https://github.com/commitizen-tools/commitizen/pull/1453)
    20. [docs(taplo): add toml formatter #1456](https://github.com/commitizen-tools/commitizen/pull/1456/)
* Close issue
    1. [Version 4.7.2 breaks cz_github_jira_conventional because of missing defaults.bump_pattern #1435](https://github.com/commitizen-tools/commitizen/issues/1435)
    2. [tag message for annotated_tag option #558](https://github.com/commitizen-tools/commitizen/issues/558)
    3. [pre-commit fail even if the problem is fixed automatically #1434](https://github.com/commitizen-tools/commitizen/issues/1434)
* Create issue
    * [Redesign how configuration, flag, and default are handled #1445](https://github.com/commitizen-tools/commitizen/issues/1445)
    * [Clarify what's a breaking change in commitizen #1446](https://github.com/commitizen-tools/commitizen/issues/1446)
* Create PR
    1. [4.8.3 candidate #1457](https://github.com/commitizen-tools/commitizen/pull/1457)
        * 其實這個只是把 Tim 大的十幾個 PR 先 merge 進來的 branch ，裡面沒有一行 code 是我寫的

## opensource4you/readme
* Create PR
    1. [Add Jason as Apache Airflow mentor #8](https://github.com/opensource4you/readme/pull/8)
        * 畢竟 Jason 大大都當上 committer 這麼久了，應該要被掛名主要 mentor 了吧

## pycon-etl
* Create PR
    1. [Upgrade to airflow 2 #158](https://github.com/pycontw/pycon-etl/pull/158)
        * 終於至少是先把 PR 開出來了，還有許多問題要解，但升到 2.11 應該不是太大的問題
        * 升到 3.0 應該會是下一個 PR ，有一兩個 clean up 用的 dag 會需要重寫，其他看起來應該是...不會有太大的問題...吧
