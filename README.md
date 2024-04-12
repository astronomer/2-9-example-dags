# Data Science DAGs with Apache Airflow 2.9

This repository contains example DAGs showing features released in Apache Airflow 2.9. 

Aside from core Apache Airflow this project uses:
- The [Astro CLI](https://docs.astronomer.io/astro/cli/install-cli) to run Airflow locally (version 1.25.0).
- The [Amazon Airflow provider](https://registry.astronomer.io/providers/apache-airflow-providers-amazon/versions/latest) with the `s3fs` extra installed.
- The [Google Airflow provider](https://registry.astronomer.io/providers/apache-airflow-providers-google/versions/latest).
- The [Microsoft Azure Airflow provider](https://registry.astronomer.io/providers/apache-airflow-providers-microsoft-azure/versions/latest).
- The [Common IO Airflow provider](https://registry.astronomer.io/providers/apache-airflow-providers-common-io/versions/latest).
- The [Slack Airflow provider](https://registry.astronomer.io/providers/apache-airflow-providers-slack/versions/latest).
- The [Snowflake Airflow provider](https://registry.astronomer.io/providers/apache-airflow-providers-snowflake/versions/latest).
- The [transformers](https://pypi.org/project/transformers/) package.
- The [torch](https://pypi.org/project/torch/) package.

For pinned versions of the provider packages see the `requirements.txt` file.

> [!NOTE]  
> You can find new Airflow 2.9 features in the DAG code by searching for `# NEW in Airflow 2.9:`.

# How to use this repository

This section explains how to run this repository with Airflow. 

> [!NOTE]  
> Some DAGs in this repository require additional connections or tools. 
> You can define these connection in the Airflow UI under **Admin > Connections** or by using the `.env` file with the format shown in `.env.example`.
> The [`load_to_snowflake`](dags/data-engineering-use-case/ingestion/load_to_snowflake.py) DAG requires some additional setup in Snowflake, see the DAG docstring for more information.
> DAGs with the tag `toy` work without any additional connections or tools.

See the [Manage Connections in Apache Airflow](https://docs.astronomer.io/learn/connections) guide for further instructions on Airflow connections. 

## Steps to run this repository

Download the [Astro CLI](https://docs.astronomer.io/astro/cli/install-cli) to run Airflow locally in Docker. `astro` is the only package you will need to install.

1. Run `git clone https://github.com/astronomer/2-9-example-dags.git` on your computer to create a local clone of this repository.
2. Install the Astro CLI by following the steps in the [Astro CLI documentation](https://docs.astronomer.io/astro/cli/install-cli). Docker Desktop/Docker Engine is a prerequisite, but you don't need in-depth Docker knowledge to run Airflow with the Astro CLI.
3. Run `astro dev start` in your cloned repository.
4. After your Astro project has started. View the Airflow UI at `localhost:8080`.

# DAGs

The following sections list the DAGs shown sorted by the feature that they showcase. You can filter DAGs in the UI by their `tags`.

### data-enineering-use-case

The DAGs in the [data-engineering-use-case](dags/data-engineering-use-case) folder showcase a data engineering use case using AWS and Snowflake with several Airflow 2.9 features implemented throughout the DAGs. 

- [`create_ingestion_dags`](dags/data-engineering-use-case/ingestion/create_ingestion_dags.py): is a script to dynamically create 3 DAGs based on the [include/ingestion_source_config.json](include/ingestion_source_config.json) file.
- [`load_to_snowflake`](dags/data-engineering-use-case/ingestion/load_to_snowflake.py): DAG that loads data from S3 to Snowflake. Uses conditional dataset scheduling.
- [`analyze_customer_feedback`](dags/data-engineering-use-case/analyze_customer_feedback.py): DAG that runs sentiment analysis on customer feedback data. Uses named dynamic task indexes.
- [`prepare_earnings_report`](dags/data-engineering-use-case/prepare_earnings_report.py): DAG hat creates a report on earnings data. Uses a DatasetOrTimeSchedule.

### Dataset toys

The DAGs in the [toy_conditional_dataset_scheduling](dags/toys/toy_conditional_dataset_scheduling/) folder show new ways to use dataset scheduling without needing any additional connections or tools.

- `upstream1`, `upstream2`, `upstream3` and `upstream4` are helper DAGs that update the datasets `dataset1`, `dataset2`, `dataset3` and `dataset4` respectively.
- [`downstream1_on_any`](dags/toys/toy_conditional_dataset_scheduling/downstream1_on_any.py): DAG that runs when any of the upstream datasets are updated.
- [`downstream2_one_in_each_group`](dags/toys/toy_conditional_dataset_scheduling/downstream2_one_in_each_group.py): DAG that runs when one dataset from each group is updated.
- [`downstream3_dataset_and_time_schedule`](dags/toys/toy_conditional_dataset_scheduling/downstream3_dataset_and_time_schedule.py): DAG that runs on a dataset schedule and a time schedule.

### Other

- [`complex_dag_structure_rainbow`](dags/toys/complex_dag_structure_rainbow.py): DAG to see UI features with a complex structure. Uses custom operators from [include/rainbow_operators/rainbow_operators.py](include/rainbow_operators/rainbow_operators.py).
- [`toy_auto_pause`](dags/toys/toy_auto_pause.py): DAG that shows how to use the `max_consecutive_failed_dag_runs` parameter.
- [`toy_custom_names_dynamic_tasks_taskflow`](dags/toys/toy_custom_names_dynamic_tasks_taskflow.py): DAG that shows how to use custom names for dynamic tasks map indexes with `@task`.
- [`toy_custom_names_dynamic_tasks_traditional_operators`](dags/toys/toy_custom_names_dynamic_tasks_traditional_operators.py): DAG that shows how to use custom names for dynamic tasks map indexes with traditional operators.
- [`toy_custom_operator_push_multiple_xcom`](dags/toys/toy_custom_operator_push_multiple_xcom.py): DAG that shows how to push multiple XComs from any operator. Uses a custom operator from [include/toy_helpers/custom_operators.py](include/toy_helpers/custom_operators.py).
- [`toy_upstream_obj_storage_dataset`](dags/toys/toy_upstream_obj_storage_dataset.py): DAG that shows how to use ObjectStoragePath with a Dataset object. Upstream.
- [`toy_downstream_obj_storage_dataset`](dags/toys/toy_downstream_obj_storage_dataset.py): DAG that shows how to use ObjectStoragePath with a Dataset object. Downstream.
- [`toy_on_skipped_callback`](dags/toys/toy_on_skipped_callback.py): DAG that shows how to use the `on_skipped_callback` parameter. Uses a slack connection for the callback.
- [`toy_task_duration_page`](dags/toys/toy_task_duration_page.py): DAG created to showcase the task duration page.
- [`toy_taskflow_bash`](dags/toys/toy_taskflow_bash.py): DAG that shows the `@task.bash` decorator.
- [`toy_xcom_big_v_small`](dags/toys/toy_xcom_big_v_small.py): DAG that pushes a big and a small object to XCom to be used with an ObjectStorage custom XCom backend using a threshold. (see `.env.example` for configuration).

## Useful links

- [Datasets guide](https://docs.astronomer.io/learn/airflow-datasets).
- [Dynamic Task Mapping guide](https://docs.astronomer.io/learn/dynamic-tasks).
- Options for custom XCom backends in Airflow guide: Coming soon!
- Set up a custom XCom backend using Object Storage tutorial: Coming soon!
- [Object Storage Basic tutorial](https://docs.astronomer.io/learn/airflow-object-storage-tutorial).
- [Object Storage OSS Docs tutorial](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/objectstorage.html#object-storage).
- [Object Storage OSS Docs guide](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/objectstorage.html#object-storage).
- [Airflow Config reference](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html).

# Project Structure

This repository contains the following files and folders:

- `.astro`: files necessary for Astro CLI commands.
-  `dags`: all DAGs in your Airflow environment. Files in this folder will be parsed by the Airflow scheduler when looking for DAGs to add to your environment. You can add your own dagfiles in this folder.
- `include`: supporting files that will be included in the Airflow environment. Among other files contains the code for the listener plugin in `include/listeners.py`.
- `plugins`: folder to place Airflow plugins. Contains a listener plugin.
- `tests`: folder to place pytests running on DAGs in the Airflow instance. Contains default tests.
- `.astro-registry.yaml`: file to configure DAGs being uploaded to the [Astronomer registry](https://registry.astronomer.io/). Can be ignored for local development.
- `.dockerignore`: list of files to ignore for Docker.
- `.env.example`: example environment variables for the DAGs in this repository. Copy this file to `.env` and replace the values with your own credentials.
- `.gitignore`: list of files to ignore for git.
- `Dockerfile`: the Dockerfile using the Astro CLI. Sets environment variables to change Airflow webserver settings.
- `packages.txt`: system-level packages to be installed in the Airflow environment upon building of the Docker image. Empty.
- `README.md`: this Readme.
- `requirements.txt`: python packages to be installed to be used by DAGs upon building of the Docker image.
