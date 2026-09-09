from utils.decorators.logger import logger
import json


@logger
def remove_command(*, id: int):
    try:
        with open("json/tasks.json", "r", encoding="utf-8") as file:
            content = file.read().strip()
            data = json.loads(content) if content else []
    except FileNotFoundError:
        data = []

    new_data = [task for task in data if task["id"] != id]

    if len(new_data) == len(data):
        print(f"Task with id {id} not found.")
        return

    with open("json/tasks.json", "w", encoding="utf-8") as file:
        json.dump(new_data, file, indent=2, ensure_ascii=False)

    print(f"Task {id} removed! Tasks total: {len(new_data)}")
