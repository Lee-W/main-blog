Title: Python@Instagram
Date: 2017-06-22 22:10
Category: Tech
Tags: Python, PyCon
Slug: Python-at-IG
Authors: Lee-W

* [Lisa Guo, Hui Ding Keynote PyCon 2017](https://www.youtube.com/watch?v=66XoCk79kjM)
* [slide](https://speakerdeck.com/pycon2017/keynote-lisa-guo-and-hui-ding-python-at-instagram)

終於好好花個時間看完今年 IG 在 PyCon US 的 Talk 了
的確蠻值得大家花這個時間去看的

<!--more-->

[TOC]

如果要看懶人包
Google 一下「PyCon」、「Instagram」有很多很清楚地整理
我也整理了一點點我覺得特別有意思的

## Why Python?

(一開始主要是歷史因素，因為當初的創辦人就這麼用了 XD)

* Use Proven Technology
    * Users do not care what database Instagram runs on. They certainly don't care what language Instagram develop in.
    * Focus on scoping and solve real problems rather than getting stuck on language detail.

## But Python is still slow, right?

At instagram, our bottlenecck is development velocity, not pure code execution

The conclusion is that you can get to a few hundred million users with Python before worrying about the performance of framework and language

## Python Efficiency Strategy

1. Build extensive tools to profile and understand performance bottleneck
2. Moving stable, citical compenents to C/C++
3. Cythonization
4. Async? New Python runtime?

## Road to Python3

這一段講到 Instragram 如何從 Python2 轉到 Python3 的過程
我覺得很精彩，所以大家就自己去看吧 XD

我只紀錄一個我覺得特別有趣的東西
如同大家所知道的 Python2 跟 Python3 一個很大的不同點，就是對於 byte 跟 str 的處理
這就會導致我們必須先確認他的型態是否符合預期
如果不符合就要在做 encode 或 decode

可能就會像下面這樣

```python
value = 'abc'
if isinstance(value, six.text_type):
    value = value.encode(encode='utf-8')
mymac = hamc.new(value)
```

Instagram 處理這種問題的功能實作成 `ensure_binary`, `ensure_str`, `ensure_text` 這類的 helper function

這也是我之前在 trace [transitions](https://github.com/pytransitions/transitions) 的 source code
發現有一個[listify](https://github.com/pytransitions/transitions/blob/2cb42916affe167a8d94cdfdf56ab08b41ccd05c/transitions/core.py#L25) 的 function
雖然是蠻簡單的小技巧，不過還算蠻實用的
