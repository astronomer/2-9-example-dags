"""
# Toy Helper DAG to show conditional dataset scheduling
"""

from airflow.decorators import dag, task
from airflow.datasets import Dataset


@dag(
    start_date=None,
    schedule=None,
    catchup=False,
    doc_md=__doc__,
    tags=["toy", "Conditional Dataset Scheduling"],
)
def upstream2():
    @task(outlets=[Dataset("dataset2")])
    def update_dataset_2() -> None:
        """
        Update the dataset
        """
        print("Updating dataset 2")

    update_dataset_2()


upstream2()
