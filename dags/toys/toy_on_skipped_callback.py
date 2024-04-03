"""
### Toy DAG showing the on_skipped_callback

on_skipped_callback: 
- is executed only if an AirflowSkipException gets raised.
- Explicitly it is NOT called if a task is not started to be executed because of a preceding branching
decision in the DAG or a trigger rule which causes execution to skip so that the task execution
is never scheduled.
"""

from airflow.decorators import dag, task
from airflow.exceptions import AirflowSkipException
from airflow.providers.slack.notifications.slack_notifier import SlackNotifier
from airflow.operators.empty import EmptyOperator
from airflow.models.baseoperator import chain
import time

SLACK_CONNECTION_ID = "slack_conn"
SLACK_CHANNEL = "alerts"
SLACK_MESSAGE = """
Hello! The {{ ti.task_id }} task has been SKIPPED! :wave: 
Timestamp {{ ts }} and this task finished with the state: {{ ti.state }} :tada:.
"""

slack_notifier_instantiated = SlackNotifier(
    slack_conn_id=SLACK_CONNECTION_ID,
    text=SLACK_MESSAGE,
    channel=SLACK_CHANNEL,
)


@dag(
    start_date=None,
    schedule=None,
    catchup=False,
    doc_md=__doc__,
    tags=["on_skipped_callback"],
)
def toy_on_skipped_callback():

    # NEW in Airflow 2.9: on_skipped_callback to fire if an AirflowSkipException is raised
    # This callback is executed only if an AirflowSkipException gets raised, not if a task is skipped
    # because of a branching decision or a trigger rule.
    @task(on_skipped_callback=slack_notifier_instantiated)
    def task_that_raises_skip_exception():
        time.sleep(5)
        raise AirflowSkipException("This task is skipped")

    task_that_raises_skip_exception()

    @task.branch
    def eins_zwei_oder_drei():
        import random

        number = random.choice([1, 2, 3])
        if number == 1:
            return "task_eins"
        elif number == 2:
            return "task_zwei"
        else:
            return "task_drei"

    @task(on_skipped_callback=slack_notifier_instantiated)
    def task_eins():
        print("Eins")

    @task(on_skipped_callback=slack_notifier_instantiated)
    def task_zwei():
        print("Zwei")

    @task(on_skipped_callback=slack_notifier_instantiated)
    def task_drei():
        print("Drei")

    end = EmptyOperator(task_id="end", trigger_rule="none_failed_or_skipped")

    chain(eins_zwei_oder_drei(), [task_eins(), task_zwei(), task_drei()], end)


toy_on_skipped_callback()
