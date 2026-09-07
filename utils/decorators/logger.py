from typing import Callable
from termcolor import colored

def logger(func: Callable):
    def wrapper(*args,**kwargs):
        print(colored("|--------------------logger---------------------|", "red"))
        print("")
        print(colored(f"{func} was called","red"))
        print("")
        print(colored("|--------------------logger---------------------|", "red")) 
        print(colored("|--------------------result---------------------|", "green"))    
        print(colored("|--------------------result---------------------|", "green"))       
        func(*args,**kwargs)
    return wrapper