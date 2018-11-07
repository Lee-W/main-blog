Title: Common Neovim Problems
Date: 2017-05-14 13:13
Category: Tech
Tags: Vim, Neovim
Slug: common-neovim-problems
Authors: Lee-W
Summary: 

<!--more-->

## Load ~/.vimrc from neovim

```sh
mkdir -p ${XDG_CONFIG_HOME:=$HOME/.config}
ln -s ~/.vim $XDG_CONFIG_HOME/nvim
ln -s ~/.vimrc $XDG_CONFIG_HOME/nvim/init.vim
```

## No python interpreter found.

```sh
pip install neovim
```


# Reference
- [.nvimrc doesn't seem to be loaded up or working and it cannot create backups on editing existing files](https://github.com/neovim/neovim/issues/3536)
- [No python interpreter found.](https://github.com/neovim/neovim/issues/1755)