"""
### Toy using @task.bash
"""

from airflow.decorators import dag, task


@dag(
    start_date=None,
    schedule=None,
    catchup=False,
    doc_md=__doc__,
    tags=["@task.bash", "toy"],
)
def toy_taskflow_bash():

    @task
    def upstream_task():
        dog_owner_data = {
            "names": ["Trevor", "Grant", "Marcy", "Carly", "Philip"],
            "dogs": [1, 2, 2, 0, 4],
        }

        return dog_owner_data

    # NEW in Airflow 2.9: task.bash, the string that is returned will be executed as a bash command
    @task.bash
    def bash_task(dog_owner_data):
        names_of_dogless_people = []
        for name, dog in zip(dog_owner_data["names"], dog_owner_data["dogs"]):
            if dog < 1:
                names_of_dogless_people.append(name)

        if names_of_dogless_people:
            if len(names_of_dogless_people) == 1:
                return f'echo "{names_of_dogless_people[0]} urgently needs a dog!"'
            else:
                names_of_dogless_people_str = " and ".join(names_of_dogless_people)
                return f'echo "{names_of_dogless_people_str} urgently need a dog!"'
        else:
            return f'echo "All good, everyone has at least one dog!"'

    bash_task(dog_owner_data=upstream_task())


toy_taskflow_bash()

