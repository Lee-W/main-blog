Title: Apache Airflow 年度問卷流程正式化
Date: 2025-12-07 13:10
Category: Tech
Tags: Airflow, Airflow 開發生情報
Slug: formalising-how-we-already-run-the-airflow-suvery
Authors: Wei Lee

因為之前 Airflow 問卷的執行沒有足夠明確被討論過，造成了一些風風雨雨
所以 Apache Airflow 的 PMC 花了點時間讓這件事正式化
不知道是不是因為沒有了風風雨雨，最近天氣都蠻好的

<!--more-->

👉 原文: [[[VOTE] Formalising how we already run the Airflow Survey]](<https://lists.apache.org/thread/tmwh4z3y4rq7bkcvgf0444gcwkprxdlb>)

## 本文
1. 年度社群問卷，應於每年年末執行
2. 目的知道大家怎麼用 Airflow，並用以改善
3. 問卷問題應在發布前要經過投票 (i.e., `[Vote]`)或默認共識 (i.e., `[Lazy Consensus]`)
    * 不需正式投票的事項
        * 問題的小幅度修正 (finalising the questions)
        * 正式發佈問卷時
    * 大部分的問題應是固定的
4. 問題不應有*必填*的個人可識別資訊 (PII, Personally Identifiable Information) ，但可以有**選填**的，讓任意單位有意願贊助
5. 沒有人會負責執行這個問卷，你也可以是[沒有人](https://g0v.tw/intl/zh-TW/novice/)，但沒有人能不能說服大家，就看沒有人的人品了
6. PMC 會幫忙推廣
7. 問卷中所有人應該看到相同的資訊
8. 結果應放在 Airflow 官方網站上
9. 原始結果全部被公開
    * 時間: 1-2個月
    * 例外: (可隱藏的資訊)
        * re 問題 4 ，如有選填的 PII
        * 詐騙資訊
10. 如果 ASF 沒有提供適合的平台，讓問卷能在 "apachr.org" 下執行，那問卷要被架在哪都可以
11. 如果有任何單位想支持或贊助問卷，並負擔費用，那沒問題
    * 應在 PMC 發佈贊助徵求 (call for sponsor) 後，進行申請，並取得 PMC 同意才行
    * 執行方
        * ✅ 可以提供免費產品來吸引更多人填問卷
        * ❌ 但不能說是 PMC 背書的，也必須符合[合理使用](https://www.apache.org/foundation/marks/#principles)的規範
12. 如果有贊助者出現，我們會根據[Targeted Sponsorship Policy](https://www.apache.org/foundation/docs/targeted-sponsorship-policy.html)政策，通知 ASF

## 我怎麼想
蠻好的，等等來回 +1
有幾個比較吹毛求疵的細節
第九點的「1–2 個月」有點模糊，直接定成 2 個月比較清楚
PII 我認為應該是必須隱藏，而不是可以選擇是否隱藏
贊助徵求的部分有點不夠明確，這樣的意思是 PMC 原則上會在年底前發布徵求嗎
