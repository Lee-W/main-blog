Title: 解決django-admin在mac找不到django.core
Date: 2015-05-10 23:42
Category: Python
Tags: django, mac
Slug: solve-django-admin-cant-find-the-djangocore-on-mac
Authors: Lee-W
Summary: 


## 問題
在mac上，用pip3安裝完django 1.8.1後
執行`django-admin`出現了以下的錯誤訊息
```
Traceback (most recent call last):
  File "/usr/local/bin/django-admin", line 2, in <module>
    from django.core import management
ImportError: No module named django.core
```
<!--more-->

## 解決
找到`/usr/local/lib/python3.4/site-packages/django/bin/django-admin.py`

把第一行的`#!/usr/bin/env python`改成Python的路徑
以我為例，我改成`#!/usr/local/bin/python3.4`
之後就可以執行了