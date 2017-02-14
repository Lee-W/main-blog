---
Title: Android Studio+Genymotion安裝(12/29更新)
Date: 2014-11-23 09:26
Category: Article
Tags: 
Slug: android-studio-and-genymotion-installation
Authors: Lee-W
Summary: 
---

# What is Android Studio?
最近Google在推行的Android IDE，前身是IntelliJ IDEA
<!--more-->
它的檔案架構跟eclipse差蠻多的，所以用不同的IDE來協作會有點麻煩
就我的經驗Android Studio比eclipse來得穩定一些
反正現在還有Google在背後支持它，就來試試看吧XD

### 2014/11/23更新
[Install SDK](#1123 update 1): 更新了Android Studio 0.8.14後需要的額外設定
[Setup SDK](#1123 update 2): SDK版本更新至API21(Android 5.0)

### 2014/12/29更新
Android Studio 正式版已經發布了，現在好像完全無法把sdk放在Android Studio資料夾內
所以之前沒有把sdk獨立出來的，記得要獨立出來，不然可能會發生無法更新的問題

# Installation
## Download Android Studio
先到官網下載Android Studio (這篇文以Windows為例)
https://developer.android.com/sdk/installing/studio.html
![1_download](http://i.imgur.com/iFQ6JJY.png)

下載後會進入到下面的教學頁面
其實寫得還蠻清楚的，所以如果可以接受就可以跳過以下的教學了XD
![2_Installation_Guide](http://i.imgur.com/gkttlS9.png)

## Install JDK
在安裝Android Studio前，要先安裝好JDK
現在最新的版本是JDK 8，可以到下面的連結下載
http://www.oracle.com/technetwork/java/javase/downloads/index.html
![3_jdk1](http://i.imgur.com/0om5D2M.png)
選好自己的作業系統
![4_jdk2](http://i.imgur.com/D0G7XLq.png)
再來就是一直下一步囉XD

### 設定環境變數
安裝完JDK後，我們還需要設定環境變數
以Win7為例
> 電腦-> 內容 -> 進階系統設定 -> 進階 -> 環境變數

接著在 `系統變數` 這個欄位按下 `新增` 
變數名稱 輸入 `JAVA_HOME` (可能會因為Android Studio的版本而不同)
變數值 輸入 你安裝JDK的路徑 (e.g. `C:\Program Files\Java\jdk1.8.0_20`)
![5_env_var](http://i.imgur.com/KYG8pBO.png)

## Install Android Studio
安裝過程中會問要讓**目前使用者**使用還是**所有使用者**使用
再來會要你選安裝目錄
如果不想理它，就一直下一步吧
除了Android Studio外，可能還會安裝一些Dependent的套件
不過就放著讓他跑就可以了

<a name="1123 update 1"></a>
## Install SDK manager
自從0.8.14版之後，SDK Manager就不會再跟Android Studio綁在一起
所以要額外[下載SDK tools](https://developer.android.com/sdk/index.html?hl=i)

```
如果是在0.8.14版前安裝的也不用擔心，更新後需要多做設定
Android Studio會自動幫你把SDK的路徑設定到原本的位置
```

把網頁往下拉會看到SDK Tools Only
![18_sdk_download](http://i.imgur.com/TctIzTa.png)
下載完解壓縮到你要的路徑
之後設定SDK manager設定到這個路徑就可以了

開始Android Studio
> Configure -> Project Default -> Project Structure

![20_set_sdk_1](http://i.imgur.com/Tj82hvs.png)

記得要把SDK的路徑改成剛剛安裝的路徑
![21_set_sdk_2](http://i.imgur.com/ETqkNhX.png)

<a name="1123 update 1"></a>
## SDK setup
接著我們要設定SDK
現在最新的版本是Android 5.0 (API 21)

先開啟Android Studio，進入`Configure`
![6_SDK1](http://i.imgur.com/c8rDZxZ.png)
進入`SDK Manager`
![7_SDK2](http://i.imgur.com/pBVHp7S.png)
把選單拉到API 21選起來
![19_sdk_21](http://i.imgur.com/3lytBi2.png)

接著把選單拉到最後選
- **Android Support Repository**
- **Android support Libarary**
- **Coogle Play services**
- **Google Repository**
- **Google USB Driver**
- **Intel X86 Emulator Accelerator(HAXM installer)**  
	最後的這個HAXM是為了讓模擬器加速用的，從SDK manager下載完之後，還有另外的安裝步驟
![9_SDK4](http://i.imgur.com/UM8w30n.png)

**安裝到這裡Android Studio已經可以使用了**，不過還可以再做一些設定讓手機模擬器跑得更快

## Emulator Accelerator
在安裝HAXM前要先確定Intel VT-x是否有在你的bios被啟用
我沒遇到這個問題，所以我也不知道怎麼解決＠＠
可以在cmd下`sc query intelhaxm`來看有沒有開啓，只要有看到Running應該就是沒問題了

再來到Android Studio的目錄下找到HAXM的安裝檔
它被放在`...\android-studio\sdk\extras\intel\Hardware_Accelerated_Execution_Manager`
...指的是安裝的目錄

看到`intelhaxm`按下去!
![10_Intel_accelator](http://i.imgur.com/NX8lULd.png)
一直按下一步就大功告成了

不過...
這樣還是不夠快，我們需要更快的模擬器！
Genymotion！！！

# Genymotion
安裝Genymotion的模擬器前，我們必須先註冊
http://www.genymotion.com/

## Download
進入下載頁面後，往下拉會看到Windows，mac 和 Liunx版

Windows只要直接安裝就可以了，它會連Oracle Virtual Box一起安裝
![11_genymotiong_win](http://i.imgur.com/4oUXeea.png)

mac 和 Linux還要額外先安裝 [Oracle Virtual Box](https://www.virtualbox.org/wiki/Downloads)
![12_genymotion_Unix](http://i.imgur.com/NMQD2Jc.png)

## Install IDE plug-in
在下載頁面往下拉會看到genymotion在IDE上的plugin，可以讓我們從IDE內直接開啟Genymothion
Android Studio屬於IntelliJ IDEA，所以我們就照著他上面的指示設定
![13_genymotion_plug in](http://i.imgur.com/7C0d8aU.png)

開啟 Android Studio
> File -> Settings

![14_plug-in](http://i.imgur.com/vemudkb.png)

找到Plungins ，接著點Browse repositories
![15_plug-in2](http://i.imgur.com/UnP1hiQ.png)

上方輸入Genymotion就可找到，接著就安裝它吧
![16_plug-in3](http://i.imgur.com/xzjsTmz.png)

安裝完記得重新啟動Android Studio，就會在工具列看到多一個按鈕，Genymotion就安裝完成囉
![17_plug-in4](http://i.imgur.com/I2RbFEG.png)

第一次使用會要求設定Genymotion安裝的資料夾 (e.g. `C:\Program Files\Genymobile\Genymotion`)
設定完就可以開始使用Genymotion了

## Plugins
IdeaVim: 如果你是重度Vim狂熱者，這絕對是你不能不裝的plugin!!!
MarkDown: 這個Plugin提供直接在Android Studio中，Preview Markdown的功能