Title: Achieve 300 contributions in Apache Airflow
Date: 2025-04-06 11:45
Category: Tech
Tags: Airflow
Slug: achieve-300-contributions-in-apache-airflow
Authors: Wei Lee

Following up on [Achieve 200 contributions in Apache Airflow]({filename}/posts/book/2024/11-achieve-200-contributions-in-apache-airflow.md).
Just a quick reflection on what I did between 200 and 300 contributions.

<!--more-->

It seems that most of the PRs still relate to Dataset/Asset. I thought I had spent more time on AIP-72 and AIP-83, but perhaps those are PRs created by others that I took over. Or maybe my memory is just failing me...

![airflow-300-contributions](/images/posts-image/2025-achieve-300-contributions-in-apache-airflow/airflow-300-contributions.jpg)

In addition to the Airflow repo itself, I also spent a decent amount of time contributing to [ruff - Airflow rules](https://github.com/astral-sh/ruff/pulls/Lee-W), which makes me the 29th contributor to ruff. It’s kind of weird, considering that I know almost nothing about Rust.

![ruff](/images/posts-image/2025-achieve-300-contributions-in-apache-airflow/ruff.png)

[TOC]

## Dataset / Asset Alias
1. [set "has_outlet_datasets" to true if "dataset alias" exists](https://github.com/apache/airflow/pull/41091)
2. [Add dataset alias unique constraint and remove wrong dataset alias removing logic](https://github.com/apache/airflow/pull/41097)
3. [docs(dataset): illustrate when dataset aliases are resolved](https://github.com/apache/airflow/pull/41152)
4. [fix DagPriorityParsingRequest unique constraint error when dataset aliases are resolved into new datasets](https://github.com/apache/airflow/pull/41398)
5. [fix(dag): avoid getting dataset next run info for unresolved dataset alias](https://github.com/apache/airflow/pull/41828)
6. [allow dataset alias to add more than one dataset events](https://github.com/apache/airflow/pull/42189)

## Dataset / Asset
1. [Add DatasetDagRunQueue to all the consuming DAGs of a dataset alias](https://github.com/apache/airflow/pull/41264)
2. [Fix dataset page cannot correctly load triggered dag runs due to lack of dagId](https://github.com/apache/airflow/pull/41279)
3. [Show only the source on the consumer DAG page and only triggered DAG run in the producer DAG page](https://github.com/apache/airflow/pull/41300)
4. [fix wrong link to the source DAG in consumer DAG's dataset event section](https://github.com/apache/airflow/pull/41301)
5. [feat(datasets): make strict_dataset_uri_validation default to True](https://github.com/apache/airflow/pull/41814)
6. [Rewrite how dag to dataset / dataset alias are stored](https://github.com/apache/airflow/pull/41987)
7. [Rewrite how DAG to dataset / dataset alias are stored](https://github.com/apache/airflow/pull/42055)
8. [fix(datasets/managers): fix error handling file loc when dataset alias resolved into new datasets](https://github.com/apache/airflow/pull/42733)

## AIP-74, 75 - Data Asset and Asset Centric Syntax
1. [Rename dataset related python variable names to asset](https://github.com/apache/airflow/pull/41348)
2. [Rename Dataset database tables as Asset](https://github.com/apache/airflow/pull/42023)
3. [Rename dataset endpoints as asset endpoints](https://github.com/apache/airflow/pull/42579)
4. [fix(assets/managers): fix error handling file loc when asset alias resolved into new assets](https://github.com/apache/airflow/pull/42735)
5. [Rename dataset as asset in UI](https://github.com/apache/airflow/pull/43073)
6. [feat(providers/amazon): Use asset in common provider](https://github.com/apache/airflow/pull/43110)
7. [feat(providers/openlineage): Use asset in common provider](https://github.com/apache/airflow/pull/43111)
8. [feat(providers/fab): Use asset in common provider](https://github.com/apache/airflow/pull/43112)
9. [Add Dataset, Model asset subclasses](https://github.com/apache/airflow/pull/43142)
10. [fix(migration): fix dataset to asset migration typo](https://github.com/apache/airflow/pull/43245)
11. [Fix AIP-74 migration errors](https://github.com/apache/airflow/pull/43313)
12. [fix typo in dag_schedule_dataset_alias_reference migration file](https://github.com/apache/airflow/pull/43314)
13. [add migration file to rename dag_schedule_dataset_alias_reference constraint typo](https://github.com/apache/airflow/pull/43373)
14. [Resolve warning in Dataset Alias migration](https://github.com/apache/airflow/pull/43425)
15. [fix(providers/fab): alias is_authorized_dataset to is_authorized_asset](https://github.com/apache/airflow/pull/43469)
16. [fix(providers/amazon): alias is_authorized_dataset to is_authorized_asset](https://github.com/apache/airflow/pull/43470)
17. [remove the to-write asset active dag warnings that already exists in the db instead of those that does not exist](https://github.com/apache/airflow/pull/43693)
18. [Move Asset user facing components to task_sdk](https://github.com/apache/airflow/pull/43773)
19. [Add missing attribute "name" and "group" for Asset and "group" for AssetAlias in serialization, api and methods](https://github.com/apache/airflow/pull/43774)
20. [fix(scheduler_job_runner/asset): fix how asset dag warning is added](https://github.com/apache/airflow/pull/43873)
21. [Raise deprecation warning when accessing inlet or outlet events through str](https://github.com/apache/airflow/pull/43922)
22. [feat(dataset): allow "airflow.dataset.metadata.Metadata" import for backward compat](https://github.com/apache/airflow/pull/44413)
23. [feat(datasets): add backward compat for DatasetAll, DatasetAny, expand_alias_to_datasets and DatasetAliasEvent](https://github.com/apache/airflow/pull/44635)
24. [Respect Asset.name when accessing inlet and outlet events](https://github.com/apache/airflow/pull/44639)
25. [fix(providers/common/compat): add back add_input_dataset and add_output_dataset to NoOpCollector](https://github.com/apache/airflow/pull/44681)
26. [Raise deprecation warning when accessing metadata through str](https://github.com/apache/airflow/pull/44791)
27. [Fail a task if an inlet or outlet asset is inactive or an inactive asset is added to an asset alias](https://github.com/apache/airflow/pull/44831)
28. [feat(asset): change asset inactive warning to log Asset instead of AssetModel](https://github.com/apache/airflow/pull/44836)
29. [Combine asset events fetching logic into one SQL query and clean up unnecessary asset-triggered dag data](https://github.com/apache/airflow/pull/46721)

## AIP-72 - Task Execution Interface
1. [feat(task_sdk): add support for inlet_events in Task Context](https://github.com/apache/airflow/pull/45960)

## Tooling for migrating Airflow 2 to 3
1. [ci(github-actions): add uv to news-fragment action](https://github.com/apache/airflow/pull/43878)
2. [docs(newsfragement): fix typos in 41762, 42060 and remove unnecessary 41814](https://github.com/apache/airflow/pull/44181)
3. [docs(newsfragment): these deprecated things are functions instead of arguments](https://github.com/apache/airflow/pull/44242)
4. [docs(newsfragment): add template for significant newsfragments](https://github.com/apache/airflow/pull/44378)
5. [feat(cli): add "core.task_runner" and "core.enable_xcom_pickling" to unsupported config check to command "airflow config lint"](https://github.com/apache/airflow/pull/45214)
6. [Update existing significant newsfragments with the later introduced template format](https://github.com/apache/airflow/pull/45678)
7. [Extend and fix "airflow config lint" rules](https://github.com/apache/airflow/pull/45701)
8. [Backport "airflow config lint"](https://github.com/apache/airflow/pull/45736)
9. [Add newsfragment and migration rules for scheduler.dag_dir_list_interval → dag_bundles.refresh_interval configuration change](https://github.com/apache/airflow/pull/45737)
10. [Add missing significant newsfragments and migration rules needed](https://github.com/apache/airflow/pull/45740)
11. [ci(github-actions): add a script to check significant newsfragments](https://github.com/apache/airflow/pull/46007)
12. [docs(newsfragment): add significant newsfragment to PR 42252](https://github.com/apache/airflow/pull/46364)
13. [ci(github-actions): relax docutils version to support python 3.8](https://github.com/apache/airflow/pull/46404)
14. [docs(newsfragments): update migration rules status](https://github.com/apache/airflow/pull/46409)
15. [fix(task_sdk): add missing type column to TIRuntimeCheckPayload](https://github.com/apache/airflow/pull/46509)
16. [docs(newsfragments): update 46572 newsfrgments content](https://github.com/apache/airflow/pull/46611)
17. [Fix significant format and update the checking script](https://github.com/apache/airflow/pull/46752)
18. [feat: migrate new config rules back to v2-10-test](https://github.com/apache/airflow/pull/46757)
19. [docs(newsfragments): update migration rules in newsfragments](https://github.com/apache/airflow/pull/47049)

## AIP-83 amendment - Restore uniqueness for logical_date while allowing it to be nullable
1. [Set logical_date and data_interval to None for asset-triggered dags and forbid them to be accessed in context/template](https://github.com/apache/airflow/pull/46460)

## Providers
1. [add missing sync_hook_class to CloudDataTransferServiceAsyncHook](https://github.com/apache/airflow/pull/41417)
2. [fix test_yandex_lockbox_secret_backend_get_connection_from_json by removing non-json extra](https://github.com/apache/airflow/pull/41815)
3. [handle ClientError raised after key is missing during DyanmoDB table.get_item](https://github.com/apache/airflow/pull/42408)
4. [fix(providers/common/sql): add dummy connection setter for backward compatibility](https://github.com/apache/airflow/pull/42490)
5. [feat(providers/common/sql): add warning to connection setter](https://github.com/apache/airflow/pull/42736)
6. [fix(providers/databricks): remove additional argument passed to repair_run](https://github.com/apache/airflow/pull/44140)
7. [fix(provider/edge): add back missing method map](https://github.com/apache/airflow/pull/44468)
8. [docs(newsfragments): fix typo and improve significant newfragment template](https://github.com/apache/airflow/pull/44833)

## Misc
1. [fix(TriggeredDagRuns): fix wrong link in triggered dag run](https://github.com/apache/airflow/pull/41166)
2. [Return string representation if XComArgs existing during resolving and include_xcom is set to False](https://github.com/apache/airflow/pull/41177)
3. [Allowing DateTimeSensorAsync, FileSensor and TimeSensorAsync to start execution from trigger during dynamic task mapping](https://github.com/apache/airflow/pull/41182)
4. [refactor how triggered dag run url is replaced](https://github.com/apache/airflow/pull/41259)
5. [Change inserted airflow version of "update-migration-references" command from airflow_version='...' to airflow_version="..."](https://github.com/apache/airflow/pull/41275)
6. [Fix missing source link for the mapped task with index 0](https://github.com/apache/airflow/pull/41403)
7. [remove the removed --use-migration-files argument of "airflow db reset" command in run_generate_migration.sh](https://github.com/apache/airflow/pull/41621)
8. [docs(deferring): fix missing import in example and remove unnecessary example](https://github.com/apache/airflow/pull/41691)
9. [Set end_date and duration for triggers completed with end_from_trigger as True](https://github.com/apache/airflow/pull/41834)
10. [ci: improve check_deferrable_default script to cover positional variables](https://github.com/apache/airflow/pull/41924)
11. [ci: improve check_deferrable_default script to cover positional variables](https://github.com/apache/airflow/pull/41942)
12. [Add warning that listeners can be dangerous](https://github.com/apache/airflow/pull/41968)
13. [ci: auto fix default_deferrable value with LibCST](https://github.com/apache/airflow/pull/41984)
14. [ci(pre-commit): lower minimum libcst version to 1.1.0 for python 3.8 support](https://github.com/apache/airflow/pull/42083)
15. [Autofix default deferrable with LibCST](https://github.com/apache/airflow/pull/42089)
16. [add "enable_tracemalloc" to log memory usage in scheduler](https://github.com/apache/airflow/pull/42304)
17. [ci(pre-commit): migrate pre-commit config](https://github.com/apache/airflow/pull/43372)
18. [fix(dag_warning): rename argument error_type as warning_type](https://github.com/apache/airflow/pull/43877)
19. [Add newsfragment PR 43393](https://github.com/apache/airflow/pull/44091)
20. [refactor(trigger_rule): remove deprecated NONE_FAILED_OR_SKIPPED](https://github.com/apache/airflow/pull/44475)
21. [Ensure check_query_exists returns a bool (#43978)](https://github.com/apache/airflow/pull/46707)

---

Okay, so that's it. If I ever have such a summary, the next time I'll start with [feat(api_fastapi): include asset ID in asset nodes when calling "/ui/dependencies" and "/ui/structure/structure_data" #47381](https://github.com/apache/airflow/pull/47381).
