---
Title: gitignore.io
Date: 2015-02-03 05:58
Category: Git
Tags: Deprecated
Slug: gitignoreio
Authors: Lee-W
Summary: 
---

每次開一個git專案，要為它找適當的.gitignore，都要上網找模板蠻麻煩的
能不能有個簡單的方法，我開什麼專案就產生怎樣的.gitignore
然後我就發現了[gitignore.io](https://www.gitignore.io)
<!--more-->

簡單來說gitignore.io提供各式各樣的gitignore，而且可以自動合併成一個file
最棒的是它有提供api讓我們在command line上使用

# gitignore.io on command
這是gitignore.io的官方文件
https://www.gitignore.io/docs

## 設定
以mac的zsh的使用者為例，只要在執行下面這段
```
echo "function gi() { curl -L -s https://www.gitignore.io/api/\$@ ;}" >> ~/.zshrc && source ~/.zshrc
```

或者在~/.zshrc加入下面這段後，執行`source ~/.zshrc`
```
function gi() { curl -L -s https://www.gitignore.io/api/$@ ;}
```

設定完成後就可以使用gi的功能

## 使用

基本上只有兩種用法
首先當然要先看gi支援哪些.gitignore
```shell
gi list
```

執行完會看到一長串的結果
```
actionscript,ada,agda,android...
```

接著在gi後面輸入想產生的.gitignore的types
```
gi "types"
```
如果有超過一個必須用,隔開
e.g.
```
gi vim,osx
```
不過這樣還不會產生.gitignore，只會顯示在螢幕上
還要再使用output redirection才會有.gitignore
```shell
gi vim,osx >> .gitignore
```

# My Custom gi
但用起來還是有點小小的不順手
尤其每次要看list都要重新連上網抓一次，挺浪費時間
所以就自己寫了一個新的gi
我把它放在我的Git Hub上
https://github.com/Lee-W/gi_extension

那我的Custom gi到底多支援了什麼呢？
1. 線下查看gitignore.io支援的類型，用更適合閱讀當方式印出
2. 將output redirection寫成一個option
3. 支援以空格作為類型的分隔(逗號依然支援)  
   e.g. `vim,osx` -> `vim osx`
 
## 安裝
```shell
git clone https://github.com/Lee-W/gi_extension && cd gi_extension
sudo cp gi_extension.sh /usr/bin/gi
```

如果之前有在shell的設定檔中，設定過gitignore.io提供的gi
記得要把它註解掉，不然那個gi會蓋過我的gi

如果想移除掉
```shell
git clone https://github.com/Lee-W/gi_extension && cd gi_extension
sudo rm gi_extension.sh /usr/bin/gi
```

## 使用
第一次使用的時候要先下`gi -u`
將原本`gi list`的output，儲存到`~/.gi_list`

### 顯示支援類型
1. 以表格的方式輸出支援的類型  
目前設定一個row容納5個column，每個column長度為25  
```shell
gi -l
```
![1_gi_l.png](https://i0.wp.com/f6daa3706f14a40c04cb86aa98ffd752d68309b0.googledrive.com/host/0BzTRBX34Y857ZDZxM3dNYm9VcDg/gitignore_io/1_gi_l.png)

2. 以字母的順序輸出
```shell
gi -L
```
![2_gi_L.png](https://i0.wp.com/f6daa3706f14a40c04cb86aa98ffd752d68309b0.googledrive.com/host/0BzTRBX34Y857ZDZxM3dNYm9VcDg/gitignore_io/2_gi_L.png)

### 顯示.gitignore的內容
跟原本的gi一樣，只是多支援了以空白作為分隔
```
gi "types"
# e.g. gi vim osx 
```

### 輸出.gitignore
將結果加入目前資料夾下的.gitignore
```
gi -a "types"
# e.g. gi -a vim osx
```

在目前的資料夾產生一份新的.gitignore取代舊有的
```
gi -e "types"
# e.g. gi -e vim osx
```

### 更新本地端的支援列表
```shell
gi -u
```
其實每次gi被執行的時候，都會在backgroud更新列表
但是這次的更新，下次才能被使用
所以如果想要強制更新就可以用上這個指令