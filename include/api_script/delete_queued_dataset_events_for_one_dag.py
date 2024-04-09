"""
Careful! This script will delete all queued dataset events fro the specified DAG.
"""

import requests
from requests.auth import HTTPBasicAuth

USERNAME = "admin"
PASSWORD = "admin"
HOST = "http://localhost:8080"

DAG_ID = "downstream2_one_in_each_group"

url = f"{HOST}/api/v1/dags/{DAG_ID}/datasets/queuedEvent"

r_get_dataset_events = requests.get(url, auth=HTTPBasicAuth(USERNAME, PASSWORD))

if r_get_dataset_events.status_code != 200:
    print(
        f"Failed to get queued dataset events for the {DAG_ID} DAG. Error: {r_get_dataset_events.text}"
    )
else:
    print(
        f"The queued dataset events for the {DAG_ID} DAG are: {r_get_dataset_events.json()['queued_events']}"
    )

    for dataset_event in r_get_dataset_events.json()["queued_events"]:
        dataset_uri = dataset_event["uri"]
        url = f"{HOST}/api/v1/dags/{DAG_ID}/datasets/queuedEvent"
        r_delete_event = requests.delete(
            url,
            json={"dataset_uri": dataset_uri},
            auth=HTTPBasicAuth(USERNAME, PASSWORD),
        )
        if r_delete_event.status_code == 200:
            print(f"Dataset event for {dataset_uri} has been deleted.")
        else:
            print(
                f"Failed to delete dataset event for {dataset_uri}. Error: {r_delete_event.text}"
            )
