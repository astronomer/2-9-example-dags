"""
### Toy DAG to show how to use custom names for dynamic tasks - TaskFlowAPI

This DAG queries the fruityvice API for information about all fruits. 
It then creates a dynamically mapped task printing the sugar content of each fruit, 
with the dynamically mapped task instances being named after the fruit.
"""

from airflow.decorators import dag, task
import requests


@dag(
    start_date=None,
    schedule=None,
    catchup=False,
    doc_md=__doc__,
    tags=["dynamic task mapping", "2-9", "toy"],
)
def toy_custom_names_dynamic_tasks_taskflow():
    @task
    def get_fruits() -> list[dict]:

        r = requests.get(f"https://www.fruityvice.com/api/fruit/all").json()
        return r

    @task(map_index_template="""{{ my_mapping_variable }}""")
    def map_fruits(fruit_info: dict):
        from airflow.operators.python import get_current_context

        fruit_name = fruit_info["name"]
        context = get_current_context()
        context["my_mapping_variable"] = fruit_name
        print(f"{fruit_name} sugar content: {fruit_info['nutritions']['sugar']}")

    map_fruits.expand(fruit_info=get_fruits())


toy_custom_names_dynamic_tasks_taskflow()
