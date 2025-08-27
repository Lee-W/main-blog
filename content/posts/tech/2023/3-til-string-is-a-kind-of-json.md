Title: TIL: 字串也是 JSON
Date: 2023-11-28 23:30
Category: Tech
Tags: JSON, TIL
Slug: til-string-is-a-kind-of-json
Authors: Wei Lee

之前在 review [airflow PR](https://github.com/apache/airflow/pull/33224) 的時候問了一個蠢問題

> May I know why is '"hello"' an valid json content?

更蠢的是這句英文還是錯的
應該要是 a valid json

<!--more-->

得到了[Jarek 的回覆](https://github.com/apache/airflow/pull/33224#discussion_r1292201137)才知道字串本身就是合法的 JSON，不需要是 object
可以從 [Introducing JSON](https://www.json.org/json-en.html) 找到 "any value on it's own (string) is perfectly valid json"

用 Python 做了點小實驗，確實也不會遇到 `JSONDecodeError`

<!-- blacken-docs:off -->

```python
>>> import json
>>> json.loads('""')
''
```

<!-- blacken-docs:on -->
