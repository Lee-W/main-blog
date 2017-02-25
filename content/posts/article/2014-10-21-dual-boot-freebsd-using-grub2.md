---
Title: Dual Boot FreeBSD Using GRUB2
Date: 2014-10-21 08:56
Category: Linux-Unix
Tags: 
Slug: dual-boot-freebsd-using-grub2
Authors: Lee-W
Summary: 
---

其實原本的標題是`Dual Boot FreeBsd with Ubuntu`
這篇文章寫的都是用Ubuntu測試的
不過我想只要是grub2應該都差不多吧XD
<!--more-->
## 加入freeBSD到grub開機選單

### 更改grub的設定檔

```shell  
vi /etc/grub.d/40_Custom
```

加入下面這幾行
```
menuentry "FreeBSD (/boot/loader)" {
    insmod ufs2
    set root=(hd0,1,a)
    kfreebsd /boot/loader
}
```

`FreeBSD (/boot/loader)`是在開機時顯示的名稱
`(hd0,1,a)`要根據你的freeBSD灌在磁碟的哪一塊決定

### 更新grub設定檔
```shell
sudo update-grub
```
這樣就會在開機選單上看到freeBSD了

其實還有一些其他的設定方法
可以參考[Set up Grub2 to boot Freebsd](http://unix.stackexchange.com/questions/16886/set-up-grub2-to-boot-freebsd-using-either-ubuntu-tools-or-liveusb-to-find-what-p)


## 換grub開機順序
如果希望改變預設的開機順序，就必須要修改下面的檔案`/etc/default/grub`
```shell
vi /etc/default/grub
```

會看到下面這串
```
GRUB_DEFAULT=0
#GRUB_HIDDEN_TIMEOUT=0
GRUB_HIDDEN_TIMEOUT_QUIET=true
GRUB_TIMEOUT=10
GRUB_DISTRIBUTOR=`lsb_release -i -s 2> /dev/null || echo Debian`
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"
GRUB_CMDLINE_LINUX=""
```

把第1行設定為多少(注意是從0開始)，就會預設從那裡開機

## 在ubuntu mount FreeBSD

```
sudo mount -t ufs -r -o ufstype=ufs2 /dev/sda4 ~/freebsd
```
