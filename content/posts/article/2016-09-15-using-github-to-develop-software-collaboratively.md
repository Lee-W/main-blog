---
Title: Using GitHub to Develop Software Collaboratively
Date: 2016-09-15 01:26
Category: Git
Tags: GitHub
Slug: using-github-to-develop-software-collaboratively
Authors: Lee-W
Summary: 
---

這是兩年前Github來成大教育課程的筆記
最近在整理git的筆記才翻出來
因為當時是以英文進行，課程筆記就也用英文做了
這篇的內容可能比較雜亂，之後還會再整理進另一篇git的筆記

<!--more-->

# Introduction to Git Hub (Company)
There are around 2600 staffs in GitHub and 40% of them live in San Fransisco.
Among them, there is one Taiwanese.

# Git
Wrote by Linus Torvalds.

## Why version control?
1. Historical propose
2. Collaboration

## Tutorial
```
git init "path"
```

.git is just a folder with normal file
There is no daemon or background progress
Everything is operated in file
Never `rm -rf .git` XD

```
git stauts
touch REAMDE.mdd
```

There are three main stages
1. working
2. staging
3. repo  

|Stage|Action||Stage|
|---|---|---|---|
|working| `add`| ->|staging|
|staging|`commit`| ->|repo|
|working|<- |`checkout`|repo|

```
git add REAMDE.md
```

When we're ready
`git commit -m "add a blank commit"`

After README.md is modified
```
git add REAMDE.md
git status
```
Now this file is in staging area  

So, how to go back to history?
`git reset REAMDE.md`

Take a look at our history
`git log`

Go back to history
`git checkout "SHA1"`

`git checkout master`
Everything comes back

`master` is the default branch name of git. It is a default word but not reserved.  

`git checkout -b "branch_name"` create a branch and checkout to it

## diff
`git diff`: View the difference between working and staging

`git diff --staged`: Difference between staging and repo

`git diff "SHA1"`: Difference between current version and SHA1

`git diff master~1`: difference between current and the one before master  
`git diff master^` -> master~1  
`git diff master^^` -> master~2  

`git diff a b`: Show the change from a to b  

## branch
In git, branch is not copy. It's like bookmark
Actually `git branch -d "name"` just delete the pointer but not the entry.

HEAD: the pointer points to current entry

### detach error
If you go back to a entry not in certain branch, a detach error might occur.
For example, checkout to a commit that is parent of more than one branch and then append a new commit to it.
In such case, this new appended commit might not be able to be referenced.  
*The solution to this problem is to create a new branch for it.*  

## log
`git log --decorate`: Show also branch info

`git log --all`: Show all branch

`git log --graph`: Show graph

### The difference between log and show
`git log`: Only the first line  
`git show`: All the message, not only the first line

# GitHub

## push
origin is a short hand name of that remote url. In other word, your repo.

`git push -u origin master`
- upload *master* to *origin*  
- -u tell git the default url to push for that branch(master) is origin, it would also make `git pull` remember  
	- Do -u and after that you can just use `git push`  

## pull
`git push --all`: push all branch
`git pull --prune`

## difference between fetch and pull
git fetch : go to remote and copy it
git pull -> fetch + merge

## on-site
pull request on GitHub  
`@person-name` -> notification  
Have a conversation with the whole team  

Write "fix #2 ...." in git commit -> special meaning -> specify the bug in issue on GitHub
Wiki -> documentation

# How to write a good git commit

## Principle
- Separate each commit
- Let the commit tell a story  

## More specific
- One line 80 character  
- Use present tense instead of past tense  
- Don't repeat what can be found in `git diff`  
- If more detail is to be written, left the second line to be blank.
- Write more detail about why this change happened after the third line.  

## Other issue
`git config --global -e`: Edit your .gitconfig file.

Not include binary files and executable
Don't version control these kinds of files.
Also, large files are not recommended to add to git.
If it's needed, try `git-annex`(web-site).

`git revert "SHA1"` -> save another entry of undo

If you commit the password -> `git rebase` can change commit, but it is not that recommended.

`git submodule` create a sub-module