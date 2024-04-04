Title: Python package installation failure inside a CircleCI pipeline
Date: 2024-04-24 15:06
Category: Tech
Tags: CircleCI, CI/CD, Python
Slug: python-package-installation-failure-inside-a-CircleCI-pipeline
Authors: Wei Lee

就像上次的[ github actions 上遇到的]({filename}/posts/tech/2024/1-how-to-deal-with-could-not-read-username-for-github.md)
原本跑得好好的 CI pipeline 又又又死掉了

<!--more-->

### Error Message

這次是在 CircleCI 中，設定 Python 的環境時，遇到以下的錯誤訊息

```
Traceback (most recent call last):
  File "/.../python3.9/site-packages/build/__main__.py", line 176, in _handle_build_error
    yield
  File "/.../python3.9/site-packages/build/__main__.py", line 427, in main
    built = build_call(
  File "/.../python3.9/site-packages/build/__main__.py", line 236, in build_package
    out = _build(isolation, srcdir, outdir, distribution, config_settings, skip_dependency_check, installer)
  File "/.../python3.9/site-packages/build/__main__.py", line 168, in _build
    return _build_in_isolated_env(srcdir, outdir, distribution, config_settings, installer)
  File "/.../python3.9/site-packages/build/__main__.py", line 130, in _build_in_isolated_env
    with DefaultIsolatedEnv(installer=installer) as env:
  File "/.../python3.9/site-packages/build/env.py", line 92, in __enter__
    _ctx.log(f'Creating isolated environment: {self._env_backend.display_name}...')
  File "/.../python3.9/site-packages/build/__main__.py", line 80, in _log
    _cprint('{bold}{}{reset}', _fill(first, initial_indent='* '))
  File "/.../python3.9/textwrap.py", line 391, in fill
    return w.fill(text)
  File "/.../python3.9/textwrap.py", line 363, in fill
    return "\n".join(self.wrap(text))
  File "/.../python3.9/textwrap.py", line 354, in wrap
    return self._wrap_chunks(chunks)
  File "/.../python3.9/textwrap.py", line 248, in _wrap_chunks
    raise ValueError("invalid width %r (must be > 0)" % self.width)
ValueError: invalid width -2 (must be > 0)
```

而且在我還無法在 local 重現 😱

### Root Cause
terminal / tty 的視窗大小設定在不正常的大小

### Solution

雖然問題根源是問同事才知道的，但後來有看一下其他人是不是遇到同樣的問題
根據[這個討論](https://github.com/Nuitka/Nuitka/issues/1803#issuecomment-1254006096) 好像是 CircleCI 的 bug
至於為什麼會突然出錯，我就沒研究到那麼細了
寬度 -2 到底是搞什麼...

解決方案也很直覺，只要把 tty 設定到正常的大小，就不會遇到相似的錯誤了

```sh
stty cols 80
```

## Reference
* [ Why the compilation fails inside a CircleCI pipeline ? #1803 ](https://github.com/Nuitka/Nuitka/issues/1803)
* [ Notes on setting tty/console/terminal width #5407 ](https://github.com/travis-ci/travis-ci/issues/5407)


