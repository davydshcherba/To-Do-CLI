from typing import Callable
from datetime import datetime
import json

def logger(func: Callable):
    def wrapper(*args,**kwargs):
        today = datetime.today().strftime('%Y-%m-%d')
        dataLog = {
            "log": f"{func}",
            "date": f"{datetime.now().strftime("%H:%M:%S")}"
        }
        with open(f"_log/{today}.json", "a", encoding="utf-8") as file:
            json.dump(dataLog, file, indent=2, ensure_ascii=False)

        func(*args,**kwargs)
    return wrapper