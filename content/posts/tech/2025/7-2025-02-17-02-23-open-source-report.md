Title: 2025/02/17 - 02/23 開源貢獻週報
Date: 2025-02-23 23:15
Category: Tech
Tags: Open Source, 開源貢獻週報
Slug: 2025-02-17-02-23-open-source-report
Authors: Wei Lee

第四周了！姑且能算是一個月了吧！

<!--more-->

## commitizen
把上週還是草稿的 [feat(providers): add uv_provider #1351](https://github.com/commitizen-tools/commitizen/pull/1351) 完成
不過激起了一些維護者們認為該如何支援 uv 的討論
還沒有時間細看，但大致看過是個有趣的討論
下週看有沒有機會再重新思考一下怎樣才是最好的解法

Review 並 merge [fix(bump): manual version bump if prerelease offset is configured #1358](https://github.com/commitizen-tools/commitizen/pull/1358)

## commitizen-action
Review 並 approve [feat: add support for manual version bumping #99](https://github.com/commitizen-tools/commitizen-action/pull/99)

赫然發現這個專案有些設定太古老了，可以找時間來更新一下

## pycon-etl
開了 PR [Remove default airflow cfg #156](https://github.com/pycontw/pycon-etl/pull/156/files)
讓 `airflow.cfg` 只記錄我們改寫的那些選項
是不是 best practice 我也不太確定
但應該是會省去管理 airflow.cfg 的成本
尤其是這種可能會一手接一手的專案
