Title: DurianPy - Apache Airflow Development Sprint
Subtitle: You were the chosen one!
Date: 2025-06-23 00:15
Category: Tech
Tags: Python, Airflow, Development Sprint, DurianPy
Slug: durianpy-apache-airflow-development-sprint
Authors: Wei Lee
Cover: /images/posts-image/2025-durianpy-apache-airflow-development-sprint/P1280744.JPG

First, I would like to thank Arnel for inviting me to the Airflow Development Sprint. It seems that the sprint I led at PyCon APAC 2025 in March was a success, encouraging him to host another in his hometown 🙌.

I also want to express my sincere gratitude to Dom, Emily, and Di-Di. You played a crucial role in making my experience in Davao memorable. My journey would not have been nearly as smooth and enjoyable without your assistance.

<!--more-->

## Before the Sprint

Honestly, I was somewhat concerned about my ability to lead a worthwhile event. It's not a small expense for both sides. However, if they believe I might be capable, then perhaps being a yes man this time might not be a bad idea.

## Development Sprint
Before this began, we had a brief chat with the DurianPy organizers. I had the honor of meeting the legendary Anakin Skywalker. I thought it was just a nickname for a Star Wars fan. It turns out to be his real name, but he hasn't yet stepped into the Star Wars world. During this year's Star Wars Celebration, I was also lucky to meet another Anakin Skywalker, Hayden Christensen. It was quite intriguing to meet two Anakins in a row.

![There is another](/images/posts-image/2025-durianpy-apache-airflow-development-sprint/17506004384785.jpg)

Even though Anakin is not a Star Wars fan, Sean is! We discussed our love for Rogue One, Andor, and Rebels. I shared some Star Wars novels that I truly enjoy. (👉 [星際大戰小說排名](https://travlog.wei-lee.me/pages/star-wars-novel-ranking.html))

It's a shame I didn't mention this quote to him in person.

> I have friends everywhere.

### What I did
I outlined the steps for initiating contributions to Airflow. This included instructions on setting up `breeze`, an overview of Airflow's high-level project structure, and guidance on identifying potential changes to create pull requests.

[🎤 Happening Now: D-Day!]

After that, I used my previous slide [Airflow 3.0 The First Glance] to introduce some of the new features in Airflow 3. DatasetAlias/AssetAlias is not an easy concept to describe 🤔. The second photo in this post (with my weird gesture) shows my attempt to explain it.

[🎙️ 𝗛𝗮𝗽𝗽𝗲𝗻𝗶𝗻𝗴 𝗡𝗼𝘄 | Introduction to Airflow 3.0]

I also discussed the Airflow instance we have in [PyCon Taiwan] - [pycon-etl] to demonstrate the power of ruff [AIR] rules. The PR [Upgrade to Airflow 3.0.2 #159], which I used for demonstration, was merged shortly after my presentation. 🙌

The rest of the time, I just sit there and see whether anyone needs my help. 👀

[📍 𝐇𝐚𝐩𝐩𝐞𝐧𝐢𝐧𝐠 𝐍𝐨𝐰: 𝐏𝐲𝐭𝐡𝐨𝐧 𝐒𝐩𝐫𝐢𝐧𝐭 – 𝐂𝐨𝐧𝐭𝐫𝐢𝐛𝐮𝐭𝐢𝐧𝐠 𝐭𝐨 𝐀𝐩𝐚𝐜𝐡𝐞 𝐀𝐢𝐫𝐟𝐥𝐨𝐰]

[Airflow 3.0 The First Glance]: https://speakerdeck.com/leew/20250328-airflow-3-dot-0-the-first-glance
[PyCon Taiwan]: https://tw.pycon.org/
[pycon-etl]: https://github.com/pycontw/pycon-etl
[Upgrade to Airflow 3.0.2 #159]: https://github.com/pycontw/pycon-etl/pull/159
[AIR]: https://docs.astral.sh/ruff/rules/#airflow-air
[🎤 Happening Now: D-Day!]: https://www.linkedin.com/posts/durianpy_durianpy-pythonsprint-opensourceph-activity-7342017222132801536-HQv-?rcm=ACoAAAwuJ3cBSUYBWI2zB_4HRnocCjUmJx9GzCg
[🎙️ 𝗛𝗮𝗽𝗽𝗲𝗻𝗶𝗻𝗴 𝗡𝗼𝘄 | Introduction to Airflow 3.0]: https://www.linkedin.com/posts/durianpy_durianpy-pythonsprint-davaotech-activity-7342029111814430720-FcQD?rcm=ACoAAAwuJ3cBSUYBWI2zB_4HRnocCjUmJx9GzCg
[📍 𝐇𝐚𝐩𝐩𝐞𝐧𝐢𝐧𝐠 𝐍𝐨𝐰: 𝐏𝐲𝐭𝐡𝐨𝐧 𝐒𝐩𝐫𝐢𝐧𝐭 – 𝐂𝐨𝐧𝐭𝐫𝐢𝐛𝐮𝐭𝐢𝐧𝐠 𝐭𝐨 𝐀𝐩𝐚𝐜𝐡𝐞 𝐀𝐢𝐫𝐟𝐥𝐨𝐰]: https://www.linkedin.com/posts/durianpy_durianpy-pythonsprint-davaotech-activity-7342090544518467585-jMXN?rcm=ACoAAAwuJ3cBSUYBWI2zB_4HRnocCjUmJx9GzCg

### What we achieved
* Pull requests created by the attendees
    1. [docs: fix grammar, spelling, and spacing in README #51980](https://github.com/apache/airflow/pull/51980)
    2. [fix(dev): guard missing --language if --add-missing is used in dev/i18n/check_translations_completeness.py #51981](https://github.com/apache/airflow/pull/51981)
        * I'm also an attendee. So technically, my PR counts ➕.
    3. [remove directed acyclic graphs #51982](https://github.com/apache/airflow/pull/51982)
        * **We finally get rid of the idea of directed acyclic graphs (DAGs) in Airflow!**
    4. [docs: update vertex AI generative model documentation #51983](https://github.com/apache/airflow/pull/51983)
    5. [refactor: remove dag.py params typechecking #51987](https://github.com/apache/airflow/pull/51987)
    6. [fix: add space to goto instances in contributors quick start #51985](https://github.com/apache/airflow/pull/51985)
    7. [docs: Format consistency for variables/directories/flags in unit_tests.rst #51986](https://github.com/apache/airflow/pull/51986)
    8. [docs: update remote logging configuration for Azure Blob Storage #51988](https://github.com/apache/airflow/pull/51988)
    9. [Add comma #51990](https://github.com/apache/airflow/pull/51990)
        * I don't even have a chance to take a look. Shahar beats me 🙌
* Other PRs I reviewed
    1. [Resolve OOM When Reading Large Logs in Webserver #49470](https://github.com/apache/airflow/pull/49470)
        * This consumes most of my energy. It's a huge PR with an awesome improvement. I'm really looking forward to its merging. 👀
    2. [fix(provider): Fix kwargs handling in Azure Data Lake Storage V2 Hook methods #51847](https://github.com/apache/airflow/pull/51847)
    3. [[Discord Provider] Add support to embeds in Discord Webhook and Notifier #51097](https://github.com/apache/airflow/pull/51097)

## One more thing
In the afternoon, I saw that Jarek and Shahar had started PR reviews. Jarek messaged me, mentioning that he noticed we were in a sprint. I then thought, why not invite him to share a few words with the DurianPy attendees? Jarek's encouragement was uplifting, and I hope it helps DurianPy's further growth.
When I served as the chair of [PyCon Taiwan], Jarek also helped us run a development sprint. Unfortunately, I couldn't participate at that time as I was leading commitizen-tools. Now, here I am, leading the Airflow development sprint.

## All about Davao
I truly appreciate my time here in Davao. It is a beautifully peaceful and cozy place. I was pleasantly surprised to find that I can even go on my anime pilgrimage here. (Thanks, Emily!) Davao is featured in the film [Mobile Suit Gundam: Hathaway's Flash](https://www.netflix.com/title/81439253). Dom took me to the most famous location shown in it. Although I haven't seen the movie yet, it's available on Netflix, so I should make time to watch it.

![P1280744](/images/posts-image/2025-durianpy-apache-airflow-development-sprint/P1280744.JPG)

![P1280750](/images/posts-image/2025-durianpy-apache-airflow-development-sprint/P1280750.JPG)

I considered eating at this specific Jollibee, but we have something even more exciting planned for later. We visited a local weekend market and enjoyed Filipino cuisine.

![913CCF6F-8048-486A-984C-EB3F20213009_1_105_c](/images/posts-image/2025-durianpy-apache-airflow-development-sprint/913CCF6F-8048-486A-984C-EB3F20213009_1_105_c.jpeg)

![EE8B4B7B-5A8D-4CE4-9FAF-FABC7530E59E_1_105_c](/images/posts-image/2025-durianpy-apache-airflow-development-sprint/EE8B4B7B-5A8D-4CE4-9FAF-FABC7530E59E_1_105_c.jpeg)

Fortunately, I still have the opportunity to grab some Jollibee for lunch during the sprint.

![5A7801F0-6986-470D-8B66-AFAA5257C424_1_105_c](/images/posts-image/2025-durianpy-apache-airflow-development-sprint/5A7801F0-6986-470D-8B66-AFAA5257C424_1_105_c.jpeg)

At dinner time, we went to a well-known local restaurant. This time, I remembered to bring my PyCon hat!

![101CFC4E-B12A-47C0-AE2C-56E0639AD4CF_1_105_c](/images/posts-image/2025-durianpy-apache-airflow-development-sprint/101CFC4E-B12A-47C0-AE2C-56E0639AD4CF_1_105_c.jpeg)

Here are the souvenirs I got: the t-shirt and tote bag from DurianPy, the adorable bubble tea doll from Charm, and some chocolate with unusual flavors that I had to buy.
(This time, I brought the Acrylic stand of Nina and Lancelot for traveling.)

![9D691FF9-5223-463A-9980-FD45060821A0_1_201_a](/images/posts-image/2025-durianpy-apache-airflow-development-sprint/9D691FF9-5223-463A-9980-FD45060821A0_1_201_a.heic)

before Dom dropped me off at the airport. These are the last gifts he shared with me. Thanks again, Dom!

![308E25B8-1B17-40EE-9294-0D333FBA4A46_1_105_c](/images/posts-image/2025-durianpy-apache-airflow-development-sprint/308E25B8-1B17-40EE-9294-0D333FBA4A46_1_105_c.jpeg)

and the trip concludes with Nina. I suppose we can regard it as somewhat similar to the Filipino beef bowl from Yoshinoya.

![3CE2D2C6-8FBE-4137-BD9F-401AB6B6ECAB_1_102_o](/images/posts-image/2025-durianpy-apache-airflow-development-sprint/3CE2D2C6-8FBE-4137-BD9F-401AB6B6ECAB_1_102_o.jpeg)

---

> You were the chosen one.
> It was said that you would take the T-shirt, not give it up.

At the close of the sprint, we had a lucky draw. Anakin was the first to be drawn. He truly is the chosen one in every regard.

![8AA26F8F-FE1D-4F04-B2F3-6BA6A3BA5A77_1_105_c](/images/posts-image/2025-durianpy-apache-airflow-development-sprint/8AA26F8F-FE1D-4F04-B2F3-6BA6A3BA5A77_1_105_c.jpeg)
