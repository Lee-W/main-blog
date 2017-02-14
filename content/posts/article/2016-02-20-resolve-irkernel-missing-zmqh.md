---
Title: 解決安裝IRKernel缺少zmq.h 
Date: 2016-02-20 03:42
Category: Article
Tags: jupiter
Slug: resolve-irkernel-missing-zmqh
Authors: Lee-W
Summary: 
---

<!--more-->

## 安裝IRKernel
進入R的命令列，輸入下面的指令
就能安裝IRKernel，以後就能在jupyter中使用R
```
install.packages(c('rzmq','repr','IRkernel','IRdisplay'),
                 repos = c('http://irkernel.github.io/', getOption('repos')))
IRkernel::installspec()
```

## 錯誤訊息
```
interface.cpp:22:10: fatal error: 'zmq.h' file not found
#include <zmq.h>
         ^
1 error generated.
make: *** [interface.o] Error 1
ERROR: compilation failed for package ‘rzmq’
```
<!--more-->

## 解決
這時候就要將缺少的套件補齊
```
brew install czmq zmq
```
再執行一次最上面的安裝指令

接著在指令列執行輸入下面的指令
```
jupyter qtconsole --kernel=ir
jupyter console --kernel=ir
```

安裝成功後就可以看到
![R_in_jupyter](http://i.imgur.com/pWf6j0q.png)

# Reference
- [Failed to install rzmq #50](https://github.com/IRkernel/IRkernel/issues/50)
- [IRkernel](https://github.com/IRkernel/IRkernel)
