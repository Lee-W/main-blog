---
Title: Reveal.js 安裝錯誤
Date: 2016-02-20 03:57
Category: Article
Tags: 
Slug: reveal-s-installation-error
Authors: Lee-W
Summary: 
---

當我安裝步驟執行到
```
npm install
```
會跳出很多錯誤訊息
<!--more-->

這才發現Reveal.js 要用python >= 2.5 and < 3.0.0
而我預設的python是python3.5
所以只要像下面的指令把python指到python2就可以了
```sh
npm install --python=python2.7
```
`--python=`後面是python2的執行擋，需要根據自己的設定做調整

# Reference
- [Reveal.js](https://github.com/hakimel/reveal.js/)

