Title: 2025/06/02 - 06/08 開源貢獻週報
Subtitle: Airflow 2 升上去了， Airflow 3 就不遠了！
Date: 2025-06-09 09:45
Category: Tech
Tags: Open Source, 開源貢獻週報
Slug: 2025-06-02-06-08-open-source-report
Authors: Wei Lee

這週熊大還是很猛的一直發 PR 給 commitizen
除了熊大外，還有新朋友幻影也立刻趕到戰場
不過這週除了 commitizen 外，我也花了不少時間在整理 PyCon TW 的 airflow！

<!--more-->

順帶一提， PyCon Taiwan 2025 的售票開始了
[現在就搶票！](https://tw.pycon.org/2025/registration/tickets)

## pycon-etl
* Pull Requests
    * 完成並且合併 [Upgrade to Airflow 2.11.0 #158](https://github.com/pycontw/pycon-etl/pull/158)
        * 時隔許久，我終於成功參加到 data team 的討論（之前每次想參加都剛好有事...）
          剛好去解釋了一下這個超大 PR 到底在幹嘛，隔天組長就幫我合併了
          （感謝 Henry!）
        * 部署上去其實還是花了一點時間，但最後終於成功了！
          **從 Airflow 1.10.15 升版到 2.11.0！**
    * 開 PR [docs: fix readme path #160](https://github.com/pycontw/pycon-etl/pull/160) 並且合併它
        * 但上面那個 PR 把 readme 的路徑改掉了
          忘記 GitHub 其實吃不到 `docs/index.md` ，所以還是得改成 `docs/README.md`
    * 開草稿 PR [Upgrade to Airflow 3 #159](https://github.com/pycontw/pycon-etl/pull/159)
        * 這個 PR 也弄到 87% 好了！
          畢竟 pycon-etl 資料庫裡面大多是遠古時代來的，又用了 airflow 不建議在 production 用的 SQLite
          資料搬遷上有不少的眉眉角角要處理
          雖然會需要手動 patch，但看起來是都解決了，之後要再貢獻回去
* Issues
    * 開 [[CI/CD] Sync up master branch to prod automatically #161](https://github.com/pycontw/pycon-etl/issues/161)
        * 總覺得現在流程有不少可以自動化，並且應該被記錄的更完整

## commitizen_cz_template
* 審查並合併 PR [Fix some typos and update link #5](https://github.com/commitizen-tools/commitizen_cz_template/pull/5)

## commitizen
* 審查 PRs
    1. [refactor: improve types and avoid nested loop, add types for untyped functions #1466](https://github.com/commitizen-tools/commitizen/pull/1466)
    2. [refactor(BaseCommitizen): remove unused process_commit #1468](https://github.com/commitizen-tools/commitizen/pull/1468)
    3. [refactor(conventional_commits): make schema_pattern more readable #1469](https://github.com/commitizen-tools/commitizen/pull/1469)
    4. [refactor(check): rename variable and compile pattern once #1470](https://github.com/commitizen-tools/commitizen/pull/1470)
    5. [refactor: do not guess if changelog format is provided, make function private #1471](https://github.com/commitizen-tools/commitizen/pull/1471)
    6. [refactor(cz): better typing and refactor message method #1472](https://github.com/commitizen-tools/commitizen/pull/1472)
    7. [Upgrade ruff and add RUF022 & RUF100 #1482](https://github.com/commitizen-tools/commitizen/pull/1482/commits)
    8. [build(.gitignore): ignore pyrightconfig.json and poetry.toml #1483](https://github.com/commitizen-tools/commitizen/pull/1483)
    9. [refactor(questions): type questions with TypedDict #1485](https://github.com/commitizen-tools/commitizen/pull/1485)
    10. [Add FAQ explaining why Pydantic is not used #1489](https://github.com/commitizen-tools/commitizen/pull/1489)
    11. [build(poetry): run poetry update to keep the packages up to date #1490](https://github.com/commitizen-tools/commitizen/pull/1490)
    12. [fix(commit): emit deprecated warning of cz commit -s BEFORE going through dialog, add deprecation warning on cz commit --help #1491](https://github.com/commitizen-tools/commitizen/pull/1491)
    13. [fix(deprecated): mark deprecated will be removed in v5 #1492](https://github.com/commitizen-tools/commitizen/pull/1492)
    14. [ci(pyproject.toml): strict check for invalid commit messages #1494](https://github.com/commitizen-tools/commitizen/pull/1494)
    15. [docs(feature_request): eliminate duplicated label #1496](https://github.com/commitizen-tools/commitizen/pull/1496)
    16. [perf(bump): avoid unnecessary list construction and rename variable t… #1504](https://github.com/commitizen-tools/commitizen/pull/1504)
    17. [refactor(bump): simplify nested if #1505](https://github.com/commitizen-tools/commitizen/pull/1505)
    18. [refactor(git): retype get_commits parameter to make it more friendly to call sites #1506](https://github.com/commitizen-tools/commitizen/pull/1506)
    19. [refactor(bump): eliminate similar patterns in code #1508](https://github.com/commitizen-tools/commitizen/pull/1508)
    20. [ci(mypy): fix linter error #1509](https://github.com/commitizen-tools/commitizen/pull/1509)
    21. [build: add PGH003 and PGH004, add types-colorama #1517](https://github.com/commitizen-tools/commitizen/pull/1517)
* 分類 issues
    1. Close [Those "XXX will be removed in commitizen 4." are not removed in v4, discuss when to remove them? #1473](https://github.com/commitizen-tools/commitizen/issues/1473)
    2. [Enable ruff rule PGH003 #1501](https://github.com/commitizen-tools/commitizen/issues/1501)
    3. [Discuss adding :meta private: to the doc string #1502](https://github.com/commitizen-tools/commitizen/issues/1502)
    4. [Fix tpl.filename type #1503](https://github.com/commitizen-tools/commitizen/issues/1503)
    5. [Deprecate Questions in defaults.py #1514](https://github.com/commitizen-tools/commitizen/issues/1514)
    6. [we might be able to move it to type_checking. but this can be next pr or let ruff handle it in the future #1515](https://github.com/commitizen-tools/commitizen/issues/1515)
* 開 issue [Generate expected bump version comment when receiving a new pull request #1510](https://github.com/commitizen-tools/commitizen/issues/1510)
    * 之前 4.0 就是不小心被升版的...

---

延續 [Airflow 多語系化]({filename}/posts/tech/2025/22-airflow-multilingual.md) 所提到的概念跟得到的反饋
我也希望我能多實踐我相信且支持的想法
所這篇試著把原本習慣使用英文的字，翻譯成漢語試試看
