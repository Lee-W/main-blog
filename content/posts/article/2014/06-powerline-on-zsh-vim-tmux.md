Title: powerline on zsh, vim, tmux
Date: 2014-07-30 15:01
Category: Tech
Tags: Linux-Unix, Utility
Slug: powerline-on-zsh-vim-tmux
Authors: Lee-W
Summary:

用了 vim 的 powerline 後覺得很酷，就找了很多的 powerline 來玩
於是這篇文章產生了 XDD

<!--more-->

這是各個 powerline 的預覽圖

1. vim  
  ![1_vim]({static}/images/posts-image/2014-07-30-powerline-on-zsh-vim-tmux/VTM4866.png)
2. tmux  
  ![2_tmux]({static}/images/posts-image/2014-07-30-powerline-on-zsh-vim-tmux/LLJ9xjk.png)
3. zsh  
  ![3_zsh]({static}/images/posts-image/2014-07-30-powerline-on-zsh-vim-tmux/tOvzhK3.png)

## powerline 字體

安裝這些 powerline 之前要先下載 powerline 字體
不然可能會無法正常顯示
在 [powerline-fonts](https://github.com/Lokaltog/powerline-fonts) 下載後，之後安裝就完成了
*記得要把終端機的字體條成這些有 powerline 結尾的字體，我當初就是沒用這個卡了很久 = =*

```shell
git clone https://github.com/Lokaltog/powerline-fonts /tmp/git/clone
sudo mv /tmp/git-clone/powerline-fonts /usr/share/fonts/powerline-fonts
sudo fc-cache -v -f
```

## zsh

其實 oh-my-zsh 本身就有 agnoster 了
但我更推薦 [oh-my-zsh-powerline-theme](https://github.com/jeremyFreeAgent/oh-my-zsh-powerline-theme)
安裝完之後記得再 zshrc 中加入
> ZSH_THEME="powerline"

如果要更多客制化設定可以參考 repo 內的設定

```shell
git clone https://github.com/jeremyFreeAgent/oh-my-zsh-powerline-theme /tmp/oh-my-zsh-powerline-theme
/tmp/oh-my-zsh-powerline-theme/oh-my-zsh-powerline-theme/install_in_omz.sh
```

## vim

其實我也不是用 vim-powerline
而是 vim-airline
不過基本上好像是差不多的東西，而且 vim-airline 比較輕量化
建議直接用 vundle 這類的套件管理安裝比較方便

[vim-airline](https://github.com/bling/vim-airline)

## tmux

tmux 有非常多的東西可以客製化設定
在各系統也有不同的安裝方式，就自己看 repo 的 readme 文件吧 XD

[tmux-powerline](https://github.com/erikw/tmux-powerline)
