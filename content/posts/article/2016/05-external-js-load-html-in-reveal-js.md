Title: External.js - Load HTML in Reveal.js
Date: 2016-03-23 01:23
Category: Tech
Tags: JavaScript, reveal.js
Slug: external-js-load-html-in-reveal-js
Authors: Lee-W

reavel.js 提供了 `data-markdown="example.md"` 這個 tag 可以載入外部的 markdown
卻沒提供可以載入 html 的 tag
於是就有人寫了這個[External.js](https://github.com/calevans/external)

<!--more-->

有了 External.js，就可以不用把所有的內容都寫在 `index.html` 裡面

# Install

## Method1: Download

1. 到 [external](https://github.com/calevans/external) 下載
2. 把 extneral 裡面的 external 資料夾放到 plugin 裡面
3. 在 `index.html` 中的 `Reveal.initalize` 這個 block 加入下面的內容

```javascript
{ src: 'plugin/external/external.js', condition: function() { return !!document.querySelector( '[data-external]' ); } },
```

## Method2: Submodule

不過為了讓他的更新也能被追蹤，我使用了 git submodule

* git submodule

```shell
git submodule add https://github.com/calevans/external plugin/external
```

* 在 `index.html` 中的 `Reveal.initalize` 這個 block 加入下面的內容

```javascript
{ src: 'plugin/external/external/external.js', condition: function() { return !!document.querySelector( '[data-external]' ); } },
```

( 注意兩種方式加入的內容有些微的不同 )

# Usage

之後就能使用 `data-external` 這個 tag 來載入外部的 html

## 原本的 index.html

```html
<section data-external="module_01/index.html"> </section>
```

## 外部 html

```html
<!-- module_01/index.html -->
<h1> This is external <h1>
```

## 載入後的 html

```html
<section data-external="module_01/index.html">
	<!-- module_01/index.html -->
	<h1> This is external <h1>
</section>
```
