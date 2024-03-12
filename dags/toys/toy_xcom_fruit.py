"""
### Query the Fruityvice API for information about a fruit

This DAG queries the [Fruityvice API](https://www.fruityvice.com/) for 
information about a fruit. It pushes the information to XCom and reads it from XCom.
"""

from airflow.decorators import dag, task
from pendulum import datetime
from airflow.models.param import Param
from airflow.models.baseoperator import chain
import requests


@dag(
    start_date=None,
    schedule=None,
    catchup=False,
    params={
        "my_fruit": Param(
            "strawberry", description="The fruit to get info about.", type="string"
        )
    },
    doc_md=__doc__,
    tags=["xcom", "2-9", "toy"],
)
def toy_xcom_fruit():
    @task
    def get_fruit_info(**context):
        my_fruit = context["params"]["my_fruit"]

        r = requests.get(f"https://www.fruityvice.com/api/fruit/{my_fruit}").json()

        for k, v in r.items():
            context["ti"].xcom_push(key=k, value=v)

        return r

    @task
    def read_info_from_xcom(**context):
        fruit_info = context["ti"].xcom_pull(task_ids="get_fruit_info")
        print(fruit_info)

    chain(get_fruit_info(), read_info_from_xcom())


toy_xcom_fruit()
