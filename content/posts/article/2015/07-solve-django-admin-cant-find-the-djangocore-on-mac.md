Title: 解決 django-admin 在 mac 找不到 django.core
Date: 2015-05-10 23:42
Category: Tech
Tags: Python, Django, mac
Slug: solve-django-admin-cant-find-the-djangocore-on-mac
Authors: Lee-W

## 問題

在 mac 上，用 pip3 安裝完 django 1.8.1 後
執行 `django-admin` 出現了以下的錯誤訊息

```text
Traceback (most recent call last):
  File "/usr/local/bin/django-admin", line 2, in <module>
    from django.core import management
ImportError: No module named django.core
```

<!--more-->

## 解決

找到 `/usr/local/lib/python3.4/site-packages/django/bin/django-admin.py`

把第一行的 `#!/usr/bin/env python` 改成 Python 的路徑
以我為例，我改成 `#!/usr/local/bin/python3.4`
之後就可以執行了
