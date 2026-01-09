Title: 一覺醒來 Neovim 的 treesitter 就壞掉了
Date: 2026-01-09 12:30
Category: Tech
Tags: Neovim
Slug: neovim-treesitter-was-broken
Authors: Wei Lee
Cover: /images/posts-image/2026/neovim-treesitter-was-broken/neovim-treesitter-was-broken.png

通常我都會讓 [LazyVim](https://www.lazyvim.org/) 每天去抓最新版本的外掛
抓著抓著，某一天就壞掉了...

<!--more-->

## 發生什麼事

更新完之後就出現了這個訊息

![neovim-treesitter-was-broken](/images/posts-image/2026/neovim-treesitter-was-broken/neovim-treesitter-was-broken.png)

```console
...m/0.11.4/share/nvim/runtime/lua/vim/treesitter/.
    "tab"
```

錯誤訊息本身幫助不大

把幾個相關套件從 Neovim 刪掉後再重裝，也沒有解決問題
而從
[Treesitter query error (“Invalid tab”) blocks command-line #8363](https://github.com/nvim-treesitter/nvim-treesitter/issues/8363#issuecomment-3678168148)
的討論可以看到提交 [4fc09be](https://github.com/nvim-treesitter/nvim-treesitter/commit/4fc09bee78e91bf4ba471cdab4bf9dfa37fde51c) 是最後穩定的版本
但照著後面的步驟執行 `:TSUpdate`，還是沒有解決問題
（如同 issue 裡面寫的）

雖然是可以把套件定在這一版，但我還是想更新上去啊！

## 原因
在同一個 GitHub issue 拉到最下面，看到另一個可能的原因
已經透過 [mason.nvim](https://github.com/mason-org/mason.nvim) 安裝的 tree-sitter 二元檔可能是不相容的

## 如何解決

```sh
rm ~/.local/share/nvim/mason/bin/tree-sitter
```

既然不相容就把它刪掉重裝吧，問題就解決了

---

寫這篇文章的時候
剛好看到 [bug: After last update Noice keep displaying message instead of textbox as usual #1183](https://github.com/folke/noice.nvim/issues/1183) 也遇到了同樣的問題

順手回了一下，希望有幫到他
