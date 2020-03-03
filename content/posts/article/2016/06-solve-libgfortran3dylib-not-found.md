Title: 解決更新 gcc 找不到 libgfortran.3.dylib (Octave,R)
Date: 2016-06-11 03:13
Category: Tech
Tags: R, mac
Slug: solve-libgfortran3dylib-not-found
Authors: Lee-W

最近在 mac 上更新了 gcc 6 後，不管是開 Octave 還是 R
都會出現以下的錯誤訊息

```sh
dyld: Library not loaded: /usr/local/lib/gcc/5/libgfortran.3.dylib
  Referenced from: /usr/local/Cellar/r/3.3.0/R.framework/Versions/3.2/Resources/lib/libR.dylib
  Reason: image not found
Trace/BPT trap: 5
```
<!--more-->

這是因為原本的 lib 會去找 /usr/local/lib/gcc/5/ 下的 lib
但是更新過後已經被變成 /usr/local/lib/gcc/6/ 了
所以只要從 `/usr/local/lib/gcc/5/` 建立 soft link 到 `/usr/local/lib/gcc/6/` 即可
( 版本號則要根據自身 gcc 的版本來做修改 )

```shell
ln -s /usr/local/lib/gcc/5/ /usr/local/lib/gcc/6/
```

## Reference

* [R and julia won't start after upgrade (perhaps gcc 5.1, Xcode 6.3.2, or Command Line Tools 6.3)](https://github.com/Homebrew/legacy-homebrew/issues/39929)
