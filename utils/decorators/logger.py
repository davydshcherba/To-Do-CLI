from typing import Callable
from datetime import datetime
import json

def logger(func: Callable):
    def wrapper(*args,**kwargs):
        today = datetime.today().strftime('%Y-%m-%d')
        print(func)
        dataLog = {
            "log": f"{func}",
            "date": f"{datetime.now()}"
        }
        with open(f"_log/{today}.json", "a", encoding="utf-8") as file:
            json.dump(dataLog, file, indent=2, ensure_ascii=False)

        print(f"Add! Tasks total: {len(dataLog)}")
        func(*args,**kwargs)
    return wrapper