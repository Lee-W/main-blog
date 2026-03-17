Title: Bartender 失去信任的此時，我們該何去何從
Date: 2024-06-15 11:58 +0800
Category: Tech
Tags: Mac
Slug: where-should-we-go-if-bartender-is-no-longer-considered-safe
Authors: Wei Lee

> 世界上絕對不能背叛客人的兩種職業，一種是醫師與藥劑是，另一種則是... 調酒師！
>
> -- 佐佐倉溜

<!--more-->

上週 Reddit 上的一篇文章 [Bartender 5 not safe anymore ? Warning from MacUpdater](https://www.reddit.com/r/macapps/comments/1d7zjv8/comment/l73h9gv/)
Bartender 默默的就易主了
默默的要了權限（好啦，沒那麼默默）
默默的裝了[Amplitude](https://amplitude.com/)
導致不少人對 Bartender 不再信任

好了，那該怎麼辦呢？

## 1. 繼續使用 Bartender
如果你對新的開發者信任，那就繼續使用吧，他們在炎上後發了一篇聲明 [Let's Try This Again](https://www.macbartender.com/b5blog/Lets-Try-This-Again/)

## 2. 降回 Bartender 被信任的版本

降版到 `<=5.0.52` ， Amplitude 應該是在這版被加入了
但官方是說 `5.0.53` 已經移除

## 3. 尋找 Bartender 的替代方案

這些都是從各大文章像是[Six Bartender Alternatives to Manage Your Mac's Menu Bar](https://www.macrumors.com/2024/06/06/alternatives-bartender-mac-menu-bar/) 或 Twitter 、Reddit 搜集來玩過的工具們

### hidden
🔗 [link to Github](https://github.com/dwarvesf/hidden)

已經沒有繼續維護了，但用起來還堪用

#### VimMotionApp
🔗 [link to Github](https://github.com/dwarvesf/VimMotionApp)

跟 menu bar 無關
意外發現 [hidden](https://github.com/dwarvesf/hidden) 開發者還有開發出這種好東西
尤其是前一天跟日本朋友吃飯，聊到在瀏覽器還用 Vim mode 很反人類
沒錯，就我，超好用好嗎！
我不當人類啦， JOJO
推薦[Vimium](https://addons.mozilla.org/firefox/addon/vimium-ff/)給你，一起反人類

### HiddenBar
🔗 [link to Github](https://github.com/UeharaYou/HiddenBar)

[UeharaYou](/UeharaYou) fork [hidden](https://github.com/dwarvesf/hidden) 出來維護的的版本
Star 數不算太多，就沒特別試了
但我有同事用這個

### Dozer
🔗 [link to Github](https://github.com/Mortennn/Dozer)

使用 Bartender 前，我是用 Dozer，但後來沒有維護了
從 macOS 14 開始就會 crash

### SketchyBar
🔗 [link to Github](https://github.com/FelixKratz/SketchyBar)

這個算是最特別的
其實蠻有趣的，但不合用
它會要你把系統 menu bar 隱藏起來
在桌面的最上方再放上另外可以互動的工具

### Bartender controversy, tutorial on how to manage menubar status items via BTT
🔗 [link to BTT forum](https://community.folivora.ai/t/bartender-controversy-tutorial-on-how-to-manage-menubar-status-items-via-btt/37429/1)

BTT 使用者的福音
在 BTT 上支援最基本的收納功能
我試用一開始用起來好好的，後來就叫不出來了
感覺應該是我設定錯誤
有空會想再回來嘗試

### Ice
🔗 [link to Github](https://github.com/jordanbaird/Ice)

說是這次 Bartender 之亂的最大受惠者也不為過吧
看那精美的 Star History

![ice star-history](https://api.star-history.com/svg?repos=jordanbaird/Ice&type=Date)

用起來蠻直覺的跟 Dozer 很像，但有支援最新的 macOS 14
不過遇到劉海還是沒辦法

> Display hidden items in a separate bar (e.g. for MacBooks with the notch)

但這件事看起來有在他們的 roadmap 中，可以期待
