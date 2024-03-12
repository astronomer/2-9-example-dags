"""
### Toy with tasks of different durations that randomly fail

Use this DAG to showcase failed tasks in the Gantt chart.
"""

from airflow.decorators import dag, task
from airflow.exceptions import AirflowException
import time
import random

random.seed(42)


@dag(
    start_date=None,
    schedule=None,
    catchup=False,
    doc_md=__doc__,
    tags=["UI", "2-9", "toy"],
)
def toy_task_fail_entries_in_gantt():

    @task
    def two_second_plus_delay_task() -> None:
        delay = random.randint(0, 10)
        fail = random.choice([True, False])
        time.sleep(2 + delay)
        if fail:
            raise AirflowException("Task failed")

    @task
    def five_second_plus_delay_task() -> None:
        delay = random.randint(0, 10)
        fail = random.choice([True, False])
        time.sleep(5 + delay)
        if fail:
            raise AirflowException("Task failed")
        

    @task
    def ten_second_plus_delay_task() -> None:
        delay = random.randint(0, 10)
        fail = random.choice([True, False])
        time.sleep(10 + delay)
        if fail:
            raise AirflowException("Task failed")

    @task
    def twenty_second_plus_delay_task() -> None:
        delay = random.randint(0, 10)
        fail = random.choice([True, False])
        time.sleep(20 + delay)
        if fail:
            raise AirflowException("Task failed")

    @task
    def thirty_second_plus_delay_task() -> None:
        delay = random.randint(0, 10)
        fail = random.choice([True, False])
        time.sleep(30 + delay)
        if fail:
            raise AirflowException("Task failed")

    two_second_plus_delay_task()
    five_second_plus_delay_task()
    ten_second_plus_delay_task()
    twenty_second_plus_delay_task()
    thirty_second_plus_delay_task()



toy_task_fail_entries_in_gantt()
