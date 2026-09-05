import json


command = input("add, list, done, remove: ")

with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

if command == "list":
    print(json.dumps(data, indent=2, ensure_ascii=False))