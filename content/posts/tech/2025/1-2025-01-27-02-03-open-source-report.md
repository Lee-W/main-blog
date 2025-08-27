Title: 2025/01/27 - 02/03 開源貢獻週報
Subtitle: 我愛慕虛榮啦
Date: 2025-02-02 21:00
Category: Tech
Tags: Open Source, 開源貢獻週報
Slug: 2025-01-27-02-03-open-source-report
Authors: Wei Lee
Cover: /images/meme/mygo-vanity.jpg

今年想做個新的嘗試
每週記錄工作以外，我在開源專案的貢獻
能看到自己量化的前進，就會有多一點動力繼續下去

<!--more-->

[原子習慣]({filename}/posts/book/2020/1-atomic-habit.md#16)將這樣的概念稱為習慣追蹤器
這本書真的很棒推薦給大家
如果看過了，再推薦一本更棒，但難啃一點的[為什麼我們這樣生活，那樣工作?]({filename}/posts/book/2015/08-the-power-of-habit.md)

如果只是要記錄，寫在筆記就好了，幹嘛還要發一篇文章呢？
這也是源自[原子習慣]({filename}/posts/book/2020/1-atomic-habit.md#17)的概念 - 問責夥伴
不過追根究底可能就跟聖愛音一樣

![mygo-vanity](/images/meme/mygo-vanity.jpg)

這週因為過年所以特別多
下週以後就不知道了
希望這個週報不要只有一回......

[TOC]

## commitizen
commitizen 是我認真進入開源很重要的開始，是我很有感情的專案
每次都想要好好整理它，無奈時間實在有限
這週花了點時間看了堆積已久的 PR ，把所有[pr-status: wait-for-review](https://github.com/commitizen-tools/commitizen/pulls?q=is%3Apr+is%3Aopen+label%3A%22pr-status%3A+wait-for-review%22)都看完了
現在還有這個 label 的應該都是我改過的 PR ，要等其他 maintainer 看

1. [Feature/multi language commitizen #1328](https://github.com/commitizen-tools/commitizen/pull/1328)
2. [fix(commands/bump): prevent using incremental changelog when it is set to false in config #996](https://github.com/commitizen-tools/commitizen/pull/996)
3. [feat: add custom validation #1236](https://github.com/commitizen-tools/commitizen/pull/1236)
4. [feat(commit): implement questions 'filter' support with handlers #1207](https://github.com/commitizen-tools/commitizen/pull/1207)
5. [feat(tags): adds legacy_tag_formats and ignored_tag_formats settings #1297](https://github.com/commitizen-tools/commitizen/pull/1297)

有些遠古 PR ，因為拖太久沒看，貢獻者可能已經不會回來了
所以我也撿了一些起來修

1. [feat: add --allow-no-commit option #723](https://github.com/commitizen-tools/commitizen/pull/723) 修到可以 review
2. [feat(commands/commit): apply prepare-commit-msg hook #250](https://github.com/commitizen-tools/commitizen/pull/250) 修到一半發現 [feat(commit): add --write-message-to-file option #731](https://github.com/commitizen-tools/commitizen/pull/731) 早就做完了...，順手把這個 PR 跟原始 issue [cz commit with prepare-commit-msg hook #249](https://github.com/commitizen-tools/commitizen/issues/249)都關了
3. [fixes yaml example #1350](https://github.com/commitizen-tools/commitizen/pull/1350) 修完就 merge 了

至於剩下的 17 隻 [pr-status: wait-for-modification] PRs
恩...就看緣分了

除此之外，我也開了幾隻 PRs

1. [Improve hooks type annotation and fix missing link #1345](https://github.com/commitizen-tools/commitizen/pull/1345): wait for review 🕑
2. [Upgrade to poetry 2.0 #1346](https://github.com/commitizen-tools/commitizen/pull/1346): merged 🙌

最近在玩 [uv] 才發現 [commitizen] 不會更新到 uv.lock，用 `version_file` 也解不了
開了 issue [Add uv provider #1349](https://github.com/commitizen-tools/commitizen/issues/1349) 跟 draft PR [feat(providers): add uv_provider #1351](https://github.com/commitizen-tools/commitizen/pull/1351)
不要問為什麼沒有人解決這個問題，我就是沒有人

下週會盡力分類一些 [issues](https://github.com/commitizen-tools/commitizen/issues)
去年 PyCon US 分類了一半，真的超花時間.....
貢獻者絕贊招募中

[pr-status: wait-for-modification]: https://github.com/commitizen-tools/commitizen/pulls?q=is%3Apr+is%3Aopen+label%3A%22pr-status%3A+wait-for-modification%22

[uv]: https://docs.astral.sh/uv/
[commitizen]: https://github.com/commitizen-tools/commitizen

## pycontw-blog
如果你還不知道， [PyCon Taiwan](https://tw.pycon.org/) 是有自己的[部落格](https://conf.python.tw/)的

Issue [Add general python distribution setup steps #112](https://github.com/pycontw/pycontw-blog/issues/112) 開了很久，但一直沒時間好好處理
最近聽說 [uv] 在 Windows 上的支援也不錯
就果斷透過[Replace pipenv with uv #200](https://github.com/pycontw/pycontw-blog/pull/200)把套件管理從 pipenv 改到 [uv] 上
原本以為更新文件要花很多時間
但 Yo 哥真的寫得太好了，我稍微改一下就結束了
大哥除了上個月飛、這個月也飛，當空中飛人很厲害以外，程式也是了得

沒想到當我在做這件事的時候，社群的夥伴也想到了類似的事
~~這是巧合嗎，我不這麼認為，一定是三角初華的陰謀~~
還好我們想做的事不同面向的
也花了點時間看了她的 PR [dependency: Update README to include prerequisites and modify the sequence of instructions #202](https://github.com/pycontw/pycontw-blog/pull/202)

## markdown-mermaidjs
這是源自於 [oruelle/md_mermaid](https://github.com/oruelle/md_mermaid) 的專案
因為原作者沒在維護，我的部落格又需要
就 fork 出 [Lee-W/markdown-mermaidjs](https://github.com/Lee-W/markdown-mermaidjs) 來用

最近熱心人士 Owyn 開了 PR [Feature/add icon packs #5](https://github.com/Lee-W/markdown-mermaidjs/pull/5) 加新功能
他幾乎已經做完，就差最後一步
我順手修完就 merge 了
感謝 Owyn 🙏

除此之外，我把專案的結構用[Update project structure with the latest template #6](https://github.com/Lee-W/markdown-mermaidjs/pull/6)根據最新版的[cookiecutter-python-template](https://github.com/Lee-W/cookiecutter-python-template/)更新了
順便找出不少模板的 bug，之後找時間來修

另外還有許久以前 ysard 開的 issue [Conflict with html minification tools #16](https://github.com/oruelle/md_mermaid/issues/16)
終於有時間認真看，意外的蠻簡單的
就發了 PR  [generate < pre class="mermaid">< /pre> instead of < div class="mermaid">< /div> #7](https://github.com/Lee-W/markdown-mermaidjs/pull/7) 把它給修了

因為這些改動，這一週就發了兩版

1. [1.1.0](https://pypi.org/project/markdown-mermaidjs/1.1.0)
2. [2.0.0](https://pypi.org/project/markdown-mermaidjs/2.0.0)

## pelican-stat

這是在 [2021 ~ 2024 年度回顧 - 持續紀錄的秘訣是寫廢文]({filename}/posts/gossiping/2025/1-2021-2024-yearly-review.rst) 提到的工具
除了更新專案結構，大多都是細碎的小 PRs 而已
原本以為更新 6.0.0 就不會有奇怪的特殊字元
結果只是換了別的特殊字元...
然後我的 RSS feed 就會壞掉
最後放棄手工休掉了

1. [Upgrade project with the latest project template #4](https://github.com/Lee-W/pelican-stat/pull/4)
2. [docs(CHANGELOG): fix typo #8](https://github.com/Lee-W/pelican-stat/pull/8)
3. [ci(github-actions): fix publish page action #9](https://github.com/Lee-W/pelican-stat/pull/9)
4. [suggest users to use uv to install this tool #10](https://github.com/Lee-W/pelican-stat/pull/10)
5. [Fix doc typo #11](https://github.com/Lee-W/pelican-stat/pull/11)
6. [fix(dep): upgrade plotly to 6.0.0 #12](https://github.com/Lee-W/pelican-stat/pull/12)
7. [ci(github-actions): fix missing pre-commit install #13](https://github.com/Lee-W/pelican-stat/pull/13)

一樣發了兩版

1. [0.3.1](https://pypi.org/project/pelican-stat/0.3.1/)
2. [0.3.2](https://pypi.org/project/pelican-stat/0.3.2/)

比較有趣的應該是有玩到 [Trusted Publisher](https://docs.pypi.org/trusted-publishers/)

### pycon-etl
因為最近 Airflow 3.0 要釋出，我希望能慢慢幫 PyCon TW 的 Airflow 也升級一下
看完文件發了 [docs(README): fix typos #153](https://github.com/pycontw/pycon-etl/pull/153)
但是 [pycon-etl](https://github.com/pycontw/pycon-etl/) 還在 Python 3.8
EOL 已經過了...
所以 workflow 不支援
看來要升版 Airflow 前， Python 要先升了...
