---
Title: [Paper] Deep Learning-Based Document Modeling for Personality Detection from Text
Date: 2017-03-29 09:36
Category: Paper
Tags: Deep Learning, Machine Learning, NLP, Big Five Theory, Personality
Slug: Deep-Learning-Based-Document-Modeling-for-Personality-Detection-from-Text
Authors: Lee-W

Summary: 
---

[Paper](https://sentic.net/deep-learning-based-personality-detection.pdf)
Implementation: [Personality-Detection](https://github.com/SenticNet/Personality-Detection)

<!--more-->

## Practical Application of Personality Detection
- Product and Service Recommandation (People with similiar personalities might have similiar favors)
- Mental Health Diagnosis
- Forensics: Reduce the circle of suspects
- Human Resource: One's suitablitlty for certain jobs 

## Personality Theory Used in This Paper
[Big Five Personality Trait](https://en.wikipedia.org/wiki/Big_Five_personality_traits)

## Idea
1. Feed Sentences from essays to convolution filter → Sentence model in the form of n-gram feature vectors
2. Aggregate the vectors of its sentences and combine with Masiresse features to represent the document
3. Classification: Feed document vector into a fully connected neural network with one hidden layer

## Overview of the Method

### 1. Preprocessing
- Sentence Splitting
- Data Cleaning
- Unification (e.g. lowercase)

### 2. Document-level feature extraction
Mairesse baseline feature set (e.g. word count, average sentence length)

### 3. Filtering
Sentences without personliaty clues are dropped

### 4. Word-level feature extraction
- word2vec embeddings → a variable-length feature set for the document
- variable number of fixed-length word feature vectors → variable number of sentences → document

### 5. Classfication
Deep CNN (Conolutional Nerual Network)

- Input
	- words: Fixed-length feature vector using word2vec
	- sentences: A variable number of word vectors
- Process
	- Word Vector is reduces to a fixed length vector of each sentence
	- Documents: a variable number of such fixed-length sentence embeddings
	- Document vector is then reduced to a fixed-length document vector
	- This Document vector is then concatenated with document-level features
- Predict
	- Yes / No (5 different personality traits are trained seperately) 


## Network Architecture

### Main Steps (7 Layers)
#### Word Vectorization
* Layer 1: Input
	* $ R ^{D \times S\times W \times E}$ 
	* Use Google's pretrained word2vec
	* In implementation, all the documents contain the same number of sentences.  
	  Shorter documents are padded shorter sentences with dummy words.

#### Sentence Vectorization
* Layer 2: Convolution
* Layer 3: Max Polling

#### Document Vectorization
* Layer 4: 1-max pooling

#### Classification: (Yes/No)
* Layer 5: Linear with Sigmoid activation
* Layer 6, 7: 2 Neuron Softmax Output


