Title: Apply Line Messaging API
Date: 2016-11-22 12:43
Category: Bot
Tags: Line Bot
Slug: apply-line-messaging-api
Authors: Lee-W
Summary: 
Series: Line Bot Tutorial


先到[Messaging API](https://business.line.me/zh-hant/services/bot)申請帳號

`開始使用Messaging API`和`開始使用Developer Trial`申請到的帳號是不同的
之後不能互換，所以一開始就要根據需求來決定申請哪種帳號

<!--more-->
![1_messaging_api](http://i.imgur.com/3i3O1wO.png)

- `開始使用Messaging API`會申請免費版的帳號
  之後可以選擇付費升級為入門版等更多功能的版本
  主要拿來做正式發佈用的帳號

- `開始使用Developer Trial`則是Developer的帳號
  雖然一開始就能使用Push API，但好友人數只有50人
  如果還在開發階段，就適合辦這個帳號來測試
  不過需要注意的是developer帳號，並不能接升級成一般帳號

![2_price](http://i.imgur.com/FmTjOBH.png)

再來會詢問業務類別，跟要求設定Bot名稱和照片
![3_apply_account](http://i.imgur.com/VdCT8JX.png)
 
回到[Line Bussiness Center](https://business.line.me/zh-hant/)的帳號清單
就能看到帳號已經創好了
![4_success_apply](http://i.imgur.com/4ViJbIR.png)

---
進入剛剛創好的帳號的`LINE@ Manager`

頁面左上方，Bot名稱下方
@開頭的就是這個Bot的id
可以從Line輸入這個id加Bot為好友 （需加上@）

![5_bot_page](http://i.imgur.com/8DC4TSG.png)

接著到設定頁面左下方，找到`Settings`->`Bot Settings`

進入以下的畫面開啟Messaging API
![6_bot_setting](http://i.imgur.com/BtaSwa5.png)

開啟Bot API後，就會不能用以下三個功能
- 1-on-1 Chat
- LINE@ app
- Store Chat


之後會進到以下畫面
記得要把`Use webhooks`調成`Allow`
才能把這個Line Bot串到自己的server上
![7_bot_webhook](http://i.imgur.com/yqpw3x7.png)

往下拉可以看到更多的選項
![8_bot_detail](http://i.imgur.com/nKegbk6.png)
如果不想要Line每次收到訊息都自動幫你回覆
就要把`Auto Reply Message`調成`Don't Allow`
`Greeting Message`則是，剛加Bot為好友時的歡迎詞

如果有需要對這些訊息做設定
都可以在左手邊選單的`Messages`找到

再回到帳號清單就會看到，帳號已經開通Messaging API了
![9_finish_all_setting](http://i.imgur.com/io9LuHs.png)


進到`LINE Developers`就能取得你的Channel Secret和Channel Access Token了
（這些都是運用Line Messaging API會用到的）

![10_line_developers_page](http://i.imgur.com/cl8k3Mh.png)

除了前面提到可以用ID加好友，也能透過這裡的QR code

另外要注意的是`Webhook URL`
這裡之後要填的就是你的Server的Webhook url

# Reference
[Enable the Messaging API for your LINE@ account](https://developers.line.me/messaging-api/getting-started#apply_messagingapi)