Title: Utterances - 用 GitHub Issues 當文章留言區
Date: 2022-02-23 11:05 +0800
Category: Tech
Tags: Pelican, blog
Slug: use-github-issues-as-comment-system
comment_id: use-github-issues-as-comment-system
Authors: Wei Lee

之前看到有人用 GitHub Issues 當部落格的留言區，一直讓我想從 Disqus 搬走
想了很久，終於在過年期間弄好了，弄起來比想像的簡單許多

<!--more-->

除了這裡，我還有經營 [Meet people around the world](https://travlog.wei-lee.me/)
（原本想寫遊記，結果現在都在記錄料理或影評 😅）
總之，它們都是透過 [pelican](https://github.com/getpelican/pelican/) 產生的部落格
分別使用了客製化的 [elegant](https://github.com/Lee-W/elegant) 和 [attila](https://github.com/Lee-W/attila) 主題

目前看到要加上 GitHub Issues 最簡單的做法是使用 [utterances 🔮](https://utteranc.es/)
由於 elegant 本身就支援 utterances ，設定起來非常簡單
而 attila 則是需要改 jinja2 template

本文會聊聊怎麼在 elegant 設定 utterances
接著看 elegant 是如何在 template 中加入 utterances，並將同樣的概念搬到 attila 上

[TOC]

### 如何在 elegant 設定 utterances

根據 [Comments — Enable Utterances](https://elegant.oncrashreboot.com/enable-utterances-comments) ， pelican 這端只要在 `pelicanconf.py` 加入 `UTTERANCES_REPO`

```py
# [username]/[repo name]
UTTERANCES_REPO = "Lee-W/Lee-W.github.io"
```

注意前面不能加上 `https://github.com/`
我因為這個愚蠢的錯誤卡了超久......

如果想為留言產生的 issue 加上特定的標籤，則可以設定 `UTTERANCES_LABEL`

```py
UTTERANCES_LABEL = "comment"
```

使用的標籤本身必須要已經存在
如果沒有的話，可以到先到 repo 的 Issues 頁面建立

![create-label](/images/posts-image/2021-use-github-issues-as-comment-system/create-label.png)

下一步要為你的 GitHub 帳號安裝 [utterances 的 GitHub App](https://github.com/apps/utterances)，並賦予部落格 repo 讀寫 issues 的權限

![utterances](/images/posts-image/2021-use-github-issues-as-comment-system/utterances.png)

設定完成後就能在文章的最下面看到留言的區塊

![comment-empty](/images/posts-image/2021-use-github-issues-as-comment-system/comment-empty.png)

完成留言後，就會出現在 GitHub Issues 上了
攥寫這篇文章的時候是用 localhost 測試，所以屆時裡面的連結會無效
但實際部署到 GitHub Pages 後，它就會寫入實際的網址

![comment-result](/images/posts-image/2021-use-github-issues-as-comment-system/comment-result.png)

如果覺得用文章的 URL 當 issue 的標題很醜，可以在文章的 metadata 中加入 comment_id
e.g.,

```markdown
Title: Utterances - 用 GitHub Issues 作為文章留言區
Date: 2022-02-23 10:40 +0800
Category: Tech
Tags: Pelican, blog
Slug: use-github-issues-as-comment-system
comment_id: use-github-issues-as-comment-system
Authors: Wei Lee
```

再留言一次就會產生以 `comment_id` 為標題的 issue

![comment-with-comment-id](/images/posts-image/2021-use-github-issues-as-comment-system/comment-with-comment-id.png)

我會建議可以的話為每篇文章加上 `commend_id`
除了比較好看以外，也能避免換網域，評論全都不見的問題
~~但像我這種沒什麼人留言的就沒差了 😭~~

## elegant 是怎麼做到的？

為了能更容易在 attlia 加入 utterances，我稍微研究了 elegant 是怎麼加的
以下的程式碼都是使用 [elegnat @ v5.4.0](https://github.com/Pelican-Elegant/elegant/tree/V5.4.0)

在 elegant 中全域搜尋 utterances，會先找到 [elegant/templates/_includes/utterances_scripts.html](https://github.com/Pelican-Elegant/elegant/blob/V5.4.0/templates/_includes/utterances_scripts.html)

```jinja2
{% macro comments_script_utterances(repo, id, label, theme) %}
<script src="https://utteranc.es/client.js"
        data-repo="{{ repo }}"
        data-issue-term="{{ id }}"
        data-label="{{ label }}"
        data-theme="{{ theme }}"
        crossorigin="anonymous"
        async>
</script>
{% endmacro %}
```

這段 [jinja2](https://jinja.palletsprojects.com/) macro 會產生的 JavaScript 程式碼會跟手動在 [utterances 🔮](https://utteranc.es/) 產生的小有不同
差別是在 `repo`, `issue-term`, `label`, `theme` 前面的 `data-` 前綴
不過不太會影響實際的使用
詳細可以參考 👉[Update index.html #334](https://github.com/utterance/utterances/pull/334)

再來能找到 macro `comments_script_utterances` 會在 [templates/_includes/comments.html#L55](https://github.com/Pelican-Elegant/elegant/blob/V5.4.0/templates/_includes/comments.html#L55) 被用到

```jinja2
{% if use_utterances %}
{% from '_includes/utterances_scripts.html' import comments_script_utterances with context %}
{{ comments_script_utterances(UTTERANCES_REPO, identifier, UTTERANCES_LABEL, UTTERANCES_THEME) }}
{% endif %}
```

其中參數 `UTTERANCES_REPO`, `UTTERANCES_LABEL`, `UTTERANCES_THEME` 都是能透過 `pelicanconf.py` 被設定的
而 `identifier` 則可以往上在 [templates/_includes/comments.html#L11](https://github.com/Pelican-Elegant/elegant/blob/V5.4.0/templates/_includes/comments.html#L11) 找到
如果沒有在文章的 metadata 加入 comment_id，則預設值是 `SITEURL + '/' + article.url`
（就是一開始比較醜的 issue 標題）

```jinja2
{% set identifier = SITEURL+ '/' + article.url %}
{% if article.comment_id %}
{% set identifier = article.comment_id %}
{% elif article.disqus_identifier %}
{% set identifier = article.disqus_identifier %}
{% endif %}
```

## 如何為其他主題加入 utterances

我將 attila 的改動細節記錄在 [commit 236706](https://github.com/Lee-W/attila/commit/236706851759c07d1ee0dd312eaf703293911c08)
流程大致如下

1. 關閉或取代預設的評論系統
    * `templates/base.html`
    * `static/js/script.js`
2. 加入 macro `comments_script_utterances`
    * `templates/partials/utterances_scripts.html`
3. 在 render每篇文章的 template 中使用 `comments_script_utterances`
    * `templates/article.html#L222`
4. 確保 macro 用到的參數，即使在 `peliconconf.py` 沒有正確設定的狀況下，依然有適當的預設值
    * `templates/partials/_defaults.html`
    * `templates/article.html#L212`

如果沒興趣看的話也可以直接使用我改的 [attila @ add-utterances-support](https://github.com/Lee-W/attila/tree/add-utterances-support)

## 雜談
雖然一直都想從 disqus 移出，但我佛系經營的部落格平常根本就不會有人留言
尤其是 [Meet people around the world](https://travlog.wei-lee.me/) 根本就不是只寫給工程師的文章，要留言還要登入 GitHub
原本留言的動機就夠低了，現在一口氣降到冰點 📉

不過往另一個方向想，反正也沒什麼人留言，我搬來 GitHub Issues 的成本根本超低 🤔

## Reference
[在 Hexo 的 Next 樣板中引入 utterances 的留言區 | GitHub Issue](https://nijialin.com/2021/05/15/hexo-utterances-comment/)
