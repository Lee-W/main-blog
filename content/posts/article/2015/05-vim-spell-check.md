Title: vimspell - vim 檢查英文文法的套件
Date: 2015-02-14 09:59
Category: Tech
Tags: Vim
Slug: vim-spell-check
Authors: Wei Lee

[vimspell](http://www.vim.org/scripts/script.php?script_id=465) 是一套提供 vim 根據字典來檢查文法的套件
有了 vimsepll，寫 Markdown 或 LaTeX 的時候，就不用再怕拼錯字了

<!--more-->

## 用 vundle 安裝

在 vimrc 中加入下面這行

```vim
Bundle 'vimspell'
```

接著用 `:BundleInstall` 安裝

## 字典檔

[下載字典檔](http://archive.services.openoffice.org/pub/mirror/OpenOffice.org/contrib/dictionaries/)

我下載的是 `en_US.zip`

解壓縮完後，用 vim 開啟街壓縮完的資料夾
應該會看到下面這樣
![1_directory](/images/posts-image/2015-02-14-vim-spell-check/gLWMnmW.png)

接著進入 vim 在 normal mode 輸入

```vim
:mkspell en en_US
```

`en` 可以自己定義，`en\_US` 必須是 .aff 和 .dic 的檔名
檢查一下 vim 資料夾下的 spell 資料夾有沒有新增字典檔，確定有了後就新增完成了

## 設定

首先要先定義要根據哪個字典檔

```vim
:set spelllang=en
```

en 就是剛剛所定義的名稱

接著 `:set spell` 就可以開啟了
`:set nospell` 則是關閉

如果每次都要設定一次，就太麻煩了
我在 vimrc 加入了下面這些

```vim
set spelllang=en
nmap <F7> :setlocal spell!<cr>
autocmd BufRead *.txt,*.md,*.tex setlocal spell
```

第二行是每次按 F7 就能開啟或關閉 vimspell，也可以換成自己想要的快捷鍵
第三行則是每次遇到副檔名是 txt, md, tex 時就自動開啟 vimspell

## 使用

vimspell 被開啟後，就會自動把拼錯的字反白起來
如果有其他的語言一樣會被反白起來
![2_vimspell_sample](/images/posts-image/2015-02-14-vim-spell-check/MGjdAoq.png)

### 指令

* `]s` : 跳到下一個錯字
* `[s` : 跳到上一個錯字
* `z=` : 開啟建議，可以參考下面的圖，選擇完按 enter 後，就會替換原本的字
* `zg` : 將目前游標上的字加入字典  
         新增的字都會被加到 `~/.vim/spell/en.utf-8.add`( 根據語言不同，檔名會不同 )
* `zug`: 復原加入字典的字 (刪除)
* `zw` : 加入壞字字典，壞字也會被加入同樣的檔案中，最後面會另外加上 `/!`
* `zuw`: 復原加入壞字字典的字 (刪除)

![3_choose_word](/images/posts-image/2015-02-14-vim-spell-check/NWHCakj.png)

## Reference

* [Vim documentation: spell](http://vimdoc.sourceforge.net/htmldoc/spell.html)
* [How to use spell check with vim](http://www.go2linux.org/linux/2010/10/how-use-spell-check-vim-795)
* [[Reply] 如何在 vim 裡用拼字檢查 - iT 邦幫忙 ::IT 知識分享社群](http://ithelp.ithome.com.tw/question/10055602)
* [Create a spell file for VIM](http://henry.precheur.org/vim/create_spell_file_for_vim)
* [vim - Automatically enabling spell checking in vimrc - Stack Overflow](http://stackoverflow.com/questions/7286207/automatically-enabling-spell-checking-in-vimrc)
