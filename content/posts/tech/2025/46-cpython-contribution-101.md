Title: 貢獻 CPython 101
Subtitle: CPython != Cython
Date: 2025-09-04 23:50
Modified: 2025-09-05 11:30
Category: Tech
Tags: Python, CPython
Slug: contribute-to-cpython-your-first-step
Authors: Wei Lee
Cover: /images/posts-image/2025-cpython-contribution-101/chi.jpg

如同副標題所說
在一切開始之前， [CPython] != [Cython]
那 CPython 是什麼？
如果你不知道你在用的 Python 是不是 CPython，那 87% 就是 CPython

<!--more-->

TL;DR: 去看 [Python Developer’s Guide]

[TOC]

## 前言
這次很開心終於有 CPython 的核心開發者，高天跟 DongHee 來台灣帶 CPython 的開發
為了讓他們可以專注帶已經進入狀況的開發者們更快進入 CPython 的開發
PyCon Taiwan 這邊也有人會帶初次接觸的人，快速設定好環境
而這次那個人就是我

![chi](/images/posts-image/2025-cpython-contribution-101/chi.jpg)

這篇文章就是明天衝刺開發要用的筆記
~~雖然我平常自己帶 Airflow 都沒這麼認真~~

## 進入正題

### 重新設定對衝刺開發的期待
這不是工作坊，也不是教學
所以環境設定完後，就是大家自己找 issue 開始做

以 CPython 來說
如果能在衝刺開發的現場成功設定完環境，就能算是及格了
能成功重現錯誤，就算相當不錯了
能成功發出一個 PR ，對於一個初心者，就太成功了！
（摘要自高天當天的分享）

### 開發環境設定
以下以 macOS 為例，畢竟我也沒其他系統
如果是 Linux，反正都用 Linux 了，這些小問題一定解得動
但如果是 Windows，我只能
![oshiyawaseni](/images/posts-image/2025-cpython-contribution-101/oshiyawaseni.jpg)
（或者請你參考 [Python Developer’s Guide] ）

1. 先將 Git 設定好（macOS 應該是預設就有吧 🤔）
2. 將 [CPython] Fork 到你的 GitHub  
   ![fork](/images/posts-image/2025-cpython-contribution-101/fork.jpg)
3. Clone 專案到本地端

```shell
git clone https://github.com/<your_username>/cpython
cd cpython
```

4. 建置你的 CPython (macOS only)

```shell
./configure --with-pydebug && make -j8
```

5. 跑測試 (macOS only)

```shell
./python.exe -m test -j8
```

沒錯，你沒看錯
只有 macOS 需要 `.exe`，
為了跟 `python` 這個資料夾做區別

這幾步都跑過，開發環境大致上就沒問題了

### 找 issue 解
接著要去 [CPython issues] 的大海中找到適合自己的 issue
~~建議先找[有 Easy 標籤，並且沒有被指派的 issues][easy-unassigned]~~
*高天後來建議不找 Easy 標籤*
*因為做標籤的人沒有足夠的心力把標籤標好*
*所以可能漏掉簡單的任務，或者只是把看起來簡單（但其實很難）的標成 Easy*
如果已經有人發 PR 了，就不要再做一次

當然也可能發現還沒被發出來的問題
這時候應該要先發 GitHub Issue
敘述問題，最重要的是遇到問題的環境，如何重現
但繁瑣的小問題，像是當英文小老師修錯字就可以不發 issue 直接發 PR

之前參加的衝刺開發的觀察
大多初次參與 CPython 的貢獻者都是以文件貢獻為主
也可以先找找看有 [Docs][docs-label] 標籤的 issue
要如何編譯文件可以參考 [Documentation - Getting Started]
如果你是 *nix 系統，而且是懶人的話，指令下收

```shell
cd Doc
make venv
make html
make check
```

除此之外這些是我在各處收集到的，各路大大的貢獻建議 ~~跟一些我的廢話~~

#### TP
TP 大大在上次 CPython 工作坊給的建議

> 如果有人有興趣開始貢獻
>
> CPython issues:
> <https://github.com/python/cpython/issues>
>
> 可以找有 easy label 的開始研究
> 這類問題很多都已經有人嘗試過，可以看看是不是已經有人發了 PR 只是還沒 merge
> 如果有就不要再做一次，不過可以考慮協助 review PR
>
> 很多 easy 也會有 docs label，代表是文件相關
> 要做這類貢獻的話需要 build docs 才知道你改的結果
> 參考 <https://devguide.python.org/documentation/start-documenting/>
>
> 我另外找了幾個簡單主題，有興趣的可以試試看
>
> 沒有標 docs 不過其實是文件相關 <https://github.com/python/cpython/issues/56959>
> 算是牽涉滿廣的問題，有興趣帶回家做的可以試試 <https://github.com/python/cpython/issues/67928>
> 已經有人發了 PR 不過放棄了，可以根據他的 PR 接過來做 <https://github.com/python/cpython/pull/19109>
> 同上，可以考慮接過來做 <https://github.com/python/cpython/pull/1011>
> 好像沒人在做 (有一些很古老的 patch 可以參考) <https://github.com/python/cpython/issues/53891>
> 三年沒更新了，應該可以接著做 <https://github.com/python/cpython/pull/30086>

或在 Python Taiwan Discord 伺服器的 `🏃｜cpython` 頻道可以翻到原文

#### 高天
高天大大建議大家先看自己有興趣的函式庫，再去找相關的 issue
[Docs][docs-label] 雖然技術要求不高，但吃表達能力跟語言能力，他也比較少碰

我自己最初碰 CPython 也是從可能比較簡單的函式庫 `json` 下手
唯一一個開過的 PR 也是延伸 `json` 的功能
（雖然最後沒合併，到現在好像還是開放 issue）
文件的部分則是有在 EuroPython 2025 聽到朋友抱怨
只為了改六行文件，花了他一整天，實在很挫折
雖然第二天的衝刺開發他還是乖乖地又回去貢獻 CPython 了 😆

#### Tachibana さん
Tachibana さん在 PyCon US 的時候聽到有 [topic-repl] 標籤的 issue，可能比較好解
我們猜應該是比較新，所以簡單的 issue 還沒被解完

順帶一提 Tachibana さん在 PyCon TW 2025 Day 1 有酷酷的演講

![tachibana](/images/posts-image/2025-cpython-contribution-101/tachibana.jpg)

雖然我聽不到，要去 PyCon JP 2025 才能聽了

### 開始修改到完成修改
如果編輯器有設定自動修正格式的話，建議關掉
避免改到不應該動的程式碼
CPython 本身沒有用 Ruff，其他的風格該怎麼寫就讀一下的空氣吧

如果成功完成了程式碼的修改，可以透過這些指令來測試

```shell
# macOS only

# 建置你的 CPython
./configure --with-pydebug && make -j8

# 執行修改過的 CPython 做人工測試
./python.exe

# 跑測試
./python.exe -m test -j8
```

如果一切都沒問題，就可以開新的 Git 分支

```shell
git checkout -b fix-issue-12345 main
```

接著做 patchcheck

```shell
make patchcheck
```

再來就可以發 Pull Request 到 [CPython] 了
標題通常會以 `gh-12345: Fix some bug in spam module` 這樣的格式

至於最後一步的 `Misc/NEWS.d`，我就不是很確定了
我看最新的幾隻 PRs 都沒有加

如果是第一次貢獻 CPython，會需要簽 Contributor Licensing Agreement (CLA)
流程可以參考 [Licensing]
沒有簽的話，發完 PR， CI 會提醒你要簽

### 除了開發以外還可以做什麼
1. 審閱 [PR](https://github.com/python/cpython/pulls?q=sort%3Aupdated-desc+is%3Apr+is%3Aopen+-is%3Adraft+)
2. 分類 issue（參考 [Issues and Triaging]）

這兩步都可以讓大家比較容易知道整個開發流程大致上是怎麼進行
也是專案中一直都會需要有人做，但可能沒那麼被重視的事
畢竟能讓自己的程式碼進入專案，聽起來就比較厲害

### 其他資源
* [Keynote: You don’t have to be a compiler engineer to work on Python — Savannah Bailey](https://www.youtube.com/watch?v=WGXXxGLBVF4)
    * Savannah 今年在 EuroPython 有分享了她成為 CPython 核心開發者的心路歷程
* [How JIT builds of CPython actually work](https://savannah.dev/posts/how-your-code-runs-in-a-jit-build/)
    * 如果對 JIT 有興趣，Savannah 最近也寫了相關的介紹文
* [來讀 CPython 原始碼]
    * 龍哥去年鐵人賽的文章，雖然 3.12 離現在 main 的 3.15 有幾個版本了，但...概念應該還是通用吧

## 雜談
今年邀請到 Donghee Na 來擔任 Keynote 講者
Kwon Han 也一直提到希望能在台灣辦 CPython 的衝刺開發
龍哥去年又在鐵人賽寫了 [來讀 CPython 原始碼]
高天也剛好會來參加 PyCon Taiwan 2025
總覺得今年是必須得做這些事的天時地利人和

說是這麼說，但我好像也就是在前期稍微推進了點事情
最後我頻寬有限，稍微有點沒力了
只能在有限的精力下盡可能的小力小力的推
最後還是由 PyCon TW 最強的，獲得世界認可的 PSF Fellow Winnie Ke 一肩扛下
👉 [Announcing Python Software Foundation Fellow Members for Q2 2024! 🎉](https://pyfound.blogspot.com/2024/10/announcing-python-software-foundation.html)

除此之外，她在官網上的自我介紹是這樣寫的
![winnie](/images/posts-image/2025-cpython-contribution-101/winnie.jpg)
有 C，有 Python
看來劍指 CPython 核心開發者的意圖是相當明顯了

---

[CPython]: <https://github.com/python/cpython/>
[Cython]: <https://cython.org/>
[Python Developer’s Guide]: https://devguide.python.org/
[CPython issues]: https://github.com/python/cpython/issues
[easy-unassigned]: https://github.com/python/cpython/issues?q=is%3Aissue%20state%3Aopen%20label%3Aeasy%20no%3Aassignee
[docs-label]: https://github.com/python/cpython/issues?q=sort%3Aupdated-desc+state%3Aopen+label%3Adocs
[Documentation - Getting Started]: https://devguide.python.org/documentation/start-documenting/
[topic-repl]: https://github.com/python/cpython/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20label%3Atopic-repl
[Licensing]: https://devguide.python.org/getting-started/pull-request-lifecycle/#cla
[Issues and Triaging]: https://devguide.python.org/triage/
[來讀 CPython 原始碼]: https://pythonbook.cc/chapters/cpython/introduction
