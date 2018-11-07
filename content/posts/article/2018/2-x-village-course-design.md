Title: X-Village 課程設計
Date: 2018-09-24 15:15
Category: Gossiping
Tags: X-Village
Slug: X-Village-Course-Design
Authors: Lee-W
Summary: 
Series: X-Village

要一次說完整個 X-Village ，還是有點太花時間
先來聊聊我這次接觸到跟課程設計有關的部分

<!--more-->

我在 X-Village 中，主要的工作還是在規劃、管理跟行政的部分
所以我要上的課也不多
跟課程相關，我接觸比較多的大概是這幾個部分

1.  Review 「程式設計基石」(a.k.a. Python 課)
2. 「資料結構」第三天下午的練習
3. 「網頁開發、資料庫、雲端運算」第三天後半課程

## 1. Review 「程式設計基石」

### 課綱
起初，我和另一位核心助教規劃了 Python 課程的大綱
但這份課綱對初學者還是太難
因為身上處理的事在太多
這些工作就逐步派給其他助教

過了一週後，我們得到了一份更難了很多的課綱 xD
畢竟大家沒有太多的教學經驗
一開始就要設計好一份適當的課綱，本來就很困難
而且初期 Target Audience 一直不太明確
造成課程難度很難抓

陸續討論了幾週後，這就是我們正式課程前的版本

| | Topics |
|---|---|
| Day 1 | <ul> <li>Opening</li> <li>Python Intro</li> <li>Editor</li> <li>Git</li> </ul>|
| Day 2 | <ul> <li>HackMD</li> <li> 淺談電腦基本運作 </li> <li> 如何自己解決問題？ (Google, Stack Overflow)</li> <li> Python Basic(I) (Synyax, Data Types)</li> </ul>|
| Day 3 | <ul> <li>Function</li> <li>Module/Package</li> <li>Class</li> </ul>|
| Day 4 | <ul> <li>OOP Introduciton</li> </ul> |
| Day 5 | <ul> <li>Exception Handling</li> <li>File</li> <li>String</li> <li>Coding Convention</li> </ul>|
| Day 6 | <ul> <li>Recap</li> <li>Built-in</li> <ul/>|
| Day 7 | <ul> <li>Regular Expression</li> <li>Python 套件管理 </li> <li>[requests](http://docs.python-requests.org/en/master/)</li>|
| Day 8 | <ul> <li>[Beautifulsoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)</li> <li>Visualization</li> </ul> |
| Day 9 | <ul> <li>Decorator</li> <li>Iterator</li> <li>Generator</li> <li>Context Manager</li> </ul>|
| Day 10 | <ul> <li>Broaden Horizon</li> </ul> |

### Rehearsal
Rehearsal 的時候，我看到了蠻多值得學習跟反省的地方
不愧是從醒獅團的人們，我看到了一些很有趣的教學方式
看著每個人不同的教學風格和內容
我在思考著
是不是有些人在以往學習程式上比較順利，比較知道如何自己找到解學辦法？
對這樣的人來說，要如何把知識傳遞給學習不那麼快的人，就會需要比較多的學習

回想起我寫程式的歷程，可是一點都不順利
我在寫 Lisp 的時候，連 Syntax Highlight 都不懂
還要不斷數括號數量，才知道程式能不能跑的

e.g., 
```
(cond ((eq 'a 'b) 'first)  (atom 'a)  'second))
```
（其實上面有少一個括號 xD）

### 課程正式開始
課程的前兩週因為在準備碩士論文口試
我沒有投入教學，也沒辦法整天跟課
但我中午跟晚上幾乎都會去 ~~拿便當、飲料~~ 關心課程狀況

課程開始後，我們要不斷看大家的狀況跟課後的回饋來調整課程的進度
因為這是密集課程
所謂的調整課程就是「今天馬上要改完，明天馬上就要上場」
而且助教們晚上也會留下來陪學員晚自習
造成大家幾乎是沒什麼休息的時間

因為第一次辦，完全無法預期大家的學習速度
只能先用一個版本出來教教看
再來看現場狀況隨時調整
不過有了這次的經驗，明年應該就比較有底了（如果還有明年的話 xD）

## 2. 「資料結構」第三天下午的練習
* Exercise ipynb: [DS-Exercise Day3](http://nbviewer.jupyter.org/github/x-village/data-structure-course/blob/master/DS_Exercise_Day3.ipynb)

雖然先前大概有稍微想了一下準備怎樣的 Exercise
但我前一天下午才口試完
我其實只有大概一個晚上的時間準備 ...

可是「資料結構」的老師又是我找的
總覺得還是得要負起一些責任

早上的課程會由老師教理論，下午由助教來帶一些練習
我帶練習的那天早上則是教排序

在教學上我並沒花多少時間
就是帶了一些影片，讓大家 Recap 一下白天老師教的內容
我主要把時間都花在 Exercise 的設計上

### Exercise4 用 Python 做排序 (ex4.py)
```python
some_list = [
    65, 81, 65, 19, 6, 28, 86, 40, 72, 27,
    76, 46, 22, 98, 49, 57, 52, 46, 47, 14,
    29, 15, 59, 74, 61, 47, 20, 33, 89, 99,
    65, 82, 84, 63, 93, 1, 42, 13, 54, 58,
    84, 17, 5, 18, 14, 14, 19, 42, 60, 77,
    17, 29, 2, 42, 42, 31, 47, 67, 15, 16,
    71, 56, 98, 46, 18, 20, 14, 36, 42, 23,
    87, 7, 5, 5, 52, 78, 76, 91, 92, 88, 38,
    66, 13, 18, 68, 96, 23, 51, 77, 93, 35,
    18, 9, 64, 51, 76, 76, 96, 5, 18
]
```

寫過 Python 的人，一定馬上就會想到用 `sort` 或 `sorted`
但我故意把練習時間拉長到 20 分鐘
中間一直會有學員、助教問我「真的可以這樣寫嗎？」
**恩，可以哦**

在早上教完「資料結構」後，馬上帶這樣的練習
很容易讓人直接聯想到要實作排序演算法
我想帶來的想法是「在要下手去做什麼之前，先找找是不是有什麼現存的工具」

回想以前的我，肯定也是埋頭就下去硬幹
甚至我第一次用 Python 爬選課系統的時候，連 json 模組都不會用
只會照著 json 規定的格式，慢慢地做字串處理
e.g., 

```python
json_str = '{"' + course_name + '": "' + course_id + '"}'
```

因為在我的 Knowledget Base，對函式庫的概念還是很模糊
也不知道為什麼要用，好處在哪
大二下的 C++ 寫的 ncurses 反而感覺像是造成我更多的麻煩 xD
因為我並不知道如果不用 ncurses ，要做同樣的事會多麻煩

所以試試看讓學員真的做一次很麻煩的處理
透過痛過，來知道為什麼要使用工具

### Exercise5 深入淺出 Python 排序 (ex5.md)
* Q1: Python 的 `some_list.sort()` 跟 `sorted(some_list)` 差別在哪
* Q2: Python 的 `sorted()` 是用哪種排序演算法 ?

這兩個問題其實並不困難

* 第一個問題是我以前寫 Python 常遇到的錯誤  
  同時也想讓大家去想想「如果有不同的做法都能解決問題，他們不同的地方在哪」
* 第二個問題則是想激起大家的好奇心，試著去探究看似理所當然的東西

最後 Exercise 4, 5 我幾乎直接把答案都公佈了
即使是在這之後才用我公布的方法，我也是會計分
因為這個思考的過程才是重要的，答案一點也不重要

### Exercise6 用 Python 做排序
我給了一筆 PTT 爬下來的資料，根據某個 key 做排序
早上才從八卦版剛爬下來的（好像有爬到一些奇怪的東西 ...）
靈感就只是前一天跟學員聊天，聊到他們的視覺化作業要用 PTT 的資料

這個練習目的在於用實際的資料
讓大家感受到程式是真的能解決實際的問題
而且並不如想像中的那麼困難

回想我大一不斷的學習用好的架構寫一個 BMI 的程式
總覺得要寫一個稍微有用的程式是非常非常遙遠的事
所以大二下的 C++ ，對我來我說是寫程式很大的里程碑

這題的解答也是差不多一行而已
```python
data = sorted(ptt_data, key=lambda x: x['some_key'])
```

但我認為這對新手來說，已經會是相對挑戰的練習了
至少以初學的我來說，我可能就要花不少時間去 survey 、去思考
 
這個練習中，我還埋了一個坑是「key 可能是空的」
~~我前一天設計這個練習的時候也入坑了，此坑不能只有我入~~
我也會下去跟大家討論要怎麼解決這個問題
這個問題本身有很多種不同的解法
我自己的解法是使用 `filter` 過濾掉空值
但我也遇到學員們有很多不一樣的想法，我覺得挺好的

### Bouns
- Bonus 3 實作各種 sort 作法 
- Bouns 4 分析各種 sort 適合的情境

因為課程的速度放慢，有些學過的就會覺得比較無聊
這兩個 Bouns 就是設計給這樣的人
至少在這的兩個小時不要是浪費時間

Bouns 4 我也沒有正確解答
我蠻好奇會不會有人能給我一點想法的
不過這麼機車的題目最後看來是沒人寫 xD

### 「資料結構」練習後記
後來有一次跟學員聊天的時候
學員跟我分享他覺得這樣的練習設計，帶著大家思考很有幫助
看來前一天沒什麼睡到是值得的

## 3. 「網頁開發、資料庫、雲端運算」第三天後半課程
* Slide: [CRUD in Flask](https://speakerdeck.com/leew/x-village-crud-in-flask-1)
* Sample Code: [web-acccounting-example](https://github.com/x-village/web-acccounting-example/)

前面的課程中有由博安老師指導的 [Database](https://speakerdeck.com/xvillage/cs-foundation-web-5-database)
 跟 [Flask Introduction](https://speakerdeck.com/xvillage/cs-foundation-web-6-flask-introduction)
（博安老師的課程可是在 Web 課程中唯一零負評的，真不愧是博安老師！）
而我的內容則會注重在 view 的撰寫上

我先讓大家對要做的東西有概念 (i.e., 記帳程式 )
在寫程式前，我帶著大家看市面上做出來的記帳程式是長怎樣的？
這些記帳程式有什麼功能？
如果用我們這幾天教的想法，我們要怎麼去思考這個後端的系統？

接著才真正要進入程式
我基於博安老師前一個半小時的程式碼在做延伸
從最原始的 [0.1](https://github.com/x-village/web-acccounting-example/tree/0.1) 版
每次只做一點點的修改，每一個修改都給那個 commit 一個 tag

![tags]({filename}/images/posts-image/2018-09-24-x-village-course-design/1-tag.jpg)

在 slide 的右下角，也會放目前到哪個版本
也希望能從這樣的做法，帶到 frequent commit 的重要

講解程式碼之前
我會先讓大家打過程式碼，並確認可以執行
再來才會解釋每一行程式碼在做什麼
但它們組合起來不見得是對的 xD
尤其剛開始講 view 的 [0.2](https://github.com/x-village/web-acccounting-example/tree/0.2.0) 版更是幾乎沒一個功能是對的
但程式是能跑的
除了聽跟照著做以外
希望能讓大家去發現哪裡有奇怪的地方
試著去想想要怎麼解決這些奇怪的地方

直到 [1.0](https://github.com/x-village/web-acccounting-example/tree/1.0) 版才看起來像是一個可以動的網站
但就算到這裡，還是有一個小錯 xD
我想從這裡帶出測試的重要性

統整一下，我整個課程設計想帶給學員的思考
1. 如何思考一個後端架構 ? → 其他人的記帳程式
2. 溝通在寫程式是很重要的 → `README.md`, `requriements.txt`
3. 如何除錯？ → 滿是錯誤的 view, postman 的使用
4. 為什麼測試是重要的？ → 整個網站雛形都出來了，還有埋錯

整個構想聽起來是很美好
但這次的嘗試，得到的評價不是很好
其中一份回饋告訴我
「他不太喜歡這樣先複製程式碼在學習如何修改的教學方式
  因為一開始看不懂程式碼，只能照著我說的改，會很不知道自己在改什麼」
很感謝願意給我建設性回饋的學員

我也在思考
到底是這樣的方式不適合初學者？
還是我沒有把這樣的內容表達好？
如果還有下次的機會
除了思考課程的內容外，我還要多花點時間準備在台上的表達