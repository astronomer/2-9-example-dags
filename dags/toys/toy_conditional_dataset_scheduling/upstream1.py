"""
# Toy Helper DAG to show conditional dataset scheduling
"""

from airflow.decorators import dag, task
from airflow.datasets import Dataset
from pendulum import datetime

@dag(
    start_date=datetime(2024, 3, 1),
    schedule=[Dataset("dataset0")],
    catchup=False,
    doc_md=__doc__,
    tags=["Dataset", "2-9", "toy", "Conditional Dataset Scheduling"],
)
def upstream1():
    @task(
        outlets=[Dataset("dataset1")]
    )
    def update_dataset_1() -> None:
        """
        Update the dataset
        """
        print("Updating dataset 1")

    update_dataset_1()

upstream1()