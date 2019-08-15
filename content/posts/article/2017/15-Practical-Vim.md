Title: Practical Vim
Date: 2017-06-26 08:50
Category: Tech
Tags: Vim, Note
Slug: Practical-Vim
Authors: Lee-W
Summary:

每天一回一回的看，終於把[Practical Vim](https://pragprog.com/book/dnvim/practical-vim)看完了
不過到了後期，大部分就真的都看不太懂了＝ ＝
所以大多還是只記錄了前期我比較看得懂的一些 tip

<!--more-->

[TOC]

## Ch1: The Vim Way

### Tip2: Don't Repeat Yourself

* `.` command: Repeat the last change
    * Command in normal mode
    * The insert mode between two normal mode

### Repeatable action and how to repeat them

| Intent | Act | Repeat | Reverse |
|---|---|---|---|
| Make a change | {edit} | . | u |
| Scan line for next character | f{char}/t{char} | ; | , |
| Scan line for previous character | F{char}/T{char} | ; | , |
| Scan document for next match | /pattern`<CR>` | n | N |
| Scan document for previous match | ?pattern`<CR>` | n | N |
| Perform substitution |:s/target/replacement | & | u |
| Execute a sequence of changes | qx{changes}q | @x| u |

## Ch2: Normal Mode

### Tip10: Use Counts to Do Simple Arithmetic

* `<C-a>`: Add number
* `<C-x>`: Sub number
* What if the cursor is not on a number?
    * Operate on the number after the cursor

### Combine and Conquer

* Operator + Motion = Action
* When an operator command is invoked in duplicate, it acts upon the current line (e.g. dd)

|Trigger|Effect|
|---|---|
|c|Change|
|d|Delete|
|y|Yank into register|
|g!|Swap case|
|gu|Make lowercase|
|gU|Make uppercase|
|>|Shift right|
|<|Shift left|
|=|Autoindent|

## Ch3: Insert Mode

### Tip13: Make Corrections Instantly from Insert Mode

If we make a mistake while composing text in Insert mode, we can fix it immediately

|Keystrokes|Effect|
|---|---|
|`<C-h>`|Delete back one character(backspace)|
|`<C-w>`|Delete back one word|
|`<C-u>`|Delete back to start of line|

The keystrokes above can also be used in bash shell

### Tip14: Get Back to Normal Mode

`<C-o>` Switch to Insert Normal mode

### Tip15: Paste from a Register Without Leaving Insert Mode

`<C-r>0`: Paste the text that we just yanked at the current cursor position

### Tip19: Overwrite Existing Text with Replace Mode

`R`: Enter replace mode

## Ch5: Command-Line Mode

### Tip28: Execute a Command on One or More Consecutive Lines

* range
    * `:{start, end}`: from line "start" to line "end"
    * `.`: current line
    * `%`: all lines

### Tip31: Repeat the Last Ex Commands

`@:`: Repeat the last Ex command

### Tip32: Tab-Complete Your Ex Commands

`<C-d>`: Reveal a list of possible completions

### Tip33: Insert the Current Word at the Command Prompt

`<C-r><C-w>`: Get the word under cursor in Ex mode

## Ch8: Navigate Inside Files with Motions

This chapter is extremely practical

## Ch9: Navigate Between Files with Jumps

### Tip55: Travel the Jump List

|Command|Effect|
|---|---|
|`[count]G`|Jump to line number|
|`//pattern<CR>/?pattern<CR>/n/N`|Jump to next/previous occurrence of pattern|
|`%`|Jump to matching parenthesis|
|`(`/`)`|Jump to start of previous/next sentence|
|`{`/`}`|Jump to start of previous/next paragraph|
|`H`/`M`/`L`|Jump to top/middle/bottom of screen|
|`gf`|Jump to file name under the cursor|
|`<C-]>`|Jump to definition of keyword under the cursor |
|`/`|Jump to a mark|

## Ch12: Matching Patterns and Literals

### Tip74: Use the \V Literal Switch for Verbatim Searches

Put `\V` before words when searching can cancel regular expression

## Ch13: Search

### Tip81: Preview the First Match Before Execution

Use `<C-r>` `<C-w>` to autocomplete when searching

## Ch14

### Tip88: Find and Replace Every Match in a File

`%s/word1/word2/g`
