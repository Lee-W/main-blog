---
Title: [Bot] Line Echo Bot on Django
Date: 2016-11-24 03:26
Category: Bot
Tags: django, Line
Slug: line-echo-bot-on-django
Authors: Lee-W
Summary: 
---

單純要寫一個只會Echo的Line Chat Bot
用flask只要85行的code就能解決
官方已經有提供相當清楚的範例[flask-echo]
(https://github.com/line/line-bot-sdk-python/tree/master/examples/flask-echo)了

這篇文章則是提供了django的做法
想直接看code也可以參考[line_echobot](https://github.com/Lee-W/line_echobot)

<!--more-->

# Line Messaging API (line-bot-sdk-python)

詳細的Line Bot提供哪些功能，該如何使用
可以在[API Reference - Messaging API](https://devdocs.line.me/en/)找到
之後的文章，會談如何使用文字以外的功能

這裡直接使用官方提供的[line-bot-sdk-python](https://github.com/line/line-bot-sdk-python)

```sh
pip3 install line-bot-sdk
```

另外官方也提供[java](https://github.com/line/line-bot-sdk-java), [go](https://github.com/line/line-bot-sdk-go), [php](https://github.com/line/line-bot-sdk-php), [ruby](https://github.com/line/line-bot-sdk-ruby), [perl](https://github.com/line/line-bot-sdk-perl)的版本

# Start Project
## Create Project

```sh
# Create a line_echobot project
django-admin startproject line_echobot

# Create an echobot app
python3 manage.py startapp echobot
```

## Setup Line Secrets

接著設定Line Bot的`Channel Secret`, `Channel Access Token`
(可以在Line Bot的`Line Deverloper`頁面取得)

不過這些值不該被git記錄，所以不該被寫死在`settings.py`中
建議將這些值寫入環境變數

```sh
export SECRET_KEY='Your django secret key'
export LINE_CHANNEL_ACCESS_TOKEN='Your line channel access token'
export LINE_CHANNEL_SECRET='Your line channel secret'
```

執行時，讓設定檔先去讀取這些環境變數
下面的`get_env_variable`函式是用來取得環境變數
只要有少設定，就會丟出ImproperlyConfigured的例外事件中斷執行

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

不過如果只是單純測試用，這些值也可以直接寫死在settings.py中

另外也不要忘了在`INSTLLED_APPS`加入echobot

一般來說，django產生project時
`settings.py`裡面就會有secret key
這裡的做法是把預設的secret key刪掉
設定到環境變數中，避免被git記錄下來
如果還需要另外還要重新產生可以透過[django-secret-keygen.py](https://gist.github.com/mattseymour/9205591)

## Setup Line Webhook URL
再來要設定一個Webhook URL
讓Line可以把Bot收到的訊息傳給我們

先在project的`urls.py`設定
讓project可以找到echobot這個app的`urls.py`

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

接著在echobot內，創一個`urls.py`
並將url再導到`callback`，呼叫`views.py`裡面的`callback`函式(接下來才會實作)

```python
# echobot/urls.py

from django.conf.urls import url

from . import views

urlpatterns = [
    url('^callback/', views.callback),
]
```

這些都設定完後，要在Line那邊設定的Webhook Url就是`https://"your domain name"/echobot/callback/`
(`your domain name`要設定什麼，會在這篇文章的[最後](#https-server)說明)

## Implement Callback Funtion
接下來就是要在`echobot/views.py`實作`callback`了

### Initial
先import相關的函式庫

```python
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser, WebhookHanlder
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
```

透過line_bot_api傳訊息給Line，讓Line轉傳給使用者

```python
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
```

### Callback Function
有兩種方法可以處理Line Server送過來的訊息
這裡先用Todo記著，待會再來補上

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
先確認這個request是不是真的是從Line Server傳來的
要確認這件事，需要
- request的body
- request header中的X-Line-Signature

也就是上面的

```python
signature = request.META['HTTP_X_LINE_SIGNATURE']
body = request.body.decode('utf-8')
```

### Handle Recevied Message
取得body跟signature後
Line Bot API會在處理訊息的同時，確認這個訊息是否來自Line

而處理Line傳過來給我們的訊息，有兩種不同的做法

#### WebhookParser

WebhookParser會Parse這個訊息的所有欄位
讓我們針對各種不同型別的訊息做個別的處理
e.g.
- UserID
- Event Type
- Message Content
- and etc.

在[這裡](https://github.com/line/line-bot-sdk-python#webhook-event-object)可以找到有哪些欄位

這段code要取代上面的`# TODO: Define Receiver`

```python
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)
```

下面三段code則要取代`# TODO: Handler when receiver Line Message`

parser會parse所有的event跟各個event中的所有欄位
如果request不是從Line Server來的，就會丟出InvalidSignatureError
其他使用錯誤，或Line Server的問題都會是丟出LineBotApiError

```python
try:
	events = parser.parse(body, signature)
except InvalidSignatureError:
	return HttpResponseForbidden()
except LineBotApiError:
	return HttpResponseBadRequest()
```

再來要判斷收到的事件是什麼事件
這個Bot只需要echo純文字訊息
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

最後的`reply_message`函式，讓我們傳訊息給Line Server
第一個參數是要回傳要用的reply\_token，可以從事件中取得 （`event.reply_token`）
使用這個reply\_token做回覆，是不用收費的
不過同一個reply\_token只能使用一次，而且在一定的時間內就會失效

第二個參數是這次要回傳的訊息
[這裡](https://github.com/line/line-bot-sdk-python#send-message-object)有所有能回傳的訊息
也可以傳一個都是訊息的list或tuple
不過一次最多只能傳5個
只要超過就會有LineBotApiError

#### WebhookHandler
WebhookHandler是針對每一種不同的訊息型態註冊一個處理器
只要收到這樣的訊息，就會丟給對應的處理器
如果確定每一類訊息，在任何情況下都會有相似的處理方式，就很適合這樣的設計

接下來的三段code要取代`# TODO: Define Receiver`

```python
handler = WebhookHandler(settings.LINE_CHANNEL_SECRET)
```

先為handler加入，TextMessage的處理器
參數是接收到的event
這裡做的也是讀取到原本event中的文字，並回傳回去

```python
@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text)
    )
```

因為沒有要處理其他訊息
如果收到其他訊息(e.g. 貼圖, 照片)或訊息以外的事件
使用default來回傳"Currently Not Support None Text Message"的文字訊息

```python
@handler.default()
def default(event):
    print(event)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='Currently Not Support None Text Message')
    )
```

下面的這段code是要取代`# TODO: Handler when receiver Line Message`
handler判斷完這個訊息，應該被哪個處理器處理，就會傳給那個函式處理

```python
try:
	handler.handle(body, signature)
except InvalidSignatureError:
	return HttpResponseForbidden()
except LineBotApiError:
	return HttpResponseBadRequest()
```

#### Full Code
由於上面的code說明比較分散
這裡附上兩個版本各自的完整版

- WebhookParser
 
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

- WebhookHandler

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

到了這裡，echo bot實作的部分就完成了


## <a name='https-server'></a> Https Server (Setup 'your domain name')
使用這些Bot的服務時，大多會要求我們一定要先有一個Https Server
除了自己架Http Server外，還透過其他服務，更方便我們做測試
接下來我會分享兩種做法

1. 架在[Heroku](https://www.heroku.com) (由於篇幅的關係，Heroku會在接下來的文章談)
2. 使用[ngrok](https://ngrok.com)

### ngrok
ngrok提供的服務是
讓外部的訊息先經過ngrok的server，ngrok再將這個訊息傳給你的server
回傳時也是從你的server傳給ngrok的server，再把訊息傳出去
所以外部都只會看到ngrok的server

![ngrok](https://ngrok.com/static/img/demo.png)

```sh
# Install ngrok on mac
brew cask install ngrok
```

先把django的server run起來

```sh
python3  manage.py runserver
```

預設django的port是8000
這裡並不需要使用0.0.0.0:8000，讓外部可以連到這個django server
ngrok會把request傳到local端相對應的port

接著就要用ngrok將request導到本地端的port 8000

```sh
ngrok http 8000
```

![1_ngrok_example](http://i.imgur.com/r525wEI.png)

再來到Line Bot的`Line Developer`頁面設定Webhook URL
這時候填上ngrok後的https那串url，再加上`echobot/callback/`(我們設定的callback url)
(e.g. `https://2.....f.ngrok.io/echobot/callback/`)
![2_webhook_url](http://i.imgur.com/qVWlwoK.png)

值得注意的是我的Webhook URL下面有一個`Read timeout.`
如果按了後面的Verify，Line Server會傳一些測試訊息過來
但是那個reply\_token 是無法被回覆的
這時候在Server就會丟出LineBotApiError
不過沒關係，這只是給我們檢查用的
並沒有一定要通過才能使用Line Bot

這時候加Bot為好友，就可以開始跟它聊天了
![3_message_sample](http://i.imgur.com/boxeHoG.png)

如果你發現除了echo訊息外，還有其他的訊息
可能就是沒有把Atuo Reply Message關掉
這時候就可以去Line Bot的`LINE@ Manger`
`Settings` -> `Bot Settings`把它關掉
或者到`Messages` -> `Auto Reply Message`做修改訊息內容


# Reference 
- [新版Line@ Messaging API使用心得 (Line Bot v2)
](http://studyhost.blogspot.tw/2016/10/line-messaging-api-line-bot-v2.html)
- [LineBot - Sinatra](http://jiunjiun.logdown.com/posts/2016/10/06/linebot-with-sinatra)
- [ngrok](https://ngrok.com)