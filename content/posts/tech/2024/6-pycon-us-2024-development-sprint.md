Title: PyCon US 2024 Development Sprint
Date: 2024-05-21 10:15
Category: Tech
Tags: PyCon, Python, Development Sprint, commitizen-tools
Slug: pycon-us-2024-development-sprint
Authors: Wei Lee

The last time I came to [PyCon US]({filename}/posts/tech/2019/03-how-was-pycon-us-2019.md). I had quite a good time during the development sprint and had a few of my PRs merged. (even though the one to CPython was later closed 🥲) So yep, I think this might be a good idea to host a [development sprint](https://us.pycon.org/2024/events/dev-sprints/) for [commitizen-tools](https://commitizen-tools.github.io/commitizen/). 👀

<!--more-->

![broad](/images/posts-image/2024-pycon-us-2024-development-sprint/broad.jpeg)

![registration-broad-1](/images/posts-image/2024-pycon-us-2024-development-sprint/registration-broad-1.jpeg)

![registration-broad-2](/images/posts-image/2024-pycon-us-2024-development-sprint/registration-broad-2.jpeg)


Disclaimer: the doll has absolutely nothing to do with Python and commitizen-tools. It's just cute, and it might make it easier for people to find me 😆

![commitizen-tools](/images/posts-image/2024-pycon-us-2024-development-sprint/commitizen-tools.jpeg)

It turns out that no one is interested in such a small project. 🥲 I met someone who said he wanted to take a look, but he left after lunch. I feel like I've already gotten used to it, or maybe I just should. Or I should just lead [airflow](https://github.com/apache/airflow/) next time 🥲

Nonetheless, this sprint was quite intensive and productive for commitizen-tools. With [@marcosdotme](https://github.com/marcosdotme) (who didn't even attend PyCon US) and I, we achieved the following results.

* [Pull Requests](https://github.com/commitizen-tools/commitizen/pulls)
    * Reviewed and Merged
        1. [ build(deps-dev): bump pytest from 8.2.0 to 8.2.1 #1123 ](https://github.com/commitizen-tools/commitizen/pull/1123)
        2. [ ci(workflow): move 'generate_cli_screenshots' steps to 'docspublish' #1126 ](https://github.com/commitizen-tools/commitizen/pull/1126) to close [ CLI screenshots will not be updated on Github Pages #1125 ](https://github.com/commitizen-tools/commitizen/issues/1125)
        3. [ Add py.typed file #1127 ](https://github.com/commitizen-tools/commitizen/pull/1127) to close [ Add py.typed marker #1106 ](https://github.com/commitizen-tools/commitizen/issues/1106)
    * Reviewed but Not Yet Merged
        1. [ fix: add description for subcommands #1120 ](https://github.com/commitizen-tools/commitizen/pull/1120)
        2. [ fix: set shell to False if running subprocess on Windows #1124 ](https://github.com/commitizen-tools/commitizen/pull/1124) to close [ cz bump fails when running with rye #1118 ](https://github.com/commitizen-tools/commitizen/issues/1118) and [ Installing pre-commit hook step in cz init fails when using rye #1117 ](https://github.com/commitizen-tools/commitizen/issues/1117)
        3. [ fix(changelog): handle custom tag_format in changelog generation #995 ](https://github.com/commitizen-tools/commitizen/pull/995)
    * Helped Fixing
        1. [ feat: draft of the --empty parameter #723 ](https://github.com/commitizen-tools/commitizen/pull/723)
        2. [ fix: add description for subcommands #1120 ](https://github.com/commitizen-tools/commitizen/pull/1120)
    * Opened
        1. [ Turn on isort for ruff #1128 ](https://github.com/commitizen-tools/commitizen/pull/1128)  
* [issues](https://github.com/commitizen-tools/commitizen/issues)
    * Triaged
        1. [ Add option for "cz.toml" config file #1111 ](https://github.com/commitizen-tools/commitizen/issues/1111)
        2. [ UnicodeDecodeError when run the command cz bump #1110 ](https://github.com/commitizen-tools/commitizen/issues/1110)
        3. [ Auto-linked references to commits/PRs in changelog #1109 ](https://github.com/commitizen-tools/commitizen/issues/1109)
        4. [ Error "fatal: unknown refname: format lstrip=2" raised when running "cz bump" #1032 ](https://github.com/commitizen-tools/commitizen/issues/1032)
        5. [ Exceptions when using cz from ISO8859-1 Terminal #956 ](https://github.com/commitizen-tools/commitizen/issues/956)
        6. [ Change default bump_message for plugin #938 ](https://github.com/commitizen-tools/commitizen/issues/938)
        7. [ cz bump cannot find version scheme "semver" after upgrade #841 ](https://github.com/commitizen-tools/commitizen/issues/841)
        8. [ Cannot create release version after creating a pre-release version #1068 ](https://github.com/commitizen-tools/commitizen/issues/798)
        9. [ Create a flag to build the changelog from commits in multiple git repositories #790 ](https://github.com/commitizen-tools/commitizen/issues/790)
        10. [ Can't bump without using annotated_tag #879 ](https://github.com/commitizen-tools/commitizen/issues/879)
        11. [ Flag to avoid creating a new commit for the bump #753 ](https://github.com/commitizen-tools/commitizen/issues/753)
        12. [ Use named capture group in bump_pattern to enable stricter check #129 ](https://github.com/commitizen-tools/commitizen/issues/129)
    * Closed
        13. [ option ci reads Changes to our CI configuration, possibly an error #1095 ](https://github.com/commitizen-tools/commitizen/issues/1095)
        14. [ cz ch cannot decode Chinese word #826 ](https://github.com/commitizen-tools/commitizen/issues/826)
        15. [ conventional keyword in body would be parsed #827 ](https://github.com/commitizen-tools/commitizen/issues/827)
        16. [ change log was generated with garbage data #798 ](https://github.com/commitizen-tools/commitizen/issues/798)
        17. [ cz bump fails if any non semver tag exist #916 ](https://github.com/commitizen-tools/commitizen/issues/916)
        18. [ Bumping issue with PATCH version #871 ](https://github.com/commitizen-tools/commitizen/issues/871)
        19. [ Shortcut for commit types #788 ](https://github.com/commitizen-tools/commitizen/issues/788)
        20. [ cz bump with a breaking change after an RC does not automatically increase the major version #757 ](https://github.com/commitizen-tools/commitizen/issues/757)
        21. [ Allow releasing after a release candidate without commits #751 ](https://github.com/commitizen-tools/commitizen/issues/751)
        22. [ Be able to configure the allowed prefixes list #672 ](https://github.com/commitizen-tools/commitizen/issues/672)
        23. [ Global Configuration #597 ](https://github.com/commitizen-tools/commitizen/issues/597)
    * Created
        1. [ Add won't added features to FAQ page #1129 ](https://github.com/commitizen-tools/commitizen/issues/1129)

I also want to thank Yucheng for attempting to address [ UnicodeDecodeError when running cz bump #1110 ](https://github.com/commitizen-tools/commitizen/issues/1110)

The great thing is that I finally managed to triage **all** issues with the `issue-status: needs-triage` label! but... found out we still need to check issues filed before [the labeling system](https://commitizen-tools.github.io/commitizen/contributing/#use-of-github-labels) was introduced.

Among all the PRs I worked on yesterday,  [ fix: add description for subcommands #1120 ](https://github.com/commitizen-tools/commitizen/pull/1120) was quite interesting. I didn't know that `argparse` changed the prompt of optional arguments from `Optional Arguments` to `options` since Python 3.10.

During the sprint, I shared commitizen-tools with Takanoryさん. Later, he introduced me to [towncrier](https://github.com/twisted/towncrier), a similar tool that I plan to explore further. We also had a great chat about Star Wars. 🌟 I was excited to share that I went to [Rise of the Resistence](https://travlog.wei-lee.me/posts/travel/2019/12/rise-of-the-resistance/) on the very first day it opened. 🚀

After the sprint, a couple of APAC folks went to this church restaurant. It was quite a pleasant dinner. Always love to hangout with Pythonistas 😄

![church-1](/images/posts-image/2024-pycon-us-2024-development-sprint/church-1.jpeg)
![church-2](/images/posts-image/2024-pycon-us-2024-development-sprint/church-2.jpeg)
![church-3](/images/posts-image/2024-pycon-us-2024-development-sprint/church-3.jpeg)
