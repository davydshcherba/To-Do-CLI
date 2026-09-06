import json


command = input("add, list, done, remove: ")



if command == "list":
    with open('data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        print(json.dumps(data, indent=2, ensure_ascii=False))

elif command == "add":
    new_data = {
        "id": 34,
        "text": "Lorem ipsum",
        "done": "False",
        "created": "09.07.2016"
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
