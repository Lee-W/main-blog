Title: 獨立地圖
Date: 2026-08-12 23:37 +0800
Category: Random Thoughts
Tags: Blog, Pelican, Tool, Lifestyle
Slug: now-i-also-have-my-own-map
Authors: Wei Lee
Lang: zh-tw
Status: draft

Wiwi 在[幫大家畫地圖](https://wiwi.blog/blog/openstreetmap/) 推薦大家可以標記 [OpenStreetMap](https://www.openstreetmap.org/) 的地圖跟經營自己的獨立網站

<!--more-->

那麼在自己的獨立網站畫地圖紀錄座標，就是一石二鳥之計啦！

從很久以前我就一直在思考
有沒有什麼辦法好好紀錄去過的地方
尤其身為一個 J 人，我每次規劃旅行，都有還算詳細的地點紀錄
我好想全部都記錄下來啊
以前一直在找有沒有什麼神秘的方式可以用一個語法，直接在 Markdown 渲染出來

而最後我找到的做法是，叫 Claude 幫我寫個 [pelican](https://getpelican.com/) 的外掛
於是 [pelican-osm](https://github.com/Lee-W/pelican-osm) 就誕生了
概念蠻簡單的，就只是把 yaml 中記錄點透過[Leaflet.js](https://leafletjs.com/) 顯示在 [OpenStreetMap](https://www.openstreetmap.org/)

目前幾個比較有整理過的地圖有

* [共同工作空間]({filename}/pages/coworking.md)
* [電影院座位個人喜好](https://travlog.wei-lee.me/pages/theaters-preference)
* [我走訪過的動漫畫／影視作品聖地](https://travlog.wei-lee.me/pages/pilgrimage)
* [餐廳地圖](https://travlog.wei-lee.me/pages/restaurant-map)

剩下就是散在文章中的地點了
