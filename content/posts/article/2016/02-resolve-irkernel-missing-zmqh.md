Title: 解決安裝 IRKernel 缺少 zmq.h
Date: 2016-02-20 03:42
Category: Tech
Tags: R, Jupyter
Slug: resolve-irkernel-missing-zmqh
Authors: Lee-W

<!--more-->

## 安裝 IRKernel

進入 R 的命令列，輸入下面的指令
就能安裝 IRKernel，以後就能在 jupyter 中使用 R

```text
install.packages(c('rzmq','repr','IRkernel','IRdisplay'),
                 repos = c('http://irkernel.github.io/', getOption('repos')))
IRkernel::installspec()
```

## 錯誤訊息

```text
interface.cpp:22:10: fatal error: 'zmq.h' file not found
#include <zmq.h>
         ^
1 error generated.
make: *** [interface.o] Error 1
ERROR: compilation failed for package 'rzmq'
```

## 解決

這時候就要將缺少的套件補齊

```shell
brew install czmq zmq
```

再執行一次最上面的安裝指令

接著在指令列執行輸入下面的指令

```shell
jupyter qtconsole --kernel=ir
jupyter console --kernel=ir
```

安裝成功後就可以看到
![R_in_jupyter](/images/posts-image/2016-02-20-resolve-irkernel-missing-zmqh/pWf6j0q.png)

## Reference

* [Failed to install rzmq #50](https://github.com/IRkernel/IRkernel/issues/50)
* [IRkernel](https://github.com/IRkernel/IRkernel)
