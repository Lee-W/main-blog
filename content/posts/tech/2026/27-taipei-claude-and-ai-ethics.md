Title: Taipei | Claude and AI Ethics
Subtitle: 起因竟是大港開唱 2026 ?!
Date: 2026-06-29 08:00 +0800
Category: Tech
Tags: AI Ethics, Claude
Slug: taipei-claude-and-ai-ethics
Cover: /images/posts-image/2026/taipei-claude-and-ai-ethics/event-photo-1.jpeg
Authors: Wei Lee
Lang: zh-tw
Status: draft

前一段時間收到朋友邀請參加 [Taipei | Claude and AI Ethics](https://luma.com/claude-taipei-3?tk=M8Qciv)

<!--more-->

先從副標題開始吧，為什麼會跟大港開唱有關呢？
因為這次的講者，也就是上面提到的朋友[Peter](https://www.igf.org.tw/%E5%B4%94%E5%AE%B6%E7%91%8B-jia-wei-cui/)就是在大港開唱意外認識的朋友
去聽 BAND-MAID 前，我跑去 OCF 的攤位打聲招呼
（終於見到 [Toomore](https://toomore.net/) 了！）
剛好跟 Peter 很聊得來，就一起去女神龍聽
後來還一起擠到更前面聽 AiNA THE END
當天我有帶了兩把王劍，就借了他一把，大家一起 high !
然後站我們旁邊的剛好是去年聽我[演講](https://speakerdeck.com/leew/unlocking-the-future-of-data-pipeline-942ed56f-0083-4e25-9e30-04850095e824)的聽眾
她跟我打招呼的時候我嚇到了，這世界到底多小...
再聊下去這篇就要變成大港文了

總之這次是在討論前段時間 Anthropic 跟美國政府的訴訟案
會場是在 g0v 的空間

![event-photo-1](/images/posts-image/2026/taipei-claude-and-ai-ethics/event-photo-1.jpeg)

![event-photo-2](/images/posts-image/2026/taipei-claude-and-ai-ethics/event-photo-2.jpeg)

![event-photo-3](/images/posts-image/2026/taipei-claude-and-ai-ethics/event-photo-3.jpeg)

![event-photo-4](/images/posts-image/2026/taipei-claude-and-ai-ethics/event-photo-4.jpeg)

![event-photo-5](/images/posts-image/2026/taipei-claude-and-ai-ethics/event-photo-5.jpeg)

![event-photo-6](/images/posts-image/2026/taipei-claude-and-ai-ethics/event-photo-6.jpeg)

![event-photo-7](/images/posts-image/2026/taipei-claude-and-ai-ethics/event-photo-7.jpeg)

整場議程蠻有趣的，也聽到不少有趣的知識和想法
最大的遺憾大概是不能留下來跟大家繼續交流，剛好當天結束後有行程 😢

---

因為我自己整理這篇文大概會天荒地老發不出來
反正筆記就是筆記，所以我請 AI 幫我把我當天手寫筆記的內容整理過
我還有再看過一次
雖然可能有點 AI，但應該是摻雜了不少的人才對
當然也有可能我其實本人也是 AI
這整個部落格從十幾年前就是 AI 寫的，我根本不存在
但話說回來，這次的講題就是 AI 相關，用一下 AI 也行吧
嗯，然後我是用 Claude Code 整理的

## Anthropic v.s. 美國政府

這場官司的背景，是有 12 份支持 Anthropic 的**法庭之友意見書（amicus brief）**
（我是聽到一半才去查，才知道原來那叫法庭之友意見書）

這 12 份大致分成五類：

1. 言論自由
2. 科技
3. 法律解釋
4. 國安建制
5. 倫理／人權

訴訟的進程，預期會一路往上走：

1. N.D. California（目前在這）
2. 9th Circuit
3. D.C. Circuit

另一條線是 **4/17 的白宮會面**
Anthropic 退出之後，Google、OpenAI、xAI 都跟五角大廈簽了合約
Google 是上週（演講時的上週）才簽的，而且 Google 沒有任何否決權

## 從 responsible 到 trustworthy：治理

討論的主軸，是 AI 治理正在從「responsible」往「trustworthy」移動。幾個被提出來的題目：

1. AI 治理、數位信任
2. 政府在設定 AI 邊界時扮演的角色
3. 國家安全例外，以及它的合法性
4. 私營企業到底該不該定義倫理規範

## Withholding AI doesn't stop military AI

一個反覆出現的論點是：把 AI 抽手，並不會讓軍事 AI 停下來。Anthropic 一退出，OpenAI 馬上就補上了
（順帶一提，現場提到原來美國政府用了很多 Azure 👀）

換句話說，**AI is not a nice-to-have**：

* 以飛彈防禦為例，從偵測到攔截不到 15 分鐘——這是物理問題，不是政策選擇
* 在這麼短的時間裡，HITL（human-in-the-loop）根本不是個選項
* 取而代之的是 **pre-design decision gate**：倫理就發生在這個環節（它本來就是系統的一部分）——但我們怎麼知道它真的如預期運作？

還有 scale 的問題：小國根本跟不上。光是 4 架無人機，背後就需要 150+ 的人力支撐

那什麼才是安全的 AI？現場給的等式是：

> Safe AI = Interpretable + Auditable
> （Bounded、可解釋、可被追溯）

結論濃縮成一句：**focus on the framework, not the fight.**

## Q&A： framework 該怎麼決定

**Q：要怎麼決定這個 framework？**

Anshuman：應該交給民選政府，而不該是單一一家公司來定。公司是利益驅動（profit-driven）的，我們已經知道那樣會走向什麼結果

**Q：要怎麼讓利益各異的人，坐進同一個房間裡討論？**
Nico：沒有好答案，這需要時間。但總得先 initiate 一些東西，否則連起點都不會有

Anshuman：人類依賴它、使用它，所以它才重要——既然如此，人類就必須參與進來。正面的例子是 OSS（開源），反面的例子是 social media
