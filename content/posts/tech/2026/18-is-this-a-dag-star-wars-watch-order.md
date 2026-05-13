Title: 星際大戰的時序是不是一個 DAG
Date: 2026-05-13 22:30 +0800
Category: Tech
Tags: Airflow, Star Wars, Python
Slug: is-this-a-dag-star-wars-watch-order
Authors: Wei Lee
Lang: zh-tw

Dag 警察知法犯法！
你被逮捕了，逼波逼波 🚨

先等等，這裡指的真的是 DAG (有向無環圖)
而不是 Airflow 的 Dag，容我娓娓道來

<!--more-->

今天翻推特看到這個很酷的東西，就把它貼到社群裡跟大家分享

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">『スターウォーズの時系列』がこちらです… <a href="https://t.co/S0aNMqfDZc">pic.twitter.com/S0aNMqfDZc</a></p>&mdash; ʚ_ 𝙢𝙖𝙞_ɞ (@mai2004_cine) <a href="https://twitter.com/mai2004_cine/status/2054154676720087421?ref_src=twsrc%5Etfw">May 12, 2026</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

就社群夥伴被問了 It is good to drink？
阿不是啦，是

> 這是一個 DAG 嗎

我想應該是吧
順帶一提，從左上到右下是發行順序（我一開始沒發現）
不過本著實事求是的精神，我寫一個 Dag，讓 Airflow 幫我驗證這是不是真的是一個 DAG

把這張圖丟給 Claude Code ，它完全亂產一通，看來星戰的世界複雜到 Claude 也無法理解
不過也先驗證了我的一個假設，如果 Airflow 的 Dag 有環，是會出錯的

![AirflowDagCycleException](/images/posts-image/2026/is-this-a-dag-star-wars-watch-order/17786528033392.jpg)

因為整個 Dag 的程式碼很長，我把它摺疊起來，想看的自己點開

<!-- rumdl-disable -->
??? "Dag star_wars_watch_order"
    ```python
    from __future__ import annotations

    from datetime import datetime

    from airflow.sdk import chain, dag, task


    @dag(
        dag_id="star_wars_watch_order",
        description="Star Wars complete watch order",
        # start_date set to the earliest release date in the series: Star Wars: A New Hope 1977-05-25
        start_date=datetime(1977, 5, 25),
        schedule=None,
        catchup=False,
        tags=["star_wars", "watch_order"],
    )
    def star_wars_watch_order():
        @task(params={"release_date": "1977-05-25", "story_time": "0 ABY"})
        def star_wars_a_new_hope(**context):
            p = context["params"]
            print(f"▶ A New Hope (Episode IV) | release: {p['release_date']} | story: {p['story_time']}")

        @task(params={"release_date": "1980-05-21", "story_time": "3 ABY"})
        def the_empire_strikes_back(**context):
            p = context["params"]
            print(
                f"▶ The Empire Strikes Back (Episode V) | release: {p['release_date']} | story: {p['story_time']}"
            )

        @task(params={"release_date": "1983-05-25", "story_time": "4 ABY"})
        def return_of_the_jedi(**context):
            p = context["params"]
            print(f"▶ Return of the Jedi (Episode VI) | release: {p['release_date']} | story: {p['story_time']}")

        @task(params={"release_date": "1999-05-19", "story_time": "32 BBY"})
        def the_phantom_menace(**context):
            p = context["params"]
            print(f"▶ The Phantom Menace (Episode I) | release: {p['release_date']} | story: {p['story_time']}")

        @task(params={"release_date": "2002-05-16", "story_time": "22 BBY"})
        def attack_of_the_clones(**context):
            p = context["params"]
            print(
                f"▶ Attack of the Clones (Episode II) | release: {p['release_date']} | story: {p['story_time']}"
            )

        @task(params={"release_date": "2005-05-19", "story_time": "19 BBY"})
        def revenge_of_the_sith(**context):
            p = context["params"]
            print(
                f"▶ Revenge of the Sith (Episode III) | release: {p['release_date']} | story: {p['story_time']}"
            )

        @task(params={"release_date": "2008-08-15", "story_time": "~22 BBY"})
        def star_wars_the_clone_wars_film(**context):
            p = context["params"]
            print(f"▶ The Clone Wars (film) | release: {p['release_date']} | story: {p['story_time']}")

        @task(params={"release_date": "2008-10-03", "story_time": "~22-19 BBY"})
        def star_wars_the_clone_wars(**context):
            p = context["params"]
            print(f"▶ The Clone Wars (series) | release: {p['release_date']} | story: {p['story_time']}")

        @task(params={"release_date": "2014-10-03", "story_time": "~5-0 BBY"})
        def star_wars_rebels(**context):
            p = context["params"]
            print(f"▶ Star Wars: Rebels | release: {p['release_date']} | story: {p['story_time']}")

        @task(params={"release_date": "2015-12-18", "story_time": "34 ABY"})
        def the_force_awakens(**context):
            p = context["params"]
            print(f"▶ The Force Awakens (Episode VII) | release: {p['release_date']} | story: {p['story_time']}")

        @task(params={"release_date": "2016-12-16", "story_time": "0 BBY"})
        def rogue_one_a_star_wars_story(**context):
            p = context["params"]
            print(f"▶ Rogue One: A Star Wars Story | release: {p['release_date']} | story: {p['story_time']}")

        @task(params={"release_date": "2017-12-15", "story_time": "~34 ABY"})
        def star_wars_the_last_jedi(**context):
            p = context["params"]
            print(f"▶ The Last Jedi (Episode VIII) | release: {p['release_date']} | story: {p['story_time']}")

        @task(params={"release_date": "2018-05-25", "story_time": "~13-10 BBY"})
        def solo_a_star_wars_story(**context):
            p = context["params"]
            print(f"▶ Solo: A Star Wars Story | release: {p['release_date']} | story: {p['story_time']}")

        @task(params={"release_date": "2018-10-07", "story_time": "~34 ABY"})
        def star_wars_resistance(**context):
            p = context["params"]
            print(f"▶ Star Wars: Resistance | release: {p['release_date']} | story: {p['story_time']}")

        @task(params={"release_date": "2019-11-12", "story_time": "~9 ABY"})
        def the_mandalorian(**context):
            p = context["params"]
            print(f"▶ The Mandalorian S1 | release: {p['release_date']} | story: {p['story_time']}")

        @task(params={"release_date": "2019-12-20", "story_time": "35 ABY"})
        def the_rise_of_skywalker(**context):
            p = context["params"]
            print(
                f"▶ [GOAL] The Rise of Skywalker (Episode IX) | release: {p['release_date']} | story: {p['story_time']}"
            )

        @task(params={"release_date": "2020-01-26", "story_time": "~34 ABY"})
        def star_wars_resistance_finale(**context):
            p = context["params"]
            print(f"▶ Star Wars: Resistance Finale | release: {p['release_date']} | story: {p['story_time']}")

        @task(params={"release_date": "2020-10-30", "story_time": "~9 ABY"})
        def the_mandalorian_s2(**context):
            p = context["params"]
            print(f"▶ The Mandalorian S2 | release: {p['release_date']} | story: {p['story_time']}")

        @task(params={"release_date": "2021-05-04", "story_time": "~19 BBY"})
        def the_bad_batch(**context):
            p = context["params"]
            print(f"▶ Star Wars: The Bad Batch | release: {p['release_date']} | story: {p['story_time']}")

        @task(params={"release_date": "2021-12-29", "story_time": "~9 ABY"})
        def the_book_of_boba_fett(**context):
            p = context["params"]
            print(f"▶ The Book of Boba Fett | release: {p['release_date']} | story: {p['story_time']}")

        @task(params={"release_date": "2022-05-27", "story_time": "~9 BBY"})
        def obi_wan_kenobi(**context):
            p = context["params"]
            print(f"▶ Obi-Wan Kenobi | release: {p['release_date']} | story: {p['story_time']}")

        @task(params={"release_date": "2022-09-21", "story_time": "~5 BBY"})
        def andor(**context):
            p = context["params"]
            print(f"▶ Andor S1 | release: {p['release_date']} | story: {p['story_time']}")

        @task(params={"release_date": "2023-03-01", "story_time": "~9 ABY"})
        def the_mandalorian_s3(**context):
            p = context["params"]
            print(f"▶ The Mandalorian S3 | release: {p['release_date']} | story: {p['story_time']}")

        @task(params={"release_date": "2023-05-04", "story_time": "~232 BBY"})
        def young_jedi_adventures(**context):
            p = context["params"]
            print(f"▶ [START] Young Jedi Adventures | release: {p['release_date']} | story: {p['story_time']}")

        @task(params={"release_date": "2023-08-22", "story_time": "~9 ABY"})
        def ahsoka(**context):
            p = context["params"]
            print(f"▶ Star Wars: Ahsoka | release: {p['release_date']} | story: {p['story_time']}")

        @task(params={"release_date": "2024-06-04", "story_time": "~100 BBY"})
        def the_acolyte(**context):
            p = context["params"]
            print(f"▶ Star Wars: The Acolyte | release: {p['release_date']} | story: {p['story_time']}")

        @task(params={"release_date": "2024-12-03", "story_time": "~9 ABY"})
        def skeleton_crew(**context):
            p = context["params"]
            print(f"▶ Star Wars: Skeleton Crew | release: {p['release_date']} | story: {p['story_time']}")

        @task(params={"release_date": "2025-04-22", "story_time": "~5-0 BBY"})
        def andor_s2(**context):
            p = context["params"]
            print(f"▶ Andor S2 | release: {p['release_date']} | story: {p['story_time']}")

        @task(params={"release_date": "2026-04-06", "story_time": "~18 BBY"})
        def maul_shadow_lord(**context):
            p = context["params"]
            print(f"▶ Maul: Shadow Lord | release: {p['release_date']} | story: {p['story_time']}")

        @task(params={"release_date": "2026-05-22", "story_time": "9 ABY"})
        def the_mandalorian_and_grogu(**context):
            p = context["params"]
            print(f"▶ The Mandalorian and Grogu | release: {p['release_date']} | story: {p['story_time']}")

        # ── Dependencies (based on arrows in the chart) ──────────────────────────
        # Arrow direction = "watch A before B"

        chain(
            young_jedi_adventures(),
            the_acolyte(),
            the_phantom_menace(),
            attack_of_the_clones(),
            star_wars_the_clone_wars_film(),
            star_wars_the_clone_wars(),
            revenge_of_the_sith(),
            the_bad_batch(),
            maul_shadow_lord(),
            solo_a_star_wars_story(),
            obi_wan_kenobi(),
            star_wars_rebels(),
            andor(),
            andor_s2(),
            rogue_one_a_star_wars_story(),
            star_wars_a_new_hope(),
            the_empire_strikes_back(),
            return_of_the_jedi(),
            the_mandalorian(),
            the_mandalorian_s2(),
            the_book_of_boba_fett(),
            the_mandalorian_s3(),
            ahsoka(),
            skeleton_crew(),
            the_mandalorian_and_grogu(),
            star_wars_resistance(),
            the_force_awakens(),
            star_wars_resistance_finale(),
            star_wars_the_last_jedi(),
            the_rise_of_skywalker(),
        )


    star_wars_watch_order()
    ```


因為 Dag 很長，理所當然它渲染出來的圖片也是很長...

![star_wars_watch_order-graph-2](/images/posts-image/2026/is-this-a-dag-star-wars-watch-order/star_wars_watch_order-graph-2.png)


這樣就很難閱讀了，所以我改成 Airflow 的 [任務群組 (Task Group)](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html#taskgroups)
將它們透過年代分組
另外改變了 task_display_name ，讓任務 (Task) 顯示的名稱是故事本身

![Airflow Task Group: high_republic](/images/posts-image/2026/is-this-a-dag-star-wars-watch-order/17786583893858.jpg)
![Airflow Task Group: prequel](/images/posts-image/2026/is-this-a-dag-star-wars-watch-order/17786584021276.jpg)
![Airflow Task Group: original](/images/posts-image/2026/is-this-a-dag-star-wars-watch-order/17786584242808.jpg)
![Airflow Task Group: sequel](/images/posts-image/2026/is-this-a-dag-star-wars-watch-order/17786584387330.jpg)

這些透過年代分組的任務群組，本身也透過時序接在一起

![star_wars_watch_order-graph](/images/posts-image/2026/is-this-a-dag-star-wars-watch-order/star_wars_watch_order-graph.png)


??? "Dag star_wars_watch_order_by_era"
    ```python
    from __future__ import annotations

    from datetime import datetime

    from airflow.sdk import chain, dag, task, task_group


    def log_watch(context):
        p = context["params"]
        title = context["task"].task_display_name
        print(f"▶ {title} | release: {p['release_date']} | story: {p['story_time']}")


    @dag(
        dag_id="star_wars_watch_order_by_era",
        description="Star Wars complete watch order",
        # start_date set to the earliest release date in the series: Star Wars: A New Hope 1977-05-25
        start_date=datetime(1977, 5, 25),
        schedule=None,
        catchup=False,
        tags=["star_wars", "watch_order"],
    )
    def star_wars_watch_order():
        # ── High Republic (~232–100 BBY) ─────────────────────────────────────────

        @task_group(group_id="high_republic")
        def high_republic():
            @task(
                task_display_name="Star Wars: Young Jedi Adventures",
                params={"release_date": "2023-05-04", "story_time": "~232 BBY"},
            )
            def young_jedi_adventures(**context):
                log_watch(context)

            @task(
                task_display_name="Star Wars: The Acolyte",
                params={"release_date": "2024-06-04", "story_time": "~100 BBY"},
            )
            def the_acolyte(**context):
                log_watch(context)

            chain(young_jedi_adventures(), the_acolyte())

        # ── Prequel (~32–18 BBY) ───────────────────────────────
        @task_group(group_id="prequel")
        def prequel():
            @task(
                task_display_name="Star Wars: Episode I – The Phantom Menace",
                params={"release_date": "1999-05-19", "story_time": "32 BBY"},
            )
            def the_phantom_menace(**context):
                log_watch(context)

            @task(
                task_display_name="Star Wars: Episode II – Attack of the Clones",
                params={"release_date": "2002-05-16", "story_time": "22 BBY"},
            )
            def attack_of_the_clones(**context):
                log_watch(context)

            @task(
                task_display_name="Star Wars: The Clone Wars (film)",
                params={"release_date": "2008-08-15", "story_time": "~22 BBY"},
            )
            def star_wars_the_clone_wars_film(**context):
                log_watch(context)

            @task(
                task_display_name="Star Wars: The Clone Wars (series)",
                params={"release_date": "2008-10-03", "story_time": "~22-19 BBY"},
            )
            def star_wars_the_clone_wars(**context):
                log_watch(context)

            @task(
                task_display_name="Star Wars: Episode III – Revenge of the Sith",
                params={"release_date": "2005-05-19", "story_time": "19 BBY"},
            )
            def revenge_of_the_sith(**context):
                log_watch(context)

            @task(
                task_display_name="Star Wars: The Bad Batch",
                params={"release_date": "2021-05-04", "story_time": "~19 BBY"},
            )
            def the_bad_batch(**context):
                log_watch(context)

            @task(
                task_display_name="Maul: Shadow Lord",
                params={"release_date": "2026-04-06", "story_time": "~18 BBY"},
            )
            def maul_shadow_lord(**context):
                log_watch(context)

            chain(
                the_phantom_menace(),
                attack_of_the_clones(),
                star_wars_the_clone_wars_film(),
                star_wars_the_clone_wars(),
                revenge_of_the_sith(),
                the_bad_batch(),
                maul_shadow_lord(),
            )

        # ── Original (~19 BBY–4 ABY, incl. Dark Times) ───────────────────────────
        @task_group(group_id="original")
        def original():
            @task(
                task_display_name="Solo: A Star Wars Story",
                params={"release_date": "2018-05-25", "story_time": "~13-10 BBY"},
            )
            def solo_a_star_wars_story(**context):
                log_watch(context)

            @task(
                task_display_name="Obi-Wan Kenobi",
                params={"release_date": "2022-05-27", "story_time": "~9 BBY"},
            )
            def obi_wan_kenobi(**context):
                log_watch(context)

            @task(
                task_display_name="Star Wars: Rebels",
                params={"release_date": "2014-10-03", "story_time": "~5-0 BBY"},
            )
            def star_wars_rebels(**context):
                log_watch(context)

            @task(
                task_display_name="Andor (Season 1)",
                params={"release_date": "2022-09-21", "story_time": "~5 BBY"},
            )
            def andor(**context):
                log_watch(context)

            @task(
                task_display_name="Andor (Season 2)",
                params={"release_date": "2025-04-22", "story_time": "~5-0 BBY"},
            )
            def andor_s2(**context):
                log_watch(context)

            @task(
                task_display_name="Rogue One: A Star Wars Story",
                params={"release_date": "2016-12-16", "story_time": "0 BBY"},
            )
            def rogue_one_a_star_wars_story(**context):
                log_watch(context)

            @task(
                task_display_name="Star Wars: Episode IV – A New Hope",
                params={"release_date": "1977-05-25", "story_time": "0 ABY"},
            )
            def star_wars_a_new_hope(**context):
                log_watch(context)

            @task(
                task_display_name="Star Wars: Episode V – The Empire Strikes Back",
                params={"release_date": "1980-05-21", "story_time": "3 ABY"},
            )
            def the_empire_strikes_back(**context):
                log_watch(context)

            @task(
                task_display_name="Star Wars: Episode VI – Return of the Jedi",
                params={"release_date": "1983-05-25", "story_time": "4 ABY"},
            )
            def return_of_the_jedi(**context):
                log_watch(context)

            chain(
                solo_a_star_wars_story(),
                obi_wan_kenobi(),
                star_wars_rebels(),
                andor(),
                andor_s2(),
                rogue_one_a_star_wars_story(),
                star_wars_a_new_hope(),
                the_empire_strikes_back(),
                return_of_the_jedi(),
            )

        # ── Sequel (~9–35 ABY, incl. New Republic) ───────────────────────────────
        @task_group(group_id="sequel")
        def sequel():
            @task(
                task_display_name="The Mandalorian (Season 1)",
                params={"release_date": "2019-11-12", "story_time": "~9 ABY"},
            )
            def the_mandalorian(**context):
                log_watch(context)

            @task(
                task_display_name="The Mandalorian (Season 2)",
                params={"release_date": "2020-10-30", "story_time": "~9 ABY"},
            )
            def the_mandalorian_s2(**context):
                log_watch(context)

            @task(
                task_display_name="The Book of Boba Fett",
                params={"release_date": "2021-12-29", "story_time": "~9 ABY"},
            )
            def the_book_of_boba_fett(**context):
                log_watch(context)

            @task(
                task_display_name="The Mandalorian (Season 3)",
                params={"release_date": "2023-03-01", "story_time": "~9 ABY"},
            )
            def the_mandalorian_s3(**context):
                log_watch(context)

            @task(
                task_display_name="Star Wars: Ahsoka",
                params={"release_date": "2023-08-22", "story_time": "~9 ABY"},
            )
            def ahsoka(**context):
                log_watch(context)

            @task(
                task_display_name="Star Wars: Skeleton Crew",
                params={"release_date": "2024-12-03", "story_time": "~9 ABY"},
            )
            def skeleton_crew(**context):
                log_watch(context)

            @task(
                task_display_name="The Mandalorian & Grogu",
                params={"release_date": "2026-05-22", "story_time": "9 ABY"},
            )
            def the_mandalorian_and_grogu(**context):
                log_watch(context)

            @task(
                task_display_name="Star Wars: Resistance",
                params={"release_date": "2018-10-07", "story_time": "~34 ABY"},
            )
            def star_wars_resistance(**context):
                log_watch(context)

            @task(
                task_display_name="Star Wars: Episode VII – The Force Awakens",
                params={"release_date": "2015-12-18", "story_time": "34 ABY"},
            )
            def the_force_awakens(**context):
                log_watch(context)

            @task(
                task_display_name="Star Wars: Resistance (Finale)",
                params={"release_date": "2020-01-26", "story_time": "~34 ABY"},
            )
            def star_wars_resistance_finale(**context):
                log_watch(context)

            @task(
                task_display_name="Star Wars: Episode VIII – The Last Jedi",
                params={"release_date": "2017-12-15", "story_time": "~34 ABY"},
            )
            def star_wars_the_last_jedi(**context):
                log_watch(context)

            @task(
                task_display_name="Star Wars: Episode IX – The Rise of Skywalker",
                params={"release_date": "2019-12-20", "story_time": "35 ABY"},
            )
            def the_rise_of_skywalker(**context):
                log_watch(context)

            chain(
                the_mandalorian(),
                the_mandalorian_s2(),
                the_book_of_boba_fett(),
                the_mandalorian_s3(),
                ahsoka(),
                skeleton_crew(),
                the_mandalorian_and_grogu(),
                star_wars_resistance(),
                the_force_awakens(),
                star_wars_resistance_finale(),
                star_wars_the_last_jedi(),
                the_rise_of_skywalker(),
            )

        # ── Era chain ────────────────────────────────────────────────────────────
        chain(high_republic(), prequel(), original(), sequel())


    star_wars_watch_order()
    ```
<!-- rumdl-enable -->

得證星際大戰的故事時序是一個 DAG ，因為寫成 Airflow 的 Dag 並不會出現 AirflowDagCycleException
恩...
真的是這樣嗎？
能證明的其實只有推特上的那張圖是不是一個 DAG
這些故事間隨便就可以想到一堆環
像是複製人之戰[^1]第七季發生到一半，會接西斯大帝的復仇[^2]，然後會回到複製人之戰[^1]第七季的最後
所以星際大戰的時序是不是一個 DAG
我想它不是
但我被問的是「這是不是一個 DAG」
這裡的「這」指的是我貼的那張圖，所以我依然正確的回答了社群朋友的問題 😆

[^1]: [Clone Wars](https://www.disneyplus.com/browse/entity-314f14b4-b70a-4ec6-b634-2559f0b1f77e)
[^2]: [Star Wars: Revenge of the Sith (Episode III)](https://www.disneyplus.com/browse/entity-eb1e2c5f-69bf-4240-a61f-7ffc4e0311b3)
