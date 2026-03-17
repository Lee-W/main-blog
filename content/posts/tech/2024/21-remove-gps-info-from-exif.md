Title: 移除照片 Exif 中的 GPSInfo
Subtitle: 氣息遮斷 A+
Date: 2024-11-03 10:40 +0800
Category: Tech
Tags: Python, Blog, Pre-commit
Slug: remove-gps-info-from-exif
Authors: Wei Lee

最近聽了 Podcast [What's on Django TV tonight?][pythonbytes] 跟 [Pre-commit Hooks for Python Devs][talkpython]
發現了 [exif-stripper][exif-stripper] 這個酷東西

<!--more-->

而且開發者竟然是今年有來 PyCon TW 的 Stefanie ⁉️
在 PyCon JP 的會後會也有稍微跟她聊到一下天

另外還要感謝 Stefanie 在 [節目中][talkpython] 有提到邊緣專案 [commitizen][commitizen]
她應該沒想到 PyCon TW 的 Development Sprint 坐她後面的就是 [commitizen][commitizen] 的維護者吧 😆
雖然那次我是帶 [airflow][airflow] 就是了

## 進入正題
Exif 是什麼？
簡單來說它是照片中儲存 metadata 的格式
除了照片本身外，照片的檔案通常很多的 metadata
裡面可能會記錄在什麼時候拍的，用什麼裝置拍的
最重要的是拍攝的地點在哪 （也就是標題提到的 GPSInfo）
洩漏 GPS 資訊到網路上就有可能讓有心人士抓到你的行蹤
Stefanie 也寫了 [Mind Your Image Metadata][Mind Your Image Metadata] 解釋為什麼這件事很重要

我對這件事一直都稍微有些注意
在匯出照片放上部落格的時候，都會確定我沒有選到 `Location Information`

![export-location](/images/posts-image/2024-remove-gps-info-from-exif/export-location.jpg)

我一直有在想應該要寫個工具自動確認並清除
如果有 pre-commit hook 就更好了
但我就爛，一直懶惰遲遲沒有動手
直到找到 [exif-stripper][exif-stripper]

不過 [exif-stripper][exif-stripper] 會把整個 [Exif 都清掉][exifclear]
我覺得其他東西留著也還好
再加上當初在我的部落格引入 [exif-stripper][exif-stripper] 的時候
可能哪裡設定錯了，圖片會一直被 pre-commit hook 修改，導致 pre-commit 的檢查永遠不會過
為了寫這篇文章，後來追了[原始碼][exifcheck]，看起來是不該發生啊 🤔
真的不知道當初怎麼了

不過我已經寫完自己的版本了，所以就想說算了

```python
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "pillow>=11.0.0",
# ]
# ///
from collections.abc import Sequence
import glob
import os

from PIL.Image import UnidentifiedImageError, open as pil_open
from PIL.ExifTags import Base as ExifBase


def get_exif_tag_ids_by_names(names: Sequence[str]) -> set[int]:
    return {getattr(ExifBase, name).value for name in names}


filenames = [path for path in glob.glob("content/images/**", recursive=True) if os.path.isfile(path)]
exif_tags_to_remove = ["GPSInfo"]
for name in filenames:
    try:
        with pil_open(name) as im:
            tag_ids = get_exif_tag_ids_by_names(exif_tags_to_remove)
            for tag_id in tag_ids:
                if im.getexif().get(tag_id) and im._exif:
                    im._exif[tag_id] = None
    except (FileNotFoundError, UnidentifiedImageError):
        continue
```

這個簡短的 script 有遵守 [PEP 723][PEP 723] 寫好相依套件
所以可以用 [uv][uv] 直接跑
跟 [exif-stripper][exif-stripper] 最大的不同是我只有指定要清除掉 GPSInfo
雖然目前要清除的 Exif tag 跟檔案路徑是寫死的
但邏輯本身應該是蠻彈性的
之後有時間可以把它貢獻回 [exif-stripper][exif-stripper]
目前我只有先把它加到我自己的部落格而已 [Add task to remove gps from exif #39](https://github.com/Lee-W/main-blog/pull/39)

為了想要只刪除 GPSInfo 我回去追了 [Pillow][Pillow] 原始碼
發現 class [Exif][Exif-class] 本身繼承了 [MutableMapping][MutableMapping]
運作起來會有點像是 `dict`
所以它的 `clear` 並非 [Pillow][Pillow] 實作要去刪除哪些 Exif 的 tag
而是繼承了 MutableMapping 的 [clear][clear] 把所有資料刪掉

```python
def clear(self):
    "D.clear() -> None.  Remove all items from D."
    try:
        while True:
            self.popitem()
    except KeyError:
        pass
```

呼叫到的 `popitem` 則是透過 [Pillow][Pillow] 實作的 [`__iter__`][pillow-image-4194] 跟 [`__getitem__`][pillow-image-4174] 決定要移除的資料

```python
def popitem(self):
    """D.popitem() -> (k, v), remove and return some (key, value) pair
    as a 2-tuple; but raise KeyError if D is empty.
    """
    try:
        key = next(iter(self))
    except StopIteration:
        raise KeyError from None
    value = self[key]
    del self[key]
    return key, value
```

為什麼追著追著就追回 CPython
窩也不知道

## 氣息遮斷是什麼？
氣息遮斷是 Fate 裡面 Assassin 職階大多具有且等級較高的能力
顧名思義就是一種消除氣息讓自己好進行暗殺的能力
當然邊緣人如我也是自帶這種消除存在感的能力
但我沒有要參加聖杯戰爭，所以也沒什麼用

![Assassin](/images/posts-image/2024-remove-gps-info-from-exif/Assassin.jpeg)

不過透過這篇文章學到如何把照片中的 GPS 資訊刪除
避免太常被奇怪的人麥當勞歡樂送，就能得到氣息遮斷 B 的證書哦（並沒有

<!--references-->

[pythonbytes]: https://pythonbytes.fm/episodes/show/406/whats-on-django-tv-tonight
[talkpython]: https://talkpython.fm/episodes/show/482/pre-commit-hooks-for-python-devs
[exif-stripper]: https://github.com/stefmolin/exif-stripper
[exifclear]: https://github.com/stefmolin/exif-stripper/blob/d387c8b3be7b6df4d9ff6da005a1081caadf1476/src/exif_stripper/__init__.py#L32
[exifcheck]: https://github.com/stefmolin/exif-stripper/blob/d387c8b3be7b6df4d9ff6da005a1081caadf1476/src/exif_stripper/__init__.py#L31
[commitizen]: https://github.com/commitizen-tools/commitizen
[airflow]: https://github.com/apache/airflow/
[Mind Your Image Metadata]: https://stefaniemolin.com/articles/devx/pre-commit/exif-stripper/
[PEP 723]: https://peps.python.org/pep-0723/
[uv]: https://docs.astral.sh/uv/guides/scripts/#declaring-script-dependencies
[Pillow]: https://github.com/python-pillow/Pillow
[Exif-class]: https://github.com/python-pillow/Pillow/blob/5771f0ec37b9d503749050b6c38f67addbd5a19d/src/PIL/Image.py#L3865-L3871
[MutableMapping]: https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableMapping
[clear]: https://github.com/python/cpython/blob/2f7793196a8feac9d5ce96ae0a8df0723ef1b044/Lib/_collections_abc.py#L971
[pillow-image-4194]: https://github.com/python-pillow/Pillow/blob/5771f0ec37b9d503749050b6c38f67addbd5a19d/src/PIL/Image.py#L4194
[pillow-image-4174]: https://github.com/python-pillow/Pillow/blob/5771f0ec37b9d503749050b6c38f67addbd5a19d/src/PIL/Image.py#L4174
