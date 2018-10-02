Title: rename - 批次更改檔名
Date: 2015-02-22 15:06
Category: Linux-Unix
Tags: Shell Script
Slug: rename
Authors: Lee-W
Summary: 


只是要改變一兩個檔案的檔名，只要 `mv` 就很夠用了
但如果要一次改很多相似的檔名就用到 `rename` 指令就會更有效率
<!--more-->

# 安裝
### Ubuntu, Linux Mint
預設就已經安裝好了

### Mac
```
brew install rename
```

# 使用
```sh
rename s/pattern1/pattern2/ files
```
把 files 中的檔案符合 pattern1 替代成 pattern2
files 要使用萬用字元，pattern 則是使用 regular expression

在改檔名之前，會想先看會改成什麼樣子
這時候就要加上參數 `-n`

***需要特別注意要跳脫的字元***
可以參考下面這篇文章整理需要跳脫的保留字
[[Regular Expression] 使用正規表達時需要 escape 的保留字](http://awei791129.pixnet.net/blog/post/53319618-%5Bregular-expression%5D-使用正規表達時需要-escape-的 )

## 保留原本檔名的片段
而在批量更改檔名時，常常會需要保留 pattern1 的某些片段
這就需要用到 regular expression 的 group

例如，我們希望把檔名從 01~05 這五個檔案改成 01A~05A
我們如果只用 `rename -n s/\[0-\9]{2}/\[0-9\]{2}A/ *` 就會錯誤
必須要改成像下面這樣
```shell
rename -n s/\(\[0-\9]{2}\)/\$1A/ *
```
扣除跳脫用的 `\`
這個例子在 `[0-9]{2}` 外面加上 `()`，將他們視為群組
在 pattern2 用 `$1`，代替第一個 group

![1_mac_rename](http://i.imgur.com/h1NV6ro.png)

# Reference
- [ubuntu linux 用 rename 指令批次改檔名](http://mix.bruceli.net/2011/01/ubuntu-linuxrename.html)
- [regular expression - Substitute text with sed and keep part of the original text - Unix & Linux Stack Exchange](http://unix.stackexchange.com/questions/20718/substitute-text-with-sed-and-keep-part-of-the-original-text)