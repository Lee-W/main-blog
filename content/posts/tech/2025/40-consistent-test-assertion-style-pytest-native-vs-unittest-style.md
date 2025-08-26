Title: Airflow 的測試要用 unittest 風格還是 pytest 風格的 assert
Subtitle: 問就是 pytest
Date: 2025-08-20 09:00
Modified: 2025-08-26 12:20
Category: Tech
Tags: Airflow, Airflow 開發生情報
Slug: consistent-test-assertion-style-pytest-native-vs-unittest-style
Authors: Wei Lee

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

## 後續討論
我就想說有印象後面還有繼續討論
稍微翻了一下信箱才找到

1. [RE: Re: [DISCUSS] Consistent test assertion style: pytest-native vs unittest-style](https://lists.apache.org/thread/1jvbqk3bw5gyyzpx1qmf4y5w8385ccrz)
2. [Re: [DISCUSS] Consistent test assertion style: pytest-native vs unittest-style](https://lists.apache.org/thread/nqb5msnr67734yx0421cpzdjw6rwvq0m)

Re: 外，還有 Re: Re:
我現在是在看孤獨搖滾劇場版嗎 😆

## Reference
* [BLUE GIANT SUPREME藍色巨星 歐洲篇](https://www.kobo.com/tw/zh/ebook/blue-giant-supreme-01)
