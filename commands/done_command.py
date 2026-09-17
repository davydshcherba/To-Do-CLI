from utils.decorators.logger import logger
from utils.storage import load_tasks, save_tasks


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

    save_tasks(data)

    print(f"Task {id} marked as done!")
