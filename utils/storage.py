import json

TASKS_FILE = "json/tasks.json"

def load_tasks():
    try:
        with open(TASKS_FILE, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            data = json.loads(content) if content else []
    except FileNotFoundError:
            data = []

    if not isinstance(existing_data, list):
        existing_data = [existing_data]

    return data

def add_task(existing_data):
    with open("json/tasks.json", "w", encoding="utf-8") as file:
        json.dump(existing_data, file, indent=2, ensure_ascii=False)