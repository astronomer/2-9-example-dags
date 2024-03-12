"""
## Toy DAG to show size dependant custom XCom serialization

This DAG pushes two dicts to XCom, one below, one above 1000 bytes. It then pulls them and prints their sizes.
Use this DAG together with the XComObjectStoreBackend's xcom_objectstorage_threshold
configuration.
See: https://airflow.apache.org/docs/apache-airflow-providers-common-io/stable/configurations-ref.html#xcom-objectstorage-threshold
"""

from airflow.decorators import dag, task
from airflow.models.baseoperator import chain


@dag(
    start_date=None,
    schedule=None,
    catchup=False,
    doc_md=__doc__,
    tags=["xcom", "2-9", "toy"],
)
def toy_xcom_big_v_small():
    @task
    def push_dicts(**context) -> None:
        """Create a small and a big dictionary, print their sizes and push them to XCom."""

        my_small_dict = {"a": 23}
        my_big_dict = {f"key{i}": "x" * 100 for i in range(100)}
        print(f"Size of small dictionary: {my_small_dict.__sizeof__()}")
        print(f"Size of big dictionary: {my_big_dict.__sizeof__()}")

        context["ti"].xcom_push(key="small_dict", value=my_small_dict)
        context["ti"].xcom_push(key="big_dict", value=my_big_dict)

    @task
    def pull_dicts(**context) -> None:
        """Pull the small and big dictionaries from XCom and print their sizes."""

        small_dict = context["ti"].xcom_pull(task_ids="push_dicts", key="small_dict")
        big_dict = context["ti"].xcom_pull(task_ids="push_dicts", key="big_dict")

        print(f"Size of small dictionary: {small_dict.__sizeof__()}")
        print(f"Size of big dictionary: {big_dict.__sizeof__()}")

    chain(push_dicts(), pull_dicts())


toy_xcom_big_v_small()
