from utils.decorators.logger import logger
from utils.storage import load_tasks
import json


@logger
def remove_command(*, id: int):
    data = load_tasks()

    new_data = [task for task in data if task["id"] != id]

    if len(new_data) == len(data):
        print(f"Task with id {id} not found.")
        return

    with open("json/tasks.json", "w", encoding="utf-8") as file:
        json.dump(new_data, file, indent=2, ensure_ascii=False)

    print(f"Task {id} removed! Tasks total: {len(new_data)}")
