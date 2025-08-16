Title: 平平都是 joinedload
Subtitle: <ruby>仝款<rt>kāng-khuán</rt></ruby>，<ruby>無仝<rt>bô kāng</rt></ruby><ruby>師傅<rt>sai-hū</rt></ruby>
Date: 2025-08-16 11:35
Category: Tech
Tags: Python, gotcha, SQLAlchemy
Slug: same-joinedload-but-not-the-same
Authors: Wei Lee
Cover: /images/meme/mygo-it-is-but-it-is-not.jpg

直覺上應該都會覺得 `from sqlalchemy.orm import joinedload` 跟 `from sqlalchemy.orm.strategy_options import joinedload` 是一樣的東西吧！
前者應該是後者的語法糖，這樣就可以少打一些字

<!--more-->

但昨天在重構 [Allow generating human-in-the-loop links that can be redirected to the corresponding page and perform action #53907][airflow-pr-53907] 並實作哲佑大大給我的 joinedload 建議時
就一切都炸掉了

```
  File "/opt/airflow/airflow-core/src/airflow/api_fastapi/core_api/services/public/hitl.py", line 59, in get_task_instnace
    query = query.options(joinedload(TI.hitl_detail))
  File "/usr/local/lib/python3.10/site-packages/sqlalchemy/orm/strategy_options.py", line 1219, in __call__
    self.name = name = fn.__name__
  File "/usr/local/lib/python3.10/site-packages/sqlalchemy/orm/attributes.py", line 334, in __getattr__
    util.raise_(
  File "/usr/local/lib/python3.10/site-packages/sqlalchemy/util/compat.py", line 211, in raise_
    raise exception
AttributeError: Neither 'InstrumentedAttribute' object nor 'Comparator' object associated with TaskInstance.hitl_detail has an attribute '__name
__'. Did you mean: '__ne__'?
```

![jotaro-nani](/images/meme/jotaro-nani.jpg)

而且還不是很好除錯
我複製了其他段已經驗證過、可以跑的程式碼來執行

測試了半小時後才回去懷疑該不會是引入 joinedload 的地方出問題吧
還真的改回 `from sqlalchemy.orm import joinedload` 就沒事了

回去查了一下 Airflow 使用的 SQLAlchemy 1.4.54 的原始碼
[sqlalchemy.orm.joinedload](https://github.com/sqlalchemy/sqlalchemy/blob/dfe401fd471323638ad3e1b1027d89e01fcbeef5/lib/sqlalchemy/orm/__init__.py#L289) 跟 [sqlalchemy.orm.strategy_options.joinedload](https://github.com/sqlalchemy/sqlalchemy/blob/dfe401fd471323638ad3e1b1027d89e01fcbeef5/lib/sqlalchemy/orm/strategy_options.py#L1397) 還真的有點微妙的不同

```python
joinedload = strategy_options.joinedload._unbound_fn
```

![mygo-it-is-but-it-is-not](/images/meme/mygo-it-is-but-it-is-not.jpg)

至於 `from sqlalchemy.orm.strategy_options import joinedload` 是怎麼來的
這是 neovim 中的 LSP 建議的，然後又是來自 SQLAlchemy
應該不會這麼剛好有一樣的變數名稱吧，不會吧不會吧
所以我就隨意選了一個
<ruby>仝款<rt>kāng-khuán</rt></ruby>，<ruby>無仝<rt>bô kāng</rt></ruby><ruby>師傅<rt>sai-hū</rt></ruby>
（為了想正確的寫出這句話，還去查了一下[芋圓字典](https://portaly.cc/taro.dict/pages/about)，確實蠻好用的）

然而實際上它們到底差在哪，就不是這篇文章的重點了
畢竟我就只是想隨筆寫下踩到的 Gotcha

[airflow-pr-53907]: https://github.com/apache/airflow/pull/53907
