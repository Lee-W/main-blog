Title: [Book] 所有問題都是一場賽局
Date: 2016-10-15 11:04
Category: Book
Tags: Game Theory
Slug: how-to-think-like-a-game-theorist
Authors: Lee-W
Summary: 


![How to think like a game theorist](http://pic.eslite.com/Upload/Product/201402/m/635279634797871250.jpg)

<!--more-->

## 序章 : 用賽局來思考，培養解決問題的「三種能力」
- 賽局理論 : 分析兩人以上的玩家，其決策和行動的理論
- 學賽局理論的目的
    1. 掌握賽局的整體樣貌 （對問題的分析能力）
    2. 預測即將發生的未來
    3. 找到適當的解決方法
- 贏不了的賽局，就改變規則吧
    - e.g. 減少排放二氧化碳有損國家經濟，所有國家都不願意，然而破壞環境卻對大家都是不好的
        - → 獎勵二氧化碳排放少的國家，讓二氧化碳變成對經濟有利

## Ch1: 合理的下一步是 ......? 「囚犯賽局」與「合理的豬」

### 囚犯賽局
相信接觸過賽局理論的人，一定會聽過囚犯賽局

```
假設今天有兩個囚犯 A 和 B，他們被分開訊問，並且知道
如果都不認罪的話，兩個人都會被關一年
都認罪的話，兩個人都會被關兩年
但是要是一方認罪，另一方不認罪的話，則認罪方無罪釋放，不認罪方要關三年
```
將上述狀況畫成表格就會像下面這樣
( 每一格左邊的數字代表左邊參與者的獲益，右邊的數字代表上面參與者的獲益 )

||B 認罪 |B 沈默 |
|---|---|---|
|A 認罪 |-2, -2|0, -3|
|A 沈默 |0, -3|-1, -1|


在考量了對方所會做的最佳選擇後，所做的最佳選擇就會導向 A 和 B 都認罪
然而對他們來說共同的最大利益，卻是都保持沈默

最後導向的這個點就是所謂的奈許均衡 (Nash Equilibrium)

## Ch2: 協調賽局 - 為何你拿蘋果、用微軟

參加賽局的玩家，透過協調讓雙方得到利益

### 協調賽局
```
以朋友出去玩作為案例
假設 A, B 有音樂劇和電影兩個方案
兩人一起去看音樂劇，滿足度是 10
一起去看電影是 9
分開去的兩種結果，雙方滿意度都是 0
```

||B 音樂劇 |B 電影 |
|---|---|---|
|A 音樂劇 |10, 10| 0, 0|
|A 電影 |0, 0| 9, 9|

此時的奈許均衡有兩個，就是雙方選擇同樣行動的兩個點

這時候只要有一方先做了選擇，則另一方就會趨向於**一樣的選擇**
協調賽局的根本就是「和大家一樣」

#### 協調的失敗
協調賽局中，有多個奈許均衡點
但最後仍有可能落在對大家都不利的均衡點上 (e.g. 以上面的例子來說就是看電影 )
而且協調賽局具有「穩定了就很難改變」的性質
所以陷入這個不好的平衡點是相當危險的

- 實際案例
    - 病態的過度加班 （有人加班，其他人不敢走）

## Ch3: 知彼知己，百戰不殆 - 三種賽局，搞懂你的對手

### 膽小鬼賽局
```
假設兩人各開一台車，朝向牆壁全速前進
看誰能不採煞車前，到離牆最近的地方 → 先踩剎車的人就輸了
```
||B 踩剎車 |B 不踩煞車 |
|---|---|---|
|A 踩煞車 |0, 0| -5, 5|
|A 不踩剎車 |5, -5| -20, -20|

- 奈許均衡有兩個
    -  對方先踩剎車，則自己不踩
    -  對方不踩剎車，則自己先踩

- 實際案例
    - 古巴危機
        - 美國要蘇聯撤除軍備，蘇聯要美國認同蘇聯裝設核子飛彈
        - 如果都不讓步，就會爆發核子戰爭
        - 不存在都讓步的情況
    - 誰都不願意做的事，為什麼有人做
      
- 膽小鬼賽局雖然是決定誰是膽小鬼的賽局，但不要只是讚賞勝利者
    - 犧牲自己成為膽小鬼的那一方也應該獲得注目

### 猜銅板賽局
```
某個城市中，有警察和小偷
警察的選擇是「巡邏」和「偷懶」
小偷則是「進入偷竊」和「不進入」
```
|| 小偷進入偷竊 | 小偷不進入 |
|---|---|---|
| 警察巡邏 |1, -1| -1, 0|
| 警察不巡邏 |1, 1|0, 0|

**這樣的賽局並不存在奈許均衡**

- 如果改變規則，則賽局構造也會改變
    - e.g. 增加警察抓到小偷的利益，或沒抓到的懲罰 

### 霍特琳賽局
```
某片沙灘上，A, B 兩家冰淇淋店都想開店
沙灘約 100m，遊客也均勻分散
那兩家店的老闆會在哪開店呢
左右兩邊是海，一個 - 代表離沙灘 10m

1.

         A B
|- - - - - - - - - - -|

左邊的 50m 都是 A 的範圍，反之亦然
但所有顧客都要走 50m

2. 
     A           B
|- - - - - - - - - - -|
對顧客最方便，因為對顧客來說最遠也不過就走 30m
```

最後的奈許平衡會是 1，即使 2 才是最好的結果
然而當 A 想要設店在離海 30m 的地方的時候
B 就會像把店往左移，如此就能吸引到更大範圍的顧客

- 實際案例
    - 日本拉麵店都集中在車站


## Ch4: 動態賽局 - 時間，可以解決問題
- 動態賽局並不是一個特定賽局，而是一種統稱
    - 隨著時間經過，賽局發展也會產生變化的結構

### 擴散型賽局
```
假設目前城市中已經有一家 A 工廠，B 工廠在考慮是否進入
A 工廠的選項是「戰鬥」和「合作」
B 工廠是「進入」和「不進入」

原本 A 工廠的利益是 3
如果 B 工廠不加入的話，自身利益是 0
如果 B 工廠加入，而 A 工廠選擇合作，則雙方利益為 1
如果 B 工廠加入，A 工廠選擇戰鬥則雙方都是 -1
```

如果用原本的 2x2 表格來做計算
可以發現奈許均衡在「A 戰鬥 Ｘ B 不進入」「A 合作 X B 進入」

||B 進入 |B 不進入 |
|---|---|---|
|A 戰鬥 |-1, -1|3, 0|
|A 合作 |1, 1| 3, 0|


不過「A 戰鬥 X B 不進入」是不會發生的


- 這時候就可以透過「賽局樹」來觀察時間流

```   
                            - 戰鬥 -> (-1, -1)
                    A 工廠
        - 進入 ->     
                            - 合作 -> (1, 1)
B 工廠
        - 不進入 -> (3, 0)
```

這種賽局要使用反向歸納（backward induction），排除「奇怪的奈許均衡」
1. 如果 B 工廠進入，A 工廠就會合作
2. 則「A 戰鬥 X B 進入」可以被排除
3. 再來 B 工廠去比較「A 合作 X B 不進入」和「B 不進入」
4. 就能消除不進入的選項

### 時間矛盾的問題 - 空包彈式的威脅
就前面的 A, B 工廠例子來說
A 工廠進入市場前的最佳行動是戰鬥，所以一定會表現出強硬的姿態
然而 B 工廠一旦進入，A 工廠就會為了利益選擇合作
像這樣 A 工廠的強勢姿態就只是「空包彈」

- 實際案例
    - 不 ... 的話，就會 ...。 然而這樣的情況卻沒發生，久而久之就無效了

#### 解決方案之一 - 創造出必須遵守約定的狀況
- 製藥特許權制度
    - 製藥需要很大的成本，如果沒給予製藥公司製藥成功有販售的特許權
    - 製藥公司就會不願意投入，最後人民會受害
    - 所以這個特許權必須被法定
- 高級品決不降價
    - 一旦降價，就會產生「等一段時間，價格會下降」的想法
    - 以後的物品更不可能用原價把商品賣出 

### 「重複賽局」和「扣板機策略」
回到最一開始的囚犯賽局
如果這個賽局會執行不止一次
最終兩人就會選擇都不認罪的最佳利益

這兩人本來就已經知道最好的選擇是都不認罪
但因為無法抹去「如果對方背叛了 ...」的想法，才會不做出最佳選擇
但是如果「對方背叛我，我就讓他好看」的策略成為可能
就會產生某種信賴關係，讓兩人都導向選擇不認罪

將無限重複的賽局視為大型賽局，而會成為奈許均衡的選項，即是採取合作關係
這稱為「無名氏定理」(folk theorem)
就算是在短期關係中極可能背叛對方的狀況
只要關係變成長期的，就有可能表現出能好好維持合作的關係

## Ch5: 人為什麼無法理性？ - 情感和賽局理論
所有的賽局都是在一個共通條件上成立的 - **玩家只考慮自己的利益，各自做出符合理性的行動**
而這個前提卻是常常不會成立的

### 人能預測未來嗎？ - 蜈蚣賽局
```
爸爸手上有 100 枚硬幣，要分配給 A, B 兩個兒子
但必須遵循以下兩個規定
首先，爸爸會在 A 面前放 1 枚
A 可以選擇「停止」或「繼續」
如果選擇「停止」就結束
選擇「繼續」，則爸爸會從 A 那邊拿起 1 枚 ( 即使後期 A 有不止 1 枚，還是只會拿 1 枚 )
並且再加上手上的 1 枚，2 枚一起給 B
```

這個狀況用反向歸納預測的結果是「A 在第一回合就應該選擇停止」
如此 A 便能獲得比 B 還多的硬幣
但是在實際實驗中，卻沒有人做出了這樣的決定

**人並沒有辦法預測未來**

### 拍賣賽局 - 證明人會從理性到瘋狂
```
與一般拍賣不同
競標成功後，未得標的前一位出價者，需要付他喊出的價錢
而這個東西依然會給得標者
也就是，前一位出價者付了錢卻什麼都拿不到
```
這種賽局一直執行下去，玩家就必須一直往高價喊

- 實際案例
    - 選舉的燒錢比賽
    - 泡沫經濟

***「你沒想清楚後果」確實是個問題，但是你還要考慮的是「其他人沒想清楚後果的可能性」***

### 只用金錢，無法驅動人心
利益並非唯一能影響人心的，往往情感也是

#### 最後通牒賽局
```
A, B 兩位玩家憑空得到 1000 元
由 B 決定分配方式，A 有同意或否決權
A 同意的話則造這個分配方式
A 否決的話就都拿不到錢
只執行一次賽局
```

如果人是理性的，A 即使只拿到 1 元都應該接受
然而實際上這樣的狀況卻幾乎不會發生

#### 獨裁者賽局 (Dicatator game)
跟上面同樣的情境
只是這次 A 沒有任何決定權，只能接受 B 的分配
此時 B 的最佳選擇就是 1000 元全部拿走
然而實驗結果，相當多的人依然會給對方一定程度的金額