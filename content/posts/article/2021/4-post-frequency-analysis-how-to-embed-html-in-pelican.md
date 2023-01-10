Title: 2020 發文頻率分析 - 如何在 pelican 頁面中嵌入 HTML
Date: 2021-01-29 23:10
Category: Tech
Tags: pelican
Slug: post-frequency-analysis-how-to-embed-html-in-pelican
Authors: Wei Lee
Series: 2020 發文頻率分析

因為不想在文章裡面直接寫 HTML（主要是不想自己去調大小、風格什麼的）
我花了點時間研究要怎麼樣正確且優雅（？）的在 pelican 中嵌入 HTML

<!--more-->

不過當我把它們放到 pelican 的專案目錄下後
就會因為這些 HTML 沒有 title 造成錯誤

```txt
ERROR: Skipping .../content/static/post-static/2021-post-frequency/all.html: could not find information about 'title'
WARNING: Meta tag in file .../content/static/post-static/2021-post-frequency/2020-by-category.html does not have a 'name' attribute, skipping. Attributes: charset="utf-8"
```

看起來是 pelican 把它們也當作文章

[ERROR: Skipping extra/XXXXX.html: could not find information about 'title'](https://github.com/getpelican/pelican/issues/1157) 中也有人遇到同樣的問題
只要在 `pelicanconf.py` 加上設定，讓 pelican 不要去讀 HTML

```python
READERS = {"html": None}
```

pelican 的文件 [including-other-files](https://docs.getpelican.com/en/4.5.4/content.html#including-other-files) 有提到 reStructuredText 有原生支援
如果是 markdown 就得安裝 [mdx_include](https://github.com/neurobin/mdx_include)
沒想到這個套件用下去我的建置時間從幾秒鐘飆升到幾分鐘...

最後我只好妥協用 reStructuredText 來寫下一篇文章

```rst
.. raw:: html
    :file: ../../../static/post-static/2021-post-frequency/all.html
```
