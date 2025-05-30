Title: Airflow 多語系化
Subtitle: Make a sunrise that I know I'll never see
Date: 2025-05-30 16:35
Category: Tech
Tags: Airflow
Slug: airflow-multilingual
Authors: Wei Lee
Image: /images/posts-image/2025-airflow-multilingual/andor-poster.jpeg
Cover: /images/posts-image/2025-airflow-multilingual/andor-poster.jpeg

> What is my sacrifice?
>
> I’m condemned to use the tools of my enemy to defeat them. I burn my decency for someone else’s future. I burn my life to make a sunrise that I know I’ll never see. And the ego that started this fight will never have a mirror or an audience or the light of gratitude.
>
> So what do I sacrifice?
>
> Everything!
>
> - Luthen Rael

<!--more-->

## TL;DR

1. [Andor: A Star Wars Story] 超級好看，做完第二點就去看！
2. 最近在 Airflow 引入 i18n 的 PR [Feature/implement i18n for Dashboard and SideBar #50626][airflow-pr-50626] 正在票選本月最棒棒 PR [[VOTE] May 2025 PR of the Month][2025-pr-vote]
    * 如果你也認同這個 PR 像那天最棒的演唱會一樣棒的話，投下你的票吧！

![mygo-best-concert](/images/meme/mygo-best-concert.jpg)

歐內該，如果沒有去投票的話，哇搭係

![mygo-everything](/images/meme/mygo-everything.jpg)

## 前言
自從 [Jason] 成為 Apache Airflow 的 committer （同場加映： [從 0 成為 Apache Airflow Committer]）
[源來適你][OpenSource4You] 的 `#apache-airflow` 就熱鬧了不少
~~我也從主要 Mentor ，追加了 Meme Bot 的 title~~
[guan404ming] 的 PR 數也快追上 [Jason]，還有族繁不及備載的新朋友們
但我怕再載下去就要壓過主角 [RoyLee1224] 的篇幅了

## 很久很久以前（其實也就不到一個月前）
某天在頻道中就出現了這篇酷酷的訊息

![start](/images/posts-image/2025-airflow-multilingual/start.jpg)

但[#50626][airflow-pr-50626]主要是前端程式碼的改動
我能提供的幫助比日本原裝進口的壓縮機還稀少

> 我可以…幫忙看中文…，我可能會一點點中文…

而且 [RoyLee1224] 大大也熟知 `#apache-airflow` 充滿迷因充滿歡樂的地方
不過沒想到這麼快樂的地方，竟然有人給 👎
壞，真的太壞了

![meme-speaks-louder](/images/posts-image/2025-airflow-multilingual/meme-speaks-louder.png)

我很喜歡這句

> memes speak louder than words:)

也許我應該把它寫進，已經很~~荒唐~~歡樂的頻道簡介中

![channel-intro](/images/posts-image/2025-airflow-multilingual/channel-intro.jpg)

翻了一下紀錄，[RoyLee1224] 是上個月才加入 Airflow 貢獻的新朋友
[Feature/implement i18n for Dashboard and SideBar #50626][airflow-pr-50626] 是他的第三個 PR
這個 PR 解的是 [Allow localization of UI #9864](https://github.com/apache/airflow/issues/9864)
馬上就被提名到每月最佳 PR [[VOTE] May 2025 PR of the Month][2025-pr-vote]
截至本文撰寫時，目前大家一致都認為就是 [#50626][airflow-pr-50626] 了
雖然他說是新的 issue 都被撿光了，才誤打誤撞碰到遠古 issue（現在的 issue 隨便都是萬來萬去）
但眾所週知，真正的大大比起巧克力薄荷更喜歡的是謙虛裝弱
✅ 真大大認證

## PR of the month
如果當選 PR of the month 的話，就會被寫進 Airflow Newsletter
（應該是 [Airflow - Community] 裡面的那個，~~不是[The Airflow Newsletter]吧~~）
另外會被邀請去 [Airflow Monthly Town-Hall] 分享

遠古時代我有因為 [Add default_deferrable config #31712][airflow-pr-31712] 去分享過一次
但那是台灣時間晚上 11 點，真的有點累 🥱
倒是想起來最近 [Jason] 也有被邀請過，但後來就不了了之了
不知道為什麼 👀

## 讓我看看！
此時此刻的 main 分支 ([6a7d257]) 跑起來大概會像是這樣
左下角的 `User` 按一下，就可以看到選擇語言的選單

![select-lang](/images/posts-image/2025-airflow-multilingual/select-lang.jpg)

選擇繁體中文就會看到以下的介面

![tw-ui](/images/posts-image/2025-airflow-multilingual/tw-ui.jpg)

瀏覽了一下， Asset 的翻譯也許可以再想想
TP 之前提議的資料也許不錯
現在是擔心 `Asset/資源` 跟 `Pool/資源池`，會讓人搞混
下週找個時間來丟出這個討論好了

## To 翻, or not to 翻
[#50626][airflow-pr-50626] 之後， Jens ([jscheffl]) 在 dev list 發起了 [[DISCUSS] Special Terms in UI Translations?][special-terms]
長話短說的話是「關於翻譯我們要翻譯到多深？所有的技術詞彙都要翻嗎」

Jens 的想法是，關於 Airflow 的技術名詞也許都保持在英文比較好
像是什麼呢？ Dag, Asset, Task, XComs 可能都是
把它翻譯成德文（或其他語言），也許會更難理解
因此應該要列出一個保留字的列表

我理解這也許在某些語系是合理的（其中也包含了我畢竟不懂其他語系，沒什麼立場置喙）
但我無法認同這適用於所有語言
（先聲明我對 Jens 大大沒意見 😱 去年我們很快樂的在金門大橋一起騎車！ 🚴）

我最核心的概念是

> 想做多語系的目的，就是為了讓那些對英文不是那麼熟悉的人可以更輕鬆接觸 Airflow
> 如果不盡可能去翻譯
> 也許我們該做的事是回去思考，為什麼要做這件事？真的要做這件事嗎？

我認為**除了 Dag, url, XCom 這些縮寫外，都不應該被加入保留字列表**
縮寫不翻譯的原因是，它們本身不具意義
`Uniform Resource Locator` 跟 `Cross Communication` 才有
而此刻的 `Dag` 也已經是個造字，不是有向無環圖了
如果想翻譯它們，也許就得在這些語言創造一個新的詞，但那就不在這次的討論範圍內了
比起它們不該被翻譯，更多的是，現在沒有更好的想法

Asset, Task 出現在 Airflow 中，都是最初借用了它們在英文中的概念
TP 在信件中所提到的 Running 也是
翻譯這些字本身就帶有「了解當初 Airflow 為何如此設計、命名」的含義在

不過 Jens 舉的幾個例子也不無道理
如果有人今天問我 git 提交該怎麼寫，我可能也會一時反應不過來
啊啊...原來是 git commit 啊（虧我還是 [commitizen] 的維護者）

只能說也許我們不是這個功能的目標客群吧
在 airflow dev mailing list 或參與 issue 討論的我們，或許都不是
我們或多或少都對英文有些熟悉
但正是因為想降低入門門檻，讓更多人接近 Airflow
我們才決定做這件事，至少我是這麼認為的

這也讓我想到， [Python 官方說明文件臺灣繁體中文翻譯計畫] 的朋友們
我不確定是他們還是 yyc 有跟我聊到（亦或者我中了強壯路人的咒術產生了不存在的記憶）
雖然我們得讀英文，也該熟悉英文
有時甚至到許多詞彙的繁體中文翻譯都不熟悉了
但做繁體中文翻譯這件事依然重要
為的就是要讓更多的臺灣人更無阻力的去接觸這些技術

![love-this-land](/images/posts-image/2025-airflow-multilingual/love-this-land.jpg)

我也是因為熱愛這片土地，所以試著用我的方式去做一些事
即使這也許是我永遠用不到的
所以副標題更應該像是

Make a sunrise that I know I'll never ~~see~~ need

但這段 Luthen 獨白實在是太棒了
我不捨得在副標題把它改掉
當初看到傻眼，直接跑去查演員到底是誰，詮釋的太好了吧

寫這篇文除了為熱帶的土地發聲
也是要推薦我熱愛的影集 [Andor: A Star Wars Story]
我最喜歡的真人影集沒有之一
這是部星戰先備知識需求最低的影集，其他作品都不看也不會看不懂
而且是影史上第一部 IMDB 連續五集高於 9.5 的優秀作品
現在就開始看吧！

[Andor: A Star Wars Story]: https://www.disneyplus.com/browse/entity-faba988a-a9f5-45f2-a074-0775a7d6f67a

[從 0 成為 Apache Airflow Committer]: https://blog.zhu424.dev/zh-tw/open-source-contribution/becoming-an-apache-airflow-committer-from-0/#%E6%88%90%E7%82%BA-committer
[OpenSource4You]: https://github.com/opensource4you/readme?tab=readme-ov-file#%E7%9B%AE%E5%89%8D%E6%9C%89-mentor-%E5%B8%B6%E7%9A%84%E5%B0%88%E6%A1%88

[Airflow - Community]: https://airflow.apache.org/community/
[Airflow Monthly Town-Hall]: https://astronomer.zoom.us/meeting/register/3NuEKTdEQfKiBhE1xFgHMg#/registration
[The Airflow Newsletter]: https://www.airflowclub.com/the-newsletter

[special-terms]: https://lists.apache.org/thread/bvsvoo4nln22wqkncxogpgtlpcd1fffj
[2025-pr-vote]: https://lists.apache.org/thread/fwn3lo21qpdg0wrfq8odcwq6ojx74784
[airflow-pr-50626]: https://github.com/apache/airflow/pull/50626
[airflow-pr-31712]: https://github.com/apache/airflow/pull/31712
[6a7d257]: https://github.com/apache/airflow/commit/6a7d25714eca008f4021457c71f86cd870ac0782

[RoyLee1224]: https://github.com/RoyLee1224
[guan404ming]: https://github.com/guan404ming
[Jason]: https://github.com/jason810496
[jscheffl]: https://github.com/jscheffl

[Python 官方說明文件臺灣繁體中文翻譯計畫]: https://github.com/python/python-docs-zh-tw
[commitizen]: https://github.com/commitizen-tools/commitizen
