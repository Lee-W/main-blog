Title: 2025/06/09 - 06/15 開源貢獻週報
Subtitle: Airflow 3 PR 準備好了！
Date: 2025-06-17 12:30
Category: Tech
Tags: Open Source, 開源貢獻週報
Slug: 2025-06-09-06-15-open-source-report
Authors: Wei Lee

原本以為這週因為有 CPython Sprint 有機會開一個 PR
但我果然不會寫 Python 😞

<!--more-->

## commitizen
* 合併 [4.8.3 candidate #1457](https://github.com/commitizen-tools/commitizen/pull/1457) 並且釋出 [4.8.3](https://github.com/commitizen-tools/commitizen/releases/tag/v4.8.3)
* 開 PR
    1. 開 [ci(github-actions): set organization to true for JamesIves/github-sponsors-readme-action@v1 #1554](https://github.com/commitizen-tools/commitizen/pull/1554)
        * 這個 PR 解決了一些問題，這是個好消息，但還需要在一個 PR 才能把問題完全解決掉
* 審閱 PRs
    1. [test(cz_customize): add missing YAML configuration file tests #1516](https://github.com/commitizen-tools/commitizen/pull/1516)
    2. [docs(CHANGELOG): run pre-commit run --all-files to fix CI #1522](https://github.com/commitizen-tools/commitizen/pull/1522)
    3. [refactor(bump): use a loop to shorten a series of similar NotAllowed exceptions #1523](https://github.com/commitizen-tools/commitizen/pull/1523)
    4. [refactor(Init): use ternary operator #1527](https://github.com/commitizen-tools/commitizen/pull/1527)
    5. [docs(defaults): deprecate type Questions #1533](https://github.com/commitizen-tools/commitizen/pull/1533)
    6. [docs(customization.md): fix grammar mistake, add title to code blocks #1535](https://github.com/commitizen-tools/commitizen/pull/1535)
    7. [docs(bump.md): fix minor grammar issue and add titles for code blocks #1536](https://github.com/commitizen-tools/commitizen/pull/1536)
    8. [refactor(ParseArgs): simplify __call__ function body #1544](https://github.com/commitizen-tools/commitizen/pull/1544)
    9. [refactor(ScmProvider): replace sorted with max #1543](https://github.com/commitizen-tools/commitizen/pull/1543)
    10. [refactor(ExpectedExit): make the constructor more compact #1546](https://github.com/commitizen-tools/commitizen/pull/1546)
    11. [refactor(git): remove redundant if branch #1547](https://github.com/commitizen-tools/commitizen/pull/1547)
    12. [refactor(TagRules): extract tag_formats property and simplify list comprehension #1549](https://github.com/commitizen-tools/commitizen/pull/1549)
    13. [fix(Changelog): fix _export_template variable type #1550](https://github.com/commitizen-tools/commitizen/pull/1550)
    14. [fix(CommitizenProvider): raise if version is None #1552](https://github.com/commitizen-tools/commitizen/pull/1552)
    15. [fix(Bump): rewrite --get-next NotAllowed error message for consistency #1553](https://github.com/commitizen-tools/commitizen/pull/1553)
* 關閉 issues
    1. [Support tox >= 4.0.0 #637](https://github.com/commitizen-tools/commitizen/issues/637)
    2. [Absolute link or link to Markdown files? #1433](https://github.com/commitizen-tools/commitizen/issues/1433)
    3. [Check every commit message in PR CI #1493](https://github.com/commitizen-tools/commitizen/issues/1493)
    4. [Support termcolor version 3 #1420](https://github.com/commitizen-tools/commitizen/issues/1420)
    5. [Enable ruff rule PGH003 #1501](https://github.com/commitizen-tools/commitizen/issues/1501)
    6. [Support the latest version of Ruff #1474](https://github.com/commitizen-tools/commitizen/issues/1474)
    7. [Add filter/search feature for commit change type #1370](https://github.com/commitizen-tools/commitizen/issues/1370)
* 分類 issue
    1. [commitizen 4.8.3 includes dependency importlib_metadata for Python > 3.9 #1525](https://github.com/commitizen-tools/commitizen/issues/1525)
    2. [2nd git.commit error: "On branch main nothing to commit, working tree clean" #1530](https://github.com/commitizen-tools/commitizen/issues/1530)

## pycon-etl
終於讓 [Upgrade to Airflow 3.0.2 #159](https://github.com/pycontw/pycon-etl/pull/159) 準備好了！
雖然還需要等 Henry 大大審閱，但目前已經把現階段遇到的問題都解掉了
Dag `airflow_log_cleanup` 重新整理過，之後應該會再用 `task_group` 重寫一次

最近剛好需要研究 [external_db_managers](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#external-db-managers)，得看 [apache-airflow-providers-fab](https://airflow.apache.org/docs/apache-airflow-providers-fab/stable/index.html) 是怎麼做的
就順便搞懂了要怎麼把 PyCon TW 這邊驗證機制設定好
