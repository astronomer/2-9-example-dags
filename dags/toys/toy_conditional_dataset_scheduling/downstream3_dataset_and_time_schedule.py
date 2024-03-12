"""
# Toy DAG scheduled to run on a cron schedule and an update to any of 2 upstream datasets
"""

from airflow.decorators import dag, task
from airflow.datasets import Dataset
from pendulum import datetime
from airflow.timetables.datasets import DatasetOrTimeSchedule
from airflow.timetables.trigger import CronTriggerTimetable


@dag(
    start_date=datetime(2024, 3, 1),
    schedule=DatasetOrTimeSchedule(
        timetable=CronTriggerTimetable("*/2 * * * *", timezone="UTC"),
        datasets=(Dataset("dataset3") | Dataset("dataset4")),
    ),  # Use () instead of [] to be able to use conditional dataset scheduling!
    catchup=False,
    doc_md=__doc__,
    tags=["Dataset", "2-9", "toy", "toy conditional dataset scheduling"],
)
def toy_downstream3_dataset_and_time_schedule():
    @task
    def say_hello() -> None:
        """
        Print Hello
        """
        print("Hello")

    say_hello()


toy_downstream3_dataset_and_time_schedule()
