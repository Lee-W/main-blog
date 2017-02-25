---
Title: autojump - 在terminal中快速跳轉資料夾
Date: 2014-02-01 13:11
Category: Linux-Unix
Tags: Utility
Slug: autojump
Authors: Lee-W
Summary: 
---

# 什麼是autojump
可以快速跳轉資料夾的工具

<!--more-->

e.g.
有個資料夾是/a/b/c/d/e/f/g/h
原本要輸入
```shell
cd /a/b/c/d/e/f/g/h
```

可是現在有了autojump，而且你也去過這個h資料夾，你就可以
```shell
j h
```
很方便吧！！！

# 安裝
```shell
cd /tmp
git clone https://github.com/joelthelion/autojump
cd autojump
chmod +x install.py
./install.py
```

然後把下面這行加入shell的設定檔(e.g. ~/.bashrc  ,  ~/.zshrc)
> [[ -s ~/.autojump/etc/profile.d/autojump.sh ]] && . ~/.autojump/etc/profile.d/autojump.sh 

最後只要重開shell就完成了

# 使用
1. 最基本的功能當然就是跳轉囉
```shell
j word
```
    如果有重複的名稱 (e.g. worda, wordb)，就在打一次同樣的指令，就會跳到下一個
**strong text**
2. list現在autojump可以跳到的資料夾
```shell 
j -s 
```

3. 刪除已經背改變路徑或刪除的紀錄
```shell 
 j --purge
```

# Reference
[autojump readme] (https://github.com/joelthelion/autojump/blob/master/README.md)