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
    tags=["Dataset", "2-9", "toy", "toy conditional dataset scheduling"],
)
def upstream3():
    @task(
        outlets=[Dataset("dataset3")]
    )
    def update_dataset_3() -> None:
        """
        Update the dataset
        """
        print("Updating dataset 3")

    update_dataset_3()

upstream3()