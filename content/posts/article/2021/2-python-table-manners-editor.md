Title: Python Table Manners 番外 - 編輯器
Date: 2021-01-02 12:57
Category: Tech
Tags: Python, editor
Slug: python-table-manner-editor
Authors: Lee-W
Series: Python Table Manners

在最開始的規劃中，並沒有想要寫編輯器
不過半年前（可能更久以前...），朋友有建議可以寫這個主題
上次去 Taichung.py 分享也有人提問
就稍微整理我在用的編輯器

<!--more-->

我主要用的編輯器是 neovim
有時候會稍微用一下 Visual Studio Code
需要輸入中文或只是快速瀏覽會開 sublime

## IDE
如果是習慣用 IDE 的人，我推薦用 [Visual Studio Code](https://code.visualstudio.com/)
看完官方的 [Python in Visual Studio Code](https://code.visualstudio.com/docs/languages/python) 應該就能弄懂大部分的功能了

## 文字編輯器
文字編輯器，我推薦 neovim，用起來跟 vim 差不多
至於要看我怎麼設定 vim 的話，可以參考 [vim-setting](https://github.com/Lee-W/vim-setting)
另外推薦 Real Python 寫的 [VIM and Python – A Match Made in Heaven](https://realpython.com/vim-and-python-a-match-made-in-heaven/#macos-os-x)

### 好用的 vim 套件
這裡整理一些我很推薦的套件們，其他套件要不要用就看個人習慣了

* Python 相關
    * [python-mode](https://github.com/python-mode/python-mode)
        * Python 相關功能的集大成，裝了這個大概就有八成的功能了
    * [black](https://github.com/psf/black)
        * 在 vim 內執行 black
    * [vim-isort](https://github.com/fisadev/vim-isort)
        * 在 vim 內執行 isort
* 通用
    * [vim-test](https://github.com/vim-test/vim-test)
        * 在 vim 內執行測試（支援 20 種以上的程式語言）
    * [vim-easymotion](https://github.com/easymotion/vim-easymotion)
        * 快速在 vim 內跳轉，點進去看文件的動畫更容易知道這個工具在幹嘛，它好用到我會為了用它在瀏覽器裝 vim 套件
            * Firefox 🦊 套件： [Vimium-FF](https://addons.mozilla.org/en-US/firefox/addon/vimium-ff/)
    * fzf： 快速在 vim 內做文字、檔案搜尋
        * 需要同時安裝 [fzf](https://github.com/junegunn/fzf.vim) 和 [fzf.vim](https://github.com/junegunn/fzf.vim)
