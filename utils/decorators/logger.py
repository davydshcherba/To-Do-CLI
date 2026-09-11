from typing import Callable
from termcolor import colored
import json

def logger(func: Callable):
    def wrapper(*args,**kwargs):
        print(func)
        dataLog = {
            "log": f"{func}"
        }
        with open("_log/11.09.json", "w", encoding="utf-8") as file:
            json.dump(dataLog, file, indent=2, ensure_ascii=False)
        print(f"Add! Tasks total: {len(dataLog)}")
        func(*args,**kwargs)
    return wrapper