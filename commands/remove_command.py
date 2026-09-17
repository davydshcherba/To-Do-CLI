from utils.decorators.logger import logger
from utils.storage import load_tasks, save_task


@logger
def remove_command(*, id: int):
    data = load_tasks()

    new_data = [task for task in data if task["id"] != id]

    if len(new_data) == len(data):
        print(f"Task with id {id} not found.")
        return

    save_task(new_data)

    print(f"Task {id} removed! Tasks total: {len(new_data)}")
