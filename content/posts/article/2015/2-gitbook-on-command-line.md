Title: Gitbook on Command Line
Date: 2015-01-23 07:34
Category: Tech
Tags: Git Book
Slug: gitbook-on-command-line
Authors: Lee-W
Summary: 


最近比較認真在寫 Gitbook，順便記錄一下該怎麼用
簡單來說 Gitbook 就是可以使用 Markdown 來寫書的平台，可以轉成各種電子書的格式
目前已經支援的有 html, pdf, ePUB, MOBI

<!--more-->

之前寫了一本 Clean Code 的筆記
最近又開始寫一本 FreeBSD 和網管相關的 Gitbook
如果有興趣可以到[我的 Gitbook](https://www.gitbook.com/@lee-w) 上看看 XD

目前 Gitbook 主要支援網站上的 Editor，不過我比較習慣在本地端進行編輯
雖然有 Gitbook 編輯器，但有時候用起來還是會出點問題
所以最後還是決定來學如何用 command line + sublime 寫 Gitbook

## 安裝 Gitbook
```
npm install gitbook -g
```

## 開始撰寫 Gitbook
一本 Gitbook 一般都會包含 `SUMMARY.md`, `README.md`, `package.json`, `book.json`
像我的 Learning Python 筆記的檔案架構大概長的是這樣
![1_learning_python_project_structure](http://i.imgur.com/6RDgdVZ.png)

README.md 是這本書的簡介
package.json 是額外使用的 package 的定義和設定
book.json 是這本書的額外設定
這裡不會多做介紹，可以參考[Reference](#Reference) 的網站，裡面有很詳細的介紹

最重要的是 SUMMARY.md，它會定義整本 gitbook 的架構
每個章節下面都還可以給予更多的小節
下面是我 Learning Python 的 SUMMARY.md

```markdown
# Summary

* [Introduction](README.md)
* [Getting Started](1_getting_started/README.md)
   * [A Python Q&A Session](1_getting_started/a_python_q&a_session.md)
   * [How Python Runs Programs](1_getting_started/how_python_runs_programs.md)
   * [How You Run Programs](1_getting_started/how_you_run_programs.md)
* [Types and Operations](2_types_and_operations/README.md)
   * [Introducing Python Object Types](2_types_and_operations/introducing_python_object_types.md)
   * [Numeric Types](2_types_and_operations/numeric_types.md)
   * [The Dynamic Typing Interlude](2_types_and_operations/the_dynamic_typing_interlude.md)
```

這是預覽的結果
![2_learning_python_web](http://i.imgur.com/d3NP0xi.png)

下了這個指令後就會根據 SUMMARY.md 的定義，自動產生相對應資料夾和檔案
```
gitbook init
```
接著就可以開始編輯裡面的檔案了

## 預覽
寫完之後當然預覽一下
```
gitbook serve 
```
用了這個指令後就會為目前的目錄開一個預覽 HTML 的 port
只要在瀏覽器上輸入 `http://localhost:4000`
就可以預覽剛剛寫的 Gitbook
只要有更新後存擋，重新整理就能看到更新後的結果

## 輸出
在 export 前，需要為 pdf, epub, mobi 三種格式多安裝程式才能使用
先到的官網下載 Calibre
http://calibre-ebook.com/download

以 mac 為例
需要下面這個指令，為 ebook-covert 建立一個捷徑，讓 gitbook 可以找到這個功能
```
ln -s /Applications/calibre.app/Contents/MacOS/ebook-convert /usr/local/bin
```
  
以下的四個指令依序可以產生 html, pdf, epub, mobi
```
gitbook build ./ 
gitbook pdf ./
gitbook epub ./
gitbook mobi ./
```
後面可以多指定一個參數 `--output="Directory"`
"Directory" 換成你要的位置或檔名
如果不指定，預設 html 會 export 到 \_book 裡面，其他檔案則會以 book 命名

## Publish 到 Gitbook.com 上
先到[Gitbook 官網](https://www.gitbook.com) 上註冊帳號
接著 create a new book，到 setting 頁面往下拉，就會看到一個 URL

接下來的操作就跟 git 基本上是一樣的，init, add, commit ... 等
只有在 remote 的設定有點不同
```
git remote add gitbook "URL"
git push -u gitbook
```
這裡要輸入的帳號、密碼是 gitbook 上的，不是與其連結的帳號的
如果還沒設定就要再去自己的 profile 內設定


<a name="reference"></a>
# Reference
- [Gitbook](https://github.com/GitbookIO/gitbook)
- [GitBook Documentaion](http://help.gitbook.io/index.html)
- [深入淺出 GitBook 寫作與自助出版，電子書也能多人協作](http://www.codedata.com.tw/social-coding/gitbook-self-publishing/)