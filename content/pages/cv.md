---
title: CV
date: 2026-04-17 00:00
modified: 2026-04-17 00:00
slug: cv
lang: en
---

[TOC]

## Skills

* **Programming Language**: Python
* **Data Engineering**: Snowflake, Redis, SQLite, PostgreSQL, MySQL, Redshift
* **MLOps**: Apache Airflow, DVC, dbt, Great Expectations
* **Backend Development**: FastAPI, Flask, Django
* **DevOps**: GitHub Actions, Docker, Kubernetes, Jenkins, Git, AWS Services

## Work Experience

**[Aug 2024 – Present] Senior Software Engineer, [Astronomer]**

* [apache-airflow]
    * Add "DatasetAlias" for creating datasets or dataset events at runtime
    * Implement half of [AIP-74](https://cwiki.apache.org/confluence/display/AIRFLOW/AIP-74+Introducing+Data+Assets) and part of [AIP-75](https://cwiki.apache.org/confluence/display/AIRFLOW/AIP-75+New+Asset-Centric+Syntax)
    * Leading the implementation of [AIP-90](https://cwiki.apache.org/confluence/display/AIRFLOW/AIP-90+Human+in+the+loop)
* [ruff](https://github.com/astral-sh/ruff)
    * Implement most of the [AIR3XX](https://docs.astral.sh/ruff/rules/#airflow-air) rules to facilitate the migration from Airflow 2 to Airflow 3

**[Feb 2023 – Jul 2024] Software Engineer, [Astronomer]**

* [apache-airflow]
    * Allow Airflow tasks to execute directly from the trigger
    * Add REST API endpoint to manipulate queued dataset events
    * Upgrade apache-airflow-providers-weaviate to 2.0.0 for weaviate-client >= 4.4.0 support
    * Add Azure managed identities support to apache-airflow-providers-microsoft-azure
    * Add `default_deferrable` configuration for easily turning on the deferrable mode of operators
* [astronomer-providers](https://github.com/astronomer/astronomer-providers)
    * Contribute existing operators/sensors back to [apache-airflow] and deprecate this project to reduce maintenance efforts
    * Automated the deployment of integration tests and testing against the release of the airflow provider ([#987](https://github.com/astronomer/astronomer-providers/pull/987), [#1107](https://github.com/astronomer/astronomer-providers/pull/1107), [#1139](https://github.com/astronomer/astronomer-providers/pull/1139), [#1110](https://github.com/astronomer/astronomer-providers/pull/1110))
* [ask-astro](https://github.com/astronomer/ask-astro)
    * Set up local dev tools and fix various existing bugs

**[Apr 2017 – Feb 2023] Machine Learning Engineer, [Rakuten USA](https://www.rakuten.com/)**

* Productionize machine learning projects
    * Implemented SQS and gRPC services for grouping emails with similar structures and extracting user-sensitive data to increase the amount of training data without violating customer privacy regulations
    * Designed and implemented a two-stage labeling system that automatically communicates between Amazon Mechanical Turk and in-house experts to generate high-quality labeled data and enhance merchandise taxonomy to increase customer conversion rate
    * Migrated and automated the deployment process of AWS Lambda procedures that process customer lifetime value, reducing the effort of maintenance and deployment
* Build and maintain data pipelines on [Apache Airflow](https://airflow.apache.org/)
    * Implemented a pipeline that processes data larger than 10 GB to infer personalized preferences to help increase customer satisfaction
    * Migrated legacy 1.x Airflow server on AWS EC2 to 2.0.2 Airflow on AWS MWAA, saving developers' effort on dealing with legacy dependencies issues, and created a development Airflow environment for doing experiments without affecting the production pipeline
    * Refactored the data writing mechanism and reduced the data write time and AWS S3 cost
    * Built alerts and dashboards to monitor pipeline metrics, minimizing the effort of troubleshooting using DataDog, Prometheus, and Kibana
* Standardize and maintain software engineering practices
    * Created and maintained the project templates, with automatic code quality check, testing, containerization, project versioning, releasing, and deployment, and a standard workflow for existing projects to update tools, which reduced project creation time, the communication overhead during code review, and provided an easy way for developers to introduce new standards
    * Implemented a life-cycle configuration management tool and a workflow for creating Amazon Sagemaker notebook instances, which saves data scientists' time in handling engineering problems
    * Improved container build time and reduced execution time by 70% for Jenkins CI/CD pipelines
    * Maintain the core package that's used among most existing projects
* Optimized SQL in a data pipeline and reduced the execution time from infeasible to within half a day
* Cooperate with overseas teams in the US, Ukraine, and India

**[Jan 2019 – Mar 2019] Project Manager, [DLT Lab](https://dlt.csie.ncku.edu.tw)**

* Containerized and fixed legacy projects in [The Mosquito Man](https://github.com/the-mosquito-man)
* Introduced code review culture to a newly formed team
* Set up a [drone](https://github.com/drone/drone) CI/CD server and created CI pipelines for two ongoing projects

**[May 2018 – Nov 2018] Chief Teaching Assistant, [X-Village](https://www.facebook.com/X-Village-423736361424301/)**

*X-Village is an experimental education program designed to equip students who do not major in computer science with computational thinking skills and to foster future collaboration between computer science and other disciplines.*

* Managed the executive team with 16 members
* Organized two months of full-time courses and a one-semester 3-credit course
* Reviewed the teaching proposal of the Python course, "Programming Design Foundation"
* Designed exercises for "Data Structure," the first section of "Computer Science Foundations"
* Lectured on "Web Programming, Database/Cloud Computing," the fourth section of "Computer Science Foundations"

**[Jul 2015 – Jul 2016] Substitute Military Service, K-12 Education Administration, Ministry of Education**

* Maintained legacy systems implemented in multiple languages, including `C#`, `VBScript`, `PHP`, etc.
* Developed automation programs for generating reports, saving 80% of human labor time
* Delivered a human resource management system using [Django](https://www.djangoproject.com)

[Astronomer]: https://www.astronomer.io/
[apache-airflow]: https://github.com/apache/airflow/

## Community Involvement

**[Nov 2023 – Present] Everywhere, [PyCon Taiwan](https://tw.pycon.org/)**

* Maintain [pycontw-blog]
* Upgrade [PyCon-ETL](https://github.com/pycontw/PyCon-ETL) from Airflow 1 to 3

**[Nov 2022 – Sep 2023] Marketing Team Lead, [PyCon Taiwan 2023](https://tw.pycon.org/2023/)**

* Migrated PyCon Taiwan Blog to [pycontw-blog] / <https://conf.python.tw>

**[Nov 2021 – Sep 2022] Vice-Chairperson, [PyCon APAC 2022](https://tw.pycon.org/2022/)**

* Coordinated three squads, including planning, sponsorship, and social media
* Hosted the first Ask Me Anything event to promote the Call for Proposals

**[Oct 2020 – Nov 2021] Chairperson, [PyCon Taiwan 2021](https://tw.pycon.org/2021/)**

* Coordinated 9 teams and hosted the first online PyCon TW with 550 participants

**[Dec 2019 – Sep 2020] Program Chair, [PyCon Taiwan 2020](https://tw.pycon.org/2020/)**

* Coordinated around 20 team members and introduced community tracks and a speaker-dispatch program to increase the interaction between local communities

**[Jul 2019 – Nov 2019] Program Committee Member, [PyCon Taiwan 2019](https://tw.pycon.org/2019)**

* Contact keynote speakers and financial aid applicants
* Contribute to the [post-event report generator](https://github.com/pycontw/pycontw-postevent-report-generator)

[pycontw-blog]: https://github.com/pycontw/pycontw-blog

## Talks

| Date | Event | Title | Links |
|------|-------|-------|-------|
| 2025/12/24 | 🇹🇼 玉山 DE Talk | 觸發觸發器器，那個你可能不熟的 Apache Airflow 元件 | [slide](https://speakerdeck.com/leew/chu-fa-chu-fa-qi-qi-na-ge-ni-ke-neng-bu-shou-de-apache-airflow-yuan-jian) |
| 2025/11/27 | 🇹🇼 Python 衝刺開發工作坊 | 開源菜雞的隨意雜談 | [slide](https://speakerdeck.com/leew/20251127-kai-yuan-cai-ji-de-sui-yi-za-tan) |
| 2025/10/08 | 🇺🇸 Airflow Summit 2025 | Seamless Migration: Leveraging Ruff for a Smooth Transition from Airflow 2 to Airflow 3 | [slide](https://drive.google.com/file/d/1_2cxR8uOtWOphPPUD3IuwuRPcIBU4DXV/view?usp=drive_link) |
| 2025/09/06 | 🇹🇼 PyCon TW 2025 | Unlocking the Future of Data Pipelines - Apache Airflow 3 | [slide](https://speakerdeck.com/leew/unlocking-the-future-of-data-pipeline-942ed56f-0083-4e25-9e30-04850095e824) |
| 2025/07/18 | 🇨🇿 EuroPython 2025 | Hold on! You have a data team in PyCon Taiwan! | [slide](https://speakerdeck.com/leew/hold-on-you-have-a-data-team-in-pycon-taiwan) |
| 2025/06/11 | 🇹🇼 工程師的搜尋紀錄 | 朝聖之旅 | [slide](https://speakerdeck.com/leew/zhao-sheng-zhi-lu) |
| 2025/03/28 | 🇹🇼 黃金流沙饅頭營 | Airflow 3.0 The First Glance | [slide](https://speakerdeck.com/leew/20250328-airflow-3-dot-0-the-first-glance) |
| 2025/03/16 | 💻 NetDB Tech Day | 踏入開源的第一步 | [slide](https://speakerdeck.com/leew/20250316-ta-ru-kai-yuan-de-di-bu) |
| 2025/03/02 | 🇵🇭 PyCon APAC 2025 | Unleash the Chaos: Developing a Linter for Un-Pythonic Code! | [slide](https://speakerdeck.com/leew/unleash-the-chaos-developing-a-linter-for-un-pythonic-code-806b2bae-e161-4762-b0d5-d9fb8efdd24a) · [recording](https://www.youtube.com/watch?v=tbSZx0UsWfQ) |
| 2024/09/28 | 🇯🇵 PyCon JP 2024 | Unlocking Python's Core Magic | [slide](https://speakerdeck.com/leew/unlocking-pythons-core-magic) · [recording](https://www.youtube.com/watch?v=9jbHA6tE9MM) |
| 2024/09/21 | 🇹🇼 PyCon TW 2024 | Unleash the Chaos: Developing a Linter for Un-Pythonic Code! | [slide](https://speakerdeck.com/leew/unleash-the-chaos-developing-a-linter-for-un-pythonic-code) · [recording](https://www.youtube.com/watch?v=2jUd0o8VuE0) |
| 2024/09/11 | 🇺🇸 Airflow Summit 2024 | What If...? Running Airflow Tasks without the workers | [slide](https://docs.google.com/presentation/d/1XGd7bQg6cGLNbHFiZjX__SmI4FLw6D_iASY9eRSO4mo/edit?usp=sharing) · [recording](https://www.youtube.com/watch?v=WkljjYtqu8Q) |
| 2024/05/08 | 💻 Airflow Town Hall | Starts Airflow task execution directly from the triggerer | [slide](https://speakerdeck.com/leew/starts-airflow-task-execution-directly-from-the-triggerer) |
| 2024/02/17 | 💻 源來適你 | Intro to Airflow - From Zero to Hero | [slide](https://speakerdeck.com/leew/intro-to-airflow-from-zero-to-hero) |
| 2023/07/29 | 🇹🇼 COSCUP 2023 | Atomic Commits: An Easy & Proven Way to Manage & Automate Release Process | [slide](https://speakerdeck.com/leew/atomic-commits-an-easy-and-proven-way-to-manage-and-automate-release-process) · [recording](https://www.youtube.com/watch?v=IxzN9ClXhs8) |
| 2020/11/07 | 🇹🇼 Taichung.py | Python Table Manners | [slide](https://speakerdeck.com/leew/python-table-manners-at-taichung-dot-py) |
| 2020/10/16 | 🇹🇼 Hualien.py | Python Table Manners | [slide](https://speakerdeck.com/leew/python-table-manners-cut-the-cookie-gracefully-at-hualien-py) |
| 2020/08/31 | 🇹🇼 Kaohsiung.py | Python Table Manners | [slide](https://speakerdeck.com/leew/python-table-manners-cut-the-cookie-gracefully-at-kaohsiung-dot-py) |
| 2020/07/24 | 💻 EuroPython 2020 | Python Table Manners | [slide](https://speakerdeck.com/leew/python-table-manners-cut-the-cookie-gracefully-at-euro-python-2020) · [recording](https://www.youtube.com/watch?v=m6rF3Kah928) |
| 2020/06/18 | 🇹🇼 Taipei.py | commitizen-tools: What can we gain from crafting a git message convention? | [slide](https://speakerdeck.com/leew/commitizen-tools-what-can-we-gain-from-crafting-a-git-message-convention-at-taipey-dot-py) |
| 2020/04/25 | 💻 Remote Python Pizza 2020 | commitizen-tools: What can we gain from crafting a git message convention? | [slide](https://speakerdeck.com/leew/what-can-we-gain-from-crafting-a-git-message-convention-at-remote-python-pizza-2020) |
| 2019/11/17 | 🇨🇦 PyCon CA 2019 | Python Table Manners | [slide](https://speakerdeck.com/leew/python-table-manners-a-clean-style-at-pycon-ca-2019) |
| 2019/10/24 | 🇹🇼 Taipei.py | Python Table Manners | — |
| 2019/09/16 | 🇯🇵 PyCon JP 2019 | How to get more than PyCon in a PyCon | [slide](https://docs.google.com/presentation/d/1buthYkXvgjbrvb3CT9eXUKklRZOTPc4aN3RgH1PZayk/edit#slide=id.g5cf8cd871b_0_9) |
| 2019/03/24 | 🇹🇼 SITCON 2019 | X-Village - 用不到兩個月準備兩個月的課程 | [slide](https://speakerdeck.com/leew/x-village-yong-bu-dao-liang-ge-yue-zhun-bei-liang-ge-yue-de-ke-cheng) · [recording](https://www.youtube.com/watch?v=kf0KFyb-wcA) |
| 2018/08/16 | 🇹🇼 X-Village | CRUD in Flask | [slide](https://speakerdeck.com/leew/x-village-crud-in-flask-1) |
| 2018/03/12 | 🇹🇼 NCKU CSIE | Intro to Python Data Science Tools | [slide](https://github.com/Lee-W/Intro_to_Python_Data_Science_Tools/tree/v.20190312) |
| 2018/02/27 | 🇹🇼 NCKU CSIE | Intro to Python Data Science Tools | [slide](https://github.com/Lee-W/Intro_to_Python_Data_Science_Tools/tree/v.20180227) |
| 2017/01/22 | 🇹🇼 成大工資管營 | 資管講座 | [slide](https://speakerdeck.com/leew/chang-gong-zi-guan-de-yan-jiang) |
| 2016/12/08 | 🇹🇼 NCKU CSIE | Bot Development | [slide](https://hackmd.io/p/HkW8LjRfl) |
| 2016/11/03 | 🇹🇼 深度之夜 | Keras Demo | [slide](https://github.com/Lee-W/Keras-Mnist-Example) |

For more slides, check my [Speaker Deck](https://speakerdeck.com/leew/).

## Podcast / Show

* [PyCast](https://pycast.firstory.io/)
    1. [S4EP6｜ Python Taiwan 年會搞了 13 年，到底在 『稿』什麼？ feat. Andy Lee, Wei Lee, TengLin Yu](https://open.firstory.me/story/clz1c1b2c03m701vggil3837p)
    2. [S2EP4 | Emergence: 佛系經營社群的二三事，原來你我都是這片雪花的一部分 - Taihsiang & Wei](https://pycast.firstory.io/episodes/cl8pof56x05p901ws56y185jl)
    3. [EP2 | 職場邊緣人教你如何讓 WFH 變得更有趣](https://pycast.firstory.io/episodes/ckovh74d9nw2t0818urqtusva)
* [WFH Pythonista](https://www.youtube.com/playlist?list=PLCBCxsuKTqkDXxXKWnWzldHUvdYbpCLij)
    * [WFH Pythonista Ep#15 w/ David Lu and Wei Lee (PyCon Taiwan Organizers)](https://www.youtube.com/watch?v=JH5HQZIfY34)

## Development Sprints

* Apache Airflow
    1. [EuroPython 2025](https://github.com/EuroPython/website/pull/1437)
    2. [DurianPy](https://www.meetup.com/durianpy/events/308390476/)
    3. PyCon APAC 2025
    4. [PyCon TW 2024](https://hackmd.io/LKLr7XyOR9mK1AEEnvnCuQ#Apache-Airflow)
* commitizen-tools
    1. [scisprint Taipei 2026 January](https://sciwork.dev/sprint/2026/01-taipei)
    2. [PyCon US 2024](https://us.pycon.org/2024/events/dev-sprints/#sprint-3)
    3. [COSCUP 2024](https://pretalx.coscup.org/coscup-2024/talk/SDR77M/)
    4. [scisprint Taipei 2024 March](https://sciwork.kktix.cc/events/scisprint-202403-taipei)
    5. [PyCon TW 2023](https://hackmd.io/R98LEB4MSxm4AeExmxuZnA#commitizen-tools)
    6. [Scisprint@Amazon Taipei 2023](https://sciwork.kktix.cc/events/scisprint-202302-taipei)
    7. [PyCon TW 2022](https://hackmd.io/UYumgLy_QxaCSCqrXKDBpw#commitizen-tools)
    8. [PyCon TW 2021](https://hackmd.io/PAgYsu5nSHyERIRaUokWxQ#commitizen-tools)
    9. PyCon TW 2020
    10. PyCon CA 2019

## Awards

* 2025 IT Matters Awards 開源社群貢獻獎
* Honorable Mention, 2013 Railway Application Section Problem Solving Competition

## Publications

1. Wei Lee, Chien-Wei Chang, Po-An Yang, Chi-Hsuan Huang, Ming-Kuang Wu, Chu-Cheng Hsieh, Kun-Ta Chuang **["Effective Quality Assurance for Data Labels through Crowdsourcing and Domain Expert Collaboration"](https://openproceedings.org/2018/conf/edbt/paper-243.pdf)** 21st International Conference on Extending Database Technology, Demo Track (EDBT-2018)
2. I-Lin Wang, Wei Lee, Chiao-Yu Liao **"Effective Heuristics for Scheduling Hump and Pullback Engines in Railroad Yard Operational Plans"** Proceedings of the 10th Annual Conference of the Operations Research Society at Taiwan (ORSTW 2013)

## Education

**[2016 – 2018] Master, Computer Science and Information Engineering**
National Cheng Kung University, Tainan
GPA: 4.16 / 4.3

**[2011 – 2015] Bachelor, Industrial and Information Management**
**Double Major: Computer Science and Information Engineering**
National Cheng Kung University, Tainan
GPA: 3.77 / 4.0 (CSIE GPA: 3.87 / 4.0)
