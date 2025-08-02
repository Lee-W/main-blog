Title: EuroPython 2025 Airflow Development Sprint
Date: 2025-08-02 22:20
Category: Tech
Tags: EuroPython, Development Sprint
Slug: europython-2025-airflow-development-sprint
Authors: Wei Lee
Cover: /images/posts-image/2025-europython-2025-airflow-development-sprint/venue.jpeg

Finally back from EuroPython and recovering a bit from the long travel.
It's time to review how the development sprint went this time.

<!--more-->

This is what the EuroPython organizers asked us after the sprint. (PyCon TW might want to consider doing something similar 🤔)

- how many participants you had;
- how many issues were tackled; and
- how many PRs you merged?

and the answers are

1. around 8
2. 2
3. 1

---

This time, we spent a lot of time setting up Breeze and faced many unexpected issues that we couldn't resolve quickly. This is the first time the environment setup has taken us so long. During DurianPy, the setup went quite smoothly. 🤔

After completing the setup, I dedicated most of my time to triaging and checking whether there were simple, easy-to-address issues we could work on.

* Issues
    * closed
        * [GCSToBigQueryOperator: TypeError: cannot serialize object of type <class 'type'> #53525](https://github.com/apache/airflow/issues/53525)
        * [Enhance Dataset Scheduling to Support Multiple DAG Completion Conditions #52637](https://github.com/apache/airflow/issues/52637)
    * triaged but not assigned to participants
        * [Add support for Papermill using https #52893](https://github.com/apache/airflow/issues/52893)
        * [Dynamically mapped task groups with expand_kwargs do not resolve arguments with default values #49376](https://github.com/apache/airflow/issues/49376)
    * assigned to participants
        * [Task group names are duplicated in Task's task_id for MappedOperator #52334](https://github.com/apache/airflow/issues/52334) (resolved)
        * [Best Practices - Unit test for custom operator #52862](https://github.com/apache/airflow/issues/52862)
        * [[Filters] Add filters to Task View - Task Instances Tab #53051](https://github.com/apache/airflow/issues/53051)
* Pull Requests
    * Created by participants
        * [Fixed Task group names duplication in Task's task_id for MappedOperator #53532](https://github.com/apache/airflow/pull/53532) (merged not long after the sprint)
        * [feat(cli): add YAML/ENV support to airflow variables import #53726](https://github.com/apache/airflow/pull/53726) (created not long after the sprint)
    * Reviewed and merged
        * [Add translation for favorite Dag (zh-TW) #53558](https://github.com/apache/airflow/pull/53558)

It's not as productive as I would have expected this time. Nonetheless, helping new friends take their first steps toward open source remains a meaningful experience.

![IMG_6993](/images/posts-image/2025-europython-2025-airflow-development-sprint/venue.jpeg)

Plus, the food was really good

![IMG_7011](/images/posts-image/2025-europython-2025-airflow-development-sprint/airflow.jpeg)
