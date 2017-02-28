---
Title: [Bot] Deploy LineBot on Heroku
Date: 2016-11-27 06:05
Category: Bot
Tags: Heroku, django, Line
Slug: deploy-linebot-on-heroku
Authors: Lee-W
Summary: 
Series: Line Bot Tutorial
---

上一篇提到如何用ngrok
讓我們可以不用架Https Server，直接在本地端測試Bot

再來要談的是如何把Bot部署到Heroku上

<!--more-->

# Why not ngrok
使用ngrok必須要讓你的本地端一直開著才能收到訊息
而且免費版的ngrok每次都會更改url
所以我們需要一個可以讓其他人較長時間測試的Server

以我自己的開發習慣
我會使用ngrok，來做Bot的基本除錯
Heroku則是用來讓其他人測試功能
真的要上線的時候才會自己架一個Https Server

Line的帳號也是ngrok, heroku跟上線需要的各申請一個
不過ngrok可以好幾個Line Bot專案共用一個即可

# Heroku

## Create App
先上[Heroku](https://www.heroku.com)辦個帳號

到個人的dashboard
`New` -> `Create New App`
選一個名字，就創好App了

## Deploy

### Add Remote
在部署之前要先安裝[Heroku CLI](https://devcenter.heroku.com/articles/heroku-command-line)

再來我們要到原本line-echobot，將heroku加入這個專案的remote

```sh
heroku login
heroku git:remote -a leewbot
```

接著用`git remote -v`就能看到`heroku`已經被加入remote了
以後只要`git push heroku master`，就能部署到Heroku
不過我們還必須要多做一些設定才能讓Bot順利的部署

### Environment Variables
首先是我們原先設定的環境變數
Heroku是透過這個指令來做設定

```sh
heroku config:set "env key":"env value"
```

或者也能到dashboard的`Settings` -> `Config Variables` -> `Reveal Config Vars`做設定

### Python Envrionments
因為Heroku支援多種不同的語言
所以要讓Heroku知道我們使用的是Python

Heroku可過專案中是否有`requirements.txt`來判斷這個專案是否為Python專案
並且安裝`requirements.txt`內的函式庫
名稱如果打錯，可能會讓Heroku不知道這是Python專案，導致部署失敗

另外可以透過`runtime.txt`來指定Python的版本
目前支援這兩種版本
- `python-2.7.12`
- `python-3.5.2`

### Deploy Settings - Procfile
再來必須要讓Heroku知道我們執行專案的指令是什麼
這個指令就是寫在`Profile`中

這裡使用的部署套件是gunicorn
先在`requirements.txt`加入`gunicorn==19.0.0`
再來創一個`Profile`，內容是

```
web: gunicorn line_echobot.wsgi --log-file -
```

如果用其他的部署套件，則需要修改web後面的指令

到了這裡就做好所有的設定了
最後只要`git push heroku master`就會部署到Heroku上

透過`heroku open`能看到剛剛部署上去的專案
接著把專案的網址加上我們先前設定的callback url `echobot/callback`
設定到Line Bot的Webhook URL，就完成了

# Reference
- [Getting Started on Heroku with Python](https://devcenter.heroku.com/articles/getting-started-with-python#introduction)
- [Deploying Python and Django Apps on Heroku](https://devcenter.heroku.com/articles/deploying-python)