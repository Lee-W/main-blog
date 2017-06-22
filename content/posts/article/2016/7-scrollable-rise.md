Title: Scrollable RISE
Date: 2016-08-15 03:22
Category: Python
Tags: Jupyter, reveal.js
Slug: scrollable-rise
Authors: Lee-W
Summary: 


RISE是一套結合[jupyter-notebook](http://jupyter.org)和[reveal.js](http://lab.hakim.se/reveal-js/#/)的專案
讓我們能在jupyter notebook直接開啟如同reveal.js的slide

<!--more-->

不過如過notebook cell中的內容太長
在播放的時候就會導致內容被裁剪
而RISE預設是無法用滑鼠滾動的
所以這裡記錄該如何讓RISE可以滾動

進入jupyter notebook的任一個notebook後
在上方工具列點選`Edit` -> `Edit Notebook Metadata`
接著在裡面加入livereveal的設定
如下 （只需加入livereveal的部分）

```json
{
	"kernelspec": {
  	...
  },
  "livereveal": {
   "scroll": true
  }
}
```

---
不過開發者其實有說，開啟滾動會造成不少問題
所以預設上才會設定為不能滾動

**damianavila commented on Jul 12**
After several and long discussions with a lot of people, we have arrived to the conclusion that scrolling on reveal.js based slideshows brings more problems than benefits, so I will not add the scrolling as a default option BUT we should clearly document how to get scrolling slides with the config option available. I will mark this as a docs issue and prioritize properly.


# Reference
[scrolling vertically #185](https://github.com/damianavila/RISE/issues/185)