Title: More than Just Echo Bot
Date: 2016-11-29 01:57
Category: Tech
Tags: Chat Bot, NLP, Machine Learning
Slug: more-than-just-echo-bot
Authors: Wei Lee
Series: Line Bot Tutorial

知道怎麼實作一個會 Echo 的 Bot 後
再來就要思考，開發一個 Bot 我們要提供什麼功能
(e.g., 天氣查詢, 訂票, 推薦旅遊景點)

不過這裡要討論的不是 Bot 的功能
Bot 的功能實作，跟一般網站或 App 的實作並沒有太大的差別

接下來來談如何從使用者說的話來判斷，使用者要使用的功能

<!--more-->

如果使用者問：「今天天氣如何？」「天氣今天好嗎？」
要如何知道，他都是要詢問今天的天氣狀況
也就是使用者的「意圖」

## Based on Keyword

上一篇文章，輸入關鍵字就能回傳 template message 的 bot 也是用這樣的方式實作的

```python
if 'button' in text:
    # Send ButtonTemplate
    ......
elif 'confirm' in text:
    # Send ConfirmTemplate
    ......
elif 'carousel' in text:
    # Send CarouselTemplate
    ......
else:
    # Echo TextMessage
    ......
```

回歸到天氣的問題
可以試著找出「天氣」是否有出現在使用者的問句中
再來判斷「今天」, 「明天」這樣敘述時間的詞

e.g.

```python
if '天氣' in text:
    if '今天' in text:
        return today_s_weather
    elif '明天' in text:
        return tomorrow_s_weather
```

### Pros

* 不需要其他的背景知識，容易實作
* 運算量小

### Cons

* 建立規則很麻煩
* 規則很容易就會出現例外，很難定義得完整
    * 只要使用者無法觸發到關鍵字，就無法使用功能
* 一堆 if else 造成程式冗長，不易擴充和維護

## AIML

Artificial Intelligence Modelling Language
它是一款基於 XML 的 markup language

這是最基本的 AIML

```xml
<aiml version="1.0.1" encoding="UTF-8"?>
   <category>
      <pattern> HELLO ALICE </pattern>

      <template>
         Hello User!
      </template>

   </category>
</aiml>
```

只要符合特定的 pattern，就回傳指定的 template
也能透過 `<random>` 這樣的 tag，從多種回覆隨機丟一種回傳

```xml
<random>
   <li> response1 </li>
   <li> response2 </li>
   ...
</random>
```

### Pros

* 比起只用 if else 更結構化，較易維護和擴充

### Cons

* 依然很難包含所有的狀況

## Other NLP Service

* [Wit.ai](https://wit.ai) (Facebook)
    * COSCUP 2016 的聊天機器人小啄，就是透過 Wit.ai 實作的
* [LUIS](https://www.luis.ai) (Microsoft)
* [API.ai](https://api.ai) (Google)

這些服務能透過標記和訓練
解析出這句話的每一個片段，所具有的意義

* e.g. 「今天西雅圖天氣如何」
    * 時間：今天
    * 地點：西雅圖
    * 意圖：天氣如何

### Wit.ai

Wit.ai 跟 LUIS, API.ai 比較不同的地方是
從 Wit.ai 得到的是，我們設定的回覆
而不是一句話解析後的結果

### LUIS

從[這裡](https://www.microsoft.com/cognitive-services/en-us/language-understanding-intelligent-service-luis) 可以測試兩個訓練過的範例機器人，看看從 LUIS 可以得到什麼

e.g.

* Question

```text
how is the weather in the Taipei
```

* Response

```json
{
    "query": "how is the weather in the Taipei",
    "topScoringIntent": {
        "intent": "GetCurrentWeather",
        "score": 0.50119406,
        "actions": [
            {
                "triggered": false,
                "name": "GetCurrentWeather",
                "parameters": [
                    {
                        "name": "location",
                        "required": true,
                        "value": null
                    }
                ]
            }
        ]
    },
    "entities": [],
    "dialog": {"contextId": "80cd646a-d85d-4b40-873d-1b47fa49adc8",
        "status": "Question",
        "prompt": "Where would you like to get the current weather for?",
        "parameterName": "location"
    }
}
```

### API.ai

* Question

```text
Hey Calendar, schedule lunch with
Mary Johnson at 12 pm tomorrow.
```

* Response

```json
{
    "action":"meeting.create",
    "name":"Lunch with Mary Johnson",
    "invitees":["Mary Johnson"],
    "time":"2014-08-06T12:00:00-07:00"
}
```

## Implement Through Powerful Libraries

不過這些服務，通常會有它的限制
這時候就能用上 Python 強大的函式庫們，來實作自己的版本

* [NLTK](http://www.nltk.org)
    * Python 經典的 NLP 函式庫
* [word2vec](https://radimrehurek.com/gensim/)
    * 透過詞向量，找出相似詞
* [jieba](https://github.com/fxsjy/jieba)
    * 中文斷詞
    * 判斷句子中的關鍵詞

我在[NLP Libs Sample](https://gist.github.com/Lee-W/72f3a59b015cd67b3a939bf8a12680ac) 寫了這些函式庫的基本使用範例

另外，也可以看[自己动手做聊天机器人教程](https://github.com/warmheartli/ChatBotCourse)
它是一系列聊天機器人教學，談這些做法背後的理論和實作

## Beyond NLP

不過就算做了這些分詞、判斷意圖
也不能保證使用者就會買單

有人稱 Chat Bot 為下一代的 UX Design

* [The Next Phase Of UX: Designing Chatbot Personalities](https://www.fastcodesign.com/3054934/the-next-phase-of-ux-designing-chatbot-personalities)

### Issue

* 如何讓使用者，在機器人的 Scope 內不會碰壁
* 如何讓機器人的判斷足夠 robust，不會每次回答都是不明白
* 如何讓使用者在最少的操作下，得到想得到的服務

更進一步是
如何設計一個有個性、有溫度的機器人
這裡就可以再去研究 NLP 的情感分析

### Read More

* [WHEN BOTS GO BAD: COMMON UX MISTAKES IN CHATBOT DESIGN](http://www.topbots.com/common-chatbot-ux-mistakes-in-bot-design/)
* [Does Conversation Hurt Or Help The Chatbot UX?](https://www.smashingmagazine.com/2016/11/does-conversation-hurt-or-help-the-chatbot-ux/)

## Reference

* [Head First ChatBot](https://hackmd.io/s/SyJUciYWg)
* [AIML Tutorial](https://www.tutorialspoint.com/aiml/index.htm)
* [AI Chat Bot in Python with AIML](http://www.devdungeon.com/content/ai-chat-bot-python-aiml)
* [Wit.ai Quickstart](https://wit.ai/docs/quickstart)
* [自己动手做聊天机器人教程](https://github.com/warmheartli/ChatBotCourse)
* [An overview of the bot landscape](https://www.oreilly.com/ideas/an-overview-of-the-bot-landscape?imm_mid=0eb199&cmp=em-data-na-na-newsltr_20161130)
