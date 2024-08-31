Title: 遇到 Error: fatal: could not read Username for 'https://github.com': terminal prompts disabled 怎麼辦 😱
Date: 2024-01-17 22:56
Category: Tech
Tags: GitHub Actions, CI/CD, GitHub
Slug: how-to-deal-with-could-not-read-username-for-github
Authors: Wei Lee

相信有在用 GitHub Actions 的大家應該都有用過 [actions/checkout](https://github.com/actions/checkout)

最近某個平常跑得好好的 CI/CD pipeline 卻噴了這個錯誤

```text
Error: fatal: could not read Username for 'https://github.com': terminal prompts disabled
```

<!--more-->

## Root Cause

這可能是因為 PAT ([Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)) 已經過期了
（我也是想了一下才看懂 PAT 是什麼縮寫...）

## Solution
先到 GitHub 個人頁面的 `Settings` > `Developer Settings` > `Personal Access Tokens`
找出[actions/checkout](https://github.com/actions/checkout)用的那個過期的 token，並且更新它

接著回到專案頁面的 `Settings` > `Secrets and variables` > `Actions` 找到對應的 secret，並取代成更新過的 token

## 雜記
遙想當初開始寫部落格，其實也就只是把筆記存起來，讓未來的自己好找
現在部落格的搜尋，好像又可以開始寫這種短短的小文章了
回歸初心（？？？）

## Reference
* [Error: fatal: could not read Username for 'https://github.com': terminal prompts disabled #664](https://github.com/actions/checkout/issues/664)
