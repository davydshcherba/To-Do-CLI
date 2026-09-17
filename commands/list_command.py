from utils.decorators.logger import logger
from utils.storage import load_tasks
import json

@logger
def list_command():
    data = load_tasks()

    print(json.dumps(data, indent=2, ensure_ascii=False))