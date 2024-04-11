"""
### Toy DAG to show how to use custom names for dynamic tasks - TaskFlowAPI

This DAG queries the fruityvice API for information about all fruits. 
It then creates a dynamically mapped task printing the sugar content of each fruit, 
with the dynamically mapped task instances being named after the fruit.
"""

from airflow.decorators import dag, task
import requests
from include.helpers import get_display_fruit


@dag(
    start_date=None,
    schedule=None,
    catchup=False,
    doc_md=__doc__,
    tags=["Dynamic Task Mapping", "toy"],
)
def toy_custom_names_dynamic_tasks_taskflow():
    @task
    def get_fruits() -> list[dict]:
        import random

        rand_int = random.randint(10, 49)

        r = requests.get(f"https://www.fruityvice.com/api/fruit/all").json()
        r = random.sample(r, rand_int)

        return r

    # NEW in Airflow 2.9: Define custom names for the map index
    @task(map_index_template="{{ my_mapping_variable }}")
    def map_fruits(fruit_info: dict):
        from airflow.operators.python import get_current_context

        fruit_name = fruit_info["name"]
        sugar_content = fruit_info["nutritions"]["sugar"]
        display_fruit = get_display_fruit(fruit_name)

        context = get_current_context()
        # The map index is added after the task has run, so it can include any computed values
        # from within the task
        context["my_mapping_variable"] = (
            f"{fruit_name} - {sugar_content}g sugar."
        )

        print(f"{fruit_name} sugar content: {sugar_content}")


    map_fruits.expand(fruit_info=get_fruits())


toy_custom_names_dynamic_tasks_taskflow()
