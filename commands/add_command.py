from datetime import datetime
from utils.decorators.logger import logger
from utils.storage import load_tasks, save_task

@logger
def add_command(* , text: str):
    existing_data = load_tasks()
    next_id = max((task["id"] for task in existing_data), default=0) + 1
    created = datetime.now().strftime("%d.%m.%Y")

    new_data = {
        "id": next_id,
        "text": text,
        "done": False,
        "created": created
    }

    existing_data.append(new_data)    
    save_task(existing_data)
    
    print(f"Add! Tasks total: {len(existing_data)}")