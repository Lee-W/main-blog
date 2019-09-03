Title: [Paper] A Learning-based Framework to Handle Multi-round Multi-party Influence Maximization on Social Networks
Date: 2016-08-22 16:53
Category: Tech
Tags: Paper, Social Network, Machine Learning, Game Theory
Slug: a-learning-based-framework-to-handle-multi-round-multi-party-inflence-maximization-on-social-networks
Authors: Lee-W
Summary:

[Paper](http://dl.acm.org/citation.cfm?id=2783392)

<!--more-->

[TOC]

## 1. Introduction

* Problem Description
    * A company intends to select a small set of customers to distribute praises of their trial products to a larger group

* Influence maximization
    * Goal: Identify a small subset of seed nodes that have the best chance to influence the most number of nodes
    * Competitive Influence Maximization (CIM)

* Assumption
    * Influence is exclusive (Once a node is influenced by one party, it will not be influenced again)
    * Each round all parties choose one node and then the influence propagates before the next round starts

* STORM (STrategy-Oriented Reinforcement-Learning based influence Maximization) performs
    * Data Generation
        * the data, which is the experience generated through simulation by applying the current model, will become the feedbacks to refine the model for better performance
    * Model Learning

### Difference with Others

1. Known strategy → Both know and unknown
    * Known or Unknown but available to compete → Train a model to learn strategy
    * Unknown → Game-theoretical solution to seek the Nash equilibrium
2. Single-roung → Multi-round
3. Model driven → learning-based, data-drivern
4. Not considering different network topology → General to adapt both opponent's strategy and environment setting (e.g. underlying network topology)

## 2. Problem Statment

### Def 1: Competive Linear Threshold (CLT)

* CLT model is a multi-party diffusion model
* The party who has the highest influence occupied the node

### Def 2: Multi-Round Competitive Influence Maximization (MRCIM)

* Max its overall relative influence

## 4. Methodology

* NP-hardness of MRCIM → looks for approxmiate solution
* Max the inflence for each round does not guarantee overall max
    * Due to the fact that each round are not independent

### 4.1 Preliminary: Reinforcement Learning

* Learn a policy $\pi(s)$ to determine which action to take state s (environment)
* How to estimated $\pi$?
    * Expected Accmulated Reward of a state (V function)
        * $ V^\pi(s) = E_\pi\{R_t|S_t=s\}=...$
    * Expected Accmulated Reward of a state-action pair (Q function)
        * $ Q^\pi(s, a) = E_\pi\{R_t|S_t=s, a_t=a\}=...$

The optimal $\pi$ can be obtained through Q functinon

$ \pi = \arg \min_{a\in A}Q(s,a)$

(i.e. For all "a" in A, find the "a" such that min Q(s, a))

### 4.2 Strategy-Oriented Reinforcement-Learning

#### Setup

* Env
    * Influence propagation process
* Reward
    * Delay Reward: The difference of activated nodes between parties at the last round
        * After the last round, rewards are propagated to the previous states through Q-function updating
        * Slow but more accurate
* Action
    * ~~Choosing certain node to activate~~
        * too many
        * overfit
    * Single Party IM strategies
        * Namely, which strategy to choose given the current state
        * The size can be reduced to strategies choosen
        * Chosen Strategies
            * sub-greedy
            * degree-first
            * block
            * max-weight
* State
    * Represents
        * network
        * environment status
    * ~~record the occupation status of all nodes~~
        * $3^{|V|}$, too many
        * overfit
    * Features Designed
        * Number of free nodes
        * Sum of degrees of all nodes
        * Sum of weight of the edges for which bot h vertices are free
        * Max degree among all free nodes
        * Max sum of free out-edge weight of a node among nodes which are the first player's neighbors
        * Second player's
        * Max activated nodes of a node for the first player alter two rounds of influence propagation
        * Second player's
    * The feautres are quantize into
        * low
        * medium
        * high
    * Totally, $3^9$ states

#### Data For Training

* Propagation model is known (e.g. LT in the experiments)
* Strategies served as actions are predefined

In training phase, train the agent aginst a certain strategy and see how it performs on the given network
These data can be used to learn the value functions

#### Training Against Opponents

* Opponent Strategy
    * Known: Simulate the strategy during training
    * Unknown but availble during training: Same as above
    * Unknown: More Gerneral Model in 4.4

#### Phase

* Phase 1: Training
    * The agent update its Q function from the simulation experiences throughout the training rounds
    * Update $\pi$ in the meantime
* Phase 2: Competition
    * The agent would not update Q-table
    * Generates $\pi$ according to Q-table

## 4.3 STORM with Strategy Known

* Training the model compete against the strategy to learn $\pi$
* STORM-Q
    * Update Q-function following the concept of Q-learning
        * Q-Learning: $Q(S_t, a_t) = Q(S_t, a_t) + \alpha * (r_{t+1} + \gamma * max_{a}Q(S_{t+1}, a) -Q(S_t, a_t))$
    * $\epsilon$-greedy
        * Determine strategies on the current policy derived from Q-table.
        * Explore the new directions to avoid local optimum
    * Pure Strategy
       * The most likely strategy is choosen

$ Algorithm $

## 4.4 STORM with Strategy Unknown

### Unknown but available to train

* The differece between the known case is that experience cannot be obtained through simulation
* Train against unknown opponent's strategy during competition
    * It's feasible because STORM-Q only needs to know the seed-selection outcoms of the opponent to update the Q-table, not exact strategy it takes

### Unknown

* Goal: Create a general model to compete a variety of rational strategies
* Assumption: The oppoent is rational (Wants to max influence and knows its oppoent wants so)
* STORM-QQ
    * Two STROM-Q compete and update Q-tabale at the same time
    * Using current Q-table during training phase
    * Pure Strategy
        * Does Not guarantee that equilibrium exists in MRCIM
* STORM-MM
    * Mix Strategy (Samples an action from the distribution of actions in each state)
    * In two-player zero-sum game
        * Nash equilibrium is graranteed to exist with miexed strategies
        * Use MINMAX theorem to find the equilibrium
    * $Q(s, a, o)$: The reward of first party when using strategy $a$ against oppoent's strategy $o$ in state $s$
    * $Q_{t+1}(s_t, a_t, o_t) = (1-\alpha)Q_t(s_t, a_t, o_t)+\alpha[r_{t+1}+\gamma V(s_{t+1})]$
    * Operations  Research

* The differece between STROM-QQ and STORM-MM

|STROM-QQ|STROM-MM|
|--|--|
|Max the reward in their own Q-table|Finds equilibrium with one Q-table and determines both side's $a$ at the same time|
|Pure Strategies|Mixed Strategies|
|Choose strategy by greedy|Samples from the mixed strategy $\pi_a$ or $\pi_o$|

* Ideally, they should have simliar result in two-party MRCIM. In practice, the result might not due to
    * STORM-QQ does not guarantee equilibrium
    * Although equilibrium exists in STORM-MM. It does not guarantee to be found due to lack of training data or bad init or such problems.
