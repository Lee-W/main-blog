Title: DAG 即將從 Airflow 移除
Subtitle: 網酸： 早該了
Date: 2025-09-04 18:45
Category: Tech
Tags: Airflow, Airflow 開發生情報
Slug: removing-DAG-from-airflow
Authors: Wei Lee

突然覺得爛新聞的聳動標題很適合這次的生情報 😆

<!--more-->

其實在 [AIP-83 - Rename execution_date -> logical_date and - DAG 即將走入歷史]({filename}/posts/tech/2024/24-aip-83.md)  就有稍微提到
（上次的副標題也是蠻爛新聞的，但沒這次爛）
只是最近又拿出來討論

---

👉 原文： [[DISCUSS] dag vs DAG vs Dag](https://lists.apache.org/thread/5fn1n188f99jspt627qhqsp2pznq545s)

## 本文
到底要用 dag、DAG 還是 Dag？！

截至本文撰寫為止，尚未開始投票
但目前的派系大概是這樣

* 不是 DAG 都好
    * Wei
    * Pierre
* Dag
    * Jarek
    * Ash
* dag
    * Daniel
    * Sumit
    * Ankit

## 我怎麼想
認真翻了一下[AIP-83 - Rename execution_date -> logical_date and - DAG 即將走入歷史]({filename}/posts/tech/2024/24-aip-83.md)才發現我真的說錯了
它其實只是提到 dag 跟 Dag 都可，並沒有說一定要用 dag

至於 Dag 跟 dag 哪個好，我偏向無所謂
還有一個很重要的原因是 -「我不是英文母語者」
我有點難判斷一個大小寫的確切是不是真的差了很多

至於為什麼不用 DAG ，則是我們希望可以跟 Directed acyclic graph脫鉤
問 AI Airflow 相關的事情，它都會丟 DAG 給我
而且還講不聽，真的很煩...
