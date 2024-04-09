"""
### Toy DAG to show default dynamic task indices
"""

from airflow.decorators import dag, task
import requests


@dag(
    start_date=None,
    schedule=None,
    catchup=False,
    doc_md=__doc__,
    tags=["Dynamic Task Mapping", "toy"],
)
def toy_dynamic_task_default_index():
    @task
    def get_fruits() -> list[dict]:
        import random

        rand_int = random.randint(10, 49)

        r = requests.get(f"https://www.fruityvice.com/api/fruit/all").json()
        r = random.sample(r, rand_int)

        return r

    @task
    def map_fruits(fruit_info: dict):

        fruit_name = fruit_info["name"]
        sugar_content = fruit_info["nutritions"]["sugar"]

        print(f"{fruit_name} sugar content: {sugar_content}")

    map_fruits.expand(fruit_info=get_fruits())


toy_dynamic_task_default_index()
