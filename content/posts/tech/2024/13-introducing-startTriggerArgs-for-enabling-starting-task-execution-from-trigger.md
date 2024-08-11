Title: Introducing StartTriggerArgs for enabling starting task execution from trigger
Date: 2024-08-09 12:50
Category: Tech
Tags: Python, Airflow, Airflow 2.10
Slug: introducing-start-trigger-args-for-enabling-starting-task-execution-from-trigger
Authors: Wei Lee


As mentioned in  [Starts Airflow task execution directly from the triggerer]({filename}/posts/tech/2024/7-airflow-start-execution-directly-from-trigger-instead-of-going-into-wroker.md), the syntax of this feature will change after [#39585](https://github.com/apache/airflow/pull/39585) merged.

<!--more-->

This is needed mainly because we don't want to run any user code in the scheduler, which might happen [here](https://github.com/apache/airflow/pull/38674/files#).

This article will cover the following 4 PRs

1. [Prevent start trigger initialization in scheduler](https://github.com/apache/airflow/pull/39585)
2. [Add start execution from trigger support for existing core sensors](https://github.com/apache/airflow/pull/41021)
3. [add next_kwargs to StartTriggerArgs](https://github.com/apache/airflow/pull/40376)
4. [Enhance start_trigger_args serialization](https://github.com/apache/airflow/pull/40993)

PR 2 is a minor fix to PR 1. PR 3 is something wrongly implemented in [#38674](https://github.com/apache/airflow/pull/38674). I did not know this part of airflow well enough 🤦‍♂️ PR 4 is adding this feature to core sensors.
