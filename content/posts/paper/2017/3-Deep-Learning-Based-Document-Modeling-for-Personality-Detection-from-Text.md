Title: [Paper] Deep Learning-Based Document Modeling for Personality Detection from Text
Date: 2017-04-11 17:59
Category: Paper Summary
Tags: Deep Learning, Machine Learning, NLP, Big Five Theory, Personality
Slug: Deep-Learning-Based-Document-Modeling-for-Personality-Detection-from-Text
Authors: Lee-W
Summary: 


* [Paper](https://sentic.net/deep-learning-based-personality-detection.pdf)
* Implementation: [Personality-Detection](https://github.com/SenticNet/Personality-Detection)
* Data Set
	* [James Pennebaker and Laura King's stream-of-consciousness essay dataset](http://mypersonality.org/wiki/doku.php?id=wcpr13)
	* [NRC Word-Emotion Association Lexicon](http://saifmohammad.com/WebPages/NRC-Emotion-Lexicon.htm)

<!--more-->

## Practical Application of Personality Detection
- Product and Service Recommandation (People with similiar personalities might have similiar favors)
- Mental Health Diagnosis
- Forensics: Reduce the circle of suspects
- Human Resource: One's suitablitlty for certain jobs

## Personality Theory Used in This Paper
[Big Five Personality Trait](https://en.wikipedia.org/wiki/Big_Five_personality_traits)

## Basic Idea of the Method
1. Feed sentences from essays to convolution filter → Sentence model in the form of n-gram feature vectors
2. Aggregate the vectors of a document's sentences and combine them with Masiresse features to represent the document
3. Classification: Feed the document vectors into a fully connected neural network

## Overview of the Method

### 1. Preprocessing
- Sentence Splitting
- Data Cleaning
- Unification (e.g. lowercase)

### 2. Document-level feature extraction
Mairesse baseline feature set (e.g. word count, average sentence length)

### 3. Filtering
Sentences without personliaty clues are dropped
(Based on [NRC Word-Emotion Association Lexicon](http://saifmohammad.com/WebPages/NRC-Emotion-Lexicon.htm))

### 4. Word-level feature extraction
- word2vec
- Variable number of fixed-length word feature vectors → Variable number of sentences → Document

### 5. Classfication
Deep CNN (Conolutional Nerual Network)

- Input
	- Words: Fixed-length feature vector using word2vec
	- Sentences: Variable number of word vectors
- Process
	- Word Vector is reduced to a fixed length vector of each sentence
	- Document: Variable number of such fixed-length sentence vector
	- Document vector is then reduced to a fixed-length document vector
	- This Document vector is then concatenated with document-level features
- Predict
	- Yes / No (5 different personality traits are trained seperately) 

## Network Architecture in Detail
### Main Steps (7 Layers)
#### Word Vectorization
* Layer 1: Input
	* $ R ^{D \times S\times W \times E}$ 
	* Use Google's pretrained word2vec
	* In implementation, all the documents contain the same number of sentences.  
	  Shorter documents are padded shorter sentences with dummy words.

#### Sentence Vectorization
* Layer 2: Convolution
	* 3 convolutional filters: unigram, bigram, trigram 
* Layer 3: Max Polling

#### Document Vectorization
* Layer 4: 1-max pooling

#### Classification: (Yes/No)
* Layer 5: Linear with Sigmoid activation
* Layer 6, 7
	* 2 Neuron (yes/no) Softmax Output (ReLU and tanh perform worse)
	* fully connected layer of size 200

### Training
Objective Function: Negative Log Likelihood


