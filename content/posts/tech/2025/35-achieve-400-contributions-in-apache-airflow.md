Title: Achieve 400 contributions in Apache Airflow
Date: 2025-08-07 20:10
Category: Tech
Tags: Airflow
Slug: achieve-400-contributions-in-apache-airflow
Authors: Wei Lee

Following up on [Achieve 300 contributions in Apache Airflow]({filename}/posts/tech/2025/12-achieve-300-contributions-in-apache-airflow.md).
Just a quick reflection on what I did between 300 and 400 contributions.

<!--more-->

The count is now quite inaccurate. I never really understood the difference between the PR I created and the number of commits I contributed. However, I decided to include PRs from [feat(api_fastapi): include asset ID in asset nodes when calling "/ui/dependencies" and "/ui/structure/structure_data" #47381](https://github.com/apache/airflow/pull/47381) to [build(pre-commit): upgrade node version to 22.18.0 and flynt 1.0.6 #54009](https://github.com/apache/airflow/pull/54009) as part of my 300 to 400 contributions. This should be approximately correct. Next time, we'll start from [build(pre-commit): upgrade node version to 22.18.0 and flynt 1.0.6 #54009](https://github.com/apache/airflow/pull/54009).

![400](/images/posts-image/2025-achieve-400-contributions-in-apache-airflow/400.jpg)

This time, I created the following script to help me list the PRs I need in my preferred format. It’s quite convenient.

```sh
START_PR_NUMBER=47381
END_PR_NUMBER=54009

START_MERGED_AT=$(gh pr view $START_PR_NUMBER --json mergedAt --jq .mergedAt)
END_MERGED_AT=$(gh pr view $END_PR_NUMBER --json mergedAt --jq .mergedAt)

echo "Start merged at: $START_MERGED_AT"
echo "End merged at:   $END_MERGED_AT"

gh pr list \
        -A @me \
        -s merged \
        --json title,mergedAt,number,url \
        -L 1000 \
        --jq "[.[]
                | select(.mergedAt > \"$START_MERGED_AT\" and .mergedAt < \"$END_MERGED_AT\")]
                | sort_by(.mergedAt)[]
                | \"1. [\(.title) #\(.number)](\(.url))\"" |
        > output.md
```

[TOC]

## Migration Tooling
1. [feat(migrations): remove dataset with duplicate uri when downgrading #48501](https://github.com/apache/airflow/pull/48501)
2. [docs(newsfragment): update the base operator path changed in #48529 #48540](https://github.com/apache/airflow/pull/48540)
3. [docs(newsfragments): uncheck rules modified in #48551 #48559](https://github.com/apache/airflow/pull/48559)
4. [Fix newsfragments migration rules content error #48566](https://github.com/apache/airflow/pull/48566)
5. [docs(newsfragments): mark implemented AIR302 rules as Done #48618](https://github.com/apache/airflow/pull/48618)
6. [Add missing `airflow config lint` rules and update/fix newsfragments #49048](https://github.com/apache/airflow/pull/49048)
7. [docs(upgrading_to_airflow3): add instruction to use ruff >= 0.11.13 for more auto fixes #51603](https://github.com/apache/airflow/pull/51603)

## Asset/Asset Alias related
1. [feat(UI): add asset-name-ref and asset-uri-ref to BaseNodeResponse #48920](https://github.com/apache/airflow/pull/48920)
2. [feat(task-sdk): add for_asset, for_asset_alias to event accessors #48999](https://github.com/apache/airflow/pull/48999)
3. [fix(serialized_dag): skip asset dag dep when the asset ref cannot be resolved into a valid asset #48795](https://github.com/apache/airflow/pull/48795)
4. [fix(example_dags): fix how asset events can be accessed through template #49044](https://github.com/apache/airflow/pull/49044)
5. [Remove asset-name-ref and asset-uri-ref node after resolving them #49008](https://github.com/apache/airflow/pull/49008)
6. [fix(serialized_dag): return original DagDependency if Asset Alias has not yet been resolved into asset #49204](https://github.com/apache/airflow/pull/49204)
7. [fix(AssetSchedule): fix how asset_expression is accessed #49214](https://github.com/apache/airflow/pull/49214)
8. [fix(AssetSchedule): use asset.name if exists #49225](https://github.com/apache/airflow/pull/49225)
9. [fix(serialized_objects): handle both inlet and outlet in v1 to v2 convert #49286](https://github.com/apache/airflow/pull/49286)
10. [fix(serialized_objects): fix how dataset/asset dag_dependency is converted from v1 to v2 #49281](https://github.com/apache/airflow/pull/49281)
11. [fix(airflow.datasets): Fix DatasetAny fallback typo #50383](https://github.com/apache/airflow/pull/50383)
12. [feat(dag_dependency): add unresolved asset ref node #49231](https://github.com/apache/airflow/pull/49231)
13. [docs(ruff): fix outdated content and add airflow rule list, ruff configuration links #50232](https://github.com/apache/airflow/pull/50232)
14. [fix(migrations): from 2.2.0 to 2.11.0 for Sqlite #50745](https://github.com/apache/airflow/pull/50745)
15. [Add back invalid inlet and outlet check before running tasks #50773](https://github.com/apache/airflow/pull/50773)
16. [Remove logical_date check when validate inlets and outlets #51464](https://github.com/apache/airflow/pull/51464)

## Taiwanese Mandarin translation
1. [docs(CODEOWNERS): Add Lee-W as Mandarian translation code owner #50951](https://github.com/apache/airflow/pull/50951)
2. [fix(CODEOWNERS): update TW translation path #51159](https://github.com/apache/airflow/pull/51159)
3. [fix(i18n): replace 插件 as 外掛 #51230](https://github.com/apache/airflow/pull/51230)
4. [Replace "Directly" with "Manually" zh-tw/assets.json #51726](https://github.com/apache/airflow/pull/51726)
5. [Add @jason810496 as a code owner and translation owner and @RoyLee1224, @guan404ming as Non-Committer Translation Owners #51728](https://github.com/apache/airflow/pull/51728)

## Fix Airflow 2 to 3 db migration for SQLite
1. [fix(serialized_object): fix how timetable and schedule_interval are handled during v1 to v2 conversion #49344](https://github.com/apache/airflow/pull/49344)
2. [fix(migrations): from 2.7.0 to 3.0.0 for SQLite #51336](https://github.com/apache/airflow/pull/51336)
3. [fix(migrations): from 2.7.0 to 3.0.0 for SQLite #51431](https://github.com/apache/airflow/pull/51431)
4. [fix(migrations): only ignore ValueError when interacting with constraints in sqlite #51529](https://github.com/apache/airflow/pull/51529)
5. [[v3-0-test] fix(serialized_objects): try to infer data interval if it's none (#51530) #51913](https://github.com/apache/airflow/pull/51913)
6. [[v3-0-test] fix(migrations): only ignore value error when interacting with constraints in sqlite (#51529) #51641](https://github.com/apache/airflow/pull/51641)

## AIP-90: Human in the loop
1. [feat(hitl): add HITLBranchOperator #53960](https://github.com/apache/airflow/pull/53960)
2. [Add Human-in-the-loop logic to core Airflow and implement `HITLOperator`, `ApprovalOperator`, `HITLEntryOperator` in standard provider #52868](https://github.com/apache/airflow/pull/52868)
3. [fix(hitl): Fix HITLEntryOperator "options" and "defaults" handling #53184](https://github.com/apache/airflow/pull/53184)
4. [feat(hitl): include task_instance detail in hitl detail response #53373](https://github.com/apache/airflow/pull/53373)
5. [Add example Dags for Human in the loop operators #53360](https://github.com/apache/airflow/pull/53360)
6. [Support Query in GetHITLDetails Public api #53376](https://github.com/apache/airflow/pull/53376)
7. [fix(hitl): handle `HITLDetail` when task instance is retried #53824](https://github.com/apache/airflow/pull/53824)
8. [fix(hitl): rename `/hitl-details` endpoints as `/hitlDetails` #53885](https://github.com/apache/airflow/pull/53885)
9. [feat(hitl): add "timedout" column to HITLTriggerEventSuccessPayload #53852](https://github.com/apache/airflow/pull/53852)
10. [fix(hitl): Handle task instance clearing when getting and updating an existing HITLDetail #53863](https://github.com/apache/airflow/pull/53863)
11. [feat(HITL): improve hitl trigger logging message #53850](https://github.com/apache/airflow/pull/53850)
12. [test(hitl): fix test_update_hitl_detail_without_ti and test_get_hitl_detail_without_ti failure #53921](https://github.com/apache/airflow/pull/53921)
13. [feat(hitl): allow filtering by taskIdPattern in "GET /hitlDetails" #53923](https://github.com/apache/airflow/pull/53923)
14. [refactor(HITL): make default options class variables to avoid typo #53849](https://github.com/apache/airflow/pull/53849)

## main branch CI failure
1. [Fix default deferrable checking script #50934](https://github.com/apache/airflow/pull/50934)
2. [docs: add comments to pytest 8.4.0 limitation #51340](https://github.com/apache/airflow/pull/51340)
3. [[v3-0-test] Add sqlalchemy-spanner limitation for broken 1.12.0 release #51432](https://github.com/apache/airflow/pull/51432)
4. [Exclude libcst 1.8.1 for Python 3.9 #51606](https://github.com/apache/airflow/pull/51606)
5. [fix(ui): rebuild ts assets #51911](https://github.com/apache/airflow/pull/51911)
6. [fix(dev): guard missing --language if --add-missing is used in dev/i18n/check_translations_completeness.py #51981](https://github.com/apache/airflow/pull/51981)

## misc
1. [Handle MappedTaskGroup map indexes #49996](https://github.com/apache/airflow/pull/49996)
2. [fix(task_instances): handle upstream_mapped_index when xcom access is needed #50641](https://github.com/apache/airflow/pull/50641)
3. [fix(breeze): fix missing ` in warning message #49000](https://github.com/apache/airflow/pull/49000)
4. [fix(serialized_dag): handle compressing serialized_dag for get_dag_dependencies #48924](https://github.com/apache/airflow/pull/48924)
5. [fix(serialized_dag): expand DagDependency generation and add fallback value #49327](https://github.com/apache/airflow/pull/49327)
6. [Update the default value of `PubSubPullOperator.deferrable` to `conf.getboolean("operators", "default_deferrable", fallback=False)` #50935](https://github.com/apache/airflow/pull/50935)
7. [docs: replace constraints-3.8.txt as constraints-3.9.txt as constraints-3.8.txt does not exist in 2.11 #51049](https://github.com/apache/airflow/pull/51049)
8. [feat(task_instances): guard ti update state and set task to fail if exception encountered #51295](https://github.com/apache/airflow/pull/51295)
9. [docs(providers): fix contributing-doc reference #51616](https://github.com/apache/airflow/pull/51616)
10. [docs(dagfile-processing): fix outdated scheduler and DAG usage #53183](https://github.com/apache/airflow/pull/53183)
11. [docs: Update DAG author as Dag author #53857](https://github.com/apache/airflow/pull/53857)
