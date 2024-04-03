"""
### Toy using a custom operator showing multiple xcom pushing
"""

from airflow.decorators import dag, task
from include.toy_helpers.custom_operators import MyBasicMathOperator


@dag(
    start_date=None,
    schedule=None,
    catchup=False,
    doc_md=__doc__,
    tags=["xcom", "toy"],
)
def toy_custom_operator_push_multiple_xcom():

    no_multiple_outputs_task = MyBasicMathOperator(
        task_id="no_multiple_outputs_task",
        first_number=23,
        second_number=19,
        operation="+",
    )

    multiple_outputs_task = MyBasicMathOperator(
        task_id="multiple_outputs_task",
        first_number=23,
        second_number=19,
        operation="+",
        multiple_outputs=True,  # NEW in Airflow 2.9: set multiple_outputs on the BaseOperator
    )


toy_custom_operator_push_multiple_xcom()
