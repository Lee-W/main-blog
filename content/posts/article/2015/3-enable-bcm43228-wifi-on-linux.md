Title: 驅動 BCM43228 網卡在 Linux 的無線功能
Date: 2015-01-28 08:52
Category: Linux-Unix
Tags: Dual Boot
Slug: enable-bcm43228-wifi-on-linux
Authors: Lee-W
Summary: 


最近本來下定決心要來玩 arch linux
結果竟然被筆電的網卡搞死了
抓了官網的驅動竟然不能 build...

沒想到改成灌 Linux mint 17，依然有問題＝＝
最後找到一個解決的辦法

<!--more-->

先確定你的網卡是不是 BC43228
```shell
lspci | grep Network
```

如果是的話就能開始進行安裝了
```shell
sudo apt-get install linux-headers-generic
sudo apt-get install --reinstall bcmwl-kernel-source
```
如果成功的話，Wifi 應該馬上就能用了

# Reference
[Ubuntu14.04 Acer Aspire V5 571 Broadcom BCM43228 WiFi - BeyondLogic](http://wiki.beyondlogic.org/index.php?title=Ubuntu14.04_Acer_Aspire_V5_571_Broadcom_BCM43228_WiFi)