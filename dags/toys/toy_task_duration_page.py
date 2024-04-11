"""
### Toy with tasks of different durations

Use this DAG to showcase the new task duration page in the UI.
"""

from airflow.decorators import dag, task
import time
import random
from pendulum import datetime

random.seed(42)


@dag(
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    doc_md=__doc__,
    tags=["UI", "toy"],
)
def toy_task_duration_page():

    @task
    def two_second_plus_delay_task() -> None:
        delay = random.randint(0, 10)
        time.sleep(2 + delay)

    @task
    def five_second_plus_delay_task() -> None:
        delay = random.randint(0, 10)
        time.sleep(5 + delay)

    @task
    def ten_second_plus_delay_task() -> None:
        delay = random.randint(0, 10)
        time.sleep(10 + delay)

    @task
    def twenty_second_plus_delay_task() -> None:
        delay = random.randint(0, 10)
        time.sleep(20 + delay)

    @task
    def thirty_second_plus_delay_task() -> None:
        delay = random.randint(0, 10)
        time.sleep(30 + delay)

    two_second_plus_delay_task()
    five_second_plus_delay_task()
    ten_second_plus_delay_task()
    twenty_second_plus_delay_task()
    thirty_second_plus_delay_task()


toy_task_duration_page()
