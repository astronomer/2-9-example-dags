from airflow.decorators import dag, task
from pendulum import datetime


@dag(
    start_date=datetime(2024, 1, 1),
    schedule="0 * * * *",
    catchup=False,
    max_consecutive_failed_dag_runs=5,
    doc_md=__doc__,
)
def toy_auto_pause():
    @task
    def say_hello() -> None:
        raise (Exception("Hello, I am an exception!"))

    say_hello()


toy_auto_pause()
