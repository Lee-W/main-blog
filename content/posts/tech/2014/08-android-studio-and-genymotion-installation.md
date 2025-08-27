Title: Android Studio + Genymotion 安裝
Date: 2014-12-29 09:26
Category: Tech
Tags: Android
Slug: android-studio-and-genymotion-installation
Authors: Wei Lee

Android Studio 最近 Google 在推行的 Android IDE，前身是 IntelliJ IDEA

<!--more-->

它的檔案架構跟 eclipse 差蠻多的，所以用不同的 IDE 來協作會有點麻煩
就我的經驗 Android Studio 比 eclipse 來得穩定一些
反正現在還有 Google 在背後支持它，就來試試看吧 XD

Android Studio 正式版已經發布了，現在好像完全無法把 sdk 放在 Android Studio 資料夾內
所以之前沒有把 sdk 獨立出來的，記得要獨立出來，不然可能會發生無法更新的問題

[TOC]

# Setup

## Android Studio
### Download Android Studio

先到[官網](https://developer.android.com/sdk/installing/studio.html)下載 Android Studio ( 這篇文以 Windows 為例 )

![1_download](/images/posts-image/2014-11-23-android-studio-and-genymotion-installation/iFQ6JJY.png)

下載後會進入到下面的教學頁面
其實寫得還蠻清楚的，所以如果可以接受就可以跳過以下的教學了 XD
![2_Installation_Guide](/images/posts-image/2014-11-23-android-studio-and-genymotion-installation/gkttlS9.png)

#### Install JDK

在安裝 Android Studio 前，要先安裝好 JDK
現在最新的版本是 JDK 8，可以到[這個連結](http://www.oracle.com/technetwork/java/javase/downloads/index.html)下載

![3_jdk1](/images/posts-image/2014-11-23-android-studio-and-genymotion-installation/0om5D2M.png)
選好自己的作業系統
![4_jdk2](/images/posts-image/2014-11-23-android-studio-and-genymotion-installation/D0G7XLq.png)
再來就是一直下一步囉 XD

#### 設定環境變數

安裝完 JDK 後，我們還需要設定環境變數
以 Win7 為例

> 電腦  內容 → 進階系統設定 → 進階 → 環境變數

接著在 `系統變數` 這個欄位按下 `新增`
變數名稱 輸入 `JAVA_HOME` ( 可能會因為 Android Studio 的版本而不同 )
變數值 輸入 你安裝 JDK 的路徑 (e.g. `C:\Program Files\Java\jdk1.8.0_20`)
![5_env_var](/images/posts-image/2014-11-23-android-studio-and-genymotion-installation/KYG8pBO.png)

### Install Android Studio

安裝過程中會問要讓**目前使用者**使用還是**所有使用者**使用
再來會要你選安裝目錄
如果不想理它，就一直下一步吧
除了 Android Studio 外，可能還會安裝一些 Dependent 的套件
不過就放著讓他跑就可以了

### Install SDK manager

自從 0.8.14 版之後，SDK Manager 就不會再跟 Android Studio 綁在一起
所以要額外[下載 SDK tools](https://developer.android.com/sdk/index.html?hl=i)

```text
如果是在 0.8.14 版前安裝的也不用擔心，更新後需要多做設定
Android Studio 會自動幫你把 SDK 的路徑設定到原本的位置
```

把網頁往下拉會看到 SDK Tools Only
![18_sdk_download](/images/posts-image/2014-11-23-android-studio-and-genymotion-installation/TctIzTa.png)
下載完解壓縮到你要的路徑
之後設定 SDK manager 設定到這個路徑就可以了

開始 Android Studio
> Configure → Project Default → Project Structure

![20_set_sdk_1](/images/posts-image/2014-11-23-android-studio-and-genymotion-installation/Tj82hvs.png)

記得要把 SDK 的路徑改成剛剛安裝的路徑
![21_set_sdk_2](/images/posts-image/2014-11-23-android-studio-and-genymotion-installation/ETqkNhX.png)

### SDK setup

接著我們要設定 SDK
現在最新的版本是 Android 5.0 (API 21)

先開啟 Android Studio，進入 `Configure`
![6_SDK1](/images/posts-image/2014-11-23-android-studio-and-genymotion-installation/c8rDZxZ.png)
進入 `SDK Manager`
![7_SDK2](/images/posts-image/2014-11-23-android-studio-and-genymotion-installation/pBVHp7S.png)
把選單拉到 API 21 選起來
![19_sdk_21](/images/posts-image/2014-11-23-android-studio-and-genymotion-installation/3lytBi2.png)

接著把選單拉到最後選

* **Android Support Repository**
* **Android support Library**
* **Coogle Play services**
* **Google Repository**
* **Google USB Driver**
* **Intel X86 Emulator Accelerator(HAXM installer)**
    * 最後的這個 HAXM 是為了讓模擬器加速用的，從 SDK manager 下載完之後，還有另外的安裝步驟

![9_SDK4](/images/posts-image/2014-11-23-android-studio-and-genymotion-installation/UM8w30n.png)

**安裝到這裡 Android Studio 已經可以使用了**，不過還可以再做一些設定讓手機模擬器跑得更快

### Emulator Accelerator

在安裝 HAXM 前要先確定 Intel VT-x 是否有在你的 BIOS 被啟用
我沒遇到這個問題，所以我也不知道怎麼解決＠＠
可以在 cmd 下 `sc query intelhaxm` 來看有沒有開啓，只要有看到 Running 應該就是沒問題了

再來到 Android Studio 的目錄下找到 HAXM 的安裝檔
它被放在 `...\android-studio\sdk\extras\intel\Hardware_Accelerated_Execution_Manager`
... 指的是安裝的目錄

看到 `intelhaxm` 按下去 !
![10_Intel_accelator](/images/posts-image/2014-11-23-android-studio-and-genymotion-installation/NX8lULd.png)
一直按下一步就大功告成了

不過 ...
這樣還是不夠快，我們需要更快的模擬器！
Genymotion ！！！

## Genymotion

安裝 Genymotion 的模擬器前，我們必須先到[官網](http://www.genymotion.com/)註冊

### Download

進入下載頁面後，往下拉會看到 Windows，mac 和 Liunx 版

Windows 只要直接安裝就可以了，它會連 Oracle Virtual Box 一起安裝
![11_genymotiong_win](/images/posts-image/2014-11-23-android-studio-and-genymotion-installation/4oUXeea.png)

mac 和 Linux 還要額外先安裝 [Oracle Virtual Box](https://www.virtualbox.org/wiki/Downloads)
![12_genymotion_Unix](/images/posts-image/2014-11-23-android-studio-and-genymotion-installation/NMQD2Jc.png)

### Install IDE plug-in

在下載頁面往下拉會看到 genymotion 在 IDE 上的 plugin，可以讓我們從 IDE 內直接開啟 Genymothion
Android Studio 屬於 IntelliJ IDEA，所以我們就照著他上面的指示設定
![13_genymotion_plug in](/images/posts-image/2014-11-23-android-studio-and-genymotion-installation/7C0d8aU.png)

開啟 Android Studio
> File → Settings

![14_plug-in](/images/posts-image/2014-11-23-android-studio-and-genymotion-installation/vemudkb.png)

找到 Plungins ，接著點 Browse repositories
![15_plug-in2](/images/posts-image/2014-11-23-android-studio-and-genymotion-installation/UnP1hiQ.png)

上方輸入 Genymotion 就可找到，接著就安裝它吧
![16_plug-in3](/images/posts-image/2014-11-23-android-studio-and-genymotion-installation/xzjsTmz.png)

安裝完記得重新啟動 Android Studio，就會在工具列看到多一個按鈕，Genymotion 就安裝完成囉
![17_plug-in4](/images/posts-image/2014-11-23-android-studio-and-genymotion-installation/I2RbFEG.png)

第一次使用會要求設定 Genymotion 安裝的資料夾 (e.g. `C:\Program Files\Genymobile\Genymotion`)
設定完就可以開始使用 Genymotion 了

### Plugins

* IdeaVim: 如果你是重度 Vim 狂熱者，這絕對是你不能不裝的 plugin!!!
* MarkDown: 這個 Plugin 提供直接在 Android Studio 中，Preview Markdown 的功能
