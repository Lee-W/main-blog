Title: 2025/07/07 - 08/03 開源貢獻週報
Subtitle: ただいま
Date: 2025-07-03 23:00
Category: Tech
Tags: Open Source, 開源貢獻週報
Slug: 2025-07-07-08-03-open-source-report
Authors: Wei Lee

雖然不多，但在這段旅行期間還是有很些微的開源貢獻

<!--more-->

這週要回來看熊大的 PR 們了

## EuroPython/website
* 開 PR [docs(sprints): add Apache Airflow #1437](https://github.com/EuroPython/website/pull/1437)
    * 雖然只是註冊 Development Sprint，但也算是貢獻開源吧！

## pycon-etl
* 開 PRs
    * [Update airflow.cfg to decrease CPU loading #174](https://github.com/pycontw/pycon-etl/pull/174)
        * 機器太小， CPU 又爆了
    * [fix(airflow.cfg): fix duplicate core.max_active_tasks_per_dag #175](https://github.com/pycontw/pycon-etl/pull/175)
    * [refactor(dags): remove redundant code in airflow_log_cleanup #180](https://github.com/pycontw/pycon-etl/pull/180)
    * [refactor(dags): remove unnecessary dag directories and add missing __init__ files #178](https://github.com/pycontw/pycon-etl/pull/178/files)
    * [build(docker-compose): Create a volume instead of mount a local one for logs #178](https://github.com/pycontw/pycon-etl/pull/178)
* 審閱 PR
    * [Load CSV ticket data #181](https://github.com/pycontw/pycon-etl/pull/181)

## commitizen
* 審閱 PRs
    * [docs(config.md): Document glob pattern support in version_files #1558](https://github.com/commitizen-tools/commitizen/pull/1558/files)
    * [docs(docs/third-party-commitizen.md): Add cz-path info #1559](https://github.com/commitizen-tools/commitizen/pull/1559)
* 開 PRs
    * [ci(github-actions): fix sponsorship page generation #1561](https://github.com/commitizen-tools/commitizen/pull/1561)
        * 畢竟贊助商有去 EuroPython，快點修好才趕去跟他們打著呼
