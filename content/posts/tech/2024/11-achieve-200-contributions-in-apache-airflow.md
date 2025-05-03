Title: Achieve 200 contributions in Apache Airflow
Date: 2024-07-31 23:55
Category: Tech
Tags: Airflow
Slug: achieve-200-contributions-in-apache-airflow
Authors: Wei Lee

This is more like a personal reflection, and I really doubt it would benefit anyone. But it's my blog anyway. I can write whatever I want, lol.

<!--more-->

There are actually 202 now, but I have the screenshot when it achieved 200, so I'll just keep 200 in the title.

![2024-07-30-05-15-PM-200-PRs](/images/posts-image/2024-achieve-200-contributions-in-apache-airflow/2024-07-30-05-15-PM-200-PRs.png)

The merged pull request is at 166 (+2). I am unsure about the remaining 34 contributions, perhaps due to the suggestions I provided for the PRs I reviewed. There are 2 PRs in review.

1. [Add dataset alias unique constraint and remove wrong dataset alias removing logic](https://github.com/apache/airflow/pull/41097)
2. [set "has_outlet_datasets" to true if "dataset alias" exists](https://github.com/apache/airflow/pull/41091)

200 contributions seem like a good opportunity to reflect on what I have done on the Airflow project since I joined Astronomer. There might be typos in the PR title, but I'll keep it as it is. I try to group related things into subgroups, and there might be things that cannot be easily categorized. I'm just putting it in the "misc" section.

The count of PRs might appear to be higher than the value I added (and it actually is). This is due to my development habits. Whenever possible, I prefer to keep the commits small and clean. It's easier to revert if I did something dumb and wrong. However, I must admit I probably created too many PRs for the Azure managed identity feature. Ideally, the feature PRs should include documentation updates as well. But yep, I was eager to land the feature first, then. It also suggested having separate PRs for each airflow provider even if it's basically the same feature.

[TOC]

## After joining Astronomer
### Add "DatasetAlias" for creating datasets or dataset events in runtime
1. [Check dataset_alias in inlets when use it to retrieve inlet_evnets](https://github.com/apache/airflow/pull/41043)
2. [Add string representation to dataset alias](https://github.com/apache/airflow/pull/41041)
3. [add example dag for dataset_alias](https://github.com/apache/airflow/pull/41037)
4. [add test case test_dag_deps_datasets_with_duplicate_dataset](https://github.com/apache/airflow/pull/40984)
5. [Extend dataset dependencies](https://github.com/apache/airflow/pull/40868)
6. [Extend get datasets endpoint to include dataset aliases](https://github.com/apache/airflow/pull/40830)
7. [Retrieve inlet dataset events through dataset aliases](https://github.com/apache/airflow/pull/40809)
8. [Link dataset event to dataset alias](https://github.com/apache/airflow/pull/40723)
9. [Scheduling based on dataset aliases](https://github.com/apache/airflow/pull/40693)
10. [Add DatasetAlias to support dynamic Dataset Event Emission and Dataset Creation](https://github.com/apache/airflow/pull/40478)

### Start task execution directly from the trigger
1. [fix: add argument include_xcom in method rsolve an optional value](https://github.com/apache/airflow/pull/41062)
2. [Add start execution from trigger support for existing core sensors](https://github.com/apache/airflow/pull/41021)
3. [Enhance start_trigger_args serialization](https://github.com/apache/airflow/pull/40993)
4. [State the limitation of the newly added start execution from trigger feature](https://github.com/apache/airflow/pull/40935)
5. [add next_kwargs to StartTriggerArgs](https://github.com/apache/airflow/pull/40376)
6. [Add start execution from triggerer support to dynamic task mapping](https://github.com/apache/airflow/pull/39912)
7. [Prevent start trigger initialization in scheduler](https://github.com/apache/airflow/pull/39585)
8. [Starts execution directly from triggerer without going to worker](https://github.com/apache/airflow/pull/38674) (PR of the month)

### Add REST API endpoint to manipulate queued dataset events
1. [add section "Manipulating queued dataset events through REST API"](https://github.com/apache/airflow/pull/41022)
2. [add "queuedEvent" endpoint to get/delete DatasetDagRunQueue](https://github.com/apache/airflow/pull/37176)

### Upgrade apache-airflow-providers-weaviate to 2.0.0 for weaviate-client >= 4.4.0 support
1. [extract collection_name from system tests and make them unique](https://github.com/apache/airflow/pull/40534)
2. [fix weaviate system tests](https://github.com/apache/airflow/pull/40517)
3. [Upgrade to weaviate-client to v4](https://github.com/apache/airflow/pull/40194)

### Improve trigger stability by adding "return" after "yield"
1. [add "return" statement to "yield" within a while loop in amazon triggers](https://github.com/apache/airflow/pull/38396)
2. [add "return" statement to "yield" within a while loop in dbt triggers](https://github.com/apache/airflow/pull/38395)
3. [add "return" statement to "yield" within a while loop in google triggers](https://github.com/apache/airflow/pull/38394)
4. [add "return" statement to "yield" within a while loop in azure triggers](https://github.com/apache/airflow/pull/38393)
5. [add "return" statement to "yield" within a while loop in http triggers](https://github.com/apache/airflow/pull/38392)
6. [add "return" statement to "yield" within a while loop in sftp triggers](https://github.com/apache/airflow/pull/38391)
7. [add "return" statement to "yield" within a while loop in airbyte triggers](https://github.com/apache/airflow/pull/38390)
8. [add "return" statement to "yield" within a while loop in core triggers](https://github.com/apache/airflow/pull/38389)
9. [retrieve dataset event created through RESTful API when creating dag run](https://github.com/apache/airflow/pull/38332)

### Contribute astronomer-providers functionality to apache-airflow providers
1. [add repair_run support to DatabricksRunNowOperator in deferrable mode](https://github.com/apache/airflow/pull/38619)
2. [remove redundant else block in DatabricksExecutionTrigger](https://github.com/apache/airflow/pull/38397)
3. [add reuse_existing_run for allowing DbtCloudRunJobOperator to reuse existing run](https://github.com/apache/airflow/pull/37474)
4. [fix how GKEPodAsyncHook.service_file_as_context is used](https://github.com/apache/airflow/pull/37306)
5. [add service_file support to GKEPodAsyncHook](https://github.com/apache/airflow/pull/37081)
6. [reword GoogleBaseHookAsync as GoogleBaseAsyncHook in docstring](https://github.com/apache/airflow/pull/36946)
7. [add WasbPrefixSensorTrigger params breaking change to azure provider changelog](https://github.com/apache/airflow/pull/36940)
8. [style(providers/google): improve BigQueryInsertJobOperator type hinting](https://github.com/apache/airflow/pull/36894)
9. [Check cluster state before defer Dataproc operators to trigger](https://github.com/apache/airflow/pull/36892)
10. [Fix WasbPrefixSensor arg inconsistency between sync and async mode](https://github.com/apache/airflow/pull/36806)
11. [avoid retrying after KubernetesPodOperator has been marked as failed](https://github.com/apache/airflow/pull/36749)
12. [check sagemaker training job status before deferring SageMakerTrainingOperator](https://github.com/apache/airflow/pull/36685)
13. [check transform job status before deferring SageMakerTransformOperator](https://github.com/apache/airflow/pull/36680)
14. [check ProcessingJobStatus status before deferring SageMakerProcessingOperator](https://github.com/apache/airflow/pull/36658)
15. [add deferrable mode to RedshiftDataOperator](https://github.com/apache/airflow/pull/36586)
16. [add use_regex argument for allowing S3KeySensor to check s3 keys with regular expression](https://github.com/apache/airflow/pull/36578)
17. [add deferrable mode to RedshiftClusterSensor](https://github.com/apache/airflow/pull/36550)
18. [check job_status before BatchOperator execute in deferrable mode](https://github.com/apache/airflow/pull/36523)
19. [remove event['message'] call in EmrContainerOperator.execute_complete|as the key message no longer exists](https://github.com/apache/airflow/pull/36417)
20. [Check redshift cluster state before deferring to triggerer](https://github.com/apache/airflow/pull/36416)
21. [handle tzinfo in S3Hook.is_keys_unchanged_async](https://github.com/apache/airflow/pull/36363)
22. [add type annotations to Amazon provider "execute_coplete" methods](https://github.com/apache/airflow/pull/36330)
23. [iterate through blobs before checking prefixes](https://github.com/apache/airflow/pull/36202)

### Add Azure managed identities support to apache-airflow-providers-microsoft-azure
1. [setting use_async=True for get_async_default_azure_credential](https://github.com/apache/airflow/pull/35432)
2. [add managed identity support to AsyncDefaultAzureCredential](https://github.com/apache/airflow/pull/35394)
3. [Refactor azure managed identity](https://github.com/apache/airflow/pull/35367)
4. [add managed identity support to fileshare hook](https://github.com/apache/airflow/pull/35330)
5. [add managed identity support to synapse hook](https://github.com/apache/airflow/pull/35329)
6. [add managed identity support to azure datalake hook](https://github.com/apache/airflow/pull/35328)
7. [add managed identity support to azure batch hook](https://github.com/apache/airflow/pull/35327)
8. [add managed identity support to wasb hook](https://github.com/apache/airflow/pull/35326)
9. [add managed identity support to adx hook](https://github.com/apache/airflow/pull/35325)
10. [add managed identity support to asb hook](https://github.com/apache/airflow/pull/35324)
11. [add managed identity support to azure cosmos hook](https://github.com/apache/airflow/pull/35323)
12. [add managed identity support to azure data factory hook](https://github.com/apache/airflow/pull/35322)
13. [add managed identity support to azure container volume hook](https://github.com/apache/airflow/pull/35321)
14. [add managed identity support to azure container registry hook](https://github.com/apache/airflow/pull/35320)
15. [add managed identity support to azure container instance hook](https://github.com/apache/airflow/pull/35319)
16. [Reuse get_default_azure_credential method from Azure utils for Azure key valut](https://github.com/apache/airflow/pull/35318)
17. [make DefaultAzureCredential configurable in AzureKeyVaultBackend](https://github.com/apache/airflow/pull/35052)
18. [Make DefaultAzureCredential in AzureBaseHook configuration](https://github.com/apache/airflow/pull/35051)
19. [docs(providers/microsoft): improve documentation for AzureContainerVolumeHook DefaultAzureCredential support](https://github.com/apache/airflow/pull/34104)
20. [docs(providers/microsoft): improve documentation for WasbHook DefaultAzureCredential support](https://github.com/apache/airflow/pull/34103)
21. [docs(providers/microsoft): improve documentation for AzureCosmosDBHook DefaultAzureCredential support](https://github.com/apache/airflow/pull/34102)
22. [docs(providers/microsoft): improve documentation for AzureFileShareHook DefaultAzureCredential support](https://github.com/apache/airflow/pull/34101)
23. [docs(providers/microsoft): improve documentation for AzureBatchHook DefaultAzureCredential support](https://github.com/apache/airflow/pull/34098)
24. [docs(providers/microsoft): improve documentation for AzureBaseHook DefaultAzureCredential support](https://github.com/apache/airflow/pull/34097)
25. [docs(providers/microsoft): improve documentation for Azure Service Bus hooks DefaultAzureCredential support](https://github.com/apache/airflow/pull/34096)
26. [docs(providers/microsoft): improve documentation for AzureDataExplorerHook DefaultAzureCredential support](https://github.com/apache/airflow/pull/34095)
27. [docs(providers/microsoft): improve documentation for AzureDataLakeStorageV2Hook DefaultAzureCredential support](https://github.com/apache/airflow/pull/34094)
28. [docs(providers/microsoft): improve documentation for AzureDataLakeHook DefaultAzureCredential support](https://github.com/apache/airflow/pull/34074)
29. [docs(providers/microsoft): improve documentation for AzureContainerRegistryHook DefaultAzureCredential support](https://github.com/apache/airflow/pull/34073)
30. [feat(providers/microsoft): add AzureContainerInstancesOperator.volume as a template field](https://github.com/apache/airflow/pull/34070)
31. [test(providers/microsfot): add system test for AzureContainerVolumeHook and AzureContainerRegistryHook](https://github.com/apache/airflow/pull/34002)
32. [docs(providers): replace markdown style link with rst style link for amazon and apache-beam](https://github.com/apache/airflow/pull/33992)
33. [test(providers/microsoft): add test cases  to AzureContainerInstanceHook](https://github.com/apache/airflow/pull/33991)
34. [Add DefaultAzureCredential support to AzureContainerRegistryHook](https://github.com/apache/airflow/pull/33825)
35. [feat(providers/microsoft): add DefaultAzureCredential support to AzureContainerVolumeHook](https://github.com/apache/airflow/pull/33822)
36. [Add AzureBatchOperator example](https://github.com/apache/airflow/pull/33716)
37. [test(providers/microsoft): add test case for AzureIdentityCredentialAdapter.signed_session](https://github.com/apache/airflow/pull/33687)
38. [fix(providers/azure): remove json.dumps when querying AzureCosmosDBHook](https://github.com/apache/airflow/pull/33653)
39. [feat(providers/azure): allow passing fully_qualified_namespace and credential to initialize Azure Service Bus Client](https://github.com/apache/airflow/pull/33493)
40. [feat(providers/microsoft): add DefaultAzureCredential support to AzureBatchHook](https://github.com/apache/airflow/pull/33469)
41. [feat(providers/microsoft): add DefaultAzureCredential support to AzureContainerInstanceHook](https://github.com/apache/airflow/pull/33467)
42. [feat(providers/microsoft): add DefaultAzureCredential support to cosmos](https://github.com/apache/airflow/pull/33436)
43. [feat(providers/microsoft): add DefaultAzureCredential to data_lake](https://github.com/apache/airflow/pull/33433)

### Make all existing sensors respect the "soft_fail" argument in BaseSensorOperator
1. [respect soft_fail argument when exception is raised for google sensors](https://github.com/apache/airflow/pull/34501)
2. [respect soft_fail argument when exception is raised for microsoft-azure sensors](https://github.com/apache/airflow/pull/34494)
3. [respect soft_fail argument when exception is raised for flink sensors](https://github.com/apache/airflow/pull/34476)
4. [respect soft_fail argument when exception is raised for jenkins sensors](https://github.com/apache/airflow/pull/34475)
5. [respect soft_fail argument when exception is raised for celery sensors](https://github.com/apache/airflow/pull/34474)
6. [Fix inaccurate test case names in providers](https://github.com/apache/airflow/pull/34473)
7. [respect soft_fail argument when exception is raised for datadog sensors](https://github.com/apache/airflow/pull/34472)
8. [respect soft_fail argument when exception is raised for http sensors](https://github.com/apache/airflow/pull/34391)
9. [respect soft_fail argument when exception is raised for sql sensors](https://github.com/apache/airflow/pull/34199)
10. [respect soft_fail argument when exception is raised for sftp sensors](https://github.com/apache/airflow/pull/34169)
11. [respect soft_fail argument when exception is raised for spark-kubernetes sensors](https://github.com/apache/airflow/pull/34167)
12. [respect soft_fail argument when exception is raised for google-marketing-platform sensors](https://github.com/apache/airflow/pull/34165)
13. [respect soft_fail argument when exception is raised for dbt sensors](https://github.com/apache/airflow/pull/34164)
14. [respect soft_fail argument when exception is raised for tableau sensors](https://github.com/apache/airflow/pull/34163)
15. [respect soft_fail argument when exception is raised for ftp sensors](https://github.com/apache/airflow/pull/34161)
16. [respect soft_fail argument when exception is raised for alibaba sensors](https://github.com/apache/airflow/pull/34157)
17. [respect soft_fail argument when exception is raised for airbyte sensors](https://github.com/apache/airflow/pull/34156)
18. [respect soft_fail argument when exception is raised for amazon sensors](https://github.com/apache/airflow/pull/34134)
19. [respect "soft_fail" argument when running BatchSensor in deferrable mode](https://github.com/apache/airflow/pull/33405)
20. [Respect "soft_fail" for core async sensors](https://github.com/apache/airflow/pull/33403)
21. [Respect "soft_fail" argument when "poke" is called](https://github.com/apache/airflow/pull/33401)
22. [respect soft_fail argument when ExternalTaskSensor runs in deferrable mode](https://github.com/apache/airflow/pull/33196)

### Add defult_deferrable configuration for easily turning on the deferrable mode of operators
1. [build(pre-commit): add list of supported deferrable operators to doc](https://github.com/apache/airflow/pull/32514)
2. [build(pre-commit): check deferrable default value](https://github.com/apache/airflow/pull/32370)
3. [Add default_deferrable config](https://github.com/apache/airflow/pull/31712) (PR of the month)

### Security improvement
1. [Disable rendering for doc_md](https://github.com/apache/airflow/pull/40522)
2. [check whether AUTH_ROLE_PUBLIC is set in check_authentication](https://github.com/apache/airflow/pull/39012)
3. [check whether AUTH_ROLE_PUBLIC is set in check_authentication](https://github.com/apache/airflow/pull/38924)
4. [fix(api_connexion): handle the cases that webserver.expose_config is set to "non-sensitive-only" instead of boolean value](https://github.com/apache/airflow/pull/32261)

### Misc (core)
1. [catch sentry flush if exception happens in _execute_in_fork finally block](https://github.com/apache/airflow/pull/40060)
2. [add PID and return code to _execute_in_fork logging](https://github.com/apache/airflow/pull/40058)
3. [add missing conn_id to string representation of ObjectStoragePath](https://github.com/apache/airflow/pull/39313)
4. [Enable "airflow tasks test" to run deferrable operator](https://github.com/apache/airflow/pull/37542)
5. [remove "to backfill" from --task-regex argument help message](https://github.com/apache/airflow/pull/34598)
6. [fix(sensors): move trigger initialization from __init___ to execute](https://github.com/apache/airflow/pull/33926)
7. [Ship zombie info](https://github.com/apache/airflow/pull/32693)
8. [Catch the exception that triggerer initialization failed](https://github.com/apache/airflow/pull/31999)
9. [feat(jobs/triggerer_job_runner): add triggerer canceled log](https://github.com/apache/airflow/pull/31757)
10. [fixing circular import error in providers caused by airflow version check](https://github.com/apache/airflow/pull/31379)

### Misc (provider)
1. [add default gcp_conn_id to GoogleBaseAsyncHook](https://github.com/apache/airflow/pull/40080)
2. [remove unexpected argument pod in read_namespaced_pod_log call](https://github.com/apache/airflow/pull/39874)
3. [fix wrong payload set when reuse_existing_run set to True in DbtCloudRunJobOperator](https://github.com/apache/airflow/pull/39271)
4. [migrate to dbt v3 api for project endpoints](https://github.com/apache/airflow/pull/39214)
5. [Replace pod_manager.read_pod_logs with client.read_namespaced_pod_log in KubernetesPodOperator._write_logs](https://github.com/apache/airflow/pull/39112)
6. [allow providing credentials through keyword argument in AzureKeyVaultBackend](https://github.com/apache/airflow/pull/34706)
7. [Fix outdated test name and description in BatchSensor](https://github.com/apache/airflow/pull/33407)
8. [add deprecation warning to DATAPROC_JOB_LOG_LINK](https://github.com/apache/airflow/pull/33189)
9. [Alias `DATAPROC_JOB_LOG_LINK` to `DATAPROC_JOB_LINK`](https://github.com/apache/airflow/pull/33148)
10. [Remove execute function of `DatabricksRunNowDeferrableOperator`](https://github.com/apache/airflow/pull/32806)
11. [Add missing execute_complete method for `DatabricksRunNowOperator`](https://github.com/apache/airflow/pull/32689)
12. [refresh connection if an exception is caught in "AzureDataFactory"](https://github.com/apache/airflow/pull/32323)
13. [feat(providers/azure): cancel pipeline if unexpected exception caught](https://github.com/apache/airflow/pull/32238)
14. [fix(providers/amazon): handle missing LogUri in emr describe_cluster API response](https://github.com/apache/airflow/pull/31482)
15. [merge AzureDataFactoryPipelineRunStatusAsyncSensor to AzureDataFactoryPipelineRunStatusSensor](https://github.com/apache/airflow/pull/30250)
16. [merge BigQueryTableExistenceAsyncSensor into BigQueryTableExistenceSensor](https://github.com/apache/airflow/pull/30235)
17. [Merge BigQueryTableExistencePartitionAsyncSensor into BigQueryTableExistencePartitionSensor](https://github.com/apache/airflow/pull/30231)
18. [Merge DbtCloudJobRunAsyncSensor logic to DbtCloudJobRunSensor](https://github.com/apache/airflow/pull/30227)
19. [Merge GCSObjectExistenceAsyncSensor logic to GCSObjectExistenceSensor](https://github.com/apache/airflow/pull/30014)

### Misc (doc only)
1. [Add in Trove classifiers Python 3.12 support](https://github.com/apache/airflow/pull/39004)
2. [add Wei Lee to committer list](https://github.com/apache/airflow/pull/38740) (This is my 133rd PR)
3. [Erd generating doc improvement](https://github.com/apache/airflow/pull/37808)
4. [fix rst code block format](https://github.com/apache/airflow/pull/34708)
5. [docs(core-airflow): replace markdown style link with rst style link](https://github.com/apache/airflow/pull/33990)
6. [docs(CONTRIBUTING): replace markdown style link with rst style link](https://github.com/apache/airflow/pull/33989)
7. [docs: fix partial doc reference error due to missing space](https://github.com/apache/airflow/pull/33770)
8. [docs(deferring): add type annotation to code examples](https://github.com/apache/airflow/pull/32422)
9. [add a note that we'll need to restart triggerer to reflect any trigger change](https://github.com/apache/airflow/pull/32140)

## Before Joining Astronomer
1. [update contributing documentations](https://github.com/apache/airflow/pull/26411)
