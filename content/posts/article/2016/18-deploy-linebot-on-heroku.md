Title: Deploy LineBot on Heroku
Date: 2016-11-27 06:05
Category: Tech
Tags: Heroku, django, Chat Bot, deploy
Slug: deploy-linebot-on-heroku
Authors: Lee-W
Summary: 
Series: Line Bot Tutorial


上一篇提到如何用 ngrok
讓我們可以不用架 Https Server，直接在本地端測試 Bot

再來要談的是如何把 Bot 部署到 Heroku 上

<!--more-->

# Why not ngrok
使用 ngrok 必須要讓你的本地端一直開著才能收到訊息
而且免費版的 ngrok 每次都會更改 url
所以我們需要一個可以讓其他人較長時間測試的 Server

以我自己的開發習慣
我會使用 ngrok，來做 Bot 的基本除錯
Heroku 則是用來讓其他人測試功能
真的要上線的時候才會自己架一個 Https Server

Line 的帳號也是 ngrok, heroku 跟上線需要的各申請一個
不過 ngrok 可以好幾個 Line Bot 專案共用一個即可

# Heroku

## Create App
先上[Heroku](https://www.heroku.com) 辦個帳號

到個人的 dashboard
`New` -> `Create New App`
選一個名字，就創好 App 了

## Deploy

### Add Remote
在部署之前要先安裝[Heroku CLI](https://devcenter.heroku.com/articles/heroku-command-line)

再來我們要到原本 line-echobot，將 heroku 加入這個專案的 remote

```sh
heroku login
heroku git:remote -a leewbot
```

接著用 `git remote -v` 就能看到 `heroku` 已經被加入 remote 了
以後只要 `git push heroku master`，就能部署到 Heroku
不過我們還必須要多做一些設定才能讓 Bot 順利的部署

### Environment Variables
首先是我們原先設定的環境變數
Heroku 是透過這個指令來做設定

```sh
heroku config:set "env key":"env value"
```

或者也能到 dashboard 的 `Settings` -> `Config Variables` -> `Reveal Config Vars` 做設定

### Python Envrionments
因為 Heroku 支援多種不同的語言
所以要讓 Heroku 知道我們使用的是 Python

Heroku 可過專案中是否有 `requirements.txt` 來判斷這個專案是否為 Python 專案
並且安裝 `requirements.txt` 內的函式庫
名稱如果打錯，可能會讓 Heroku 不知道這是 Python 專案，導致部署失敗

另外可以透過 `runtime.txt` 來指定 Python 的版本
目前支援這兩種版本
- `python-2.7.12`
- `python-3.5.2`

### Deploy Settings - Procfile
再來必須要讓 Heroku 知道我們執行專案的指令是什麼
這個指令就是寫在 `Profile` 中

這裡使用的部署套件是 gunicorn
先在 `requirements.txt` 加入 `gunicorn==19.0.0`
再來創一個 `Profile`，內容是

```
web: gunicorn line_echobot.wsgi --log-file -
```

如果用其他的部署套件，則需要修改 web 後面的指令

到了這裡就做好所有的設定了
最後只要 `git push heroku master` 就會部署到 Heroku 上

透過 `heroku open` 能看到剛剛部署上去的專案
接著把專案的網址加上我們先前設定的 callback url `echobot/callback`
設定到 Line Bot 的 Webhook URL，就完成了

# Reference
- [Getting Started on Heroku with Python](https://devcenter.heroku.com/articles/getting-started-with-python#introduction)
- [Deploying Python and Django Apps on Heroku](https://devcenter.heroku.com/articles/deploying-python)