Title: 讓照片自動分類的腳本
Subtitle: 我明明一直知道照片的數量很多，為什麼沒有想過早一點整理呢。
Date: 2025-06-06 23:15
Category: Tech
Tags: Python
Slug: script-to-organize-photo
Authors: Wei Lee
Cover: /images/posts-image/2025-script-to-organize-photo/Frieren.jpeg

這篇文章想記錄下我分類照片的腳本
但一直想不到有趣的標題
原本想放棄時後才發現，這直白的標題...

<!--more-->

不就跟芙莉蓮內的魔法很像嗎！
所以才想到了這個副標題，並且附上了四月初的芙莉蓮快閃店
而且也符合現實
需要整理的照片，最早可以回朔到兩年前的...
所以我也開始接受了「恩...照片就是整理不完了吧...」

## 怎麼突然要整理照片了呢

最近源來適你有個有趣的活動 - 《工程師的搜尋紀錄》
前幾場有講到火鳳燎原、奇幻文學跟活俠傳
雖然都不太熟，但每一場都超有趣的！

想說也可以來分享些什麼，就決定分享「朝聖之路」
（也因此要從照片堆中翻出相關的照片...）

![you-went-?](/images/posts-image/2025-script-to-organize-photo/you-went.jpg)

我今天把九成的投影片做完了
雖然有點花了太多時間在這件事上...
但我覺得會是一場很好玩的分享！
歡迎下週三 6/11 20:30 (TST) 透過 [這個連結](https://meet.google.com/gyr-szii-eos) 一起來找我聊聊 🙂

## 目標： 要把照片整理成什麼怎樣

G7 拍的照片會分為 jpg 跟 rw2 檔
我希望他們能根據日期以及檔案類型被歸類在不同的資料夾
大致的結構如下

```
.
├── 0101
│   ├── JPG
│   └── RW2
└── 0102
    ├── JPG
    └── RW2
```

## 腳本設計

首先要找出跟拍攝日期相關的 [Exif](https://zh.wikipedia.org/zh-tw/Exif)
其中包含

* 306 DateTime
* 36867 DateTimeOriginal
* 36868 DateTimeDigitized
* 36880 OffsetTime
* 36881 OffsetTimeOriginal
* 36882 OffsetTimeDigitized

雖然最後發現，照片們都只有 `306 DateTime`...

上次已經有了用 [Pillow](https://pypi.org/project/pillow/) 寫腳本刪除部落格照片 Exif 標籤的經驗

這次只要

1. 讀完 Exif 標籤
2. 建立資料夾
3. 再將相對應的照片放進

輕鬆愜意就能解決了

沒想到整理到 RW2 檔的時候， Pillow 告訴我

![daga-kotowaru](/images/meme/jojo-daga-kotowaru.png)

[Add support of RW2 files #1118](https://github.com/python-pillow/Pillow/issues/1118)

還好後來還是有找到適合的函式庫 [ExifRead](https://pypi.org/project/ExifRead/)

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "ExifRead",
#     "tqdm"
# ]
# ///

import glob
import shutil
from collections import defaultdict
from datetime import datetime
from pathlib import Path

import exifread
from tqdm import tqdm


def build_directory_mapping(root: str = ".") -> dict[str, list[str]]:
    directory_mapping: dict[str, list[str]] = defaultdict(list)
    pbar = tqdm(
        glob.glob("**/*", root_dir=root, recursive=True),
        desc="Building directory mapping",
    )
    for filename in pbar:
        file_path = Path(filename)
        if not file_path.is_file():
            continue

        with open(filename, "rb") as file_handle:
            exif = exifread.process_file(file_handle, details=False, extract_thumbnail=False, strict=True)
            if exif:
                datetime_str = exif["EXIF DateTimeOriginal"].values
                created_time = datetime.strptime(datetime_str, "%Y:%m:%d %H:%M:%S")

                created_year: str = str(created_time.year)
                created_date: str = created_time.strftime("%m%d")
                file_ext: str = file_path.suffix

                directory_name = f"{created_time.year}/{created_date}/{file_path.suffix[1:]}"
                directory_mapping[directory_name].append(filename)
            else:
                tqdm.write(f"Cannot get exif from {filename}")
        pbar.set_description(f"Processing {filename}")

    return directory_mapping


if __name__ == "__main__":
    directory_mapping = build_directory_mapping()

    tqdm.write("-" * 10)

    pbar = tqdm(directory_mapping.items(), leave=False)
    for directory_name, images in pbar:
        directory = Path(directory_name)
        directory.mkdir(parents=True, exist_ok=True)
        pbar.set_description(f"Directory '{directory_name}' created")

        for image in tqdm(images, leave=False):
            pbar.set_description(f"Moving {image}")
            shutil.move(image, directory)
```

再來只要輸入指令

```sh
uv run --script photo_organizer.py
```

就能讓照片被分類進對應的資料夾

---

什麼？你說上面那串酷酷的註解是什麼
那是 uv 根據 [PEP 723](https://peps.python.org/pep-0723/) 所實作的功能
讓使用者讀取了腳本的 metadata 後，自動去安裝需要的套件後執行腳本
👉 [uv - Running scripts](https://docs.astral.sh/uv/guides/scripts/#running-scripts)

---

結束後，照片就整理完了對吧！
對吧...

沒有，這只是個開始
再來還得花時間看完照片們，看哪些要留些不要留
畢竟[少，但是更好]({filename}/posts/book/2016/05-essentialism.md)
我已經接受照片是整理不完的事實了 🤷‍♂️
