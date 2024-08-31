Title: [Note] Clean Code
Date: 2018-11-16 17:08
Modified: 2020-10-08 16:12
Category: Tech
Tags: Note, Software Engineering
Slug: clean-code
Authors: Wei Lee

既然都把 The Clean Coder 做完了
就順便把原本在 GitBook 的 The Clean Code 一起搬過來好了

![clean code](/images/books/clean code.jpg)

<!--more-->

> Lee-W @ 2020-10-08
> 隔了兩年又再回來翻這本書
> 這次除了打算把後面的章節全部看完外，也會重新把筆記順過一次
>
> 第四次把前十章看完後，感到一些原本似懂非懂的概念，變得理所當然
> 但依然會對巧妙的地方感到讚嘆

[TOC]

## 第1章：無暇的程式碼
* LeBlanc's Law: 待會而等於永不
    * 待會兒再回來整理程式，等於讓程式一直限於髒亂
* 髒亂的程式只會讓開發速度更慢。**趕上期限的方法是隨時都確保程式儘可能的乾淨**
* What is Clean Code?
    * 只做好一件事
    * 可以被原作者以外的開發者閱讀與擴充的
    * Beck's rules for simple code
        * 通過所有測試
        * 沒有重複的程式碼
        * 充份表達系統設計的構思
        * 具有最少的 entities (e.g., class, methods, functions, and etc.)
* 每一次修改程式碼之後，都得讓程式碼變得比修改之前再更乾淨
    * 童子軍原則: 每次你到過的營地，離開後要比之前更乾淨

## 第2章：有意義的命名
* Variables, methods, classes 要能解釋他們為什麼在這、做什麼用和怎麼使用它
* 變數名稱要唸得出來 (e.g., ~~genYMDHMS~~)
* 較小的名稱如果能表達足夠的意義，通常比較長的名稱好，儘量減少再命名上不必要的文字
* 不要用變數型態作為變數名稱
    * e.g., `accountList` → `accountGroup` or `accounts`
* 要區別名稱，用**讀者能分辨的區別方式**！！！
    * e.g.,
        * ~~moneyAmount~~ → `money`
        * ~~customerInfo~~ → `customer`
* 命名的長度應該要與 scope 大小對應
    * 一個常用到的變數或常數，最好給它一個容易被搜尋的名子
* 詞性
    * class, object → 名詞
    * method → 動詞
* 替單一的概念選一個詞
    * e.g., get, fetch, retrieve 混用是一件很糟的事
* 避免用雙關語，或可以表達兩個意思的字
    * e.g., 加入一個新的值 : ~~add~~ → append, insert

## 第3章：函式
* 寫一個好的函式有兩個守則
    * 簡短
    * 比簡短來得更簡短
* 準則
    * 每行應該少於150字，函式應該少於20行
    * 但最重要的是，**每個函式都要能清楚的告訴你本身的意圖，並帶領你到下個函式**
* **別去害怕取較長的函數名稱**
    * 長但具描述性質 > 註解 > 短而無法理解
* 降層準則： 由上而下閱讀的程式
* Don't repeat yourself at any cost!!!
* `if`, `else`, `while` 這些敘述最好都只有一行，而那行通常是函式呼叫
    * 避免巢狀結構，**函式內的縮排不該超過一或兩層**
* **函式應該只做好做一件事情**
    * 做一件事的函式不應該被合理的分成不同的段落 (e.g., 宣告區, 初始區... and etc.)
* 函式要能**做好某件事**，或**回答某個問題**，而這代表**兩者不該同時發生！！！**

```java
if (set("username", "bob")) ......

// refactored
if (attrExists("userName")) {
    setAttr("userName", "bob");
}
```

### 錯誤處理
* 用例外處理取代錯誤碼回傳
    * 而錯誤處理是會混淆程式結構的，比較好的作法就是把 try catch 區塊提出來

```java
if (deletePage(page) == E_OK) {
    if (registry.deleteReference(page.name) == E_OK) {
        if (configKeys.deleteKey(page.name.makeKey()) == E_OK) {
            logger.log("page deleted");
        } else {
            logger.log("configKey not delete")
        }
    } else {
        logger.log("deleteReference from registry failed")
    }
} else {
    logger.log("delete failed");
}

// refactored
try {
    deletePage(page);
    registry.deleteReference(page.name);
    configKeys.deleteKey(page.name.makeKey());
} catch(Exception e) {
    logger.log(e.getMessage());
}

// even more refactored
public void delete(Page page) {
    try {
        deletePageAndAllReferences(page);
    } catch(Exception e) {
        logError(e);
    }
}

private void deletePageAndAllReferences(Page page)
            throws Exception {
    deletePage(page);
    registry.deleteReference(page.name);
    configKeys.deleteKey(page.name.makeKey());
}

private void logError(Exception e) {
    logger.log(e.getMessage());
}
```

### 參數
* 函式最好是不使用到參數，可以的話不要超過3個
    * 除非有非常特殊的理由，否則都不該超過3個
* **別傳flag參數(e.g. isSutie)進入函式**，那代表這個函式一定做超過一件事！！！
* 單一參數函式
    * 問與這個參數有關的問題 (e.g., `fileExists("MyFile")`)
    * 對這個參數進行操作，並且 **回傳**
    * 事件，利用參數去改變系統的狀態
* 2 ~ 3 個參數
    * 注意參數順序性
* 利用建立物件的方式，減少函式參數的數量

```java
Circle makeCircle(double x, double y, double radius);
// refactored
Circle makeCirecle(Point center, double radiue);
```

* 避免使用輸出型參數，這十分的讓人困惑

```java
appendFooter(s);

// refactored
s.appendFooter();
```

### 如何寫出這樣函式？？？
一直修改和重構，直到足夠精簡
不用一開始就要寫到最精簡，實際上那也是辦不到的

## 第4章：註解
* **不要替糟糕的程式碼寫註解 ─ 重寫它！！！**
* 即使是適當的使用註解，也只是用來彌補程式碼表達意思的失敗
    * 每次要寫註解時，先思考是否能**直接用程式碼表達**
* 註解只應該描述附近的程式碼，不要在區域性註解內放入系統全域資訊
* 替只做一件事的小函式選一個好名稱，多半比將註解寫在函式標頭優雅

### 有用的註解
* 提供資訊的註解

```Java
//format matched kk:mm:ss EEE, MMM dd, yyyy
Pattern tiMatcher = Pattern.compile(
    "\\d*:\\d*:\\d* \\w*, \\w* \\d*, \\d*"
)
```

* 對後果的告誡： 警告會出現某種特殊後果的註解
* TODO
* 公開 API 中的 Javadoc

### 糟糕的註解
* 大部分的註解
* 多餘的註解： 沒比程式碼本身透露更多資訊的註解

```Java
class Person() {
    # The name of this person
    private String name;
}
```

* ~~每個函式，每個變數都該有註解來說明~~。**不，別這麼做**
* 把暫時無用的程式碼註解掉並留著，是很惱人的 → 版本控制會幫我們記下它

## 第5章：編排
* 選擇一些簡單的縮排規則，並持續的運用它
    * 如果在一個團隊，所有成員都該依循著一套統一的編排規則
* 團隊合作時，事先決定編排方式是值得的
    * 該在哪裡放括號
    * 縮排寬度多少
    * 如何命名變數、類別、方法
* 編排是一種溝通方式，可以嚴重影響可讀性，所以我們要很重視它
* 垂直邊排： 一份程式檔大概多長比較好？
    * 一份重要的大型專案也可以在大多數程式檔都只有200行左右的情況下完成
    * 這沒有硬性規定。但要知道**簡短的程式檔總是比大型的程式檔容易理解**
* 變數應該被宣告在接近它被使用的地方
    * 區域變數應該在函式的最上方被宣告
    * 迴圈的控制變數應該在回圈敘述內宣告

### 函式間的編排
* 如果一個函式呼叫了另一個函式，這個函式最好放在被呼叫函式的上方
* 概念高度相似的函式也應該垂直的放在一起
    * 也許是類似的命名或相同工作的變異版本，就算沒相互呼叫，還是應該放在一起
* 談到了垂直的寬度後，那水平的寬度呢?
    * 雖然我們喜歡較短的程式碼，但只要是**不需要用到捲軸捲到右方就可以稱為適當的寬度**
* 有時候if, while或簡單的函式，可以被縮減為一行，讓我們違反一般的縮排規則，**不建議這麼做**

```java
public String render() throws Exception {return "";}

//better
public String render() throws Exception {
    return "";
}
```

### 使用空行、空白
* 每一段程式碼都代表一個完整思緒，而我們用空行來區隔它們
    * 而如果程式碼們是相關的，它們就該是垂直緊密的
    * 相似的概念應該要放在同一份檔案中
* 我們用水平的空白來區分高度和低度相關的概念，也可以作為強調用，下面的程式碼是書中一個很棒的例子
    * 注意到return那行，這裡用空格來強調運算子的優先權

```java
public class Quadratic {
    public static double root1(double a, double b, double c) {
        double determinant = determinant(a, b, c);
        return (-b + Math.sqrt(determinant)) / (2*a);
    }
    ......
}
```

## 第6章：物件及資料結構
* **資料結構容易新增函式，而物件容易增加新類別。** 反之亦然
* 模組不該知道它操作的物件的內部操作
* 別使用一連串的程式呼叫

```java
final String outputDir = ctxt.getOptions().getScratchDir().getAbsolutePaty();

//refactored
Option opts = ctxt.getOptions();
File scratchDir =opts.getScractchDir();
final String outputDir = scratchDir.getAbsolutePath();
```

## 第7章：錯誤處理
* 例外處理應該要能提供**有用的錯誤訊息**，
    * e.g, 哪裡發生錯誤、錯誤型態是什麼
* 別回傳 null，試著拋出例外事件是更好的作法
    * 函式回傳 null 已經夠糟了，但傳遞 null 進去更是糟糕透頂
* Wrapper: 從呼叫者的角度定義例外class -> 減少依賴

Wrapper Example

```Java
// original
ACMEPort port = new ACMEPort(12);

try {
 port.open();
} catch (DeviceResponseException e) {
 reportPortError(e);
 logger.log("Device response exception", "e");
} catch (ATM1212UnlockedException e) {
 reportPortError(e);
 logger.log("ATM1212UnlockedException");
} catch (HMXError e) {
 reportPortError(e);
 logger.log("Device response exception");
} finally {
 ...
}


// refactored
LocalPort port = new LocalPort(12);
try {
 port.open();
} catch (PortDeviceFailure e) {
 reportPortError(e);
 logger.log(e.getMessage, e);
}

public class LocalPort {
 private ACMEPort innerPort;

 public LocalPort(int portNumber) {
  innerPort = new ACMEPort(portNumber);
 }

 public void open() {
  try {
   innerPort.open();
  } catch (DeviceResponseException e) {
   throw new PortDeviceFailure(e);
  } catch (ATM1212UnlockedException e) {
   throw new PortDeviceFailure(e);
  } catch (GMXError e) {
   throw new PortDeviceFailure(e);
  }
 }
}
```

## 第8章：邊界
* 學習型測試： 不在產品程式（production）裡實驗新的東西，而是另外寫測試程式，來了解第三方軟體
    * 學習型測試不會花太多額外時間（因為原本就要研究 API），而且能用來**確認第三方軟體是否能照我們預期的執行**
    * 如果沒有這種**邊界測試**來減輕版本更新時的整合負擔，我們**只能一直停留在舊的版本**
* 避免我們的程式過度的使用第三方軟體的特殊之處，最好是依靠在可以控制的程式之上。免得到最後反而受到第三方軟體的控制
* 使用尚未存在的程式（e.g., 尚未開定義好）
    * 自行定義介面，並用 adapter 封裝與 API 的互動
        * 額外的好處是如果 API 升級，也只需要改動 adapter

## 第9章：單元測試
* 為什麼要寫測試？
    * 測試讓程式保有彈性
    * 不用怕修改程式會造成程式結果不如預期
* 測試程式跟產品程式一樣重要，一樣需要整潔
    * **可讀性**造就了整潔的測試程式
    * 但是測試程式並不需要產品程式一樣的有效率
* 整潔測試程式的 5 個原則 F.I.R.S.T.
    1. Fast: 能快速的被執行
    2. Independent: 測試程式不該相互依賴
    3. Repeatable: 可以在任何環境重複執行
    4. Self-Validating: 輸出 boolean ，你不該手動比較兩個檔案才知道有沒有通過測試
    5. Timely: 單元測試要在恰好能使其通過的產品程式**之前**不久撰寫
* BUILD-OPERATE-CHECK
    1. 建立測試資料
    2. 操作測試資料
    3. 檢查「操作測試資料」後的結果是否如預期
* ~~一個測試只能有一個assert~~ → **一個測試只測試一個概念**
* TDD (Test Driven Development) 三大法則
    1. 在撰寫一個單元測試前，不可撰寫任何產品程式
    2. 只撰寫剛好無法通過的單元測試，不能編譯也算無法通過
    3. 只撰寫剛好能通過當前測試的產品程式

## 第10章：類別
* Java的慣例
    * 類別以變數開頭
        * `public static final` → `private static` → `private` >>>>> `public` (幾乎很少有理由要用到)
    * public 函式緊跟在變數
    * private 的工具函式，會跟在呼叫它的函式後
* 不用過度執著於封裝，有時候為了讓測試程式存取， protected 是必要的
* 設計程式時，一次只專注在「讓程式運作」或「讓程式整潔」之一，而兩者是同樣重要的
* 系統應該要由很多小的 class 組成，而不是少數的大 class 組成
* 我們架構的系統，在未來想新增或修改功能時，應該要儘可能不動到其他程式碼
* **開放閉合原則**： 類別應該要對擴充有開放性，對修改有封閉性
* **相依性反向原則**： 類別應該要相依於抽象概念，而不是相依在具體細節

### 職責
* class 除了簡短還是要簡短
    * 在函式計算行數，class算的是**職責的數量**
* class的命名要能足夠描寫他的職責
    * 如果無法取個明確的名稱，這個 class 可能就太大了
    * 模稜兩可的名稱，代表 class 可能包含愈多的職責，而這是我們不希望的
    * 用 25 個字詞為這個 class 寫出簡短的描述，而不使用到模糊的字眼，這樣的 class 就是職責數量恰當
* **單一職責原則**： 一個 class 或 module 應該有也只能有一個修改的理由

### 凝聚性
* class 只應該要有少量的實體變數， class 的每個方法都應該操作一個或更多這些變數
* 不用也不太可能產生最大凝聚性類別
    * 但當凝聚性增加，就代表方法和變數結合成一個邏輯的整體，這是我們所希望的
* class 累積越來越多實體變數，但只有少數函式操作著他們，就會開始喪失凝聚性
    * 而這就是應該拆開 class 的時候了！！！
    * 不用重新撰寫程式，而是應該改變它
        * 先寫好一套驗證的測試程式，一次一個地改變
        * 每一次變動都重新驗證是否如預期執行
        * 重構完成
