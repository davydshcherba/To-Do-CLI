import json
from utils.decorators.logger import logger
from utils.storage import load_tasks

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
    
    with open("json/tasks.json", "w", encoding="utf-8") as file:
        json.dump(existing_data, file, indent=2, ensure_ascii=False)
    
    print(f"Add! Tasks total: {len(existing_data)}")