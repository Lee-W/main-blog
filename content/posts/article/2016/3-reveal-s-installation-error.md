Title: Reveal.js 安裝錯誤
Date: 2016-02-20 03:57
Category: JavaScript
Tags: reveal.js
Slug: reveal-s-installation-error
Authors: Lee-W
Summary: 


當我安裝步驟執行到
```
npm install
```
會跳出很多錯誤訊息

<!--more-->

這才發現 Reveal.js 要用 python >= 2.5 and < 3.0.0
而我預設的 python 是 python3.5
所以只要像下面的指令把 python 指到 python2 就可以了
```sh
npm install --python=python2.7
```
`--python=` 後面是 python2 的執行擋，需要根據自己的設定做調整

# Reference
- [Reveal.js](https://github.com/hakimel/reveal.js/)