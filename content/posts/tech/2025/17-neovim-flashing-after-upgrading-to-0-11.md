Title: 更新 Neovim 0.11.0 後， iTerm 視窗一直閃
Subtitle: 沒有大意是好事，但過猶不及
Date: 2025-05-07 09:20
Category: Tech
Tags: Neovim
Slug: neovim-flashing-after-upgrading-to-0-11
Authors: Wei Lee

大意了沒有閃，確實不是件好事
但一直閃也很令人困擾啊！

<!--more-->

[TOC]

## 發生什麼事
上個月更新到 Neovim 0.11.0 後
每次存檔後， iTerm 的視窗就會不斷閃爍
關閉的時候還會出現一串亂碼
直覺想是不是在存檔後會自動執行的 auto formatter
或是 [LazyVim] 的某些 UI 元件壞掉惹
但試著試著都解決不了這個問題

## 原因
後來翻到[iterm2 3.5.6+ with neovim 0.11, on FocusGained, j/k jump to top/bottom of buffer #33127](https://github.com/neovim/neovim/issues/33127)

原來是因為之前 iTerm 有問過我要不要允許 session 去 resize 我的 window
看起來很合理就按了允許

## 如何解決
解決方式也很簡單，就是「回到過去，阻止按下允許的自己」
或者你可以在 iTerm 的設定中，再次把這個選項關閉

`Settings` > `Profile` > `Terminal`

把 `Emulation features` 中的 `Disable session-initiated window resizing` 選起來

![neovim-iTerm2](/images/posts-image/2025-neovim-flashing-after-upgrade-to-0-11/neovim-iTerm2.png)

[LazyVim]: https://www.lazyvim.org/
