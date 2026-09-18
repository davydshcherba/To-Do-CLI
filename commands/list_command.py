from utils.decorators.logger import logger
from utils.storage import load_tasks

@logger
def list_command():
    data = load_tasks()

    if not data:
        print("No tasks yet. Use add to create one.")
        return

    for task in data:
        mark = "x" if task["done"] else " "
        print(f"[{mark}] {task['id']}. {task['text']} ({task['created']})")
