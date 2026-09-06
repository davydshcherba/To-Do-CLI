from utils.decorators.logger import logger
import json

@logger
def list_command():
    try:
        with open("json/tasks.json", 'r', encoding='utf-8') as file:
            content = file.read().strip()
            data = json.loads(content) if content else []
    except FileNotFoundError:
        data = []

    print(json.dumps(data, indent=2, ensure_ascii=False))