Title: Pagefind UI 我的超人
Subtitle: 你也許不會發現，但這裡多了搜尋功能
Date: 2023-11-01 23:10 +0800
Category: Tech
Tags: blog
Slug: pagefind-ui
Authors: Wei Lee
Lang: zh-tw

當我說搜尋功能，我指的是真的可以用的搜尋功能

<!--more-->

會這麼說是因為之前的真的是不能用的 🥲

[TOC]

### 什麼是 [Pagefind UI](https://pagefind.app/) 呢

根據官網的介紹

> Pagefind is a fully static search library that aims to perform well on large sites, while using as little of your users’ bandwidth as possible, and without hosting any infrastructure.

* Pagefind 是
    * **靜態搜尋的函式庫**
    * 即使在很大的網站也有不錯的表現
    * 盡可能的減少使用者的頻寬
    * **不用架任何的 infra**

再往下滑一點還有很多酷功能，但我大多還沒用到 😆
其中比較重要的是多語言支援，尤其是中文

而設定上很簡單，也是我喜歡 Pagefind UI 的一點

我的 blog 都是使用 [Pelican](https://getpelican.com/) 產生，並 host 在 Github Pages 上
下一段會分享如何將 Pagefind UI 整合進 Pelican
關於 Pelican 的細節不會贅述太多

## 如何將 Pagefind UI 整合進 Pelican？

首先可以在 pelican 的設定檔（i.e., `pelicanconf.py`）加入 `PAGEFIND_ENABLED` 變數
用它來決定是否使用 Pagefind UI

再來要去修改主題
以我使用的主題 [elegant](https://github.com/Lee-W/elegant) 為例
需要將載入 [css](https://github.com/Lee-W/elegant/blob/blog-pagefindui-example/templates/base.html#L18-L20) 和 [js](https://github.com/Lee-W/elegant/blob/blog-pagefindui-example/templates/base.html#L128-L138) 的部分加入 [templates/base.html](https://github.com/Lee-W/elegant/blob/blog-pagefindui-example/templates/base.html)

```html
<!--templates/base.html-->

  {% if PAGEFIND_ENABLED|default(False) %}
  <link href="/pagefind/pagefind-ui.css" rel="stylesheet">
  {% endif %}
```

```html
<!--templates/base.html-->

  {% if PAGEFIND_ENABLED|default(True) %}
  <script src="/pagefind/pagefind-ui.js"></script>
  <script>
      window.addEventListener('DOMContentLoaded', (event) => {
          new PagefindUI({
              element: "#search",
              showImages: false,
          });
      });
  </script>
  {% endif %}
```

理想上應該要把這幾段拆成各自的 template，然後在 `templates/base.html` include 他們
但我有點懶，之後想 refactor 再說

搜尋區塊的改動則會根據主題的設計跟你希望如何呈現搜尋有關
在 elegant 中是把搜尋欄放在 [base.html](https://github.com/Lee-W/elegant/blob/blog-pagefindui-example/templates/base.html#L90-L92) 的一個項目
所在這我用 `li` 包住 `<div id="search"></div>`

```html
<!--templates/base.html-->

{% if PAGEFIND_ENABLED %}
<li><div id="search"></div></li>
{% else %}
```

而在我[另一個 blog](https://travlog.wei-lee.me/)則把它設定成獨立的頁面
如果沒意外的話，就大功告成了
（另一個 blog 因為 css 的調整確實有多花了點時間，但功能上是這樣就完成了）

沒錯！ 就是這麼簡單

![easy](/images/posts-image/2023-pagefindui/easy.jpg)

如果這時候直接把 Pelican 的 local server 跑起來，你就會發現
什麼都搜尋不到 🔍
因為沒有產生 search index 給 Pagefind UI 去找

而 search index 可以透過以下指令產生

```sh
npx -y pagefind --site output
```

`--site` 後面吃的參數是 Pelican 的輸出資料夾
預設通常是 `output`

## 將產生 search index 整合進 GitHub Actions
我的 blog 在寫完文章後，只要推上 main 分支
GitHub Actions 就會自動幫我產出最新的 blog ，並且部署到 GitHub Pages 上

為了讓 Pagefind UI 有 search index 可以找
必須在產出 blog 跟部屬的步驟中間，加入以下的步驟讓 GitHub Actions 也幫我產生 search index

```yaml
      # steps that build the blog

      - name: GitHub Action for npx
        uses: mikeal/npx@1.0.0

      - name: Build search index
        run: |
          npx -y pagefind --site output

      # steps that deploy the blog
```

## 看起來如何呢？
這個 blog

![this-blog](/images/posts-image/2023-pagefindui/this-blog.jpg)

[另一個 blog](https://travlog.wei-lee.me/)

![another-blog](/images/posts-image/2023-pagefindui/another-blog.jpg)

## 那些你不需要知道的背後故事
以下聽故事

當初使用 [elegant](https://github.com/Pelican-Elegant/elegant) 主題，其中一個原因就是它自帶搜尋功能（[Add Search to Your Site](https://elegant.oncrashreboot.com/add-search)）
結果它背後用的 [tipue-search](https://github.com/pelican-plugins/tipue-search) 壞掉了，搜尋功能就跟著死掉了

之前有想換到 [pelican-search](https://github.com/pelican-plugins/search)
搞了好久才弄起來，但他對中文斷詞的支援很差，基本上可以當作不存在
👉 [Search in Chinese seems to be not working#191](https://github.com/jameslittle230/stork/issues/191#)
後來還跑去玩 [luar.js](https://lunrjs.com/)，也是中文支援不行
之前原本還想寫一篇 "pelican-search does not work for Madarain."
但一直躺在草稿夾，就躺到死掉惹
不過也算是這篇的養分，是否也能算是某種轉生呢 🤔

最近心血來潮就想再回來看 [pelican-search](https://github.com/pelican-plugins/search)
然後就找到 [Consider alternatives to Stork #35](https://github.com/pelican-plugins/search/issues/35) ...
pelican-search 背後的 Strok 將不再維護 🥲

只好回去翻翻看 [pelican-themes](https://github.com/getpelican/pelican-themes) 中，比較有在更新的主題有沒有支援搜尋的
還真的讓我找到 [pelican-haerwu-theme](https://github.com/hrw/pelican-haerwu-theme/tree/ea01213468a775dcd14e6aa5800f654af5670bc5)

![pelican-theme](/images/posts-image/2023-pagefindui/pelican-theme.jpg)

![search](/images/posts-image/2023-pagefindui/search.jpg)

去追一下原始碼就找到 Pagefind UI
恩，整個故事大概就是這樣
