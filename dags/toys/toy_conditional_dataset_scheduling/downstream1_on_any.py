"""
# Toy DAG scheduled to run on an update to any of 4 upstream datasets
"""

from airflow.decorators import dag, task
from airflow.datasets import Dataset
from pendulum import datetime


@dag(
    start_date=datetime(2024, 3, 1),
    schedule=(
        Dataset("dataset1")
        | Dataset("dataset2")
        | Dataset("dataset3")
        | Dataset("dataset4")
    ),  # Use () instead of [] to be able to use conditional dataset scheduling!
    catchup=False,
    doc_md=__doc__,
    tags=["Dataset", "2-9", "toy", "toy conditional dataset scheduling"],
)
def downstream1_on_any():
    @task
    def say_hello() -> None:
        """
        Print Hello
        """
        print("Hello")

    say_hello()


downstream1_on_any()
