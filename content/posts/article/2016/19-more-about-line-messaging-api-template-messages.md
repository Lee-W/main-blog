Title: More About Line Messaging API - Template Messages
Date: 2016-11-27 06:08
Category: Tech
Tags: Chat Bot
Slug: more-about-line-messaging-api-template-messages
Authors: Lee-W
Summary: 
Series: Line Bot Tutorial


除了傳送文字外，Line Bot 還可以傳

- 圖片, 影像, 聲音, 地圖
- 貼圖 (Line Bot 所能使用的[貼圖清單](https://devdocs.line.me/files/sticker_list.pdf))
- Imagemap
- Tempalte
	- Button
  - Confirm
  - Carousel
  
大部分使用上很直覺，可以直接參考[API Reference - Messaging API](https://devdocs.line.me/en/) 和[line-bot-sdk-python](https://github.com/line/line-bot-sdk-python)

這篇文章主要談 Template Messages 的使用

<!--more-->

# Template

Template 分為 Button, Confirm 跟 Carousel 三種
這些功能也是我認為從 Line Bot Trail 升級到 Line Messaging API 最好用的功能

## Example
以下的測試是 bot 收到關鍵字，回傳相對應的訊息

- Button
![button_example](http://i.imgur.com/KYN6kDR.png)

- Confirm
![confirm_example](http://i.imgur.com/pUFboL5.png)

- Carousel (如果超出版面，則可以左右滑動)
![carousel_example](http://i.imgur.com/Pxvj6om.png)

另外必須要注意的是，這些功能目前都只支援手機版
在電腦版上的 Line 看到的訊息會是這樣
![template_message_on_pc](http://i.imgur.com/ZdGQjc6.png)
這個文字內容可以透過 template 的 alt\_text 參數設定

上面的例子是[line-bot-sdk-python](https://github.com/line/line-bot-sdk-python#templatesendmessage---buttonstemplaten) 的使用範例
([可以回傳 template message 的 echo bot](https://github.com/Lee-W/line_echobot/tree/template-message))
大部分都能透過 Code 和 Example 比對，找到需要調整的參數


接下來談的是那些按鍵的設定
上面所看到的按鍵都是一個 Action
三種 Template 最大的不同，主要是這些 action 擺設的方式不同
限制的數量也不同

- Button 一次可以支援四個 action
- Confirm 支援三個 action
- Carousel 則可以用 5 個 CarouselColumn，每一個 Column 支援 3 個 Action
	- 另外需要注意的是 Carousel 中每一個 Column 的 action 數量必須是一樣的

# Action
這些 action 的 label 參數，就是顯示在按鍵上的文字，必須在 20 字以內

text 參數則是按下這個按鍵，會由使用者回傳設定的文字
e.g. 這是我按下上面 Button 的 postback 的效果
![text_example](http://i.imgur.com/ow2G8wU.png)
而 text 就是設定為 postback ( 注意並非 label 的 'postback')

## Postback
當使用者按了這個按鍵
Line Server 會傳一個 postback event 給我們，裡面包含著 data 參數中設定的字串 
在收到 event 的時候，透過 `event.postback.postback.data` 取出 data

Postback 可以不給 text 參數

## Message
text 參數在 Message Action 是必須的，也不能給空字串
如果希望這個按鍵，只有顯示但不會由使用者傳文字過來，可以給一串空白 (e.g. ' ')

## URI
使用者按下這個按鍵就會用 Line 的瀏覽器跳到外部網頁

# Reference
- [API Reference - Messaging API](https://devdocs.line.me/en/#template-messages)
- [line-bot-sdk-python](https://github.com/line/line-bot-sdk-python#templatesendmessage---buttonstemplate)