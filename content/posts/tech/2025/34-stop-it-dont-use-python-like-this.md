Title: 住手啊，這樣用 Python 寫程式沒有人會獲得幸福的
Subtitle: 小林寫得很好，學學小林
Date: 2025-08-06 23:27
Category: Tech
Tags: Anime, Python
Slug: stop-it-dont-use-python-like-this
Authors: Wei Lee

內有[九龍大眾浪漫]暴雷，請小心服用
倒是最近意外發現原來漫畫還在連載中
好久沒看到被動畫先結束的作品了

<!--more-->

動畫結尾的味道跟愛在雨過天晴時有那麼一點點像
讓我覺得好像蠻自然的
不過兩部比起來，我還是更喜歡愛在雨過天晴時多了不少
愛在雨過天晴時真的是一部很美的作品
但九龍大眾浪漫的鋪成真的是相當相當的有趣

---

說了這麼多應該防雷防夠了
有看動畫大概都猜到我要說什麼了
就是動畫第 11 集
鼬瓏打算透過這段程式碼關掉地球子星

![Python Code](/images/posts-image/2025-stop-it-dont-use-python-like-this/python-code.jpg)

為了跟上 AI 的時代，我也跟隨潮流問了一下 ChatGPT 確認這是哪個程式語言
果然是我稍微懂一點點，但不太多的 Python
既然是 ChatGPT 說的，那肯定不會錯吧
你不會騙我吧， ChatGPT，現代人最相信你了

![ChatGPT](/images/posts-image/2025-stop-it-dont-use-python-like-this/chatgpt.jpg)

## 程式碼本體

```python
print("Hello, World!")
# Imaginary Code to delete a specific program


def delete_program(program_name):
    try:
        # Check if the program exists
        if program_exists(program_name):
            # Perform the deletion of the program
            delete_file(program_name)
            print(f"The program '{program_name}' has been successfully deleted.")
        else:
            print(f"The program '{program_name}' does not exist.")
    except Exception as e:
        print(f"An error occurred while deleting the program: {str(e)}")


def program_exists(program_name):
    # Here we simulate checking if the program exists in the system
    # In reality, this would check the filesystem or registry
    return program_name in ["program1", "program2", "program3"]  # Example programs


def delete_file(program_name):
    # Simulate the file deletion
    print(f"Deleting program: {program_name}...")


# Example usage
```

## 閱讀程式碼

來看看這段程式碼是實際上在幹麻

1. 印出 "Hello, World!" *（不是...為什麼...）*
2. 定義 `delete_program` 函式
    1. 確認程式是否存在
        1. 如果存在，嘗試刪除它，印出檔案已刪除的訊息
        2. 如果不存在，印出檔案不存在的訊息
    2. 如果刪除的期間發生例外事件，則印出警告訊息 *(TP 表示 `{str(e)}` 到底是誰教的)*
3. 定義 `program_exists` 函式
    1. 程式名稱是否為 "program1", "program2", "program3" 之一
4. 定義 `delete_file` 函式
    1. 印出刪除檔案的訊息

![can't delete](/images/posts-image/2025-stop-it-dont-use-python-like-this/cannot-delete.jpg)

> 丟臉死了，根本不敢說出去
> 不管下了幾次停止命令，都沒有反應

自己打造的東西刪除不了應該不是什麼太奇怪的事
隨便都可以刪的話，公司的權限也設的太隨意

先不說裡面所有的邏輯都只有印出訊息
照劇情看來，問題比較像是正在執行中的程式沒有回應
把程式碼本身刪掉應該也是沒用
還是它支援熱插拔，但生產環境的程式不會這樣吧...

後面說要下停止命令倒是比較合理一點
假設主機就是遠在天上的地球子星
看來是想 ssh （或其他方式）連進去，然後輸入的指令無效
但看到這段程式碼，我開始懷疑輸入的指令會不會也是錯的...

還是去學學小林吧，小林比較會用 Python 寫程式
👉 [小林的程式會不會遇到 SQL Injection]({filename}/posts/tech/2020/17-will-kobayashi-s-code-encounter-sql-injection.md))

## 參考作品
* [九龍大眾浪漫]

[九龍大眾浪漫]: https://ani.gamer.com.tw/animeVideo.php?sn=42909
