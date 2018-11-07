Title: Create a Telegram EchoBot
Date: 2017-03-31 19:24
Category: Tech
Tags: Chat Bot, Flask
Slug: create-a-telegram-echobot
Authors: Lee-W
Summary: 


最近當助教要出一個 Telegram Bot 相關的 Project
先來寫一篇簡單的教學，減少之後的問題 XDD

<!--more-->

如果對 Chat Bot 的基本運作概念不太熟
可以參考[[Bot] Introduction to Chatbot](http://lee-w.github.io/posts/bot/2016/11/introduction-to-chatbot/#introduction-to-chatbot)

## What is Telegram
在台灣，好像還沒有那麼多人用 Telegram
簡單來說就跟 Facebook Messenger 或 Line 這類的 IM 差不多

## Why Telegram
至於這次為什麼要選用 Telegram 麻
是因為上次有聽其他開發者說 Telegram Bot 提供相當多的功能
就想說來試試看

## Web Framework
上次寫 Line EchoBot 的教學是用 django
這次來試試 Flask

Source Code 一樣放在 GitHub 上
這篇文章會用[minimal-flask](https://github.com/Lee-W/telegram_echobot/tree/minimal-flask) branch 當範例
只有 31 行 Code，比較容易理解

[master](https://github.com/Lee-W/telegram_echobot/tree/master) 上也是用 Flask
只是架構比較複雜，有試一下 Flask 的 blueprint，之後可能還會多加一些奇怪的功能 xd

## Apply a telegram bot
首先當然必須要有[Telegram](https://telegram.org) 的帳號
再來要加[BotFather](https://telegram.me/botfather) 為好友

跟他說 `/newbot`
接著他會問你，Bot 的 name 跟 username

- name 是 Bot 在聯絡人資訊顯示的名稱
- username 則比較像 id 的概念，而且一定要用 Bot 結尾

之後就會得到剛申請 Bot 的 API Token
然後你就可以從 `https://telegram.me/<bot_username>` 找到剛申請的 bot


## Telegram Bot API Wrapper
開發上，我使用的是[python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)

```shell
pip install python-telegram-bot
```

它其中一點設計的很不錯的是
Telegram API 的命名是 CamelCase (e.g. sendMessage)
但 Python 的命名 convention 卻是 lowercase_separated_by_underscores (e.g. send_message)
而它是兩種都支援

## Star Programming
先附上全部的 code，後面再慢慢解釋

```python
import sys

import telegram
from flask import Flask, request


app = Flask(__name__)
bot = telegram.Bot(token='Your API Token')


def _set_webhook():
    status = bot.set_webhook('https://Your URL/hook')
    if not status:
        print('Webhook setup failed')
        sys.exit(1)


@app.route('/hook', methods=['POST'])
def webhook_handler():
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)

        text = update.message.text

        update.message.reply_text(text)
    return 'ok'


if __name__ == "__main__":
    _set_webhook()
    app.run()
```


### Setup 
其中有兩個地方，必須要改成自己的設定

#### 1. API Token

```python
bot = telegram.Bot(token='Your API Token')
```
Your API Token 要改成剛剛取得的 API Token

#### 2. Webhook URL
_set_webhook 中的 Your URL

```python
statue = bot.set_webhook('https://Your URL/hook')
```

這裡的 URL 就是設定成你這個 Bot Server 的 URL
不過 Telegram 一樣要求必須要是 https
最簡單的方式就是使用 ngrok
(ngrok 的使用在[[Bot] Line Echo Bot on Django](http://lee-w.github.io/posts/bot/2016/11/line-echo-bot-on-django/#line-echo-bot-on-django) 最後面有介紹 )
平常測試使用 ngrok 就很足夠了
之後要 production 的時候，在 deploy 到適當的 server 就好了

### \_set\_webhook
Telegram 有兩種接收訊息的方式
隨時去監聽的 webhook，和主動去要求更新的 `get_updates`
這裡使用的是 webhook

這個 function 先設定 Bot 的 webhook URL，如果設定失敗就直接終止程式
也就是告訴 Telegram 要把 Bot 收到的訊息傳到哪
而 `set_webhook` 前面要有個 \_的原因是我不希望它被其他的 code 使用
但 Python 本身並不支援 Private 的概念，而是慣例上在前面加一個底線

```python
def _set_webhook():
    status = bot.set_webhook('https://Your URL/hook')
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
```

在最後 run Flask app 前，要先把 webhook URL 設定好

```python
if __name__ == "__main__":
    _set_webhook()
    app.run()
```

### wehook\_handler
這裡就是 bot 收到訊息要怎麼處理

```python
@app.route('/hook', methods=['POST'])
def webhook_handler():
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)

        text = update.message.text

        update.message.reply_text(text)
    return 'ok'
```

`app.route` 這個 decorator 是 Flask 的語法
表示 `https:/Your URL/hook` 會導到這個 function，而它只能接受 POST
這裡設定的 `/hook` 也就是為什麼在 `_set_webhook` 中的 URL 最後面必須有 `/hook`

另外還可以發現 webhook_handler 是不帶任何參數的
跟 django 不同的是
Flask 把 request 這種幾乎所有 view function 都會用到的參數直接變成全域可讀取的變數
也就是最一開始的

```python
from flask import Flask, request
```

接下來 `webhook_handler` 內做的就只是把收到的訊息轉成 `update`
再從裡面讀到對方傳來的 `text`
最後用 `reply_text` 回傳同樣的 text 回去

---

這是最簡單的 Telegram Bot
不過我覺得開始學一個東西，還是會希望能在最短時間看到點東西，再慢慢專研
接下來可以從[python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) 的[wiki](https://github.com/python-telegram-bot/python-telegram-bot/wiki)，試更多 Telegram Bot 的功能

## Reference
- [Simple-Echo-Telegram-Bot](https://github.com/sooyhwang/Simple-Echo-Telegram-Bot)
- [開發 Telegram Bot 簡介](http://blog.30sparks.com/develop-telegram-bot-introduction/)