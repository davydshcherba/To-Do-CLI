from utils.decorators.logger import logger
from utils.storage import load_tasks, save_task

@logger
def add_command(* , text: str, done: str, created: str):
    existing_data = load_tasks()
    next_id = max((task["id"] for task in existing_data), default=0) + 1
    
    new_data = {
        "id": next_id,
        "text": text,
        "done": done,
        "created": created
    }

    existing_data.append(new_data)    
    save_task(existing_data)
    
    print(f"Add! Tasks total: {len(existing_data)}")