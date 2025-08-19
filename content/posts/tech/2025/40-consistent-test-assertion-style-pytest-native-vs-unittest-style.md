Title: Airflow 的測試要用 unittest 風格還是 pytest 風格的 assert
Subtitle: 問就是 pytest
Date: 2025-08-20 08:50
Category: Tech
Tags: Airflow, Airflow 開發生情報
Slug: consistent-test-assertion-style-pytest-native-vs-unittest-style
Authors: Wei Lee
Status: draft

剛開始貢獻 Airflow 的時候
非常的訝異，怎麼到處都是 unittest 風格的測試
我...真的要讀空氣的就寫 unittest 風格嗎
但我以為那已經跟白鬍子一樣，是上個時代的敗北者了

<!--more-->

👉 原文： [[DISCUSS] Consistent test assertion style: pytest-native vs unittest-style](https://lists.apache.org/thread/41b04mg0rolv0sj98jhogsztstxnqfg5)

結論是 TP 所提出的

```python
from unittest.mock import call

assert mock_http_run.mock_calls == [
    call(
        endpoint="api/v2/accounts/test_account_id/",
        data=None,
        extra_options=None,
    )
]
assert mock_paginate.mock_calls == []
```

![blue-giant-chris-3](/images/meme/blue-giant-chris-3.jpg)

## Reference
* [BLUE GIANT SUPREME藍色巨星 歐洲篇](https://www.kobo.com/tw/zh/ebook/blue-giant-supreme-01)
