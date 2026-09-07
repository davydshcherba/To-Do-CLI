from utils.decorators.logger import logger
import json


@logger
def done_command(*, id: int):
    try:
        with open("json/tasks.json", "r", encoding="utf-8") as file:
            content = file.read().strip()
            data = json.loads(content) if content else []
    except FileNotFoundError:
        data = []

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
