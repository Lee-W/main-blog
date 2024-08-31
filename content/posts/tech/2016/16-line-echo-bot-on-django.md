Title: Line Echo Bot on Django
Date: 2016-11-24 03:26
Category: Tech
Tags: Django, Chat Bot
Slug: line-echo-bot-on-django
Authors: Wei Lee
Series: Line Bot Tutorial

單純要寫一個只會 Echo 的 Line Chat Bot
用 flask 只要 85 行的 code 就能解決
官方已經有提供相當清楚的範例[flask-echo](https://github.com/line/line-bot-sdk-python/tree/master/examples/flask-echo) 了

這篇文章則是提供了 django 的做法
想直接看 code 也可以參考[line_echobot](https://github.com/Lee-W/line_echobot)

<!--more-->

# Line Messaging API (line-bot-sdk-python)

詳細的 Line Bot 提供哪些功能，該如何使用
可以在[API Reference - Messaging API](https://devdocs.line.me/en/) 找到
之後的文章，會談如何使用文字以外的功能

這裡直接使用官方提供的[line-bot-sdk-python](https://github.com/line/line-bot-sdk-python)

```shell
pip3 install line-bot-sdk
```

另外官方也提供[java](https://github.com/line/line-bot-sdk-java), [go](https://github.com/line/line-bot-sdk-go), [php](https://github.com/line/line-bot-sdk-php), [ruby](https://github.com/line/line-bot-sdk-ruby), [perl](https://github.com/line/line-bot-sdk-perl) 的版本

# Start Project

## Create Project

```shell
# Create a line_echobot project
django-admin startproject line_echobot

# Create an echobot app
python3 manage.py startapp echobot
```

## Setup Line Secrets

接著設定 Line Bot 的 `Channel Secret`, `Channel Access Token`
( 可以在 Line Bot 的 `Line Developer` 頁面取得 )

不過這些值不該被 git 記錄，所以不該被寫死在 `settings.py` 中
建議將這些值寫入環境變數

```shell
export SECRET_KEY='Your django secret key'
export LINE_CHANNEL_ACCESS_TOKEN='Your line channel access token'
export LINE_CHANNEL_SECRET='Your line channel secret'
```

執行時，讓設定檔先去讀取這些環境變數
下面的 `get_env_variable` 函式是用來取得環境變數
只要有少設定，就會丟出 ImproperlyConfigured 的例外事件中斷執行

```python
# line_echobot/settings.py

......

def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = 'Set the {} environment variable'.format(var_name)
        raise ImproperlyConfigured(error_msg)

SECRET_KEY = get_env_variable('SECRET_KEY')
LINE_CHANNEL_ACCESS_TOKEN = get_env_variable('LINE_CHANNEL_ACCESS_TOKEN')
LINE_CHANNEL_SECRET = get_env_variable('LINE_CHANNEL_SECRET')

......

INSTALLED_APPS = [
    ......,
    'echobot'
]
```

不過如果只是單純測試用，這些值也可以直接寫死在 settings.py 中

另外也不要忘了在 `INSTLLED_APPS` 加入 echobot

一般來說，django 產生 project 時
`settings.py` 裡面就會有 secret key
這裡的做法是把預設的 secret key 刪掉
設定到環境變數中，避免被 git 記錄下來
如果還需要另外還要重新產生可以透過[django-secret-keygen.py](https://gist.github.com/mattseymour/9205591)

## Setup Line Webhook URL

再來要設定一個 Webhook URL
讓 Line 可以把 Bot 收到的訊息傳給我們

先在 project 的 `urls.py` 設定
讓 project 可以找到 echobot 這個 app 的 `urls.py`

```python
# line_echobot/urls.py
......

import echobot

urlpatterns = [
    ......,
    url(r'^echobot/', include('echobot.urls')),
]

......
```

接著在 echobot 內，創一個 `urls.py`
並將 url 再導到 `callback`，呼叫 `views.py` 裡面的 `callback` 函式 ( 接下來才會實作 )

```python
# echobot/urls.py

from django.conf.urls import url

from . import views

urlpatterns = [
    url('^callback/', views.callback),
]
```

這些都設定完後，要在 Line 那邊設定的 Webhook Url 就是 `https://"your domain name"/echobot/callback/`
(`your domain name` 要設定什麼，會在這篇文章的[最後](#https-server) 說明)

## Implement Callback Function

接下來就是要在 `echobot/views.py` 實作 `callback` 了

### Initial

先 import 相關的函式庫

```python
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser, WebhookHandler
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
```

透過 line_bot_api 傳訊息給 Line，讓 Line 轉傳給使用者

```python
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
```

### Callback Function

有兩種方法可以處理 Line Server 送過來的訊息
這裡先用 Todo 記著，待會再來補上

```python
# TODO: Define Receiver

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        # TODO: Handler when receiver Line Message

        return HttpResponse()
    else:
        return HttpResponseBadRequest()
```

### Validate Signature

處理訊息之前
先確認這個 request 是不是真的是從 Line Server 傳來的
要確認這件事，需要

* request 的 body
* request header 中的 X-Line-Signature

也就是上面的

```python
signature = request.META['HTTP_X_LINE_SIGNATURE']
body = request.body.decode('utf-8')
```

### Handle Received Message

取得 body 跟 signature 後
Line Bot API 會在處理訊息的同時，確認這個訊息是否來自 Line

而處理 Line 傳過來給我們的訊息，有兩種不同的做法

#### WebhookParser

WebhookParser 會 Parse 這個訊息的所有欄位
讓我們針對各種不同型別的訊息做個別的處理
e.g.

* UserID
* Event Type
* Message Content
* and etc.

在[這裡](https://github.com/line/line-bot-sdk-python#webhook-event-object) 可以找到有哪些欄位

這段 code 要取代上面的 `# TODO: Define Receiver`

```python
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)
```

下面三段 code 則要取代 `# TODO: Handler when receiver Line Message`

parser 會 parse 所有的 event 跟各個 event 中的所有欄位
如果 request 不是從 Line Server 來的，就會丟出 InvalidSignatureError
其他使用錯誤，或 Line Server 的問題都會是丟出 LineBotApiError

```python
try:
    events = parser.parse(body, signature)
except InvalidSignatureError:
    return HttpResponseForbidden()
except LineBotApiError:
    return HttpResponseBadRequest()
```

再來要判斷收到的事件是什麼事件
這個 Bot 只需要 echo 純文字訊息
所以先判斷這個事件是不是訊息事件，而這個訊息是不是文字訊息

```python
for event in events:
    if isinstance(event, MessageEvent):
        if isinstance(event.message, TextMessage):
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=event.message.text)
            )
```

最後的 `reply_message` 函式，讓我們傳訊息給 Line Server
第一個參數是要回傳要用的 reply\_token，可以從事件中取得 （`event.reply_token`）
使用這個 reply\_token 做回覆，是不用收費的
不過同一個 reply\_token 只能使用一次，而且在一定的時間內就會失效

第二個參數是這次要回傳的訊息
[這裡](https://github.com/line/line-bot-sdk-python#send-message-object) 有所有能回傳的訊息
也可以傳一個都是訊息的 list 或 tuple
不過一次最多只能傳 5 個
只要超過就會有 LineBotApiError

#### WebhookHandler

WebhookHandler 是針對每一種不同的訊息型態註冊一個處理器
只要收到這樣的訊息，就會丟給對應的處理器
如果確定每一類訊息，在任何情況下都會有相似的處理方式，就很適合這樣的設計

接下來的三段 code 要取代 `# TODO: Define Receiver`

```python
handler = WebhookHandler(settings.LINE_CHANNEL_SECRET)
```

先為 handler 加入，TextMessage 的處理器
參數是接收到的 event
這裡做的也是讀取到原本 event 中的文字，並回傳回去

```python
@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text)
    )
```

因為沒有要處理其他訊息
如果收到其他訊息 (e.g. 貼圖 , 照片 ) 或訊息以外的事件
使用 default 來回傳 "Currently Not Support None Text Message" 的文字訊息

```python
@handler.default()
def default(event):
    print(event)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='Currently Not Support None Text Message')
    )
```

下面的這段 code 是要取代 `# TODO: Handler when receiver Line Message`
handler 判斷完這個訊息，應該被哪個處理器處理，就會傳給那個函式處理

```python
try:
    handler.handle(body, signature)
except InvalidSignatureError:
    return HttpResponseForbidden()
except LineBotApiError:
    return HttpResponseBadRequest()
```

#### Full Code

由於上面的 code 說明比較分散
這裡附上兩個版本各自的完整版

* WebhookParser

```python
# line_echobot/echobot/views.py
# WebhookParser version

from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):
                if isinstance(event.message, TextMessage):
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text=event.message.text)
                    )

        return HttpResponse()
    else:
        return HttpResponseBadRequest()
```

* WebhookHandler

```python
# line_echobot/echobot/views.py
# WebhookHandler version

from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage, TextMessage

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(settings.LINE_CHANNEL_SECRET)


@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text)
    )


@handler.default()
def default(event):
    print(event)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='Currently Not Support None Text Message')
    )


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()
        return HttpResponse()
    else:
        return HttpResponseBadRequest()
```

到了這裡，echo bot 實作的部分就完成了

<a name='https-server'></a>

## Https Server (Setup 'your domain name')

使用這些 Bot 的服務時，大多會要求我們一定要先有一個 Https Server
除了自己架 Http Server 外，還透過其他服務，更方便我們做測試
接下來我會分享兩種做法

1. 架在[Heroku](https://www.heroku.com) ( 由於篇幅的關係，Heroku 會在接下來的文章談 )
2. 使用[ngrok](https://ngrok.com)

### ngrok

ngrok 提供的服務是
讓外部的訊息先經過 ngrok 的 server，ngrok 再將這個訊息傳給你的 server
回傳時也是從你的 server 傳給 ngrok 的 server，再把訊息傳出去
所以外部都只會看到 ngrok 的 server

![ngrok](https://ngrok.com/static/img/demo.png)

```sh
# Install ngrok on mac
brew cask install ngrok
```

先把 django 的 server run 起來

```sh
python3  manage.py runserver
```

預設 django 的 port 是 8000
這裡並不需要使用 0.0.0.0:8000，讓外部可以連到這個 django server
ngrok 會把 request 傳到 local 端相對應的 port

接著就要用 ngrok 將 request 導到本地端的 port 8000

```sh
ngrok http 8000
```

![1_ngrok_example](/images/posts-image/2016-11-24-line-echo-bot-on-django/r525wEI.png)

再來到 Line Bot 的 `Line Developer` 頁面設定 Webhook URL
這時候填上 ngrok 後的 https 那串 url，再加上 `echobot/callback/`( 我們設定的 callback url)
(e.g. `https://2.....f.ngrok.io/echobot/callback/`)
![2_webhook_url](/images/posts-image/2016-11-24-line-echo-bot-on-django/qVWlwoK.png)

值得注意的是我的 Webhook URL 下面有一個 `Read timeout.`
如果按了後面的 Verify，Line Server 會傳一些測試訊息過來
但是那個 reply\_token 是無法被回覆的
這時候在 Server 就會丟出 LineBotApiError
不過沒關係，這只是給我們檢查用的
並沒有一定要通過才能使用 Line Bot

這時候加 Bot 為好友，就可以開始跟它聊天了
![3_message_sample](/images/posts-image/2016-11-24-line-echo-bot-on-django/boxeHoG.png)

如果你發現除了 echo 訊息外，還有其他的訊息
可能就是沒有把 Atuo Reply Message 關掉
這時候就可以去 Line Bot 的 `LINE@ Manager`
`Settings` → `Bot Settings` 把它關掉
或者到 `Messages` → `Auto Reply Message` 做修改訊息內容

## Reference

* [新版 Line@ Messaging API 使用心得 (Line Bot v2)
](http://studyhost.blogspot.tw/2016/10/line-messaging-api-line-bot-v2.html)
* [LineBot - Sinatra](http://jiunjiun.logdown.com/posts/2016/10/06/linebot-with-sinatra)
* [ngrok](https://ngrok.com)
