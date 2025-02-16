Title: 2025/02/10 - 02/16 開源貢獻週報
Subtitle: iThome 的得獎者還在 GO
Date: 2025-02-16 22:35
Category: Tech
Tags: Open Source, 開源貢獻週報
Slug: 2025-02-10-02-16-open-source-report
Authors: Wei Lee
Cover: /images/meme/mygo-accumulate-2.jpg

我也要！

<!--more-->

## commitizen
上週看 PR 的時候，發現更新過後的 CI 沒檢查到 commit 的格式
身為 commit 警察的 commitizen 怎麼能容許有不合乎規範的 commit message
所以我就開了 [ci(github-actions): add check-commit task #1357] 把它加回去

## pycon-etl
原本應該拿來準備 PyCon APAC 2025 的投影片，最後都拿來處裡這個 PR 了...
[Use uv as python, dependencies, virtual environment management tools #155]
還以為只要換成 uv 就可以過著幸福快樂的日子
但要裝一些舊套件還是蠻頭痛的
不過快是真的有快，方便也是真的方便

---

這週的開源貢獻應該就是發了這兩個 PR

雖然只是小小、少少的貢獻

![mygo-accumulate](/images/meme/mygo-accumulate.jpg)
![mygo-accumulate-2](/images/meme/mygo-accumulate-2.jpg)

今年 iThome 鐵人賽頒獎典禮，其中一組的得獎者也引用了這段話
我的心中已經給他的致詞滿分了

[ci(github-actions): add check-commit task #1357]: https://github.com/commitizen-tools/commitizen/pull/1357
[Use uv as python, dependencies, virtual environment management tools #155]: https://github.com/pycontw/pycon-etl/pull/155
