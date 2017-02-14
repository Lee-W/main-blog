---
Title: 在mac上安裝gcc
Date: 2016-01-06 06:40
Category: Article
Tags: 
Slug: install-gcc-on-mac
Authors: Lee-W
Summary: 
---

最近用brew來安裝gcc 5.3，一直卡在`make --bootstrap`
放了幾個小時還是停在這

<!--more-->

之後才查到，要用xcode的命令來安裝
`xcode-select --install`

主要是因為homebrew下載的是還沒compile過的版本
而compile gcc需要非常長的時間
根據Reference中的文章，至少要超過45分鐘 (雖然我放了一天還是沒好)

# Reference
- [brew install gcc too time consuming](http://stackoverflow.com/questions/24966404/brew-install-gcc-too-time-consuming)
- [brew install gcc /Mac OS 10.9 Mavericks](http://superuser.com/questions/788256/brew-install-gcc-mac-os-10-9-mavericks)