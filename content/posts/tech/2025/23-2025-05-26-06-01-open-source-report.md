Title: 2025/05/26 - 06/01 開源貢獻週報
Subtitle: 無心插柳柳橙汁
Date: 2025-06-04 09:50
Category: Tech
Tags: Open Source, 開源貢獻週報
Slug: 2025-05-26-06-01-open-source-report
Authors: Wei Lee

commitizen 終於不用寄生在 airflow 的頻道
而是有自己獨立的頻道啦！

<!--more-->

![commitizen-channel-annoucement](/images/posts-image/2025-open-source-report/commitizen-channel-annoucement.jpg)

MyGO!!!!! 怎麼可能是浪費時間呢
是心靈的饗宴

倒是我也被發現在 [sciwork] 有一席之地

![sciwork-commitizen-channel-found](/images/posts-image/2025-open-source-report/sciwork-commitizen-channel-found.jpg)

不過我其實很潛水
大多都是被邀請去參加活動的時候，我會回一下我沒辦法去
我也沒有不想去，但我就...真的大多數被找的時間都不在
不然就是真的沒精力了...

## commitizen

* Review PRs
    1. [refactor(changelog): cleanup and add test cases #1425](https://github.com/commitizen-tools/commitizen/pull/1425)
    2. [refactor: misc cleanup #1428](https://github.com/commitizen-tools/commitizen/pull/1428/files)
    3. [refactor(git): extract _create_commit_cmd_string, better test coverage #1442](https://github.com/commitizen-tools/commitizen/pull/1442/files)
    4. [refactor(cli): early return and improve test coverage #1449](https://github.com/commitizen-tools/commitizen/pull/1449)
    5. [refactor(changelog): better typing, yield #1453](https://github.com/commitizen-tools/commitizen/pull/1453)
    6. [docs: add installation and usage guide for cz-ai plugin leveraging GP… #1458](https://github.com/commitizen-tools/commitizen/pull/1458)
    7. [build(termcolor): remove termcolor <3 restriction #1450](https://github.com/commitizen-tools/commitizen/pull/1450)
    8. [docs(faq): add "features we won't add" section #1451](https://github.com/commitizen-tools/commitizen/pull/1451)
    9. [docs(bump): rewrite bump about section, fix incorrect version increment rules #1452](https://github.com/commitizen-tools/commitizen/pull/1452)
    10. [docs(init): rewrite commands init page #1461](https://github.com/commitizen-tools/commitizen/pull/1461)
    11. [docs(README): fix broken bullet points #1462](https://github.com/commitizen-tools/commitizen/pull/1462)
    12. [docs(commit): rewrite command commit page #1463](https://github.com/commitizen-tools/commitizen/pull/1463)
    13. [docs: correct case GitHub #1464](https://github.com/commitizen-tools/commitizen/pull/1464)
    14. [refactor(check): capitalize error message, rename variable #1470](https://github.com/commitizen-tools/commitizen/pull/1470)
    15. [refactor: some clean up #1471](https://github.com/commitizen-tools/commitizen/pull/1471)
    16. [refactor(cz): better typing and refactor message method #1472](https://github.com/commitizen-tools/commitizen/pull/1472)
    17. [Add type hints for cli.py#1479](https://github.com/commitizen-tools/commitizen/pull/1479)
    18. [build(deps-dev): bump mypy to 1.16.0 #1480](https://github.com/commitizen-tools/commitizen/pull/1480)
    19. [docs(contributing): improve documentation for first-time contributors #1486](https://github.com/commitizen-tools/commitizen/pull/1486)
    20. [docs(pull_request_template): add task to fix broken external links in the docs #1487](https://github.com/commitizen-tools/commitizen/pull/1487)
* Triage issues
    1. [Mention why we don't use pydantic in FAQ #1488](https://github.com/commitizen-tools/commitizen/issues/1488)
    2. [Support the latest version of Ruff #1474](https://github.com/commitizen-tools/commitizen/issues/1474)
    1. Close [[Feature Request] Respect --allow-empty flag #247](https://github.com/commitizen-tools/commitizen/issues/247)
    2. Close [Option to allow fixup! and squash! in commit messages #414](https://github.com/commitizen-tools/commitizen/issues/414)
    3. Close [commitizen v4 #1073](https://github.com/commitizen-tools/commitizen/issues/1073) in favor of  [Release commitizen v5 #1481](https://github.com/commitizen-tools/commitizen/issues/1481)

這週依然是滿滿的 commitizen
還蠻開心讓我初入開源的專案，到現在還在緩慢成長中
雖然緩慢是因為我們 PR 看得慢嗚嗚嗚

## pycon-etcl
這週除了 commitizen，我花了不少時間中於把 [Upgrade to Airflow 2.11.0 #158](https://github.com/pycontw/pycon-etl/pull/158/files) 整理完了！
只要等 Henry 看完這個 PR ，就可以部署上去試試看了
migration 的 patch 跟幾個可以玩的 dag 有試試看，目前看起來應該、可能、大概沒問題...吧
下一步就是要升上 Airflow 3 了！


[sciwork]: https://sciwork.dev/
