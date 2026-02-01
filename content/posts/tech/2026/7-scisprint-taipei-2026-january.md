Title: scisprint Taipei 2026 January
Subtitle: The famous Tim!
Date: 2026-02-01 13:45
Category: Tech
Tags: Development Sprint
Slug: scisprint-taipei-2026-january
Authors: Wei Lee
Cover: /images/posts-image/2026/scisprint-2026-jan/scisprint.jpg

It's been a long time since I last led a development sprint for [commitizen-tools].
I've been focused on the Airflow community for some time, and the Taiwan community now seems to be doing well. It feels like a good time for me to come back and make some more contributions to [commitizen-tools].

<!--more-->

## What is scisprint
Scisprint is a development sprint held by [sciwork](https://sciwork.dev/), a community for researchers and engineers to share and discuss computer code for scientific, numerical, and engineering work.

How does [commitizen-tools] have anything to do with science? Well… yyc once told me that Git is part of scientific programming, so improving Git usage could also count as part of Scisprint. If [sciwork] is okay with it, I'm good with it too.

## What did we achieve?

This time, Tim and I were the group leaders, and three friends joined us and contributed.

### What did I do?
* Reviewed PRs
    1. [docs(github_actions): improve github action tutorial page#1782](https://github.com/commitizen-tools/commitizen/pull/1782)
    2. [docs(changelog): fix minor mistakes in changelog documentation, improve fluency #1792](https://github.com/commitizen-tools/commitizen/pull/1792)
    3. [docs: add revision date plugin #1814](https://github.com/commitizen-tools/commitizen/pull/1814)
    4. [docs(contributing): add pull request guideline and add notes about AI assisted contributions #1778](https://github.com/commitizen-tools/commitizen/pull/1778)
    5. [refactor(bump): fix unbounded variable type issue #1823](https://github.com/commitizen-tools/commitizen/pull/1823)
    6. [fix: add pytest ruff rule PT and fix missing deprecation warning #1826](https://github.com/commitizen-tools/commitizen/pull/1826)
    7. [fix(changelog): add incremental parameter to changelog generation #1808](https://github.com/commitizen-tools/commitizen/pull/1808)
    8. [fix(message_length_limit): align the behavior of message_length_limit #1813](https://github.com/commitizen-tools/commitizen/pull/1813)
    9. [feat(tags): enable version schemes with less than 3 components #1705](https://github.com/commitizen-tools/commitizen/pull/1705)
    10. [fix(config): include pyproject.toml in multi config file warning #1803](https://github.com/commitizen-tools/commitizen/pull/1803)
    11. [feat(version): add --tag for version command #1819](https://github.com/commitizen-tools/commitizen/pull/1819)
* Triaged issues
    1. [Allow matching a range of occurrences #659](https://github.com/commitizen-tools/commitizen/issues/659)

I originally wanted to write some code and open a PR myself, but I didn't really have the luxury to do so. I didn't even finish reviewing all the existing PRs—still a few more to go…

### Pull Requests created by participants
* Tim
    1. [refactor(bump): fix unbounded variable type issue #1823](https://github.com/commitizen-tools/commitizen/pull/1823)
    2. [fix: add pytest ruff rule PT and fix missing deprecation warning #1826](https://github.com/commitizen-tools/commitizen/pull/1826)
* andre.liang
    1. [feat(cli): add description when choosing a commit rule #1825](https://github.com/commitizen-tools/commitizen/pull/1825)
    2. [Add documentation when choosing a commit rule #1822](https://github.com/commitizen-tools/commitizen/issues/1822)
* YU HAN-CHENG
    1. [docs(READMD.md): add star history to README #1824](https://github.com/commitizen-tools/commitizen/pull/1824)
    2. [fix: add match parameter to pytest.warns to resolve PT030 #1828](https://github.com/commitizen-tools/commitizen/pull/1828)

### Other contributions right after the event

* Triaged issues
    1. [Commitizen now attempts to enforce its rules the entire history of the project #1818](https://github.com/commitizen-tools/commitizen/issues/1818)
    2. [feat(bump): add --version-files-only and deprecate --files-only #1802](https://github.com/commitizen-tools/commitizen/pull/1802)
    3. [Redesigning cz init self.config #1831](https://github.com/commitizen-tools/commitizen/issues/1831)
* Reviewed PRs
    1. [test(init): cover cz without descriptions#1829](https://github.com/commitizen-tools/commitizen/pull/1829)
    2. [refactor: replace hard-coded string "cz_conventional_commits" with DEFAULT_SETTINGS #1830](https://github.com/commitizen-tools/commitizen/pull/1830)
    3. [build: remove unnecessary poe config in pyproject.toml #1795](https://github.com/commitizen-tools/commitizen/pull/1795)

### Surprising Guest!
Like [DurianPy - Apache Airflow Development Sprint]({filename}/posts/tech/2025/27-durianpy-airflow-sprint.md), we also had a surprising guest this time. **woile**, the author of commitizen-tools, noticed the burst of activity and dropped us a message. I asked whether he wanted to join a short call and say hi to everyone, and he kindly did.

We chatted about how things have been going lately, and he finally had the chance to see "the famous Tim", who has created so many pull requests and improved the commitizen-tools codebase tremendously. Our review capacity honestly can't keep up with his development speed.

I couldn't even remember the last time I chatted with *woile*, so it was really good to see him again. He's one of the most important mentors and friends on my open-source development path. Oh, and by the way, he also built a very cool receipts platform called [Reciperium](https://www.reciperium.com/). Go check it out!

![scisprint](/images/posts-image/2026/scisprint-2026-jan/scisprint.jpg)

Side note: If you look closely, I was holding an acrylic stand. I brought Tomorin with me this time. She was there to watch everyone contribute. No one ignores her. If you do… Rikki will know.

![mygo-ignore-tomorin](/images/meme/mygo-ignore-tomorin.jpg)

[commitizen-tools]: https://github.com/commitizen-tools
[sciwork]: https://sciwork.dev/
