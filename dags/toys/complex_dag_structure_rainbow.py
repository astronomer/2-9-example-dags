"""
## Example DAG with a complex structure

This DAG doesn't really do anything other than attempting to look pretty.
Used to show UI features.
"""

from airflow.decorators import dag, task_group, task
from airflow.operators.empty import EmptyOperator
from airflow.models.baseoperator import chain, chain_linear
from airflow.utils.edgemodifier import Label
from airflow.datasets import Dataset
from pendulum import datetime

from include.rainbow_operators.rainbow_operators import (
    ExtractFromObjectStorageOperator,
    TransformOperator,
    LoadtoDWHOperator,
    LoadAPItoDWHOperator,
    TransformReportOperator,
    PublishReportOperator,
    SpinUpGPUOperator,
    TrainProprietaryLLMOperator,
    TearDownGPUOperator,
)


@dag(
    start_date=datetime(2024, 1, 1),
    schedule=[Dataset("s3://in_sales_data"), Dataset("az://in_internal_api")],
    catchup=False,
    doc_md=__doc__,
    dag_display_name="🌈 Rägeboge DAG",  # NEW in Airflow 2.9: Define a display name that can include non-ascii characters
    # (the dag_id only allows alphanumeric characters, dashes, dots and underscores)
    tags=["toy", "UI DAG"],
)
def complex_dag_structure_rainbow():

    start = EmptyOperator(task_id="start", task_display_name="🏁")

    sales_data_extract = ExtractFromObjectStorageOperator.partial(
        task_id="sales_data_extract", 
        task_display_name="📦 für Sales!"
    ).expand(my_param=[1, 2, 3, 4])
    internal_api_extract = ExtractFromObjectStorageOperator.partial(
        task_id="internal_api_extract"
    ).expand(my_param=[1, 2, 3, 4])

    @task.branch
    def determine_load_type():
        return "internal_api_load_incremental"

    sales_data_transform = TransformOperator(task_id="sales_data_transform")

    determine_load_type_obj = determine_load_type()

    sales_data_load = LoadtoDWHOperator(task_id="sales_data_load")
    internal_api_load_full = LoadAPItoDWHOperator(task_id="internal_api_load_full")
    internal_api_load_incremental = LoadAPItoDWHOperator(
        task_id="internal_api_load_incremental"
    )

    @task_group()
    def sales_data_reporting(a):
        prepare_report = TransformReportOperator(
            task_id="prepare_report", trigger_rule="all_done"
        )
        publish_report = PublishReportOperator(task_id="publish_report")

        chain(prepare_report, publish_report)

    sales_data_reporting_obj = sales_data_reporting.expand(a=[1, 2, 3, 4, 5, 6])

    @task_group
    def cre_integration():
        cre_extract = EmptyOperator(task_id="cre_extract", trigger_rule="all_done")
        cre_transform = EmptyOperator(task_id="cre_transform")
        cre_load = EmptyOperator(task_id="cre_load")

        chain(cre_extract, cre_transform, cre_load)

    cre_integration_obj = cre_integration()

    @task_group()
    def mlops():
        set_up_cluster = SpinUpGPUOperator(
            task_id="set_up_cluster", trigger_rule="all_done"
        )
        train_model = TrainProprietaryLLMOperator(
            task_id="train_model", outlets=[Dataset("model_trained")]
        )
        tear_down_cluster = TearDownGPUOperator(task_id="tear_down_cluster")

        chain(set_up_cluster, train_model, tear_down_cluster)

        tear_down_cluster.as_teardown(setups=set_up_cluster)

    mlops_obj = mlops()

    end = EmptyOperator(task_id="end", task_display_name="✅")

    chain(
        start,
        sales_data_extract,
        sales_data_transform,
        sales_data_load,
        [sales_data_reporting_obj, cre_integration_obj],
        end,
    )
    chain(
        start,
        internal_api_extract,
        determine_load_type_obj,
        [internal_api_load_full, internal_api_load_incremental],
        mlops_obj,
        end,
    )

    chain_linear(
        [sales_data_load, internal_api_load_full],
        [sales_data_reporting_obj, cre_integration_obj],
    )

    chain(
        determine_load_type_obj, Label("additional data"), internal_api_load_incremental
    )
    chain(
        determine_load_type_obj, Label("changed existing data"), internal_api_load_full
    )


complex_dag_structure_rainbow()
