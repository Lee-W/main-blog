---
title: About Me
date: 2017-02-03 13:06
modified: 2025-10-21 22:55
slug: about-me
---

This is Wei Lee / 李唯. I'm a

* 🐍 [Pythonista](https://pycon-note.wei-lee.me/)
* 🐍 [PyCon Taiwan](https://tw.pycon.org/) organizer
* [commitizen-tools](https://github.com/commitizen-tools) maintainer
* [Apache Airflow](https://github.com/apache/airflow/) PMC Member, Taiwanese Mandarin Code Owner and Translation Owner
* `#apache-airflow` Mentor and Memebot Bot, `#commitizen` Mentor @ [OpenSource4You](https://github.com/opensource4you/)
* [📷 Traveler][travlog]
* ⛺ [台湾野クル▲](https://twitter.com/Taiwannokuru) 部員
* 📺 [Anime Lover](https://anilist.co/user/clleew/animelist/)
* 📖 Reader
* 🎵 Ukulele Player
* 🔒 Locker

I enjoy automating tedious tasks and creating high-quality code. Enjoy participating in open-source communities and contributing to open-source projects. Traveling is also a passion of mine, and I often use Python events as an opportunity to explore new places. I have attended PyCon Taiwan 🇹🇼, PyCon US 🇺🇸, PyCon JP 🇯🇵, PyCon CA 🇨🇦, Remote Python Pizza 💻, Euro Python 💻 🇨🇿, PyCon APAC 🇵🇭, and DurianPy 🇵🇭.

I share my technical notes, book digests, and occasional thoughts here. If you're interested in cooking, anime, and traveling, I chat about those things on [Those things no one cares about][travlog].

[travlog]: https://travlog.wei-lee.me/

---

You can find me through

* [![linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://in.linkedin.com/in/clleew)
* [![twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/clleew)
* [![github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Lee-W/)
* [![Mastodon](https://img.shields.io/mastodon/follow/109323826846876448?domain=mtd.pythonasia.org)

---

I use

* ![Neovim](https://img.shields.io/badge/NeoVim-%2357A143.svg?&style=for-the-badge&logo=neovim&logoColor=white)
* ![Sublime Text](https://img.shields.io/badge/sublime_text-%23575757.svg?style=for-the-badge&logo=sublime-text&logoColor=important)
* ![macOS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=macos&logoColor=F0F0F0)
* ![Firefox](https://img.shields.io/badge/Firefox-FF7139?style=for-the-badge&logo=Firefox-Browser&logoColor=white)
* ![Spotify](https://img.shields.io/badge/Spotify-1ED760?style=for-the-badge&logo=spotify&logoColor=white)
* ![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-017CEE?style=for-the-badge&logo=Apache%20Airflow&logoColor=white)

---

[TOC]

## Skill

* **Programming Language**: Python
* **Data Engineering**: Snowflake, Redis, SQLite, PostgreSQL, MySQL, Redshift
* **MLOps**: Apache Airflow, DVC, dbt, Great Expectations
* **Backend Development**: FastAPI, Flask, Django,
* **DevOps tools and others**: GitHub Actions, Docker, Kubernetes, Jenkins,  Git, AWS Services

## Work Experience
**[Aug 2024 - Current] Senior Software Engineer, [Astronomer]**

* [apache-airflow]
    * Add "DatasetAlias" for creating datasets or dataset events at runtime
    * Implement half of [AIP-74](https://cwiki.apache.org/confluence/display/AIRFLOW/AIP-74+Introducing+Data+Assets) and part of [AIP-75](https://cwiki.apache.org/confluence/display/AIRFLOW/AIP-75+New+Asset-Centric+Syntax)
    * Leading the implementation of [AIP-90](https://cwiki.apache.org/confluence/display/AIRFLOW/AIP-90+Human+in+the+loop)
* [ruff](https://github.com/astral-sh/ruff)
    * Implement most of the [AIR3XX](https://docs.astral.sh/ruff/rules/#airflow-air) rules to facilitate the migration from Airflow 2 to Airflow 3

**[Feb 2023 - July 2024] Software Engineer, [Astronomer]**

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

[Astronomer]: https://www.astronomer.io/

[apache-airflow]: https://github.com/apache/airflow/

**[Apr 2017 - Feb 2023] Machine Learning Engineer, [Rakuten USA](https://www.rakuten.com/)**

* Productionize machine learning projects
    * Implemented SQS and gRPC services for grouping emails with similar structures and extracting user-sensitive data to increase the amount of training data without violating customer privacy regulations.
    *  Designed and implemented a two-stage labeling system that automatically communicates between Amazon Mechanical Turk and in-house experts to generate high-quality labeled data and enhance merchandise taxonomy to increase customer conversion rate.
    * Migrated and automated the deployment process of AWS Lambda procedures that process customer lifetime value, reducing the effort of maintenance and deployment.
* Build and maintain data pipelines on [Apache Airflow]
    * Implemented a pipeline that processes data larger than 10 GB to infer personalized preferences to help increase customer satisfaction.
    * Migrated legacy 1.x Airflow server on AWS EC2 to 2.0.2 Airflow on AWS MWAA, saving developers' effort on dealing with legacy dependencies issues, and created a development Airflow environment for doing experiments without affecting the production pipeline.
    * Refactored the data writing mechanism and reduced the data write time and AWS S3 cost.
    * Built alerts and dashboards to monitor pipeline metrics, minimizing the effort of troubleshooting using DataDog, Prometheus, and Kibana.
* Standardize and maintain software engineering practices
    * Created and maintained the project templates, with automatic code quality check, testing, containerization, project versioning, releasing, and deployment, and a standard workflow for existing projects to update tools, which reduced project creation time, the communication overhead during code review, and provided an easy way for developers to introduce new standards.
    * Implemented a life-cycle configuration management tool and a workflow for creating Amazon Sagemaker notebook instances, which saves data scientists' time in handling engineering problems.
    * Improved container build time and reduced execution time by 70\% for Jenkins CI/CD pipelines.
    * Maintain the core package that's used among most existing projects
* Optimized SQL in a data pipeline and reduced the execution time from infeasible to within half a day.
* Cooperate with overseas teams in the US, Ukraine, and India

**[Jan 2019 - March 2019] Project Manager, [DLT Lab](https://dlt.csie.ncku.edu.tw)**

* Containerized and fixed legacy projects in [The Mosquito Man](https://github.com/the-mosquito-man)
* Introduced code review culture to a newly formed team
* Set up a [drone](https://github.com/drone/drone) CI/CD server and created CI pipelines for two ongoing projects

**[May 2018 - Nov 2018] Chief Teaching Assistant, [X-Village](https://www.facebook.com/X-Village-423736361424301/?ref=br_rs)**

* Managed the executive team with 16 members
* Organized two months of full-time courses and a one-semester 3-credit course
* Reviewed the teaching proposal of the Python course, "Programming Design Foundation"
* Designed exercises for "Data Structure," the first section of "Computer Science Foundations."
* Lectured on "Web Programming, Database/Cloud Computing," the fourth section of "Computer Science Foundations"

*X-Village* is an experimental education program designed to equip students who do not major in computer science with computational thinking skills and to foster future collaboration between computer science and other disciplines.

I was the program executor and the leader of the teaching assistant team. I also designed a half-day exercise for *Data Structure* and lectured on a four-hour web backend course for *Web Programming, Database/Cloud Computing*.

* [Website](https://sites.google.com/view/x-village/home?authuser=0)
* [Facebook Fan Page](https://www.facebook.com/X-Village-423736361424301/)

**[July 2015 - July 2016] Substitute Military Service, K-12 Education Administration, Ministry of Education**

* Maintained legacy systems implemented in multiple languages, including `C#`, `VBScript`, `PHP`, etc.
* Developed automation programs for generating reports, which save 80% of human labor time
* Delivered a human resource management system using [Django](https://www.djangoproject.com)

## Community Involvement
**[Nov 2023 - Current] Everywhere, [PyCon Taiwan](https://tw.pycon.org/)**

* Maintain [pycontw-blog]
* Upgrade [PyCon-ETL](https://github.com/pycontw/PyCon-ETL) from Airflow 1 to 3

**[Nov 2022 - Sep 2023] Marketing Team Lead, [PyCon Taiwan 2023](https://tw.pycon.org/2023/)**

* Migrated PyCon Taiwan Blog to [pycontw-blog] / <https://conf.python.tw>

**[Nov 2021 - Sep 2022] Vice-Chairperson, [PyCon APAC 2022](https://tw.pycon.org/2022/)**

* Coordinated three squads, including planning, sponsorship, and social media
* Hosted the first Ask Me Anything event to promote the Call for Proposals

**[Oct 2020 - Nov 2021] Chairperson, [PyCon Taiwan 2021](https://tw.pycon.org/2021/)**

* Coordinated 9 teams and hosted the first online PyCon TW with 550 participants

**[Dec 2019 - Sep 2020] Program Chair, [PyCon Taiwan 2020](https://tw.pycon.org/2020/)**

* Coordinated around 20 team members and introduced community tracks and a speaker-dispatch program to increase the interaction between local communities.

**[Jul 2019 – Nov 2019] Program Committee Member, [PyCon Taiwan 2019](https://tw.pycon.org/2019)**

* Contact keynote speakers and financial aid applicants
* Contribute to the [post-event report generator](https://github.com/pycontw/pycontw-postevent-report-generator)

[pycontw-blog]: https://github.com/pycontw/pycontw-blog

## Talk and Tutorial
* Seamless Migration: Leveraging Ruff for a Smooth Transition from Airflow 2 to Airflow 3
    * **2025/10/08** 🇺🇸 - [Airflow Summit 2025](https://airflowsummit.org/sessions/2025/seamless-migration-leveraging-ruff-for-a-smooth-transition-from-airflow-2-to-airflow-3/) → [slide](https://drive.google.com/file/d/1_2cxR8uOtWOphPPUD3IuwuRPcIBU4DXV/view?usp=drive_link)
* Unlocking the Future of Data Pipelines - Apache Airflow 3
    * **2025/09/06** 🇹🇼 - [PyCon TW 2025](https://tw.pycon.org/2025/en-us/conference/talk/366) → [slide](https://speakerdeck.com/leew/unlocking-the-future-of-data-pipeline-942ed56f-0083-4e25-9e30-04850095e824)
* Hold on! You have a data team in PyCon Taiwan!
    1. **2025/07/18** 🇨🇿 - [EuroPython 2025](https://ep2025.europython.eu/session/hold-on-you-have-a-data-team-in-pycon-taiwan) → [slide](https://speakerdeck.com/leew/hold-on-you-have-a-data-team-in-pycon-taiwan)
* 朝聖之旅
    1. **2025/06/11** 🇹🇼 - 工程師的搜尋紀錄 → [slide](https://speakerdeck.com/leew/zhao-sheng-zhi-lu)
* Airflow 3.0 The First Glance
    1. **2025/03/28** 🇹🇼 [黃金流沙饅頭營](https://www.icloud.com/pages/0c6_qp3_RnuCJfcIh8_9xnqLA#2025_%E9%BB%83%E9%87%91%E6%B5%81%E6%B2%99%E9%A5%85%E9%A0%AD%E7%87%9F) → [slide](https://speakerdeck.com/leew/20250328-airflow-3-dot-0-the-first-glance)
* 踏入開源的第一步
    1. **2025/03/16** 💻 NetDB - Tech Day, Invited Talk  → [slide](https://speakerdeck.com/leew/20250316-ta-ru-kai-yuan-de-di-bu)
* Unleash the Chaos: Developing a Linter for Un-Pythonic Code!
    1. **2025/03/02** 🇵🇭 [PyCon APAC 2025](https://pycon-apac.python.ph/) → [slide](https://speakerdeck.com/leew/unleash-the-chaos-developing-a-linter-for-un-pythonic-code-806b2bae-e161-4762-b0d5-d9fb8efdd24a), [🎬recording](https://www.youtube.com/watch?v=tbSZx0UsWfQ)
    2. **2024/09/21** 🇹🇼 [PyCon TW 2024](https://tw.pycon.org/2024/conference/talk/311) → [slide](https://speakerdeck.com/leew/unleash-the-chaos-developing-a-linter-for-un-pythonic-code), [🎬recording](https://www.youtube.com/watch?v=2jUd0o8VuE0)
* Unlocking Python's Core Magic
    1. **2024/09/28** 🇯🇵 [PyCon JP 2024](https://2024.pycon.jp/en/talk/AQKFHX) → [slide](https://speakerdeck.com/leew/unlocking-pythons-core-magic), [🎬recording](https://www.youtube.com/watch?v=9jbHA6tE9MM)
* What If...? Running Airflow Tasks without the workers
    1. **2024/09/11** 🇺🇸 [Airflow Summit 2024](https://airflowsummit.org/sessions/2024/what-if-running-airflow-tasks-without-the-workers/) → [slide](https://docs.google.com/presentation/d/1XGd7bQg6cGLNbHFiZjX__SmI4FLw6D_iASY9eRSO4mo/edit?usp=sharing), [🎬recording](https://www.youtube.com/watch?v=WkljjYtqu8Q)
* Starts Airflow task execution directly from the triggerer
    1. *2024/05/08* 💻 Airflow Town Hall → [slide](https://speakerdeck.com/leew/starts-airflow-task-execution-directly-from-the-triggerer)
* Intro to Airflow - From Zero to Hero
    1. *2024/02/17* 💻 [源來適你](https://www.facebook.com/opensource4you) → [slide](https://speakerdeck.com/leew/intro-to-airflow-from-zero-to-hero)
* Atomic Commits: An Easy & Proven Way to Manage & Automate Release Process
    1. **2023/07/29** 🇹🇼 [COSCUP 2023](https://coscup.org/2023/zh-TW/session/TUGLJP) → [slide](https://speakerdeck.com/leew/atomic-commits-an-easy-and-proven-way-to-manage-and-automate-release-process), [🎬recording](https://www.youtube.com/watch?v=IxzN9ClXhs8)
* Python Table Manners
    1. *2020/11/07* 🇹🇼 [Taichung.py](https://taichung-py.kktix.cc/events/meetup-202011-clleew) → [slide](https://speakerdeck.com/leew/python-table-manners-at-taichung-dot-py)
    2. *2020/10/16* 🇹🇼 [Hualien.py](https://www.meetup.com/Hualien-Py/events/273609065/) → [slide](https://speakerdeck.com/leew/python-table-manners-cut-the-cookie-gracefully-at-hualien-py)
    3. *2020/08/31* 🇹🇼 [Kaohsiung.py](https://kaohsiungpy.kktix.cc/events/20200831) → [slide](https://speakerdeck.com/leew/python-table-manners-cut-the-cookie-gracefully-at-kaohsiung-dot-py)
    4. **2020/07/24 💻 [Euro Python 2020](https://ep2020.europython.eu/)** → [slide](https://speakerdeck.com/leew/python-table-manners-cut-the-cookie-gracefully-at-euro-python-2020), [🎬recording](https://www.youtube.com/watch?v=m6rF3Kah928)
    5. **2019/11/17 🇨🇦 [PyCon CA 2019](https://2019.pycon.ca/)** → [slide](https://speakerdeck.com/leew/python-table-manners-a-clean-style-at-pycon-ca-2019)
    6. *2019/10/24* 🇹🇼 [Taipei.py](https://www.meetup.com/Taipei-py/events/265743666/)
* commitizen-tools: What can we gain from crafting a git message convention?
    1. *2020/06/18* 🇹🇼 [Taipei.py](https://www.meetup.com/Taipei-py/events/271185591/) → [slide](https://speakerdeck.com/leew/commitizen-tools-what-can-we-gain-from-crafting-a-git-message-convention-at-taipey-dot-py)
    2. **2020/04/25 💻 [Remote Python Pizza 2020](https://remote.python.pizza/)** → [slide](https://speakerdeck.com/leew/what-can-we-gain-from-crafting-a-git-message-convention-at-remote-python-pizza-2020)
* How to get more than PyCon in a PyCon
    1. **2019/09/16 🇯🇵 [PyCon JP 2019](https://pycon.jp/2019/) - Peer Reviewed Lightning Talk** → [slide](https://docs.google.com/presentation/d/1buthYkXvgjbrvb3CT9eXUKklRZOTPc4aN3RgH1PZayk/edit#slide=id.g5cf8cd871b_0_9)
* X-Village - 用不到兩個月準備兩個月的課程
    1. **2019/03/24 🇹🇼 [SITCON 2019](https://sitcon.org/2019)** → [slide](https://speakerdeck.com/leew/x-village-yong-bu-dao-liang-ge-yue-zhun-bei-liang-ge-yue-de-ke-cheng), [🎬recording](https://www.youtube.com/watch?v=kf0KFyb-wcA)
* Intro to Python Data Science Tools
    1. *2018/03/12* 🇹🇼 NCKU CSIE - Competitions in Data Sciences and Artificial Intelligence → [slide](https://github.com/Lee-W/Intro_to_Python_Data_Science_Tools/tree/v.20190312)
    2. *2018/02/27* 🇹🇼 NCKU CSIE - Competitions in Data Sciences and Artificial Intelligence → [slide](https://github.com/Lee-W/Intro_to_Python_Data_Science_Tools/tree/v.20180227)
* CRUD in Flask
    1 .*2018/08/16* 🇹🇼 [X-Village](https://sites.google.com/view/x-village/home?authuser=0) - Web Course → [slide](https://speakerdeck.com/leew/x-village-crud-in-flask-1)
* 資管講座 (一場工資管營的演講)
    1. *2017/01/22* 2018成大工資管營 → [slide](https://speakerdeck.com/leew/chang-gong-zi-guan-de-yan-jiang)
* Bot Development
    1. *2016/12/08* 🇹🇼 NCKU CSIE - Introduction to Knowledge Discovery and Data Engineering → [slide](https://hackmd.io/p/HkW8LjRfl)
* Keras Demo
    1. *2016/11/03* 🇹🇼 [深度之夜](https://ncku-ccs.kktix.cc/events/97f7bd96) → [slide](https://github.com/Lee-W/Keras-Mnist-Example)

For more slides, please check my [Speaker Deck](https://speakerdeck.com/leew/).

## Podcast / Show
* [PyCast](https://pycast.firstory.io/)
    1. [S4EP6｜ Python Taiwan 年會搞了 13 年，到底在 『稿』什麼？ feat. Andy Lee, Wei Lee, TengLin Yu](https://open.firstory.me/story/clz1c1b2c03m701vggil3837p)
    2. [S2EP4 | Emergence: 佛系經營社群的二三事，原來你我都是這片雪花的一部分 - Taihsiang & Wei](https://pycast.firstory.io/episodes/cl8pof56x05p901ws56y185jl)
    3. [EP2 | 職場邊緣人教你如何讓 WFH 變得更有趣](https://pycast.firstory.io/episodes/ckovh74d9nw2t0818urqtusva)
* [WFH Pythonista](https://www.youtube.com/playlist?list=PLCBCxsuKTqkDXxXKWnWzldHUvdYbpCLij)
    * [WFH Pythonista Ep#15 w/ David Lu and Wei Lee (PyCon Taiwan Organizers)](https://www.youtube.com/watch?v=JH5HQZIfY34)

## Development Sprint
* Apache Airflow
    1. [EuroPython 2025](https://github.com/EuroPython/website/pull/1437)
    2. [DurianPy](https://www.meetup.com/durianpy/events/308390476/)
    3. PyCon APAC 2025
    4. [PyCon TW 2024](https://hackmd.io/LKLr7XyOR9mK1AEEnvnCuQ#Apache-Airflow)
* commitizen-tools
    1. [PyCon US 2024](https://us.pycon.org/2024/events/dev-sprints/#sprint-3)
    2. [COSCUP 2024](https://pretalx.coscup.org/coscup-2024/talk/SDR77M/)
    3. [scisprint Taipei 2024 March](https://sciwork.kktix.cc/events/scisprint-202403-taipei)
    4. [PyCon TW 2023](https://hackmd.io/R98LEB4MSxm4AeExmxuZnA#commitizen-tools)
    5. [Scisprint@Amazon Taipei 2023](https://sciwork.kktix.cc/events/scisprint-202302-taipei)
    6. [PyCon TW 2022](https://hackmd.io/UYumgLy_QxaCSCqrXKDBpw#commitizen-tools)
    7. [PyCon TW 2021](https://hackmd.io/PAgYsu5nSHyERIRaUokWxQ#commitizen-tools)
    8. PyCon TW 2020
    9. PyCon CA 2019

## Award
* Honorable Mention, 2013 Railway Application Section Problem Solving Competition

## Publication
1. Wei Lee, Chien-Wei Chang, Po-An Yang, Chi-Hsuan Huang, Ming-Kuang Wu, Chu-Cheng Hsieh, Kun-Ta Chuang **["Effective Quality Assurance for Data Labels through Crowdsourcing and Domain Expert Collaboration"](https://openproceedings.org/2018/conf/edbt/paper-243.pdf)** 21st International Conference on Extending Database Technology, Demo Track (EDBT-2018)
2. I-Lin Wang, Wei Lee,  Chiao-Yu Liao **"Effective Heuristics for Scheduling Hump and Pullback Engines in Railroad Yard Operational Plans"** Proceedings of the 10th Annual Conference of the Operations Research Society at Taiwan (ORSTW 2013)

## Education
[2016-2018]
**Master, Computer Science and Information Engineering**
National Cheng Kung University, Tainan
GPA: 4.16/4.3

[2011-2015]
**Bachelor, Industrial and Information Management**
**Double Major: Computer Science and Information Engineering**
National Cheng Kung University, Tainan
GPA: 3.77/4.0 (CSIE GA: 3.87/4.0)

## Tutorial and Study Note

### Slide
* [Git Tutorial](https://github.com/Lee-W/git-tutorial)
    * example: [Git-Tutorial-Sample](https://github.com/Lee-W/Git-Tutorial-Sample)

### Book Notes
* [Learning Python 5e Note](https://github.com/Lee-W/Learning_Python)
* [Python Cookbook](https://github.com/Lee-W/Python_Cookbook)
* [The Clean Code](http://wei-lee.me/posts/tech/2018/11/the-clean-code/)
* [The Clean Coder](http://wei-lee.me/posts/tech/2018/11/the-clean-coder/)

### MOOCs Note
* [Machine Learning (Coursera)](https://github.com/Lee-W/Machine-Learning-Coursera)
* [Intro to Machine Learning](https://github.com/Lee-W/Intro_to_Machine_Learning_Udacity)
* [Intro to Data Science Udacity](https://github.com/Lee-W/Intro_to_Data_Science_Udacity)
* [Assignments for Udacity Deep Learning class with TensorFlow](https://github.com/Lee-W/Deep-Learning-Udacity)

[Apache Airflow]: https://airflow.apache.org/
