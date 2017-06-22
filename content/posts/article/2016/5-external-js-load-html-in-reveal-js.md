Title: External.js - Load HTML in Reveal.js
Date: 2016-03-23 01:23
Category: JavaScript
Tags: reveal.js
Slug: external-js-load-html-in-reveal-js
Authors: Lee-W
Summary: 


reavel.js提供了`data-markdown="example.md"`這個tag可以載入外部的markdown
卻沒提供可以載入html的tag
於是就有人寫了這個[External.js](https://github.com/calevans/external)

<!--more-->

有了External.js，就可以不用把所有的內容都寫在`index.html`裡面

# Install

## Method1: Download
1. 到https://github.com/calevans/external下載
2. 把extneral裡面的external資料夾放到plugin裡面
3. 在`index.html`中的`Reveal.initalize`這個block加入下面的內容
```
{ src: 'plugin/external/external.js', condition: function() { return !!document.querySelector( '[data-external]' ); } },
```

## Method2: Submodule
不過為了讓他的更新也能被追蹤，我使用了git submodule

1. git submodule
```sh
git submodule add https://github.com/calevans/external plugin/external
```

2. 在`index.html`中的`Reveal.initalize`這個block加入下面的內容
```
{ src: 'plugin/external/external/external.js', condition: function() { return !!document.querySelector( '[data-external]' ); } },
```
(注意兩種方式加入的內容有些微的不同)

# Usage
之後就能使用`data-external`這個tag來載入外部的html

## 原本的index.html
```html
<section data-external="module_01/index.html"> </section>
```

## 外部html
```html
<!-- module_01/index.html -->
<h1> This is external <h1>
```

## 載入後的html
```html
<section data-external="module_01/index.html">
	<!-- module_01/index.html -->
	<h1> This is external <h1>
</section>
```