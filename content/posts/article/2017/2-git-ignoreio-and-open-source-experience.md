Title: git ignore-io 與 開源貢獻經驗
Date: 2017-02-28 21:56
Category: Tech
Tags: Open Source
Slug: git-ignoreio-and-open-source-experience
Authors: Lee-W
Summary:


雖然已經隔了一年多
當初 git ignore-io 這個小功能，也是花了一兩個月
好不容易才[git extras](https://github.com/tj/git-extras) merge 回去的

<!--more-->

當初看到這封信的時候，很是感動啊 xd
![accepted]({filename}/images/posts-image/2017-02-28-git-ignoreio-and-open-source-experience/1-accepted.jpg)

## git ignore-io
這個工具主要是從[gitignoore.io](https://www.gitignore.io) 上下載 .gitignore 的範本
e.g. 
```bash
git ignore-io -a vim osx python
```

像這就是 vim 常見的暫存檔們
一般來說應該被忽略掉，不用被 commit

```
# Created by https://www.gitignore.io/api/vim

### Vim ###
# swap
[._]*.s[a-v][a-z]
[._]*.sw[a-p]
[._]s[a-v][a-z]
[._]sw[a-p]
# session
Session.vim
# temporary
.netrwhist
*~
# auto-generated tag files
tags

# End of https://www.gitignore.io/api/vim
```


---
當初可是連文件都要寫好，才會被作者接受
所以我這裡就直接沿用我當初寫的文件了 xd

Without option, `git ignore-io <type>` shows the sample gitignore of specified types on screen.  

```bash
$ git ignore-io vim

    # Created by https://www.gitignore.io/api/vim

    ### Vim ###
    [._]*.s[a-w][a-z]
    [._]s[a-w][a-z]
    *.un~
    Session.vim
    .netrwhist
    *~
```

To export it to `.gitignore` file you can use the following options:  

* `-a` or `--append` to append the result to `.gitignore`
* `-r` or `--replace` to export `.gitignore` with the result

```bash
$ git ignore-io vim python
```

For efficiency, `git ignore-io` store all available types at `~/.gi_list`.  
To list all the available types:

* `-l` or `-L` : These two options will show the list in different format. Just try it.

You can also search type from the list by:

* `-s <word>` or `--search <word>`

```bash
$ git ignore-io -s ja

    django
    jabref
    java
    ninja
```

---

## 為什麼要貢獻開源專案？
貢獻開源專案最主要的原因
還是就是**我需要這個功能啊！！！**
但是就沒有人寫，bug 沒有人修
所以就只好先承認自己就是「沒有人」了 xd

其實 gitignore.io 本身就有提供一個簡單的 script [gi](https://www.gitignore.io/docs#-install-command-line)
不過實在有點不夠我用 xd
於是我就寫了[gi_extension](https://github.com/Lee-W/gi_extension)
後來又覺得，如果整併的 git extras
我就能透過 homebrew 安裝了 (?????

整個從 pull request 到 merge 的過程其實蠻有趣的
我找到當初我開的[pr #439](https://github.com/tj/git-extras/pull/439) 和[pr #448](https://github.com/tj/git-extras/pull/448)
從 shell script 的風格（有人建議我用[shellcheck](https://github.com/koalaman/shellcheck)）到 command 的 option 為什麼要這樣命名
都有人跟我討論，給我建議
從中也學到了很多
<s> 貢獻這些專案還能去申請 SITCON 跟 COSCUP 的開源貢獻票，這樣就不用跟大家搶票了 </s>