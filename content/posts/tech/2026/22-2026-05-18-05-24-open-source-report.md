Title: 2026/5/18 - 5/24 開源貢獻週報
Subtitle: 就連寫程式也在 GO
Date: 2026-05-25 22:05 +0800
Category: Tech
Tags: Open Source, 開源貢獻週報
Slug: 2026-05-18-2026-05-24-open-source-report
Authors: Wei Lee
Lang: zh-tw

部落格的改善到了一個階段
又到了 AI token 燒不完要找個東西做的階段
終於可以來做我的 MyGO!!!!! agent 工作流了！

<!--more-->

## Lee-W/maigo
* 釋出 [v0.10.0](https://github.com/Lee-W/maigo/releases/tag/v0.10.0)
    * 目前支援以下的指令
        * address-comments
        * describe-pr
        * doctor
        * fix
        * go
        * memory
        * remember
        * retro
        * review
        * team
    * 除了 MyGO!!!!! 的五個角色外，還有 Doloris 跟 Mortis 作為旁白

最近 Airflow 的開發都有 MyGO!!!!! 的團員幫我規劃、開發跟驗證
貓貓負責探索，燈負責規劃，愛音實作，交給爽世驗證，最後給立希測試
除了 token 會燒得比較快，整體使用體驗還不錯
不過梗的濃度還不夠，需要再調整一下

## commitizen-tools/commitizen
* 開 PRs
    1. [Add 4-day dependency cooldown to reduce supply chain risk #1997](https://github.com/commitizen-tools/commitizen/pull/1997)
* 審閱 PRs
    1. [ci(deps): bump pymdown-extensions from 10.21.2 to 10.21.3 #1995](https://github.com/commitizen-tools/commitizen/pull/1995)
    2. [ci(deps): bump peter-evans/create-or-update-comment from 4 to 5 #1998](https://github.com/commitizen-tools/commitizen/pull/1998)
    3. [ci(deps): bump idna from 3.11 to 3.15 #1996](https://github.com/commitizen-tools/commitizen/pull/1996)

也因為花了太多時間在 maigo 上，這週 commitizen 的貢獻很少......
