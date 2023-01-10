Title: PyCon TW 2017 - Day 1
Date: 2017-06-09 09:00
Modified: 2017-06-18 11:41
Category: Tech
Tags: Python, Conference, PyCon
Slug: PyCon-TW-2017-Day1
Authors: Wei Lee
Series: PyCon TW 2017

今年 PyCon 終於比起上次聽得懂多了！
看來這兩年來，還是有點進步的 XD

先放上今年的[共筆](https://hackfoldr.org/pycontw2017/)
這幾篇記錄我參加議程的筆記
有些投影片跟共筆就很清楚的，就直接放連結了

<!--more-->

---

## 議程

* [[Keynote] Choices for Smarter AI](#1)
* [Python 開源軟體考古 - 以Viper為例](#2)
* [整合 Slack 與 Docker 搭建 Jupyter 線上程式面試系統](#3)
* [[Keynote] The State of Python for ~~Education~~ Learning](#4)
* Building Microservices in Python 個案分享
    * [Slide](https://www.slideshare.net/jonascheng3/building-microservices-in-python-pycon2017)
    * [共筆](https://hackmd.io/s/Sk5LNzQke#1455-1540-talk-building-microservices-in-python-個案分享)
* [Understanding Serverless Architecture](#6)
    * 同場加映：[Don't Reinvent Sandwich](https://drive.google.com/file/d/0Bz8Kfu_94VuJcVo1a1drQjhReU0/view) (本議程沒供餐 XD)
* [Tensorflow & Python: Fault Detection System](#7)

---

<a name='1'></a>

## [Keynote] Choices for Smarter AI

* [共筆](https://hackfoldr.org/pycontw2017/https%253A%252F%252Fhackmd.io%252Fs%252FHywa7M7Jx)

* Better AI
    * Traditional: 更像人類
    * New: 更好用

### Choice[0]: What Language for AI?

* 現場會眾一致通過是 Python (Bias Sampling XD)
* Useful libs
    * [xgboost](https://github.com/dmlc/xgboost)
    * [libact](https://github.com/ntucllab/libact): Active Learning

### Choice[1]: What Application Should AI Help?

* AI Starts From Problem Solving
    * Motivation
        * Publishable (academia), Profitable
    * Feasibility
        * Modeling, Timeline, Budge
* Big Problems from Big Data
    * Velocity: Evolving data, Evolving problems
    * Volume: Computational Bottleneck
    * Veracity: Modeling with non-textbook data → Noise, Bias

### Choice[2]; What Route for AI

| Human-er | Machine-er |
| --- | --- |
| Subjective | Objective |
| Domain Knowledge | Computing Power |
| Fast Basic Solution |  Continuous Improvement |

**Tip: As much human as possible before going to machine**

### Choice[3]: How to Measure AI Goal?

**Tip: Start with reasonable, measurable and prioritized goals for AI**

### Choice[4]: What Data to (or not to) Use?

* Choice factors for data
    * Utility: Relationship with goal
    * Necessity: Uniqueness to goal
    * Quality: Noise, Freshness
    * Cost

**Tip: Start with "minimum viable data"**

### Choice[5]: What Model to Start?

Linear (Simpler) Model First

### Choice[6]: What Improvement Steps to Take?

* Lose Reason
    * Overfitting
    * Misfitting
    * Over-reusing
        * Keep data fresh

### Choice[-1]: How to verify and Deploy?

| Code Deployment Workflow | AI Deployment Workflow |
| --- | --- |
|`Development → Staging → Production` | `Offline → Online → Production` |

* Human Trust matters
    * Need a baseline to be compared

### Misc[0]: No Choice is a Choice

### Misc[1]: Learning from Mistake

### Misc[2]: ???

---

<a name='2'></a>

## Python 開源軟體考古 - 以 [Viper](https://github.com/viper-framework/viper) 為例
這場很實用，slide 也很清楚
蠻推薦影片出來可以看一下

* [slide](https://docs.google.com/presentation/d/1HwBrETgmEz6-igEVaPAtQPWyuBljyFyvXtKzHLSVaMk/edit#slide=id.p)
* [共筆](https://hackmd.io/CYYw7ARgjFBsCsBaMAGYAWR6DMIBMiAnABx7aLzGH4QCmUwxAZiEA===?view#1050-1120-talk-python-開源軟體考古-以-viper-為例)
* [viper-research](https://github.com/18z/viper-research)

從開源專案學習寫 code

### 讀 code 技巧

#### 降低專案複雜度

* 從早期版本追
    * 如何挑版本？ ( 搭配 tig 服用 )
        * 重大版本號
        * 簡單、可運作之版本 (e.g. viper 的 commit hash: [46a2a](https://github.com/viper-framework/viper/tree/46a2a))
* 感覺太複雜？
    * 砍！
    * 鎖定特定功能，移除其他雜質
    * 測試，能動就可以

#### 專案程式邏輯架構
模組相依性 → 一直 trace 到沒有 import 專案自己寫的 code

* Tools
    * [modulegraph](https://bitbucket.org/ronaldoussoren/modulegraph)
    * [pydegraph (py2degraph)](http://www.tarind.com/depgraph.html)
    * [snackfood](http://furius.ca/snakefood/)
* 數據分析
    * e.g. 被用最多的反而不是核心 → 這些程式碼好用、易用
* 走訪專案
    * 建立專案整體架構邏輯
    * 深度走訪
        * 由下往上
        * 仔細閱讀單一程式
    * 廣度走訪
        * 由上往下
        * 解釋特定組合的程式的意義

### Conclusion

* 系統化讀 code
* 從 Commit 學習
    * 架構變化
    * Commit Message 規則
    * Branching Model
    * Issue Handling

---

<a name='3'></a>

## 整合 Slack 與 Docker 搭建 Jupyter 線上程式面試系統

* [slide](https://www.slideshare.net/KevinShyu/slack-docker-jupyter)
* [pnp-interview](https://github.com/kkshyu/pnp-interview)
* [共筆](https://hackmd.io/CYYw7ARgjFBsCsBaMAGYAWR6DMIBMiAnABx7aLzGH4QCmUwxAZiEA===?view#1145-1230-talk-整合-slack-與-docker-搭建-jupyter-線上程式面試系統)

這場最重要的大概就是 slide ~~第 12 頁~~ 第 11 頁的架構圖

### Tools Used

* Flask
    * Python 中最簡單使用的 web framework
    * 做小型 web 應用非常適合
* Docker
    * 容器化
    * 一鍵部署
    * 限制容器耗費的 CPU, GPU
* Slack
    * Integration 很好

### Bugs

* Pull Image First
    * So it can be fast
* Try except for any case
    * dockerpy 的雷 xD
* File Permission
    * 要採 docker 坑，這很重要

---

<a name='4'></a>

## [Keynote] The State of Python for ~~Education~~ Learning

* [slide](https://speakerdeck.com/willingc/the-state-of-python-for-education)
* [共筆](https://hackfoldr.org/pycontw2017/https%253A%252F%252Fhackmd.io%252Fs%252FHk-NVGXke)

這場 Talk 主要講學習、推廣和社群

Carol 有提到幾個學習 Python 很棒的資源
其中我覺得最有用的大概就是[pyvideo.org](http://pyvideo.org) 了
之前回去聽工資管系系友演講，趨勢的學長就有提到看 Talk 是很快的學習方式

另外，Carol 強力推薦今年 PyCon US，Instagram 給的 Talk
[Lisa Guo, Hui Ding Keynote PyCon 2017](https://www.youtube.com/watch?v=66XoCk79kjM)
之後，應該也會找個時間來看一下

---

<a name='6'></a>

## Understanding Serverless Architecture

* [slide](https://speakerdeck.com/dawny33/understanding-serverless-architectures)
* [共筆](https://hackmd.io/s/Sk5LNzQke#1610-1655-talk-understanding-serverless-architecture)

### Serverless

* Function as a service (FaaS)
    * e.g. AWS lambda
* Advantage
    * Don't need to maintain servers
* Disadvantages
    * Functions are allowed to run for only a limited amount of time
    * Heavy workloads cannot be run
    * No control over containers
    * Hard to monitor
    * Hard to scale up
* It's awesome but not the best choice for everyone.

---

<a name='7'></a>

## Tensorflow & Python: Fault Detection System

* [slide](https://www.slideshare.net/EricAhn/tensorflow-and-python-fault-detection-system-pycon-taiwan-2017)
* [共筆](https://hackmd.io/s/BJqH4M7kl#1720-1750-talk-tensorflow-amp-python-fault-detection-system)

Fault: An abnormal condition or defect at the component

* Logs
    * Usage of CPU
    * Memory
    * Disk I/O
    * Network Bandwidth
    * System Log
    * Application Log
    * and etc.

Log is also natural language.
The sequence of words and expression is important sequential data.

這場我真的就有點聽不太懂了＠＠
