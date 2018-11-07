Title: Introduction to Chatbot
Date: 2016-11-21 08:18
Category: Tech
Tags: Chat Bot
Slug: introduction-to-chatbot
Authors: Lee-W
Summary: 
Series: Line Bot Tutorial


有人說聊天機器人 Chat Bot 將要取代 APP

- [Why chatbots are replacing apps](http://venturebeat.com/2016/08/02/why-chatbots-are-replacing-apps/)
- [This is how Chatbots will Kill 99% of Apps](https://chatbotslife.com/this-is-how-chatbots-will-kill-99-of-apps-2fd938a22c99#.tdfugot4m)

各大軟體公司也爭相提供 Bot 的服務
<!--more-->

- [Facebook Messenger Platform](https://messengerplatform.fb.com)
- [Line Messaging API](https://developers.line.me/messaging-api/overview)
- [Slack API](https://api.slack.com)
- [Telegram Bot Platform](https://core.telegram.org/bots/api)

## What can Bot Do?
那 Chat Bot 究竟能幹嘛呢 ?

先來看段影片吧
[【公式】BOT & THE NEW WORLD by LINE](https://www.youtube.com/watch?v=C7ZuzJe24y4)

### 影片中出現了什麼？
- 預約餐廳
- 訂車
- 偵測 Beacon 提供 coupon
- 遠端控制家中的 IoT 設備澆水

原本在 App 上處理的這些服務
未來都有可能逐漸被 Chat Bot 所取代

### 背後發生了什麼事
e.g. 預約餐廳

1. User 傳一個訊息給 Bot 的帳號
2. Bot 把訊息傳給服務提供者的 Server
3. 服務提供者的 Server 把訊息，傳給指定的 Server
4. 指定的 Server 做了適當的運算和判斷，把結果回傳給服務提供者 Server
5. 服務提供者 Server 收到後，再傳給 User 的帳號

e.g. Line Chat Bot 架構
![Line Chat Bot Architect](https://developers.line.me/media/messaging-api/overview/messaging-api-architecture-ee0356bd.png)


## Why Chat Bot?
- 市面上 App 太多了，要開發使用者黏著度高的 App 很困難
- 每一個 App 都有自己的介面，對使用者都是一次學習成本
	- 不如把服務嵌入現在使用者常用的 App
	  (e.g. Facebook Messenger, Line)
- 文字是人類相對直覺的溝通方式

## Why not Chat Bot?
- 設計彈性不如 App
	- 雖然 Chat Bot 大多提供按鍵等功能，但使用上的彈性不像 App 那麼大
- 文字處理依然不夠好
	- 簡單的 Bot，如果使用者一直無法對應到相對的關鍵字，就無法觸發功能 

## How to Design a Bot?
那麼開發一個 Bot 需要什麼呢？

1. 選擇使用的 Bot 平台 (e.g., Facebook Messenger Platform, Line Messaging API and etc.)
2. 寫一些服務 (e.g., 訂票、新聞推播)
3. 把服務架在一台 https server
4. 用 Bot 平台提供的 sdk，把 Server 跟平台串起來
5. 用 NLP 判斷使用者的意思，串接到服務上

## Chatbot Platform - Line Messaging API
既然看了 Line Bot 的新功能

接下來的幾篇文章會談要如何在 Line 平台上
做一個最簡單只會 Echo 的 Chat Bot

# Reference
這篇文章整理了相當多的相關資源
[The Rise of Chat Bots: Useful Links, Articles, Libraries and Platforms](https://stanfy.com/blog/the-rise-of-chat-bots-useful-links-articles-libraries-and-platforms/)
相當推薦對 ChatBot 有興趣的人參考

# Slide
如果有點不喜歡看文章的，也可以看看[slide](https://hackmd.io/p/HkW8LjRfl#/) 的版本
