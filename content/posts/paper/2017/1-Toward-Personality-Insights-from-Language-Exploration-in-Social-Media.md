Title: [Paper] Toward Personality Insights from Language Exploration in Social Media
Date: 2017-04-04 18:45
Category: Paper Summary
Tags: Visualization, NLP, Big Five Theory, Personality
Slug: Toward-Personality-Insights-from-Language-Exploration-in-Social-Media
Authors: Lee-W
Summary: 


- [Paper](http://wwbp.org/papers/sam2013-dla.pdf)
- [Demo](http://wwbp.org/personality_wc.html)
- [My Slide](https://speakerdeck.com/leew/toward-personality-insights-from-language-exploration-in-social-media)

The main purpose of this paper is to show how social media can be used to gain psychological insights.

<!--more-->

Different from other papers in the past which use a pre-compiled word category list (e.g. LIWC),
it uses an open vocabulary approach that allowing discovery of unanticipated language.

### Data
- 75,000 Volunteers
	- Facebook Status Update
	- Age
	- Gender
	- Personality (Through Standard Personality Questionnaire)

### Architecture
1. Linguistic Feature Extraction
	- N-Gram
		- Point-Wise Mutual Information
	- Topic
		- Probability a person mentioning a topic (Derived from LDA)
	
2. Correlation analysis
	- Least Squares Linear Regression	
3. Visualization
	- [Differential Word Clouds](http://wwbp.org/personality_wc.html)
		- Word size represents correlation strength.
		- Color represents relative frequency
	- Standardized Frequency Plot
		- Plot the word frequency against age

### Result
Most results confirm what is already known or obvious.
However, I think this method might still be useful to gain insight in other kinds of datasets.