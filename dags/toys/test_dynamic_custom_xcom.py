from airflow.decorators import dag, task
import requests


@dag(
    start_date=None,
    schedule=None,
    catchup=False,
)
def test_dynamic_custom_xcom():
    @task
    def get_fruits() -> list[dict]:

        r = requests.get(f"https://www.fruityvice.com/api/fruit/all").json()
        return r

    @task
    def map_fruits(fruit_info: dict):
        from airflow.operators.python import get_current_context

        print(fruit_info)

    map_fruits.expand(fruit_info=get_fruits())


test_dynamic_custom_xcom()
