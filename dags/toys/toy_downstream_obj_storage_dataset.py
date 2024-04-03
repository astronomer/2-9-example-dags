"""
## Toy DAG to show how to use a Dataset in the ObjectStoragePath class - downstream

As of Airflow 2.9, the ObjectStoragePath class now recognizes the Dataset object.
Use together with the toy_upstream_obj_storage_dataset DAG.
"""

from airflow.decorators import dag, task
from airflow.io.path import ObjectStoragePath
from pendulum import datetime
from airflow.datasets import Dataset

MY_DATASET = Dataset("file://include/toy_helpers/my_text_file.txt")
MY_CONN_ID = None  # connecting to the local file system does not require a connection


@dag(
    start_date=datetime(2024, 3, 1),
    schedule=[MY_DATASET],
    catchup=False,
    doc_md=__doc__,
    tags=["ObjectStorage", "toy", "Dataset"],
)
def toy_downstream_obj_storage_dataset():

    @task
    def read_text_from_file(my_dataset: Dataset, my_conn_id: str) -> None:
        """
        Read contents from the file passed into the ObjectStoragePath class
        using the Dataset Object.
        Args:
            my_dataset (Dataset): The dataset to read from.
            my_conn_id (str): The connection id to use.
        """
        # NEW in 2.9: The ObjectStoragePath class now recognizes the Dataset object
        contents = ObjectStoragePath(my_dataset, conn_id=my_conn_id).read_text()
        print(contents)

    read_text_from_file(my_dataset=MY_DATASET, my_conn_id=MY_CONN_ID)


toy_downstream_obj_storage_dataset()
