import json

TASKS_FILE = "json/tasks.json"

def load_tasks():
    try:
        with open(TASKS_FILE, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            data = json.loads(content) if content else []
    except FileNotFoundError:
            data = []

    return data