Title: Optimizing Airflow Operators
Subtitle: Converting to Async with default_deferrable Config
Date: 2024-08-29 22:00
Modified: 2025-12-22 09:30
Category: Tech
Tags: Python, Airflow, Airflow 2.7
Slug: optimizing-airflow-operators-with-default_deferrable
Authors: Wei Lee
Series: Unleash the Chaos: Developing a Linter for Un-Pythonic Code!

In the article series [What If...? Running Airflow Tasks without the workers]({filename}/posts/tech/2024/7-airflow-start-execution-directly-from-trigger-instead-of-going-into-worker.md), I introduced one of the new features of Airflow 2.10.0. It's time to introduce a feature in Airflow 2.7.0 (no, it's not).

<!--more-->

Even though Grammarly suggested such a fancy post title, this article will only discuss the simple pull request [Add default_deferrable config #31712](https://github.com/apache/airflow/pull/31712). This was the first major thing I did since joining Astronomer.io and the first pull request that got voted PR of the month. Even though it turned out to be relatively easy, we tried some hacky things with [Cluster Policty](https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/cluster-policies.html) before it looks like this. But I think that a topic for another day.

## So, what is this default_deferrable config?
It's a [configuration](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#default-deferrable) that you can specify in the `airflow.cfg` file.

```cfg
# airflow.cfg
[operators]
default_deferrable = true
```

or through the environment variable

```shell
AIRFLOW__OPERATORS__DEFAULT_DEFERRABLE=true
```

By enabling this configuration, all the current operators that support deferrable mode (see the complete list [here](https://airflow.apache.org/docs/apache-airflow-providers/core-extensions/deferrable-operator-ref.html)) will now operate in deferrable mode. The primary advantage of deferrable operators is that part of the logic is run asynchronously by the Airflow triggerer. For more details, please refer to [Deferrable Operators & Triggers](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/deferring.html).

## How was it done?

**Step 1**: Add this configuration to [airflow/config_templates/config.yml](https://github.com/apache/airflow/pull/31712/files#diff-0a480a8b563e200f749424d7e761555e543588ff39a0b11cce7e34d522f38e0eR1308-R1314)

```yaml
    default_deferrable:
      description: |
        The default value of attribute "deferrable" in operators and sensors.
      version_added: ~
      type: boolean
      example: ~
      default: "false"
```

**Step 2**: Change the default value of the argument `deferrable` in every operator/sensor to `conf.getboolean("operators", "default_deferrable", fallback=False)`; this is how Airflow retrieves the value from `airflow.cfg` or environment variables.

<!-- blacken-docs:off -->

```python
        deferrable: bool = conf.getboolean("operators", "default_deferrable", fallback=False),
```

<!-- blacken-docs:on -->

**Step 3**: Kindly ask every contributor to add this default value to every operator/sensor and reviewer to check

**Step 4**: Pray that everyone will follow 🙏...... at least that is what we did at that moment
