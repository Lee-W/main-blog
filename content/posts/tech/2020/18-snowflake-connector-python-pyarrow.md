Title: snowflake-connector-python: 你的 pyarrow 不是你的 pyarrow
Date: 2020-12-22 23:20 +0800
Category: Tech
Tags: Python, snowflake
Slug: snowflake-python-connector-install-extra-pyarrow-will-not-solve-your-problem
Authors: Wei Lee

這是個不好好看文件，胡亂嘗試、多繞了一圈才解決問題的經驗

<!--more-->

最近剛好接手了別人弄到一半的專案
在嘗試把專案跑起來的時候，遇到了這個問題

```txt
Optional dependency: 'pyarrow' is not installed, please see the following link for install instructions: https://docs.snowflake.com/en/user-guide/python-connector-pandas.html#installation
```

看起來是 `pyarrow` 沒有裝起來，所以可以先嘗試 `pip install pyarrow`
但很不幸的，這麼做並不會解決問題
[snowflake-connector-python](https://github.com/snowflakedb/snowflake-connector-python) v2.3.7 需要的 `pyarrow` 版本必須是 >=0.17.0, < 0.18.0
這也不是什麼大問題，只要改成 `pip install pyarrow==0.17.0` 就可以解決

不過如果每個套件遇到類似的問題都要這樣試，可能會花上不少的時間
對 pip 稍有概念的人看到 *Optional dependency: 'pyarrow' is not installed* 可能會聯想到沒裝 extra requirement
所以我第一個嘗試其實是 `pip install snowflake-connector-python[pyarrow]`
但安裝完以後，還是跳出了同樣的錯誤訊息
而且進到虛擬環境中會發現連 `pyarrow` 都沒有被安裝

這時也只好點進它的文件，看是不是有需要額外設定什麼
👉 [Using Pandas DataFrames with the Python Connector](https://docs.snowflake.com/en/user-guide/python-connector-pandas.html#installation)
點進文件馬上就會看到的指令是 `pip install snowflake-connector-python[pandas]`
因為我要裝 `pyarrow` 所以我將後面的 `pandas` 改成 `pyarrow`
不過這其實就跟前次嘗試的指令是一樣的，同樣不能解決問題
就在我百思不得其解時，我隨意測試了跟文件上一模一樣的指令
(i.e., `pip install snowflake-connector-python[pandas]`)
然後一切的問題就解決了......

既然解決了，就要回去思考為什麼能解決
回去看 [snowflake-python-connector @ v2.3.7](https://github.com/snowflakedb/snowflake-connector-python/tree/v2.3.7/) 的 setup.py
在 [44行](https://github.com/snowflakedb/snowflake-connector-python/blob/v2.3.7/setup.py#L44) 可以找到 `'pyarrow>=0.17.0,<0.18.0'`

```python
pandas_requirements = [
    # Must be kept in sync with pyproject.toml
    "pyarrow>=0.17.0,<0.18.0",
    "pandas>=1.0.0,<1.2.0",
]
```

接著可以看到 `pandas_requirements` 在 [240行](https://github.com/snowflakedb/snowflake-connector-python/blob/v2.3.7/setup.py#L240) 被用到

<!-- blacken-docs:off -->

```python
    ...
    extras_require={
        "secure-local-storage": [
            'keyring<22.0.0,!=16.1.0',
        ],
        "pandas": pandas_requirements,
    ...

```

<!-- blacken-docs:on -->

原來 `pip install snowflake-connector-python[pandas]` 同時會安裝 `pandas_requirements` 中的 pandas 跟 pyarrow
snowflake-connector-python 並不會單獨裝 pyarrow，這也難怪前面的嘗試會失敗
但其實這個問題只要都造著文件做就能解決，就是因為自作聰明才繞了一大圈
所以我說文件還是要好好的看啊！
