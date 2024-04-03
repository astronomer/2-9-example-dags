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
    tags=["Dataset", "toy", "Conditional Dataset Scheduling"],
)
def upstream4():
    @task(outlets=[Dataset("dataset4")])
    def update_dataset_4() -> None:
        """
        Update the dataset
        """
        print("Updating dataset 4")

    update_dataset_4()


upstream4()
