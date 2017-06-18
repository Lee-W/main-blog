---
Title: PyCon TW 2017 - Day 2
Date: 2017-06-15 16:07
Category: Python
Tags: PyCon
Slug: PyCon-TW-2017-Day2
Authors: Lee-W
Summary: 
Series: PyCon TW 2017
---

第二天有一整個時段的Job Fair，可以出去晃晃到各個攤販聊天
最有印象的大概就是Carousel
（在conf看到他這麼多次，第一次知道他們來自新加坡
隔天還會有一位待過Apple的VP會來Unconf分享

<!--more-->

* [[Keynote] Building for Failure: Leraning Lessons from Aviation](#1)
* [自py系列2] 投資策略驗證系統
	* [slide](https://docs.google.com/presentation/d/1i5PwAHxXZQ2fewn194_gRU3kMG5s-04s1Pil0yJREHQ/edit#slide=id.g1ce6af9da4_1_8)
	* [共筆](https://hackfoldr.org/pycontw2017/https%253A%252F%252Fhackmd.io%252Fs%252FBkMVJwTy-)
* [對話機器人的腦子與靈魂 Bot's Brain and Soul](#3)
* [鄉民教我做的聊天機器人](#4)
* Why do projects fail?
	* [Slide](https://www.slideshare.net/ssuser2cbb78/pycon-tw-2017-why-do-projects-fail-lets-talk-about-the-story-of-sinonpy) 
* [利用 Python 與人工智慧快速打造人性化聊天機器人](#6)
* [Chatbot @ E.Sun Bank – 玉山小i 隨身金融顧問的兩三事](#7)

---

<a name='1'></1>
## [Keynote] Building for Failure: Leraning Lessons from Aviation

- [slide](https://speakerdeck.com/andrewgodwin/building-for-failure-learning-lessons-from-aviation)
- [共筆](https://hackfoldr.org/pycontw2017/https%253A%252F%252Fhackmd.io%252Fs%252FBk3_mwakZ)

### Warnings

- Noisy Warnings
	- Engineers ignore logs/notifications
- Precise Warnings
	- Alert on actionable things, then fix them

```python
try:
	requests.get('http://api.com/user')
except RequestError:
	raise APIFetchError('Could not get user list')
```

### Testing
- `100% Coverage Fallacy`
	- Too many tests that are fragile so you ignore them

### Checklist
- The step between manual and automation
- Cheap and very effective 

### Find the limits
- The Load Testing
- [Chaos Monkey](https://github.com/Netflix/chaosmonkey)
	- 測試server復原能力
- Restore from backups
- The "Red Team"
	- 攻擊系統的工程師們

### Trade off between Redundancy & Acceptable Loss
- Redundancy
	-  What do you fall back to?
- Acceptable Loss
	- Quantify the loss, and recovery

### Team
- No Single Cause
- No Blame Culture
	- Not someone's mistake
	- Systematic Problem
- Clear command chains
	- Who makes decisions?
	- Who does the fixing?
- Leadership can blind
	- Debate for what is right
- Crew Resource Management
- Increase your "bus factor"
	- People get ill → 一個專案至少要2個以上的人懂 
- Good engineering is not just code
	- Communiation matters
- Slower can be faster
	- Testing, Writing Documents make a project slower in short term, but faster in long term

### Speakers Advice
- Checklists
- Restore your backups
- Work out roughly what happens for every part of a system failing, and if you care
- Reward people whose code quietly works, not those who firefight and take the glory
- Checklists

---
<a name='3'></a>
## 對話機器人的腦子與靈魂 Bot's Brain and Soul
* [共筆](https://hackfoldr.org/pycontw2017/https%253A%252F%252Fhackmd.io%252Fs%252FHyt_yvak-) 

這場人太多了，連坐下來的位置都沒有ＱＱ
不過共筆寫得很清楚了
我這裡記錄的是會後跟講者討論的一些問題

- Q: Language Generation要怎麼做Evaluation，怎樣才算是符合文法？怎樣算是合理的回答？
	- 這個判定很主觀
	- 很多研究會導入Human Evalutaion
	- 目前這還是一個Open Question

- Q: 目前關於情緒判斷，是否已經到了Production了？
	- 尚未到Production
	- 這樣的問題很難做，其中一個原因在於資料很難收集
	- 另外是就算沒有辦法判斷情緒，通常也不會造成太大的問題。不像意圖如果判斷錯誤，就會提供錯誤的服務
	- 香港科技大學目前有一個可以判斷人格的Bot(我找不太到＠＠)

---

<a name='4'></a>
## 鄉民教我做的聊天機器人
- [slide](https://www.slideshare.net/RyanChao3/pycon2017-chatbot)
- [共筆](https://hackfoldr.org/pycontw2017/https%253A%252F%252Fhackmd.io%252Fs%252FHyt_yvak-)

`Work in Progress`

### Chinese Coversation Data
- Movie subtitle
	- 主題發散，不太容易收斂  
		- Seq2seq
			- 只能回應簡單的問題 
- PTT

### Backend & Platform
~48萬篇文章

### Informaition Retrieval
找出文章標題符合

- Jaccard Simularity
	- 不能處理介系詞 
- BM25

#### Improvements
- Tokenizer Improvement
	- Emoji icon pre-preocessing
	- Imporve tokenizer accuracy
	- 把jieba換成用繁體中文字典，並加入PTT會用的常見詞彙
- Keyword Extraction & Association
	- Word2Vec
		- query associative term if the original one doesn't exist 

### Evaluate
- represent for document with vector
	- Doc2Vec (gensim)
	- RNN-encoder (arXiv: 1506.08909v3)

- NDCG
	- 量化標注

- 讓那篇文章的回應當作ground truth
	- 來評斷機器人產生的結果好不好  	

---

<a name='6'></a>
## 利用 Python 與人工智慧快速打造人性化聊天機器人
- [Source Code](https://git.ng.bluemix.net/tommywu/pyconbot2017/blob/master/run.py)

`Work in Progress`

### 有溫度的聊天機器人
- 輔助性答案 (互動性)
	- 引導性回饋 - 開放話題
- 不定時提醒 - 貼近使用者
- 隨機答案 - 提高趣味 	
- 學習與進化
- Multi-channel (多渠道互動)

### Watson
- NP, ML的語意理解
- Zero Downtime
- 擴充
- 可訓練
- 搜尋引擎

### Watson AI Flow
Intent, Parameter, Entity Type

---

<a name='7'></a>
## Chatbot @ E.Sun Bank – 玉山小i 隨身金融顧問的兩三事
- [slide](https://drive.google.com/file/d/0B8hlay_yY5e7QTE0U3JDUXloeXM/view)

`Work in Progress`
還有沒有其他的<s>客訴</s>問題呢
 
