Title: gitignore.io
Date: 2015-02-03 05:58
Category: Tech
Tags: Git, Deprecated, Utility
Slug: gitignoreio
Authors: Lee-W
Summary:

每次開一個 git 專案，要為它找適當的 .gitignore，都要上網找模板蠻麻煩的
能不能有個簡單的方法，我開什麼專案就產生怎樣的 .gitignore
然後我就發現了[gitignore.io](https://www.gitignore.io)

<!--more-->

簡單來說 gitignore.io 提供各式各樣的 gitignore，而且可以自動合併成一個 file
最棒的是它有提供 api 讓我們在 command line 上使用

## gitignore.io on command

這是 gitignore.io 的官方文件
[doc](https://www.gitignore.io/docs)

### 設定

以 mac 的 zsh 的使用者為例，只要在執行下面這段

```shell
echo "function gi() { curl -L -s https://www.gitignore.io/api/\$@ ;}" >> ~/.zshrc && source ~/.zshrc
```

或者在 ~/.zshrc 加入下面這段後，執行 `source ~/.zshrc`

```shell
function gi() { curl -L -s https://www.gitignore.io/api/$@ ;}
```

設定完成後就可以使用 gi 的功能

### 使用

基本上只有兩種用法
首先當然要先看 gi 支援哪些 .gitignore

```shell
gi list
```

執行完會看到一長串的結果

```text
actionscript,ada,agda,android...
```

接著在 gi 後面輸入想產生的 .gitignore 的 types

```shell
gi "types"
```

如果有超過一個必須用 `,` 隔開
e.g.,

```shell
gi vim,osx
```

不過這樣還不會產生 .gitignore，只會顯示在螢幕上
還要再使用 output redirection 才會有 .gitignore

```shell
gi vim,osx >> .gitignore
```

## My Custom gi

但用起來還是有點小小的不順手
尤其每次要看 list 都要重新連上網抓一次，挺浪費時間
所以就自己寫了一個新的 gi
我把它放在我的 GitHub 上
[gi_extension](https://github.com/Lee-W/gi_extension)

那我的 Custom gi 到底多支援了什麼呢？

1. 線下查看 gitignore.io 支援的類型，用更適合閱讀當方式印出
2. 將 output redirection 寫成一個 option
3. 支援以空格作為類型的分隔 ( 逗號依然支援 )  
   e.g., `vim,osx` → `vim osx`

### 安裝

```shell
git clone https://github.com/Lee-W/gi_extension && cd gi_extension
sudo cp gi_extension.sh /usr/bin/gi
```

如果之前有在 shell 的設定檔中，設定過 gitignore.io 提供的 gi
記得要把它註解掉，不然那個 gi 會蓋過我的 gi

如果想移除掉

```shell
git clone https://github.com/Lee-W/gi_extension && cd gi_extension
sudo rm gi_extension.sh /usr/bin/gi
```

## 使用

第一次使用的時候要先下 `gi -u`
將原本 `gi list` 的 output，儲存到 `~/.gi_list`

### 顯示支援類型

* 以表格的方式輸出支援的類型  
   目前設定一個 row 容納 5 個 column，每個 column 長度為 25  

```shell
gi -l
```

![1_gi_l.png]({static}/images/posts-image/2015-02-03-gitignoreio/WjrHpdZ.png)

* 以字母的順序輸出

```shell
gi -L
```

![2_gi_L.png]({static}/images/posts-image/2015-02-03-gitignoreio/9j2PdP4.png)

### 顯示 .gitignore 的內容

跟原本的 gi 一樣，只是多支援了以空白作為分隔

```shell
gi "types"
# e.g., gi vim osx
```

### 輸出 .gitignore

將結果加入目前資料夾下的 .gitignore

```shell
gi -a "types"
# e.g., gi -a vim osx
```

在目前的資料夾產生一份新的 .gitignore 取代舊有的

```shell
gi -e "types"
# e.g.,e.g.,, gi -e vim osx
```

### 更新本地端的支援列表

```shell
gi -u
```

其實每次 gi 被執行的時候，都會在 backgroud 更新列表
但是這次的更新，下次才能被使用
所以如果想要強制更新就可以用上這個指令
