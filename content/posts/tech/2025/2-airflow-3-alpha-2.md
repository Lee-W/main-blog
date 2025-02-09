Title: Play with the latest Airflow 3.0.0 alpha 1!
Subtitle: I mean alpha 2...
Date: 2025-02-09 11:20
Category: Tech
Tags: Airflow, Airflow 3.0
Slug: airflow-3-0-0-a2
Authors: Wei Lee
Cover: /images/posts-image/2025-airflow-alpha-2/airflow-3-ui.png

As announcements in the Airflow dev mailing list, ~~[📢 Apache Airflow 3.0.0apha1 is available for testing! 🎉]~~ [📢 Apache Airflow 3.0.0apha2 is available for testing! 🎉]

<!--more-->

Here are some of the remarkable features listed in the mail

* Dag versioning & Bundles (AIP-63)
    * Some projects highlight concerns about Airflow's lack of dag versioning. We now have it, haha!
* Modern Web Application (AIP-38)
* Task Execution Interface (AIP-72)
* **Data Assets & Asset-Centric Syntax (AIP-73)**
* External Event-Driven Scheduling (AIP-82)

This post won’t demonstrate any of these features but will serve as a quick guide for setting up the testing environment.

~~The reason I highlighted Asset is definitely not because I contributed a considerable amount to this feature.~~
~~DEFINITELY NOT!~~

[📢 Apache Airflow 3.0.0apha1 is available for testing! 🎉]: https://lists.apache.org/thread/7hdy8w8d9xq2z29hx0l02r3gsshdzwok
[📢 Apache Airflow 3.0.0apha2 is available for testing! 🎉]: https://lists.apache.org/thread/lh3ywqn084s3clr3ldr2wzgx7q696lsg

## Install Airflow 3.0.0 alpha1 for testing
[uv] is likely the simplest way for you to test. As it has yet to be uploaded to [PyPI], we could use the command provided in the mail. I set the Python version to 3.12 since 3.13 (my default python setup) is not yet supported by Airflow

```sh
uv venv --python 3.12

uv pip install \
    --find-links https://dist.apache.org/repos/dist/dev/airflow/3.0.0a2/ \
    apache-airflow==3.0.0a2 \
    apache-airflow-task-sdk==1.0.0a2 \
    apache-airflow-providers-standard==0.1.0a2 \
    apache-airflow-providers-fab==2.0.0a2 \
    apache-airflow-providers-celery==3.11.0a2
```

As for the minimum Python version that Airflow 3 will support, there's an ongoing discussion [Airflow 3 min python version to 3.10 early?] so I guess it will be 3.10 (?)

[Airflow 3 min python version to 3.10 early?]: https://lists.apache.org/thread/yln0jw0qkq928kpqnozty8gvlh1p8w0s

## Quick setup

I will only use the easiest `airflow standalone` command for testing. It's probably not something you want to try out in production. But Airflow 3.0.0 alpha2 is not for production either; we're good.

```sh
export AIRFLOW_HOME=`pwd`

uv run airflow db migrate
uv run airflow standalone
```

If everything works fine, you should to able to find  `airflow.db`, `airflow.cfg`, `standalone_admin_password.txt`, and other files.

Now go to your browser and open `http://localhost:8080`.
Use `admin` as the username and the content of the file `standalone_admin_password.txt` as the password to log in.

Then, you'll see the familiar Airflow 2 homepage.

![airflow-2-ui](/images/posts-image/2025-airflow-alpha-2/airflow-2-ui.jpg)


Let's click the "Check it out now" link and we'll find

![page-not-found](/images/posts-image/2025-airflow-alpha-2/page-not-found.jpg)

![nani](/images/meme/jotaro-nani.jpg)

If you look at the URL, it goes to `http://localhost:29091/webapp`. Out of curiosity, I changed it to `http://localhost:9091/webapp`, and the new UI is here.

![airflow-3-ui](/images/posts-image/2025-airflow-alpha-2/airflow-3-ui.png)


[Breeze] (Airflow's local development tool) uses port `28080` as the homepage. So... the counterpart of `29091` would probably be `9091`, and it turns out that I'm right.

It's now tracked by issue ["Check it out" link to New UI does not work #46514](https://github.com/apache/airflow/issues/46514).

In the new UI, you can find a `Legacy UI` button on the left-hand side.

![legacy-ui](/images/posts-image/2025-airflow-alpha-2/legacy-ui.png)


After you click it, you'll find out it does not work either, and that's why I created the issue ["Legacy UI" button in New UI does not work #46516](https://github.com/apache/airflow/issues/46516).

Now you're ready to test all the new features. Please create an issue if you encounter any bugs.

---

But... if you want to test Airflow 3 with an existing `airflow.cfg` or some legacy dags, you come to the right place!

## Tools that help you migrate to Airflow 3

### airflow.cfg - "airflow config lint"
We introduce a `lint` sub-command to `airflow config`.

```sh
uv run airflow config lint
```

This command tells you what configuration has been removed or moved somewhere else. It also detected environment variables and whatever will be loaded into Airflow. Check [Setting Configuration Options](https://airflow.apache.org/docs/apache-airflow/stable/howto/set-config.html) for details.

If you follow the examples above, it comes with a default `airflow.cfg`. After running the command above, you'll see

```
Found issues in your airflow.cfg:
  - Removed deprecated `cookie_samesite` configuration parameter from `webserver` section.
  - `dag_dir_list_interval` configuration parameter moved from `scheduler` section to `dag_processor` section as `refresh_interval`.

Please update your configuration file accordingly.
```

Even Airflow has not migrated to Airflow 3 yet.

![ironic](/images/meme/star-wars-ironic.jpg)

Issue [Legacy configuration not removed or updated #46517](https://github.com/apache/airflow/issues/46517) was also created.  

### Dags - ruff >= 0.95
Yep, this is the [ruff](https://docs.astral.sh/ruff/) you know (or probably should know). Recently, we added more [Airflow rules (with code AIR)](https://docs.astral.sh/ruff/rules/#airflow-air) to ruff. The ones that start with `3` (i.e., AIR301, AIR302, AIR302) are those that help you migrate to Airflow 3.0.

Given the following legacy dag

```python
from airflow import dag
from airflow.datasets import Dataset

from airflow.sensors.filesystem import FileSensor


@dag()
def air_301_dag():
    pass


@dag(schedule_interval="0 * * * *")
def air_302_dag():
    pass


@dag(schedule=Dataset("test"))
def air_303_dag():
    FileSensor(task_id="wait_for_file", filepath="/tmp/temporary_file_for_testing")
```

You can run the following comment

```shell
uv pip install "ruff>=0.9.5"
uv run ruff check dags/ --preview --select AIR301,AIR302,AIR303
```

and get the following error message

```
dags/legacy_dag.py:7:2: AIR301 DAG should have an explicit `schedule` argument
  |
7 | @dag()
  |  ^^^^^ AIR301
8 | def air_301_dag():
9 |     pass
  |

dags/legacy_dag.py:12:6: AIR302 [*] `schedule_interval` is removed in Airflow 3.0
   |
12 | @dag(schedule_interval="0 * * * *")
   |      ^^^^^^^^^^^^^^^^^ AIR302
13 | def air_302_dag():
14 |     pass
   |
   = help: Use `schedule` instead

dags/legacy_dag.py:17:15: AIR302 `airflow.datasets.Dataset` is removed in Airflow 3.0
   |
17 | @dag(schedule=Dataset("test"))
   |               ^^^^^^^ AIR302
18 | def air_303_dag():
19 |     FileSensor(task_id="wait_for_file", filepath="/tmp/temporary_file_for_testing")
   |
   = help: Use `airflow.sdk.definitions.asset.Asset` instead

dags/legacy_dag.py:19:5: AIR303 `airflow.sensors.filesystem.FileSensor` is moved into `standard` provider in Airflow 3.0;
   |
17 | @dag(schedule=Dataset("test"))
18 | def air_303_dag():
19 |     FileSensor(task_id="wait_for_file", filepath="/tmp/temporary_file_for_testing")
   |     ^^^^^^^^^^ AIR303
   |
   = help: Install `apache-airflow-provider-standard>=0.0.2` and use `airflow.providers.standard.sensors.filesystem.FileSensor` instead.

Found 4 errors.
[*] 1 fixable with the `--fix` option.
```

If you find anything missing regarding migration tooling, please comment on  [Airflow 2 to 3 auto migration rules #41641]. This is the root issue where we try to track everything related to migration rules.

## Why does the title look so weird
Well... this post was supposed to be published on Thursday. It was still alpha1. Then, alpha2 was released around the Airflow 3.0 dev call. It's midnight where I am, so... I can't really attend. Sleep is important. Staying up is bad.

![avemujica-bad-for-helth](/images/meme/avemujica-bad-for-helth.jpg)

If you're curious about why sleep is important, I recommend reading [[Book] 為什麼要睡覺]({filename}/posts/book/2020/5-why-we-sleep.md) (Why We Sleep), one of my favorite books. I probably should re-read it as well...

But the truth is, this is just another excuse of mine; I simply couldn't finish the post this quickly. 😆 Just like my [PEP 735] digest. The PEP was still in draft status when I wrote it. Now that the PEP is final, my digest still hasn't been published yet. 🥲

[uv]: https://docs.astral.sh/uv/
[PyPI]: https://pypi.org/
[Breeze]: https://github.com/apache/airflow/blob/main/dev/breeze/doc/README.rst
[PEP 735]: https://peps.python.org/pep-0735/

[Airflow 2 to 3 auto migration rules #41641]: https://github.com/apache/airflow/issues/41641
