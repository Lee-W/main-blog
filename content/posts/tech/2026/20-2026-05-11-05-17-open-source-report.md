Title: 2026/05/11 - 05/17 開源貢獻週報
Date: 2026-05-17 22:12 +0800
Category: Tech
Tags: Open Source, 開源貢獻週報
Slug: 2026-05-11-2026-05-17-open-source-report
Authors: Wei Lee
Lang: zh-tw

我以為我花了不少時間看 commitizen 的 PR ，其實並沒有......

<!--more-->

## commitizen-tools/commitizen
* 審閱 PRs
    1. [ci(deps): bump urllib3 from 2.6.3 to 2.7.0 #1992](https://github.com/commitizen-tools/commitizen/pull/1992)
    2. [test: skip invalidCommand argparse fixture on Python 3.14.5+ #1991](https://github.com/commitizen-tools/commitizen/pull/1991)
    3. [chore(CODEOWNERS): remove blanket-ownership file #1989](https://github.com/commitizen-tools/commitizen/pull/1989)

## Lee-W/bahamut_ani_stat
因為 token 還有剩，就花了一點點時間把原本爬蟲的 bug 修了
現在 [Plots - 巴哈姆特動畫瘋 - 歷史資料](https://lee-w.github.io/bahamut_ani_stat/plots/)，動畫列表跟觀看趨勢應該又是對的了

* 開 PRs
    1. [Fix plot command #175](https://github.com/Lee-W/bahamut_ani_stat/pull/175)
    2. [ci: doc publish fixing #174](https://github.com/Lee-W/bahamut_ani_stat/pull/174)
    3. [fix: fix new anime parsing broken by site HTML change and add request… #173](https://github.com/Lee-W/bahamut_ani_stat/pull/173)

## Lee-W/pelican-heatmap
我不想日更了，加了一個週更紀錄，放過自己的同時，但又不會像是斷了就沒了

* 新增 [feat(streak): add weekly streak stat alongside daily streak](https://github.com/Lee-W/pelican-heatmap/commit/29667d52afb340805e68d5d119627c8ff72db254)

## Lee-W/pelican-osm
為了讓之後的文章可以有辦法連結到產出來的資料表的某處，新增 [Add link anchor #15](https://github.com/Lee-W/pelican-osm/pull/15)
其他應該都是小修正

## pycontw/pycon-etl
* 開 PR
    1. [chore: hardening pass — CI tests, error handling, configs #199](https://github.com/pycontw/pycon-etl/pull/199): 燒了一些 token 整理一下歷史的技術債
* 重新把 [feat(discord): centralize Discord notifications via asset-driven Dag](https://github.com/pycontw/pycon-etl/pull/167) 寫過，但還沒有時間把它部署上去（需要手動改一些東西），先開著

## pycontw/pycontw-blog
* 審閱 PRs
    1. [new post: add 2026-05-15-cfp-postponed-to-june-1 #221](https://github.com/pycontw/pycontw-blog/pull/221)
