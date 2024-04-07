Title: 將終端機畫面紀錄成 gif
Date: 2024-04-07 22:42
Category: Tech
Tags: tool
Slug: record-terminal-actions-and-export-as-gif
Authors: Wei Lee

想說 [commitizen](https://github.com/commitizen-tools/commitizen) README 的 demo 動畫也好久沒更新了
可以來研究一下怎麼產出新的動畫更新上去

![commitizen-demo](/images/posts-image/2024-record-terminal-actions-and-export-as-gif/commitizen-demo.jpg)

<!--more-->

之前做簡報的時候就有用過一次
本文是當時的草稿，躺到現在才下定決心要整理完
記錄一下為了發[這個 PR](https://github.com/commitizen-tools/commitizen/pull/1055/files)所用到的工具 [asciinema](https://github.com/asciinema/asciinema) 跟 [agg](https://github.com/asciinema/agg)

## asciinema
asciinema 是負責進行終端機紀錄的工具，會存成 `.cast` 的格式
可以存在 local 或上傳到 [asciinema.org](https://asciinema.org/)

使用 `asciinema rec` 開始紀錄
要結束錄影時可以按 `<ctrl-d>` 或輸入 `exit`
結束錄影時會詢問要不要存擋，要存在哪

```sh
$ asciinema rec <output path (with extension .cast)>

asciinema: recording asciicast <output path>
asciinema: press <ctrl-d> or type "exit" when you're done


asciinema: recording finished
(s)ave locally, (u)pload to asciinema.org, (d)iscard
[s,u,d]?
```

透過 `asciinema play` 可以在終端機重新播放剛剛的紀錄

```sh
asciinema play <.cast file path>
```

想要一次看完所有內容可以使用

```sh
asciinema cat <.cast file path>
```

## agg
agg 則是 asciinema 組織中的專案，負責產生 gif
（全名是  asciinema gif generator ）
有不少可以客製化的參數
我比較常用的是 `--font-family`, `--speed`, `--no-loop`
分別可以設定字體、播放速度跟是否要讓 gif 重播

```sh
agg --font-family "ComicShannsMono Nerd Font" \
    --speed 2.5 \
    <input cast path> <output gif path>
```

## Let's put everything together
既然是分享 asciinema 的文章
當然是得把文章用到的指令們直接做成 gif demo 吧！

![asciinema](/images/posts-image/2024-record-terminal-actions-and-export-as-gif/asciinema.gif)
