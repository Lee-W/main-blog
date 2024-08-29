Title: 從 Andromoney 到 MOZE
Date: 2018-09-09 16:00
Category: Tech
Tags: Develop, Utility
Slug: from-andromoney-to-moze
Authors: Wei Lee

最近不小心被 [MOZE](https://www.mozeapp.com) 的介面燒到
一個衝動就從 [AndroMoney](https://web.andromoney.com) 轉到 MOZE
這篇算是來記錄從 AndroMoney 把資料轉換到 MOZE 的過程

<!--more-->

## 一些無關本文的前言

雖然 X-Village 暫時告一個段落，好像應該來寫個什麼
但真的要寫起來還要再花一點時間

上次 Blog 發文都已經是一年前的事了
但點閱率竟然有一點在上升（雖然還是很低 QAQ）
還有一些人看了我在 Logdown 的 LineBot 文跑來找我討論
覺得蠻開心的 xD
但這邊還是一直都沒辦法被找到 QQ
以後考慮同步發到 Medium 好了

不過好像該進入本文了 xD

## 為什麼換到 MOZE

當初在 Android 上使用 AndroMoney 就只是因為他免費，而且還算是好用
剛好換到 iOS 的時候，這款 app 也在 App Store 有上架
懶得轉換資料的情況下就繼續買了
用下來覺得 AndroMoney 好像還是在 Android 上比較好用
AndroMoney 的各種功能都很方便，只是介面上就比較普通 xD
而且 AndroMoney 各個平台都有，就算哪天想換 Android 的手機也不怕轉換問題
但是啊， MOZE 的介面就是好看 xD

再來就要說說其他我喜歡 MOZE 的原因

### AndroMoney 沒有 (或我不會用) 的功能

#### 借款事件

![3-borrow.png](/images/posts-image/2018-09-09-andromoney-to-moze/3-borrow.png)

MOZE 會幫我記住我借錢給誰，而且會一直提醒我誰跟我借了錢
以前都還要特地記錄到其他 app

![4-borrow.png](/images/posts-image/2018-09-09-andromoney-to-moze/4-borrow.png)
而且借出的錢，不會算在我的支出，所以也不會影響到我的預算
算是蠻方便的功能

#### 繳費事件

提醒我信用卡要繳費的時間
也會有跟借款事件差不多的提醒

#### 動態改變每天剩餘的預算

這是一個我還蠻需要的功能
我會想知道前幾天花的錢如何影響我這個月剩下的日子的預算
而不是一個從月初的預算直接除以 30 都不改變的數字

#### 帳戶 icon

每個帳戶都能加入自己的 icon
只要是付費版的 MOZE 就會有各家銀行的 icon
![5-icon.jpeg](/images/posts-image/2018-09-09-andromoney-to-moze/5-icon.jpeg)
雖然他說是付費圖示，但其實這幾個是免費的
只有其他類別的彩色圖是要購買
但我是覺得原本的我比較喜歡 xD
另外，也可以自己製作想要的 icon 匯入 ~

#### 電子發票載具

以前都沒有什麼要用電子載具的誘因
就完全忘了這回事
現在這個可以直接幫我記帳就很吸引我
而且他也有支援 wideget ，給店家掃過後，馬上就能用 Apple Pay

另外，我原本以為從雲端載下消費紀錄，一定會要再創一個紀錄
但其實這是可以連結到某一筆過去的紀錄
這對我也是蠻重要的功能

只是目前好像還不能針對轉帳或借款事件歸帳
希望這些能透過 MOZE 3.0 會有的分帳功能解決

#### 拆帳 (MOZE 3.0 才有)

雖然目前還沒有，但這個功能我現在很期待
所以還是想列一下 xD

### MOZE 沒有 (或我不會用) 的功能

#### 專案不能跨幣別

我之前去歐洲的那些紀錄就因為這樣，必須用標籤來分類 QQ
不過聽說 MOZE 3.0 會新增就是

#### 不能將單一紀錄不計算在花費中

主要是有些特別的花費我不會想要扣在我的預算中
這樣那個月剩下的天數的預算就都會是 0，好像也不太對 ...

#### 【AndroMoney 功能教學目錄】

這個我真的覺得超棒的
他把目前能用他現有功能做到的事，全部整理起來
現在 MOZE 還是比較需要去爬舊文翻，或直接問粉專
但不得不說 MOZE 回復速度真的超快

## AndroMoney to MOZE transformater

身為一個攻城獅，當然還是要寫自動化的程式來幫我轉換資料格式
手動要處理 5、6000 筆帳務紀錄有點太累了
btw MOZE 有說之後會提供 web 版的匯入工具

在 MOZE 首頁 FAQ 可以找到要如何匯入資料 ([MOZE 格式](https://docs.google.com/spreadsheets/d/1OeVuhID8l_vhmjHbDKReAXcLkIi0NvDUDIAwD9I8AYQ/edit?usp=sharing))
基本上就是照著他的格式就能轉換大部分的資料

當然我也寫了一個小 script
**[AndroMoney_to_MOZE_transformater](https://github.com/Lee-W/AndroMoney_to_MOZE_transformater)**

### Script 使用方式

```sh
python transformater.py --input_file "Your input filename" extract
```

在轉換的過程中，會有一些資料還是要手動輸入的
其實後來大多時間是花在這 ...

會抓出的資料有

* 帳戶（以及其起始金額）
* 專案
* 主類別、次類別

後來發現還有另一個問題是不同幣別的轉帳， AndroMoney 匯出的資料不會有轉入的金額
所以沒辦法自動化，這點倒是比較麻煩

```sh
python transformater.py transformat --input_file "Your input filename" --output_file MOZE.csv
```

再來就是要把原本 AndroMoney 的紀錄轉成 MOZE 的格式
只要把這個 `MOZE.csv` (一定要是這個檔名) 丟到 Dropbox 的 `應用程式/MOZE`
MOZE 就能找到，並能選擇匯入

### 踩到的一些坑

寫這個 script 的過程中，其實踩到蠻多坑的
匯入了好幾次才成功

一來這是我第一次從[argparse](https://docs.python.org/3/library/argparse.html) 換到[click](http://click.pocoo.org)
原本想說 argparse 已經算是蠻好用的了
click 真的又更直覺了一點，難怪這麼多人推薦

第一個遇到的問題就是轉帳的「相關行數」
一開始不知道這個行數是從多少開始
以寫程式來說，我就直接去抓那個 row 的 index
所以抓到的 index 是 0-based
後來想到可以試試看 1-based，還是無法匯入成功
最後才發現還要把標頭也考慮進去
第一個 row 其實 index 是 2

第二個問題是轉帳的類別
文件其實只說不用「子類別」，沒說「主類別」要怎麼處理 xD
我試了各種可能的類別後
自己去匯出了一筆轉帳紀錄，才解決
原來轉帳的主類別分別會是「轉入」跟「轉出」
![1-doc.png](/images/posts-image/2018-09-09-andromoney-to-moze/1-doc.png)

後來弄完後有再去看一下文件，才發現下面其實有寫 ......
![2-doc.png](/images/posts-image/2018-09-09-andromoney-to-moze/2-doc.png)

這些問題我都跟作者反應了，他都超快就回了
他是說之後會透過 web 版的工具匯入

## Future Improvement

其實我還是蠻喜歡 AndroMoney 的
所以也許會找個時間寫怎麼把 MOZE 轉回 AndroMoney 的功能會寫個 MOZE to AndroMoney
避免我哪天又想回到 Android 了 xD
