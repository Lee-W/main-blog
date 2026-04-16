Title: 2020 發文頻率分析 - 如何得到 pelican 文章資訊並用來做圖
Date: 2021-01-29 18:45 +0800
Category: Tech
Tags: Python, pelican
Slug: post-frequency-analysis-how-i-get-pelican-article-data-and-plot
Series: 2020 發文頻率分析
Authors: Wei Lee
Lang: zh-tw

原本只打算發篇文簡單回顧 2020 年我寫了什麼文章
沒想到就慢慢演變成開發 [pelican-stat](https://github.com/Lee-W/pelican-stat) ......

<!--more-->

原本只打算寫一篇的回顧文，就莫名其妙變成了三篇文章的系列文

1. [如何得到 pelican 文章資訊並用來做圖]({filename}/posts/tech/2021/3-post-frequency-analysis-how-i-get-pelican-article-data-and-plot.md)： 就是本文，主要會聊開發 [pelican-stat](https://github.com/Lee-W/pelican-stat) 的過程
2. [如何在 pelican 頁面中嵌入 HTML]({filename}/posts/tech/2021/4-post-frequency-analysis-how-to-embed-html-in-pelican.md)： 將產生的互動式趨勢圖嵌入 pelican 的文章中，遇到的各種雷
3. [2020 過去了，我寫了什麼文章]({filename}/posts/random-thoughts/2021/1-post-frequency-analysis.rst)： 2020 主要發了什麼文章，並聊聊當初為什麼會想寫這些文章

[TOC]

## 什麼是 pelican-stat
[pelican](https://github.com/getpelican/pelican) 是用來產生靜態網頁的工具，最常見的用途應該是寫部落格
你所看到的這個部落格就是透過這套工具產生的

[pelican-stat](https://github.com/Lee-W/pelican-stat) 則是我這次開發來蒐集pelican 文章資料並作圖的工具

## 如何使用 pelican-stat

### 安裝
因為我把 [pelican](https://github.com/getpelican/pelican/tree/4.5.4) 的版本定在 4.5.4
為了避免跟你的 pelican 版本打架，強烈建議使用 [pipx](https://github.com/pipxproject/pipx) 安裝

```sh
pipx install pelican-stat
```

pelican-stat 目前支援 `collect` 和 `plot` 兩種指令

```sh
Usage: pelican-stat [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  collect  Collect data from pelican project and export article metadata
  plot     Draw trend plot based on the frequency of new posts
```

### collect
將文章的資訊整理並輸出成 json 檔

e.g.,

```json
[
    ...,
    {
        "timestamp": 1560308220.0,
        "category": "Travel",
        "authors": [
            "Lee-W"
        ],
        "reader": "markdown",
        "status": "published",
        "tags": [
            "Star Wars",
            "Galaxy's Edge"
        ],
        "timezone": "Asia/Taipei",
        "title": "Star Wars: Galaxy's Edge - First Peek"
    }
]
```

第一個參數吃的是 pelican 的設定檔，第二個則是輸出的位置

### plot
就如同指令的名稱，它就是拿來做圖用的
目前只支援趨勢圖

使用上比 `collect` 複雜一點，有 5 個可以設定的參數

* `--pelican-conf-path [PATH]`： pelican 設定檔的路徑
* `--articles-metadata-path [PATH]`： 用 `collect` 指令所產生的文章資料 json 檔的路徑

上面兩個一定要有一個有值，不然 pelican-stat 不知道要去哪抓文章資料

* `--output-path [PATH]`： 輸出檔名
* `--year [YEAR]`： 篩選特定年份的文章
* `--groupby-category`： 作圖是否要根據文章類別分群

最後就能做出像這樣的圖
產生的會是可以互動的 HTML 檔案

![newplot](/images/posts-image/2021-2020-post-frequency/newplot.png)

## 設計 pelican-stat
在開始寫 pelican-stat 前，我有找到類似的工具 👉 [panorama](https://github.com/romainx/panorama)
不過它是作為 pelican-plug 來使用，而不是獨立的指令列工具
所以就只好自己來寫了

### collect
第一個收集文章資訊的想法是寫 parser 去解析這些文章
但是這麼做的話，這個工具可能就很難被其他人使用
每個人指定 metadata 、放置文章的方式可能都不同
甚至有人根本是用 reStructuredText 寫的
（pelican 支援 reStructuredText 跟 markdown）

不過有個工具一定有辦法抓到這些資訊
沒錯💡
那就是 pelican 本身！
所以第二個想法是觀察 pelican 怎麼去解析這些文章
如果能的話，直接呼叫它的函式，不要重造輪子

從使用 pelican 指令到產生文章，會用這個順序追朔程式碼

1. [pelican/\_\_main\_\_.py#L9](https://github.com/getpelican/pelican/blob/4.5.4/pelican/__main__.py#L9)
2. [pelican/\_\_init\_\_.py#L491](https://github.com/getpelican/pelican/blob/4.5.4/pelican/__init__.py#L491)
3. [pelican/\_\_init\_\_.py#L501](https://github.com/getpelican/pelican/blob/4.5.4/pelican/__init__.py#L501)
4. [pelican/\_\_init\_\_.py#L403-418](https://github.com/getpelican/pelican/blob/master/pelican/__init__.py#L403-418)

這就是為什麼我的 [\_get\_pelican\_instance](https://github.com/Lee-W/pelican-stat/blob/0.3.0/pelican_stat/collector.py#L15) 會這樣寫

而我額外多做了兩個處理

```python
settings["PLUGINS"] = []
settings["MARKDOWN"] = {}
```

原因是 MARKDOWN 跟 PLUGINS 都有可能有額外的相依套件
尤其是 pelican 自從 [4.5.0](https://docs.getpelican.com/en/4.5.0/plugins.html#how-to-use-plugins) 之後開始支援從 pip 安裝的 pelican-plugins
但它們對文章的 metadata 大多不會有影響
所以將他們從設定中清掉可以避免遇到相依套件沒裝的問題

接著繼續追程式碼

1. [pelican/\_\_init\_\_.py#L527](https://github.com/getpelican/pelican/blob/4.5.4/pelican/__init__.py#L527)
2. [pelican/\_\_init\_\_.py#L85-100](https://github.com/getpelican/pelican/blob/4.5.4/pelican/__init__.py#L85-L100)

我透過 pdb 看到 `generators[0]` 是 `ArticlesGenerator`
看起來透過它就有很大的機會能取得文章資訊
它也會對應到我所寫的 [pelican_stat/collector.py#L29-L43](https://github.com/Lee-W/pelican-stat/blob/0.3.0/pelican_stat/collector.py#L29-L43)
這裡也是我會把 pelican-stat 相依的 pelican 釘在 4.5.4 的主因
[\_get\_generator\_classes](https://github.com/getpelican/pelican/blob/4.5.4/pelican/__init__.py#L169) 在 4.5.2 以前是 `get_generator_classes`
雖然可以用 `getattr(pelican_instance, "get_generator_classes")` 來支援不同的版本
但難保 pelican 什麼時候又會改 API
而且即使 pelican 的版本不同，對於文章 metadata 的格式應該都不會有改變
所以作為一個工具，使用特定版本的 pelican 應該就足夠了

最後在 [pelican/\_\_init\_\_.py#L111-L113](https://github.com/getpelican/pelican/blob/4.5.4/pelican/__init__.py#L111-L113) 執行完 `generate_context()` 就能從 `article_generator.aricles` 取得文章

而每篇文章都是 [pelican.context.Article](https://github.com/getpelican/pelican/blob/4.5.4/pelican/contents.py#L514) 的 instance
所以只要看裡面有哪些資訊是我要的，在進行輸出就可以了 👉 [pelican_stat/collector.py#L47](https://github.com/Lee-W/pelican-stat/blob/0.3.0/pelican_stat/collector.py#L47)

### plot
最初版測試用的 script，先了用我比較熟悉的 [bokeh](https://docs.bokeh.org/en/latest/index.html) 寫
但上次有朋友安利我 [ploty](https://plotly.com/python/) 很好用，就決定來玩玩看
使用上覺得兩個函式庫都還蠻直覺的
但 ploty 可以不用多做設定就有 hover tool ，還蠻方便的
因為這部分的程式碼大多都是看文件就能找到，就不特別聊了
