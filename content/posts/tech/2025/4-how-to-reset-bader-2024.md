Title: 重設 Badger 2040
Subtitle: 客製化自己的電子識別證！
Date: 2025-02-12 23:35
Category: Tech
Tags: Hardware
Slug: how-to-reset-bader-2024
Authors: Wei Lee
Cover: /images/posts-image/2025-badger-2040/badger-2040.jpeg

前年去 PyCon APAC 抽到酷酷的 Badger 2040
可以當時鐘、當電子書（但應該是沒人會這樣用啦...）
最重要的是可以客製化寫入自己的識別證！
但它重設起來有點麻煩...

<!--more-->

去年出差的時候，有遇到手上也有一片的同事
它也是說每次要重寫就會斷線...

但是啊，只要帶著它出去參加研討會
就會有人來問「這是什麼」就能開起話提
實在是 I 人在必須社交的 SSR 禮裝

上週 FF 為了避免大家把我認成鏈鋸人的マキマ
我還特別把小林的資訊寫進去
恩...但我後來沒有拿出來...

![badger 2040](/images/posts-image/2025-badger-2040/badger-2040.jpeg)


## 如何重設
進入正題，其實一切都寫在 [badger2040] 這個 repo 的 README 中了

1. 到 [badger2040] 下載最新的韌體更新 (e.g., `pimoroni-badger2040-v0.0.5-micropython-with-badger-os.uf2`)
2. 透過 USB 將 Badger 2040 的板子連接到電腦
3. 長按 Badger 2040 背後的 `BOOT/USR` 鍵，並按下 `RESET` 鍵，這時電腦應該會連接到板子
4. 以 macOS 為例，把最新的韌體拉近連接到的裝置，它會重設整台裝置
6. 接下來就可以跟著 [Badger 2040 W] 的教學步驟，把識別證的內容寫進去了

[badger2040]: https://github.com/pimoroni/badger2040
[Badger 2040 W]: https://developer.auth0.com/resources/labs/events/badger-2040-w#troubleshooting

## Gotchas

* **不要妄想寫過一次，Badger 2040 能再連得到，直接整台重設吧**
* 應該不支援 ASCII 以外的字元，至少之前測試中文跟日文都無效
* [digital-badges-bundle] 的 [upload_these] 指的是上傳這個資料夾的東西，不是上傳這個資料夾
* [badges/badge.txt] 只能 7 行，就算只是多了 EOF ， badge 2040 還是會直接 error
    * 雖然 vim 好，vim 棒，但這次不要用 vim 補上 EOF

[digital-badges-bundle]: https://github.com/auth0-developer-hub/digital-badges-bundle
[upload_these]: https://github.com/auth0-developer-hub/digital-badges-bundle/tree/main/badger2040wifi/upload_these
[badges/badge.txt]: https://github.com/auth0-developer-hub/digital-badges-bundle/blob/main/badger2040wifi/upload_these/badges/badge.txt
