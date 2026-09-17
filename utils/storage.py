import json
import os
from pathlib import Path

APP_DIR = Path.home() / ".todo-cli"
TASKS_FILE = APP_DIR / "tasks.json"

def load_tasks():
    try:
        with open(TASKS_FILE, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            data = json.loads(content) if content else []
    except FileNotFoundError:
        data = []

    if not isinstance(data, list):
        data = [data]

    return data

def save_task(existing_data):
    os.makedirs(os.path.dirname(TASKS_FILE), exist_ok=True)
    with open(TASKS_FILE, "w", encoding="utf-8") as file:
        json.dump(existing_data, file, indent=2, ensure_ascii=False)