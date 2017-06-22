Title: powerline on zsh, vim, tmux
Date: 2014-07-30 15:01
Category: Linux-Unix
Tags: Utility
Slug: powerline-on-zsh-vim-tmux
Authors: Lee-W
Summary: 


用了vim的powerline後覺得很酷，就找了很多的powerline來玩
於是這篇文章產生了XDD

<!--more-->

這是各個powerline的預覽圖
1. vim
![1_vim](http://i.imgur.com/VTM4866.png)
2. tmux
![2_tmux](http://i.imgur.com/LLJ9xjk.png)
3. zsh
![3_zsh](http://i.imgur.com/tOvzhK3.png)


## powerline 字體
安裝這些powerline之前要先下載powerline字體
不然可能會無法正常顯示
在https://github.com/Lokaltog/powerline-fonts下載後，之後安裝就完成了
*記得要把終端機的字體條成這些有powerline結尾的字體，我當初就是沒用這個卡了很久= =*

```shell
git clone https://github.com/Lokaltog/powerline-fonts /tmp/git/clone
sudo mv /tmp/git-clone/powerline-fonts /usr/share/fonts/powerline-fonts
sudo fc-cache -v -f
```

## zsh
其實oh-my-zsh本身就有agnoster了
但我更推薦下面這個https://github.com/jeremyFreeAgent/oh-my-zsh-powerline-theme
安裝完之後記得再zshrc中加入
> ZSH_THEME="powerline"

如果要更多客制化設定可以參考repo內的設定

```shell
git clone https://github.com/jeremyFreeAgent/oh-my-zsh-powerline-theme /tmp/oh-my-zsh-powerline-theme
/tmp/oh-my-zsh-powerline-theme/oh-my-zsh-powerline-theme/install_in_omz.sh
```

## vim
其實我也不是用vim-powerline
而是vim-airline
不過基本上好像是差不多的東西，而且vim-airline比較輕量化
建議直接用vundle 這類的套件管理安裝比較方便

https://github.com/bling/vim-airline

## tmux
tmux有非常多的東西可以客製化設定
在各系統也有不同的安裝方式，就自己看repo的readme文件吧XD

https://github.com/erikw/tmux-powerline