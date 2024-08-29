Title: EDBT-ICDT 2018
Date: 2020-01-03 15:30
Category: Tech
Tags: Conference
Slug: edbt-icdt-2018
Authors: Wei Lee

整理筆記時，翻到兩年前去研討會的筆記
想說放著也不會增值，就整理出來了
雖然大部分的內容的印象都已經有點模糊了
不過就加減把當初的筆記湊起來

<!--more-->

當時我覺得最有趣的論文是 [Interactive Rule Refinement for Fraud Detection.](http://www.vldb.org/pvldb/vol9/p1465-milo.pdf)
不過竟然沒有做到太多筆記

[TOC]

## Day 1 - Keynote
* In theoretical CS
    * Polynomial time → easy/fast
        * However, that's not always the case
        * e.g., $O(n^{100})$
        * When `n` grows, even $O(n^2)$ is not efficient
* We're stuck on many problems even just in $O(n^2)$
* No $N^{2-\epsilon}$ time algorithms known for
    * String matching
    * computational geometry
    * graph problem in sparse graphs
    * many problems from database
    * many other problems
* **Why are we stuck?**
    * The traditional hardness in complexity tells us little about runtime
    * fine-grained hardness idea
        1. identify key hard problem
        2. ......

## Large Scale Machine Learning: Where Do Relational Systems Fit In? (by Chris Jermaine)

Currently, ML community cares about new models instead of theory and fundamental ML design

### ML vs AI
* ML is one approach to AI
* Classic AI: a programmer/expert imparting knowledge to a system
* ML is fundamentally statistical

### Intro to ML
* Distributed ML
    * Most ML systems use a "parameter server" model
        * Essentially a distributed key-value pair
    * Negatives
        * Parameter server compute model very limiting
* Data Parallel ML
    * Each compute server runs same computation on different data
    * Global state updated via aggregation

#### Want to scale out to speed up learning?
* scale out ineffective in data parallel param server
    * no easy way to add machines and have a graph execute faster
* Only easy way to scale out is to add compute servers

### Take-Home Point
* Current ML systems are **easily** applicable only to
    * Relatively small model problems
    * That is run on a single machine

## Detecting Database File Tampering through Page Carving
* Attack Vector: File Tampering
    * Occurs at the OS level → outside DBMS control
        * Bypass DBMS control
* Page Deconstruction
    * Page Header
        * Checksum
        * PageID
        * Row Count
* DBStorageAuditor
    * Goal: find inconsistency in storage
        * which is created by direct file manipulation

## Extracting Statistical Graph Features for Accurate and Efficient Time Series Classification
* Time series: Any data that is ordered
* Time Series Classification
    * similarity-based kNN (e.g., kNN-ED, kNN-DTW)
        * similarity can be unreliable
    * Shaplets
        * high computation complexity
* Why multiscale
    * sometimes global features are more important while sometimes local features are more important
    * in this research, both global and local are considered
* Visibility Graphs
* Multiscale Visibility Graphs
