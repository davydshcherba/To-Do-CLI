from typing import Callable

def logger(func: Callable):
    def wrapper(*args,**kwargs):
        print(f"{func} was called")
        func(*args,**kwargs)
    return wrapper