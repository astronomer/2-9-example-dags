"""
## Toy DAG scheduled to run on an update to any of 4 upstream datasets
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
    ),  # Runs when any of the datasets are updated
    # NEW in Airflow 2.9: Use conditional logic to schedule a DAG based on datasets
    # Use () instead of [] to be able to use conditional dataset scheduling!
    catchup=False,
    doc_md=__doc__,
    tags=["toy", "Conditional Dataset Scheduling"],
)
def downstream1_on_any():
    @task
    def say_hello() -> None:
        """
        Print Hello
        """
        import time 
        time.sleep(10)
        print("Hello")

    say_hello()


downstream1_on_any()
