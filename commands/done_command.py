from utils.decorators.logger import logger
from utils.storage import load_tasks
import json


@logger
def done_command(*, id: int):
    data = load_tasks()

    found = False
    for task in data:
        if task["id"] == id:
            task["done"] = "True"
            found = True
            break

    if not found:
        print(f"Task with id {id} not found.")
        return

    with open("json/tasks.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

    print(f"Task {id} marked as done!")
