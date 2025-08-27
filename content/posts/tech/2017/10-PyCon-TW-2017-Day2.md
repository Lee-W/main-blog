Title: PyCon TW 2017 - Day 2
Date: 2017-06-10 09:00
Modified: 2017-06-18 12:37
Category: Tech
Tags: Python, Conference, PyCon
Slug: PyCon-TW-2017-Day2
Authors: Wei Lee
Series: PyCon TW 2017

第二天有一整個時段的 Job Fair，可以出去晃晃到各個攤販聊天
最有印象的大概就是 Carousel，跟他們聊得還蠻開心的
還多玩了幾次他們的大家來找碴 XD
在 conf 看到他們這麼多次，第一次知道他們來自新加坡
隔天還會有一位待過 Apple 的 VP 會來 Unconf 分享

<!--more-->

今年還有音樂會呢，覺得還蠻有趣的
雖然聽完有點晚才去吃晚餐，剩的東西都不多了ＱＱ

![Piano](/images/posts-image/2017-06-10-PyCon-TW-2017-Day2/1-piano.jpg){: style="width:50%"}

![Symphony](/images/posts-image/2017-06-10-PyCon-TW-2017-Day2/2-symphony.jpg){: style="width:50%"}

---

## 議程

* [[Keynote] Building for Failure: Leraning Lessons from Aviation](#1)
* [自py系列2] 投資策略驗證系統
    * [slide](https://docs.google.com/presentation/d/1i5PwAHxXZQ2fewn194_gRU3kMG5s-04s1Pil0yJREHQ/edit#slide=id.g1ce6af9da4_1_8)
    * [共筆](https://hackfoldr.org/pycontw2017/https%253A%252F%252Fhackmd.io%252Fs%252FBkMVJwTy-)
* [對話機器人的腦子與靈魂 Bot's Brain and Soul](#3)
* [鄉民教我做的聊天機器人](#4)
* Why do projects fail?
    * [Slide](https://www.slideshare.net/ssuser2cbb78/pycon-tw-2017-why-do-projects-fail-lets-talk-about-the-story-of-sinonpy)
* [利用 Python 與人工智慧快速打造人性化聊天機器人 (IBM)](#6)
* [Chatbot @ E.Sun Bank – 玉山小i隨身金融顧問的兩三事 (玉山)](#7)

---

<a name='1'></a>

## [Keynote] Building for Failure: Learning Lessons from Aviation

* [slide](https://speakerdeck.com/andrewgodwin/building-for-failure-learning-lessons-from-aviation)
* [共筆](https://hackfoldr.org/pycontw2017/https%253A%252F%252Fhackmd.io%252Fs%252FBk3_mwakZ)

### Warnings

| Soft Failure | Hard Failure |
| --- | --- |
| Obscure errors and try to carry on | Quit at the first error and log it |

* Noisy Warnings
    * Engineers ignore logs/notifications
* Precise Warnings
    * Alert on actionable things, then fix them

Raise clear, verbose exception

```python
try:
    requests.get("http://api.com/user")
except RequestError:
    raise APIFetchError("Could not get user list")
```

### Testing

* `100% Coverage Fallacy`
    * Too many tests that are fragile so you ignore them

### Checklist

* The step between manual and automation
* Cheap and very effective

### Find the limits

* The Load Testing
* [Chaos Monkey](https://github.com/Netflix/chaosmonkey)
    * 測試 server 復原能力
* Restore from backups
* The "Red Team"
    * 攻擊系統的工程師們

### Trade off between Redundancy & Acceptable Loss

| Redundancy | Acceptable Loss |
| --- | --- |
| What do you fall back to? | Quantify the loss, and recovery |

### Team

* No Single Cause → No Blame Culture
    * Not someone's mistake
    * Systematic Problem
* Clear command chains
    * Who makes decisions?
    * Who does the fixing?
* Leadership can blind
    * Debate for what is right
* Crew Resource Management
* Increase your "bus factor"
    * People get ill → 一個專案至少要 2 個以上的人懂
* Good engineering is not just code
    * Communication matters
* Slower can be faster
    * Testing, Writing Documents make a project slower in short term, but faster in long term

### Speakers Advice

* Checklists
* Restore your backups
* Work out roughly what happens for every part of a system failing, and if you care
* Reward people whose code quietly works, not those who firefight and take the glory
* Checklists

---

<a name='3'></a>

## 對話機器人的腦子與靈魂 Bot's Brain and Soul

* [共筆](https://hackmd.io/s/Hyt_yvak-#1130-1215-talk-對話機器人的腦子與靈魂-bot’s-brain-and-soul)

這場人太多了，連坐下來的位置都沒有ＱＱ
不過共筆寫得很清楚了
我這裡記錄的是會後跟講者討論的一些問題

* Q: Language Generation 要怎麼做 Evaluation，怎樣才算是符合文法？怎樣算是合理的回答？
    * 判定很主觀
    * 很多研究會導入 Human Evaluation
    * 目前還是一個 Open Question

* Q: 目前關於情緒判斷，是否已經到了 Production 了？
    * 尚未到 Production
    * 這樣的問題很難做，其中一個原因在於資料很難收集
    * 另一個原因是，就算沒有辦法判斷情緒，通常也不會造成太大的問題。不像意圖如果判斷錯誤，就會提供錯誤的服務
    * 香港科技大學目前有一個可以判斷人格的 Bot( 我找不太到＠＠ )

---

<a name='4'></a>

## 鄉民教我做的聊天機器人

* [slide](https://www.slideshare.net/RyanChao3/pycon2017-chatbot)
* [共筆](https://hackmd.io/s/Hyt_yvak-#1325-1355-talk-鄉民教我做的聊天機器人)
* [Line Bot](https://line.me/R/ti/p/%40nlj2850e)

### Chinese Conversation Data

* Movie subtitle
    * 主題發散，不太容易收斂
        * 先過去出資料用語
    * Seq2seq
        * 只能回應簡單的問題
        * 大部分回答都是「我不知道」
* PTT
    * 八卦版標題和推文有應對關係 → 問答

### Backend & Platform

~48 萬篇文章

### Information Retrieval

找出文章標題符合

* Jaccard Similarity
    * 不能處理介系詞
* Modified BM25
    * 針對重要的字給予較大的權重
    * TF 對短句比較不好用 → 用詞性作為權重

#### Tried Improvements

* Tokenizer Improvement
    * Emoji icon pre-processing
    * Improve tokenizer accuracy
    * 把 jieba 換成用繁體中文字典，並加入 PTT 會用的常見詞彙
* Keyword Extraction & Association
    * Word2Vec → Query associative term if the original one doesn't exist

### Evaluate

* Represent for document with vector
    * Doc2Vec (gensim)
    * RNN-encoder (arXiv: 1506.08909v3)

* NDCG
    * 量化標注

* 讓那篇文章的回應當作 ground truth
    * 來評斷機器人產生的結果好不好

---

<a name='6'></a>

## 利用 Python 與人工智慧快速打造人性化聊天機器人 (IBM)

* [Source Code](https://git.ng.bluemix.net/tommywu/pyconbot2017/blob/master/run.py)

### 有溫度的聊天機器人

* 輔助性答案 ( 互動性 )
    * 引導性回饋 → 開放話題
* 不定時提醒 → 貼近使用者
* 隨機答案 → 提高趣味
* 學習與進化
* Multi-channel ( 多渠道互動 )

### Watson

* NP, ML 的語意理解
* Zero Downtime
* 擴充
* 可訓練
* 搜尋引擎

### Watson AI Flow

Intent, Parameter, Entity Type

---

<a name='7'></a>

## Chatbot @ E.Sun Bank – 玉山小i隨身金融顧問的兩三事 (玉山)

* [slide](https://drive.google.com/file/d/0B8hlay_yY5e7QTE0U3JDUXloeXM/view)

### Q & A

還有沒有其他的 ~~客訴~~ 問題呢
