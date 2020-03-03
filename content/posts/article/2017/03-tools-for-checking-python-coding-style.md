Title: Tool for Checking Python Coding Style
Date: 2017-03-15 19:13
Category: Tech
Tags: Python, Code Quality, Vim
Slug: tools-for-checking-python-coding-style
Authors: Lee-W

[Pylint](https://www.pylint.org)

## Setup

```shell
pip install pylint
```

## Usage

### Generate a code quality report

```shell
pylint your_code.py
```

<!--more-->

### Customize your pylint settings

Some rules in default settings might be too trivial.
(e.g. PEP8 E501: line too long error (no more than 79 characters) )

* Generate `pylintrc` file

```shell
pylint --generate-rcfile > ~/.pylintrc
```

This generate a common used `pylintrc`.
For further customization, you'll have to change this file.

* Generate a code quality report using you `pylintrc`

```shell
pylint --rcfile ~/.pylintrc you_code.py
```

## Integrate with Vim

### 1. [ale](https://github.com/w0rp/ale)

![ale-screenshot](/images/posts-image/2017-03-15-tools-for-checking-python-coding-style/vwpqY4G.png)

`ale` also supports other linters in other languages.
It uses the new async feature in vim 8.
Thus, it checks your code when you are typing. (You can disable it.)

The following settings are for pylint in `~/.vimrc`

```shell
# The default value is pytlinh
# If your pylint executable is not pylint, it should be set
let g:ale_python_pylint_executable = 'pylint'

# options of your pylint command
let g:ale_python_pylint_options = '--rcfile ~/.pylintrc'
```

All the available linters are enabled by default.
For Python, `flake8`, `mypy` are also used.
Thus, you might find that even if you ignore some rules in `pylintc`, you are still notified.

In this case, add the following setting in `~/.vimrc`

```shell
let g:ale_linters = {
\   'python': ['pylint'],
\}
```

This enables `pylint` as the only linter for Python

p.s. `mypy`, `flake8` are also great linters. I'm just not familiar with it

### 2. [python-mode](https://github.com/python-mode/python-mode)

It's a powerful package supports not only linters but also plenty of useful features a python programer would need.

![python-mode-screenshot](/images/posts-image/2017-03-15-tools-for-checking-python-coding-style/5FffIqN.png)
Unlike `ale`, `python-mode` check your code only when you save or open your python file (You can set this in your `~/.vimrc`)

Add these lines in `~/.vimrc`  to enable `pylint`

```vim
let g:pymode_lint_checkers = ['pyflakes', 'pylint', 'pep8']
let g:pymode_lint_ignore = "C0111,W0621,E501,F0002"
```

Note that space cannot appear in `pymode_lint_ignore`
