Title: Fix Neovim "'fzf' extension doesn't exist or isn't installed:"
Date: 2024-06-25 23:25
Category: Tech
Tags: Neovim
Slug: neo-vim-fzf-not-loaded
Authors: Wei Lee

簡單記錄一下之前使用 Neovim 遇到的套件問題
不是什麼有深度的技術文章

<!--more-->

許久以前的某一天突然就遇到了 [fzf](https://github.com/junegunn/fzf) 壞掉的問題

```
Failed to run `config` for telescope-fzf-native.nvim

...m/lazy/telescope.nvim/lua/telescope/_extensions/init.lua:10: 'fzf' extension doesn't exist or isn't installed: ...hare/nvim/lazy/telescope-fzf-native.nvim/lua/fzf_lib.lua:11: dlopen(/.../.local/share/nvim/lazy/telescope-fzf-native.nvim/lua/../build/libfzf.so, 0x0005): tried: '/.../.local/share/nvim/lazy/telescope-fzf-native.nvim/lua/../build/libfzf.so' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/.../.local/share/nvim/lazy/telescope-fzf-native.nvim/lua/../build/libfzf.so' (no such file), '/.../.local/share/nvim/lazy/telescope-fzf-native.nvim/lua/../build/libfzf.so' (no such file)

# stacktrace:
  - /telescope.nvim/lua/telescope/_extensions/init.lua:10 _in_ **load_extension**
  - /telescope.nvim/lua/telescope/_extensions/init.lua:62 _in_ **load_extension**
  - /LazyVim/lua/lazyvim/plugins/editor.lua:110 _in_ **fn**
  - /LazyVim/lua/lazyvim/util/init.lua:286 _in_ **on_load**
  - /LazyVim/lua/lazyvim/plugins/editor.lua:109 _in_ **config**
  - /cmake-tools.nvim/lua/cmake-tools/init.lua:3
  - /cmake-tools.nvim/plugin/cmake-tools.lua:4
  - vim/_editor.lua:0 _in_ **cmd**
```

檢查了幾個地方都沒發現問題
也透過當時使用的套件管理工具重新安裝，依然沒有解決
忘記那時候用什麼工具管，但我最近是使用 [Lazyvim](https://www.lazyvim.org/)，很好用
順手分享一下我的 [nvim-config](https://github.com/Lee-W/nvim-config)

後來找到了 [ AstroVim: This extension doesn't exist or is not installed: fzf #58 ](https://github.com/AstroNvim/AstroNvim/issues/58#issuecomment-1504303757) 的 comment
原來只用套件管理工具重裝可能是沒用的
後來透過下面的指令，手動重新 build 一次就好了

```sh
cd ~/.local/share/nvim/lazy/telescope-fzf-native.nvim
make clean
make
```

換成 Lazyvim 後，又隔了這麼久已經沒再遇過同樣的問題

至於為什麼都隔了這麼久，還要寫這篇文章
反正草稿都躺這麼久了，刪掉也可惜
也許哪天還是會遇到類似的問題，筆記一下也好