import json
from typing import Callable

try:
    command = input("add, list, done, remove: ")
except ValueError:
    print("Something went wrong..")
    print(ValueError)

def logger(func: Callable):
    def wrapper(*args,**kwargs):
        print(f"{func} was called")
        func(*args,**kwargs)
    return wrapper

@logger
def list_command():
    with open('data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            print(json.dumps(data, indent=2, ensure_ascii=False))

@logger
def add_command(* ,id: int, text: str, done: str, created: str):
    new_data = {
        "id": id,
        "text": text,
        "done": done,
        "created": created
    }
    
    try:
        with open("data.json", "r", encoding="utf-8") as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = []
    
    if not isinstance(existing_data, list):
        existing_data = [existing_data]
    existing_data.append(new_data)
    
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(existing_data, file, indent=2, ensure_ascii=False)
    
    print(f"Add! Tasks total: {len(existing_data)}")

if command == "list":
    list_command()
elif command == "add":
    id = int(input("Enter ID: "))
    text = input("Enter text: ")
    done = input("Is Done (True/False): ")
    created = input("Enter date (01.01.2000): ")
    add_command(id=id,text=text,done=done,created=created)
else:
    print("                   :(                    ")
    print("|------------------404------------------|")
    print("|        You wrote incorrect command    |")
    print("|------------------404------------------|")
