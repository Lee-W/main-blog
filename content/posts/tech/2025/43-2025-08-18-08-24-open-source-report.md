Title: 2025/08/18 - 08/24 開源貢獻週報
Subtitle: 手起刀落，再見了遠古 PRs 😢
Date: 2025-08-25 09:25
Category: Tech
Tags: Open Source, 開源貢獻週報
Slug: 2025-08-18-08-24-open-source-report
Authors: Wei Lee

終於把熊大的 PR 們都看完了
雖然還有幾個需要討論還沒合併

<!--more-->

## commitizen
除了看 PR 外，這週也花了點時間整理 PR
如果是太久沒修改，程式碼衝突又太多的，我就直接關掉了
commitizen 也應該導入像 Airflow 那樣的 stale bot 才對
雖然很有可能是因為我們都沒時間看就關掉了...

老實說關掉它們還是令人有些難過呢 😢
但這些大概再也不會更新的 PRs 不關掉，也只是讓我們繼續看著它們感到壓力而已
維護者的量能是有限的

* 審閱 PRs
    1. [refactor(Init): remove the variable values_to_add and the _update_config_file function for readability #1537](https://github.com/commitizen-tools/commitizen/pull/1537)
    2. [feat: add check against default branch #1519](https://github.com/commitizen-tools/commitizen/pull/1519)
        * 讚讚的新功能，我很訝異 commitizen 沒有更早就有
    3. [refactor(changelog): shorten generate_tree_from_commits and use set to check used tags #1540](https://github.com/commitizen-tools/commitizen/pull/1540)
    4. [refactor(changelog): simplify logic for get_oldest_and_newest_rev #1539](https://github.com/commitizen-tools/commitizen/pull/1539)
    5. [fix semver not fully covered #1548](https://github.com/commitizen-tools/commitizen/pull/1548)
    6. [test(changelog): ensure error on missing changelog template filename #1557](https://github.com/commitizen-tools/commitizen/pull/1557)
    7. [feat(bump_rule): add BumpRule, VersionIncrement, Prerelease Enum #1518](https://github.com/commitizen-tools/commitizen/pull/1518)
        * 很棒的重構 PR ，但我們需要再討論一下向下相容的問題
    8. [feat: add config option for line length warning #1574](https://github.com/commitizen-tools/commitizen/pull/1574)
* 關閉 PRs
    1. [Feature/allow empty commit #592](https://github.com/commitizen-tools/commitizen/pull/592)
    2. [feat(ConventionalCommitsCz): allow to override defaults from config #546](https://github.com/commitizen-tools/commitizen/pull/546)
    3. [feat: configurable commit validation #648](https://github.com/commitizen-tools/commitizen/pull/648)
    4. [First take at ConventionalCommitsAppenderCz #486](https://github.com/commitizen-tools/commitizen/pull/486)
    5. [test(git): add a test for handling blank with path in git commit #1044](https://github.com/commitizen-tools/commitizen/pull/1044)
    6. [feat: Introduce tag_regex option with smart default #692](https://github.com/commitizen-tools/commitizen/pull/692)
* 思考並回覆 [Clarify what's a breaking change in commitizen #1446](https://github.com/commitizen-tools/commitizen/issues/1446)

## pycon-etl

* 關閉 PR [build: upgrade airflow to 3.0.5 #184](https://github.com/pycontw/pycon-etl/pull/184)
    * airflow 3.0.5 被發現 bug ，所以被拿掉了
* 開草稿 PR [build: upgrade airflow to 3.0.6rc1 #185](https://github.com/pycontw/pycon-etl/pull/185)
    * 因為 airflow 3.0.5 被拿掉了，所以修好的 3.0.6 很快就會釋出，就開了 PR 測試一下
