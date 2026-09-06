from commands.list_command import list_command
from commands.add_command import add_command

def command_checker(*, command):
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