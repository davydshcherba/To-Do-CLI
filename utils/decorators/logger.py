from typing import Callable
from datetime import datetime
import json
import os

def logger(func: Callable):
    def wrapper(*args,**kwargs):
        today = datetime.today().strftime('%Y-%m-%d')
        dataLog = {
            "log": func.__name__,
            "date": f"{datetime.now().strftime('%H:%M:%S')}"
        }
        os.makedirs("_log", exist_ok=True)

        log_path = f"_log/{today}.json"
        if os.path.exists(log_path):
            with open(log_path, "r", encoding="utf-8") as file:
                entries = json.load(file)
        else:
            entries = []
        entries.append(dataLog)

        with open(log_path, "w", encoding="utf-8") as file:
            json.dump(entries, file, indent=2, ensure_ascii=False)

        func(*args,**kwargs)
    return wrapper