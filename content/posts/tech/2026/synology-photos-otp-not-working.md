Title: Synology Photos 驗證碼又又又又又沒用了
Date: 2026-09-11 15:30 +0800
Category: Tech
Tags: Synology, NAS
Slug: synology-photos-otp-not-working
Authors: Wei Lee
Lang: zh-tw
Status: draft

太久沒有登入 Synology Photos ，就會因為 session 過期需要重新登入
然後重新登入的時候，有時候又會一直遇到驗證碼錯誤...

<!--more-->

已經遇到這件事很多次了，是該寫篇筆記記錄下來

## 原因

手機跟 NAS 的系統時間對不上
因為 TOTP 是基於時間產生的
只要兩邊的時間對不上，就驗證碼就不會過

## 解法

* DSM 控制台
    * 區域選項
        * 時間
            * [x] 與 NTP 伺服器同步時間」
                * 立即更新

同步完時間之後，再重新輸入驗證碼，通常就可以正常登入了
