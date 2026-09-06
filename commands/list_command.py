from utils.decorators.logger import logger
import json

@logger
def list_command():
    with open("json/tasks.json", 'r', encoding='utf-8') as file:
            data = json.load(file)
            print(json.dumps(data, indent=2, ensure_ascii=False))