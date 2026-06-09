Title: CV
Date: 2026-04-17 00:00 +0800
Modified: 2026-06-09 18:00 +0800
Slug: cv
Lang: en

[TOC]

Apache Airflow [PMC member](https://projects.apache.org/committee.html?airflow) and committer, and Senior Software Engineer with 9 years of experience. Leads major platform features (multiple AIPs) and the Airflow 2-to-3 migration tooling, mentors contributors into committers, and speaks at international conferences. Experienced working across globally distributed teams in the US, Europe, and Asia. Background in data engineering and MLOps; recipient of the 2025 IT Matters Open Source Community Contribution Award.

## Skills

* **Programming Language**: Python, Rust
* **Data Engineering**: Snowflake, Redis, SQLite, PostgreSQL, MySQL, Redshift
* **MLOps**: Apache Airflow, DVC, dbt, Great Expectations
* **Backend Development**: FastAPI, Flask, Django
* **DevOps**: GitHub Actions, Docker, Kubernetes, Jenkins, Git; AWS (S3, Lambda, EC2, MWAA, SageMaker, SQS)

## Work Experience

**[Aug 2024 – Present] Senior Software Engineer, [Astronomer]**

* [apache-airflow] (Apache Software Foundation top-level project) — committer and Project Management Committee (PMC) member
    * Contribute to project governance, release management, and technical direction as a PMC member; one of its most active contributors and reviewers, with 500+ commits
    * Drove the implementation of [AIP-76](https://cwiki.apache.org/confluence/display/AIRFLOW/AIP-76+Asset+Partitions) (Asset Partitions — processing large datasets partition by partition), first released in Airflow 3.2.0 and completing in 3.3.0, including the partition and temporal mappers and backfill support; to be presented at [Airflow Summit 2026](https://airflowsummit.org/sessions/2026/asset-partitions-matching-workflow-to-the-right-data/)
    * Led the end-to-end design and backend implementation of [AIP-90](https://cwiki.apache.org/confluence/display/AIRFLOW/AIP-90+Human+in+the+loop) (Human in the Loop — letting data pipelines pause for human review or input), delivered in Airflow 3.1.0, collaborating with PMC members and community contributors and demoing at Airflow dev calls and town halls
    * Designed and implemented [AIP-74](https://cwiki.apache.org/confluence/display/AIRFLOW/AIP-74+Introducing+Data+Assets) and part of [AIP-75](https://cwiki.apache.org/confluence/display/AIRFLOW/AIP-75+New+Asset-Centric+Syntax) (Data Assets — a flagship Airflow 3 redesign of how pipelines declare the data they produce and consume), unblocking the asset features for Airflow 3
    * Designed and implemented "DatasetAlias" (shipped in 2.10.0) for creating datasets or dataset events at runtime
    * Stepped in to deliver the authentication layer of [AIP-84](https://cwiki.apache.org/confluence/display/AIRFLOW/AIP-84+UI+REST+API) (UI REST API), driving the implementation with the community when it became critical and the team was stretched thin
    * Contributed across core Airflow 3 components, including the Task SDK (asset events / `inlet_events`), mapped operators, task groups, and the SQLite metadata DB migration
    * Added missing Taiwanese Mandarin translations to Airflow's i18n
* [ruff](https://github.com/astral-sh/ruff)
    * Led the development of the automated Airflow 2-to-3 migration tooling — a critical lever for Airflow 3 adoption — implementing 100+ auto-fixing Rust lint rules ([AIR3XX](https://docs.astral.sh/ruff/rules/#airflow-air)) that let users upgrade with minimal manual effort; built with the Astral team and presented at [Airflow Summit 2025](https://airflowsummit.org/sessions/2025/seamless-migration-leveraging-ruff-for-a-smooth-transition-from-airflow-2-to-airflow-3/)
* Mentored multiple community members into Apache Airflow committers and grew an Airflow OSS community in Taiwan

**[Feb 2023 – Jul 2024] Software Engineer, [Astronomer]**

* [apache-airflow]
    * Optimized task scheduling by allowing deferrable tasks to execute directly from the triggerer (Airflow's component for efficient asynchronous task execution), bypassing the worker; presented this work at [Airflow Summit 2024](https://airflowsummit.org/sessions/2024/what-if-running-airflow-tasks-without-the-workers/)
    * Added REST API endpoint to manipulate queued dataset events
    * Added `default_deferrable` configuration for easily turning on the deferrable mode of operators
    * Added Azure Managed Identity support to apache-airflow-providers-microsoft-azure (Microsoft Liftr project) for near-credential-free authentication
    * Upgraded apache-airflow-providers-weaviate to 2.0.0 for weaviate-client >= 4.4.0 support
* [astronomer-providers](https://github.com/astronomer/astronomer-providers)
    * Led the deprecation of this project (125+ PRs), contributing existing operators/sensors back to [apache-airflow] to reduce maintenance efforts
    * Automated the provider release-candidate verification and release process, and the integration test deployment ([#987](https://github.com/astronomer/astronomer-providers/pull/987), [#1107](https://github.com/astronomer/astronomer-providers/pull/1107), [#1139](https://github.com/astronomer/astronomer-providers/pull/1139), [#1110](https://github.com/astronomer/astronomer-providers/pull/1110))
* [ask-astro](https://github.com/astronomer/ask-astro)
    * Built data-ingestion pipelines (Stack Overflow, astro-cli, blog content) feeding ask-astro's LLM/RAG knowledge base, added request metric tracking and answer-retry reliability, and set up its dev tooling, docs, and CI

**[Apr 2017 – Feb 2023] Machine Learning Engineer, [Rakuten USA](https://www.rakuten.com/)**

* Productionized machine learning projects
    * Implemented SQS and gRPC services for grouping emails with similar structures and extracting user-sensitive data to increase the amount of training data without violating customer privacy regulations
    * Designed and implemented a two-stage labeling system that automatically communicates between Amazon Mechanical Turk and in-house experts to generate high-quality labeled data and enhance merchandise taxonomy to increase customer conversion rate
    * Migrated and automated the deployment process of AWS Lambda procedures that process customer lifetime value, reducing the effort of maintenance and deployment
* Built and maintained data pipelines on [Apache Airflow](https://airflow.apache.org/)
    * Implemented a pipeline that processes data larger than 10 GB to infer personalized preferences to help increase customer satisfaction
    * Migrated legacy 1.x Airflow server on AWS EC2 to 2.0.2 Airflow on AWS MWAA, saving developers' effort on dealing with legacy dependencies issues, and created a development Airflow environment for doing experiments without affecting the production pipeline
    * Refactored the data writing mechanism and reduced the data write time and AWS S3 cost
    * Built alerts and dashboards to monitor pipeline metrics, minimizing the effort of troubleshooting using DataDog, Prometheus, and Kibana
* Standardized and maintained software engineering practices
    * Created and maintained the project templates, with automatic code quality check, testing, containerization, project versioning, releasing, and deployment, and a standard workflow for existing projects to update tools, which reduced project creation time, the communication overhead during code review, and provided an easy way for developers to introduce new standards
    * Implemented a life-cycle configuration management tool and a workflow for creating Amazon Sagemaker notebook instances, which saves data scientists' time in handling engineering problems
    * Improved container build time and reduced execution time by 70% for Jenkins CI/CD pipelines
    * Maintained the core package that was used among most existing projects
* Optimized SQL in a data pipeline and reduced the execution time from infeasible to within half a day
* Cooperated with overseas teams in the US, Ukraine, and India

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

* Contacted keynote speakers and financial aid applicants
* Contributed to the [post-event report generator](https://github.com/pycontw/pycontw-postevent-report-generator)

[pycontw-blog]: https://github.com/pycontw/pycontw-blog

## Talks

{% table data/talks.yaml fields="date,event,title,slide,recording" sort_by="date" sort_order="desc" group_by="date:year" group_summary_at="date:year" date_format="%m/%d" field_labels="date:Date,event:Event,title:Title,slide:Slide,recording:Recording" aria_columns="slide,recording" %}

For more slides, check my [Speaker Deck](https://speakerdeck.com/leew/).

## Podcast / Show

* [PyCast](https://pycast.firstory.io/)
    1. [S4EP6｜ Python Taiwan 年會搞了 13 年，到底在 『稿』什麼？ feat. Andy Lee, Wei Lee, TengLin Yu](https://open.firstory.me/story/clz1c1b2c03m701vggil3837p)
    2. [S2EP4 | Emergence: 佛系經營社群的二三事，原來你我都是這片雪花的一部分 - Taihsiang & Wei](https://pycast.firstory.io/episodes/cl8pof56x05p901ws56y185jl)
    3. [EP2 | 職場邊緣人教你如何讓 WFH 變得更有趣](https://pycast.firstory.io/episodes/ckovh74d9nw2t0818urqtusva)
* [WFH Pythonista](https://www.youtube.com/playlist?list=PLCBCxsuKTqkDXxXKWnWzldHUvdYbpCLij)
    * [WFH Pythonista Ep#15 w/ David Lu and Wei Lee (PyCon Taiwan Organizers)](https://www.youtube.com/watch?v=JH5HQZIfY34)

## Development Sprints

{% table data/sprints.yaml fields="event,link" group_by="project" group_summary_at="project" field_labels="event:Event,link:Link" aria_columns="link" %}

## Awards

* 2025 IT Matters Awards 開源社群貢獻獎 — awardees were [received by the President of Taiwan](https://www.president.gov.tw/News/39967)
* [Honorable Mention, 2013 Railway Application Section Problem Solving Competition](https://ilin.iim.ncku.edu.tw/files/ilinwang_NCKU_INFORMS_RAS2013_newsletter%208.pdf)

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
