Title: 解決 Win 8、Ubuntu 雙系統無法掛載 NTFS 分割區問題
Date: 2014-02-25 15:40
Category: Tech
Tags: Linux-Unix, Dual Boot
Slug: solution-to-win-8-ubuntu-dual-system-cannot-mount-ntfs-parition-problem
Authors: Lee-W

現在安裝了 Win8 和 Ubuntu 雙系統
每次只要開 Win 8 ，再重新開機進到 Ubuntu 就會出現 file system 無法掛載的問題
然後我在兩個系統間共同的 data 分割區就會無法掛載
可是再重開一次 Win 8，問題就神祕的解決了 @@
後來才發現原來是因為 Win 8 的 **Fast Boot**  造成的

<!--more-->

## 解決

![win8_start_up](/images/posts-image/2014-02-25-solution-to-win-8-ubuntu-dual-system-cannot-mount-ntfs-parition-problem/ohEfCkR.png)

> 控制台 \ 硬體和音效 \ 電源選項 \ 系統設定

只要把 `開啟快速啟動` 取消掉就可以了

## Reference

[Cannot mount NTFS partition in Ubuntu 13.04 [duplicate]](http://askubuntu.com/questions/291864/cannot-mount-ntfs-partition-in-ubuntu-13-04)
