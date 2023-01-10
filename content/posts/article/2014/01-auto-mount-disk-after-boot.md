Title: Linux 開機自動掛載分割區
Date: 2014-02-01 16:44
Category: Tech
Tags: Linux-Unix, Dual Boot
Slug: auto-mount-disk-after-boot
Authors: Wei Lee

分割區的掛載資訊，存在 /etc/fstab 中，所以需要自動掛載分割區時可以針對此檔案做修改
需要注意的是，如果設定不好，可能會沒辦法開機的！！！

<!--more-->

我們先來看一下 /etc/fstab 內的東西

```shell
sudo cat /etc/fstab
```

```text
# /etc/fstab: static file system information.
#
# Use 'blkid' to print the universally unique identifier for a
# device; this may be used with UUID= as a more robust way to name devices
# that works even if disks are added and removed. See fstab(5).
#
# <file system> <mount point>   <type>  <options>       <dump>  <pass>
# / was on /dev/sda1 during installation
UUID=c5744283-f105-47e9-8a2e-21f477d895b7 /               ext4    errors=remount-ro 0       1
# swap was on /dev/sda5 during installation
UUID=72b6a10a-f0b6-43ef-927d-0d74673febe7 none            swap    sw              0       0
#data
UUID=571F168F3D98D759 /media/lee/data ntfs auto,rw 0 2
```

\# 是註解
最後六行是比較重要的
1~2 是 root 的掛載
3~4 是 swap 的掛載
5~6 是我自己的 data 的掛載

```text
#data
UUID=571F168F3D98D759 /media/lee/data ntfs auto,rw 0 2
```

總共有 6 個欄位

1. 掛載硬碟的標籤
    - 掛載硬碟的標籤我用的是 UUID 的標籤，可以用下面的指令查詢
    `ls -l /dev/disk/by-uuid/`
    - 也可以直接使用 /dev/sda1 這樣的格式，只是如果硬碟的代號改變，就要再去手動改變比較麻煩
2. 掛載位置
    - 掛載的位置要是一個已經存在的位置，建議是一個空的資料夾
    - 如果不是空的，裏面的東西應該都會被清空
    - 另外，一個掛載點只能掛載一個 disk
    - 另外，注意在 Linux 中大小寫是不同的
3. 分隔區格式
    - 而一般的檔案朝的分割驅格式都是都是 ntfs，不過也可以用指令來查詢
    `df`
4. 選項
5. 是否被 dump 備份指令作用
6. 是否以 fsck 檢驗磁區

基本上 4 5 6 我也沒去研究，如果有興趣的話可以在我最後面附上的參考資料中找到

## 測試

先看一下是否有掛載成功

```sh
df
```

```text
檔案系統         1K-區段      已用      可用 已用 % 掛載點
/dev/sda1      103081248   9259936  88562048   10% /
none                   4         0         4    0% /sys/fs/cgroup
udev             3992780         4   3992776    1% /dev
tmpfs             801368      1168    800200    1% /run
none                5120         0      5120    0% /run/lock
none             4006840      1032   4005808    1% /run/shm
none              102400        44    102356    1% /run/user
/dev/sda6      459942908 229176172 230766736   50% /media/lee/data
```

像我的最後面就出現了 data

之後暫時將它卸載 (若 `df` 之後，分割區沒有出現，那就不用做這步了)

```shell
sudo umount /dev/sda6
```

(/dev/sda6 要取代成你自己的位置 )
接著再執行一次

```shell
df
```

剛剛的分割區應該會不見，然後執行
開機自動掛載分割區

```shell
sudo mount -a
```

如果沒有錯誤訊息，就在執行一次

```shell
df
```

如果掛載的分隔驅再裡面就是成功了

如果有任何異常，就去看一下 /etc/fstab 是不是有哪裡寫錯了

## Reference

[巴特的微花盆： 筆記： Linux 中設定開機時自動掛載分割區](http://255121.blogspot.tw/2010/05/linux.html)
