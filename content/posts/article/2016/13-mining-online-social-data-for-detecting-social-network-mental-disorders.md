Title: [Paper] Mining Online Social Data for Detecting Social Network Mental Disorders
Date: 2016-11-18 16:53
Category: Tech
Tags: Paper, Social Network, Machine Learning
Slug: mining-online-social-data-for-detecting-social-network-mental-disorders
Authors: Wei Lee

* [Paper](http://www2016.net/proceedings/proceedings/p275.pdf)
* [My Slide](https://speakerdeck.com/leew/mining-online-social-data-for-detecting-social-network-mental-disorders)

This paper proposes a model named SNMDD to detect Social Network Mental Disorder (SNMD) through users' behaviors on online social networks (OSN) instead of asking their mental condition.

<!--more-->

In addition, multi-source learning (FB and IG) is used to improve performance through STM.

* SNMDD is a classification model based on TSVM
The use of domain knowledge from psychology to extract features is the core of this model.
The most interesting part is choosing features as the proxy features to replace ones that are hard to detect.
For example, distinguishing whether a social capital is a strong tie or a weak tie is crucial to the detection of SNMD. However, it's hard to detect through OSNs data. Thus, it guesses that friends you interacts (e.g. posts, likes, comments) with might be the strong tie ones.

* STM is a tensor model based on Tucker Decomposition
Through Tucker Decomposition, it's possible to combine data from different sources and extract new features vectors.
