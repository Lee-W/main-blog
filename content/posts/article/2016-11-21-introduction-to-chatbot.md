---
Title: [Bot] Introduction to Chatbot
Date: 2016-11-21 08:18
Category: Article
Tags: 
Slug: introduction-to-chatbot
Authors: Lee-W
Summary: 
---

有人說聊天機器人Chat Bot將要取代APP

- [Why chatbots are replacing apps](http://venturebeat.com/2016/08/02/why-chatbots-are-replacing-apps/)
- [This is how Chatbots will Kill 99% of Apps](https://chatbotslife.com/this-is-how-chatbots-will-kill-99-of-apps-2fd938a22c99#.tdfugot4m)

各大軟體公司也爭相提供Bot的服務
<!--more-->

- [Facebook Messenger Platform](https://messengerplatform.fb.com)
- [Line Messaging API](https://developers.line.me/messaging-api/overview)
- [Slack API](https://api.slack.com)
- [Telegram Bot Platform](https://core.telegram.org/bots/api)

## What can Bot Do?
那Chat Bot究竟能幹嘛呢?

先來看段影片吧
[【公式】BOT & THE NEW WORLD by LINE](https://www.youtube.com/watch?v=C7ZuzJe24y4)

### 影片中出現了什麼？
- 預約餐廳
- 訂車
- 偵測beacon提供coupon
- 遠端控制家中的IoT設備澆水

原本在App上處理的這些服務
未來都有可能逐漸被Chat Bot所取代

### 背後發生了什麼事
e.g. 預約餐廳

1. User傳一個訊息給Bot的帳號
2. Bot把訊息傳給服務提供者的Server
3. 服務提供者的Server把訊息，傳給指定的Server
4. 指定的Server做了適當的運算和判斷，把結果回傳給服務提供者Server
5. 服務提供者Server收到後，再傳給User的帳號

e.g. Line Chat Bot 架構
![Line Chat Bot Architect](https://developers.line.me/wp-content/uploads/2016/09/bottrial-fig1.png)


## Why Chat Bot?
- 市面上App太多了，要開發使用者黏著度高的App很困難
- 每一個App都有自己的介面，對使用者都是一次學習成本
	- 不如把服務嵌入現在使用者常用的App
	  (e.g. Facebook Messenger, Line)
- 文字是人類相對直覺的溝通方式

## Why not Chat Bot?
- 設計彈性不如App
	- 雖然Chat Bot大多提供按鍵等功能，但使用上的彈性不像App那麼大
- 文字處理依然不夠好
	- 簡單的Bot，如果使用者一直無法對應到相對的關鍵字，就無法觸發功能 

## How to Design a Bot?
那麼開發一個Bot需要什麼呢？

1. 選擇使用的Bot平台 (e.g. Facebook Messenger Platform, Line Messaging API and etc.)
2. 寫一些服務 (e.g. 訂票、新聞推播)
3. 把服務架在一台https server
4. 用Bot平台提供的sdk，把Server跟平台串起來
5. 用NLP判斷使用者的意思，串接到服務上

## Chatbot Platform - Line Messaging API
既然看了Line Bot的新功能

接下來的幾篇文章會談要如何在Line平台上
做一個最簡單只會Echo的Chat Bot

# Reference
這篇文章整理了相當多的相關資源
[The Rise of Chat Bots: Useful Links, Articles, Libraries and Platforms](https://stanfy.com/blog/the-rise-of-chat-bots-useful-links-articles-libraries-and-platforms/)
相當推薦對ChatBot有興趣的人參考