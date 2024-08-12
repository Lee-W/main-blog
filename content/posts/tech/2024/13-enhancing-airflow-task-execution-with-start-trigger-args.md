Title: Enhancing Airflow Task Execution with StartTriggerArgs
Date: 2024-08-12 22:54
Category: Tech
Tags: Python, Airflow, Airflow 2.10
Slug: enhancing-airflow-task-execution-with-start-trigger-args
Authors: Wei Lee
Series: What If...? Running Airflow Tasks without the workers

As mentioned in  [Starts Airflow task execution directly from the triggerer]({filename}/posts/tech/2024/7-airflow-start-execution-directly-from-trigger-instead-of-going-into-wroker.md), the syntax of this feature will change after [#39585](https://github.com/apache/airflow/pull/39585) merged.

<!--more-->

This is needed mainly because we don't want to run any user code in the scheduler, which might happen [here](https://github.com/apache/airflow/pull/38674/files#).

This article will cover the following 3 PRs

1. [Prevent start trigger initialization in scheduler](https://github.com/apache/airflow/pull/39585)
2. [add next_kwargs to StartTriggerArgs](https://github.com/apache/airflow/pull/40376)
3. [Add start execution from trigger support for existing core sensors](https://github.com/apache/airflow/pull/41021)

PR 2 is a minor fix to PR 1. PR 3 is adding this feature to core sensors.

[TOC]

## What does it look like now?
The following code snippet shows how to define an operator that can start task execution directly from the trigger. I have kept the code simple and removed unnecessary details.

```python
from airflow.sensors.date_time import DateTimeSensorAsync
from airflow.triggers.base import StartTriggerArgs


class ExecuteFromTriggerDateTimeSensor(DateTimeSensor):
    start_trigger_args: StartTriggerArgs = StartTriggerArgs(
        trigger_cls="airflow.triggers.temporal.DateTimeTrigger",
        trigger_kwargs={"moment": "", "end_from_trigger": False},
        next_method="execute_complete",
        next_kwargs=None,
        timeout=None,
    )
    start_from_trigger: bool = True

    def __init__(self, *, trigger_kwargs, **kwargs) -> None:
        super().__init__(**kwargs)

        self.start_trigger_args.trigger_kwargs = dict(
            moment=timezone.parse(self.target_time),
            end_from_trigger=self.end_from_trigger,
        )

    def execute_complete(self, context, event) -> None:
        return
```

To enable an operator or a sensor with this feature, we must define the attributes `start_trigger_args` and `start_from_trigger`. We use `start_from_trigger` to determine whether we want to enable this feature and `start_trigger_args` to decide which trigger we want to use and how to use it. `start_trigger_args` should be an instance of `airflow.triggers.base.StartTriggerArgs` and it should contain the following arguments.

* `trigger_cls`
    * the full import path of the trigger to run
    * e.g., `airflow.triggers.temporal.DateTimeTrigger`
* `trigger_kwargs`
    * the keyword arguments passed into the trigger for initialization
    * e.g., `{"moment": "", "end_from_trigger": False}`
* `next_method`
    * the name of the method to run after execution done in the trigger
    * Most of the time, it's `execute_complete`
* `next_kwargs`
    * the keyword arguments passed into the next method
    * Most of the time, it's `None`. I never saw it used. 🤔
* `timeout`
    * the timeout for the trigger
    * Most of the time, it'll be set to `self.execution_timeout`.

If the attributes `start_trigger_args` and `start_from_trigger` are defined as class attributes, we could set `trigger_kwargs` as a temporary value and update the values in the `__init__` method. However, implementing a DAG with dynamic task mapping on an operator supporting this feature works differently, which will be detailed in the next article.

## What's changed under the hook
Let's start from [airflow/models/dagrun.py](https://github.com/apache/airflow/blob/9901a065fcd93307d8e1d69e34621966d7313511/airflow/models/dagrun.py#L1541-L1545). Airflow verifies if the `start_from_trigger` attribute is set to `True` and the `start_from_trigger` attribute is set. If both conditions are met, the `defer_task` method will be called with `exception=None`.

```python
            elif ti.task.start_from_trigger is True and ti.task.start_trigger_args is not None:
                ti.start_date = timezone.utcnow()
                if ti.state != TaskInstanceState.UP_FOR_RESCHEDULE:
                    ti.try_number += 1
                ti.defer_task(exception=None, session=session)
```

Then, let's go to [airflow/models/taskinstance.py](https://github.com/apache/airflow/blob/9901a065fcd93307d8e1d69e34621966d7313511/airflow/models/taskinstance.py#L1607-L1621).

```python
    if exception is not None:
        trigger_row = Trigger.from_object(exception.trigger)
        next_method = exception.method_name
        next_kwargs = exception.kwargs
        timeout = exception.timeout
    elif ti.task is not None and ti.task.start_trigger_args is not None:
        trigger_row = Trigger(
            classpath=ti.task.start_trigger_args.trigger_cls,
            kwargs=ti.task.start_trigger_args.trigger_kwargs or {},
        )
        next_kwargs = ti.task.start_trigger_args.next_kwargs
        next_method = ti.task.start_trigger_args.next_method
        timeout = ti.task.start_trigger_args.timeout
    else:
        raise AirflowException("exception and ti.task.start_trigger_args cannot both be None")
```

We handle standard task deferral in the first `if` condition. This happens when a task runs the `defer` method and raises a `TaskDeferred` exception. For a more detailed version, you can refer to [this link]({filename}/posts/tech/2024/7-airflow-start-execution-directly-from-trigger-instead-of-going-into-wroker.md#how-did-the-deferrable-operator-work-before-this-change). Therefore, we need to set `exception=None` in the previous code block, as we are not handling it in the standard way.

The `elif` statement checks whether this operator has a `start_trigger_args` attribute, which indicates that this operator supports the "starting execution from the trigger" feature. Airflow will then load the value from `start_trigger_args` and assign it to the variables that will later be used in the rest of the deferral process, similar to the standard task deferral.

The next article in this series will cover how to utilize this feature with dynamic task mapping (well.. partially). The implementation details will change somewhat, but the core idea remains unchanged.
