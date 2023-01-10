Title: Dual Boot FreeBSD Using GRUB2
Date: 2014-10-21 08:56
Category: Tech
Tags: Linux-Unix, Dual Boot
Slug: dual-boot-freebsd-using-grub2
Authors: Wei Lee

其實原本的標題是 `Dual Boot FreeBSD with Ubuntu`
這篇文章寫的都是用 Ubuntu 測試的
不過我想只要是 grub2 應該都差不多吧 XD

<!--more-->

## 加入 FreeBSD 到 grub 開機選單

### 更改 grub 的設定檔

```shell
vi /etc/grub.d/40_Custom
```

加入下面這幾行

```text
menuentry "FreeBSD (/boot/loader)" {
    insmod ufs2
    set root=(hd0,1,a)
    kfreebsd /boot/loader
}
```

`FreeBSD (/boot/loader)` 是在開機時顯示的名稱
`(hd0,1,a)` 要根據你的 FreeBSD 灌在磁碟的哪一塊決定

### 更新 grub 設定檔

```shell
sudo update-grub
```

這樣就會在開機選單上看到 FreeBSD 了

其實還有一些其他的設定方法
可以參考[Set up Grub2 to boot Freebsd](http://unix.stackexchange.com/questions/16886/set-up-grub2-to-boot-freebsd-using-either-ubuntu-tools-or-liveusb-to-find-what-p)

## 換 grub 開機順序

如果希望改變預設的開機順序，就必須要修改下面的檔案 `/etc/default/grub`

```shell
vi /etc/default/grub
```

會看到下面這串

```text
GRUB_DEFAULT=0
#GRUB_HIDDEN_TIMEOUT=0
GRUB_HIDDEN_TIMEOUT_QUIET=true
GRUB_TIMEOUT=10
GRUB_DISTRIBUTOR=`lsb_release -i -s 2> /dev/null || echo Debian`
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"
GRUB_CMDLINE_LINUX=""
```

把第 1 行設定為多少 (注意是從 0 開始)，就會預設從那裡開機

## 在 ubuntu mount FreeBSD

```shell
sudo mount -t ufs -r -o ufstype=ufs2 /dev/sda4 ~/freebsd
```
