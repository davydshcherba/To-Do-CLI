from commands.list_command import list_command
from commands.add_command import add_command
from commands.done_command import done_command
from commands.remove_command import remove_command
from termcolor import colored

def command_checker(*, command):
    if command == "list":
        list_command()
    elif command == "add":
        id = int(input("Enter ID: "))
        text = input("Enter text: ")
        done = input("Is Done (True/False): ")
        if done == "True" or done == "False":
            created = input("Enter date (01.01.2000): ")
            add_command(id=id,text=text,done=done,created=created)
        else:
            print(colored("You wrote incorrect done field","red"))
    elif command == "done":
        id = int(input("Enter ID: "))
        done_command(id=id)
    elif command == "remove":
        id = int(input("Enter ID: "))
        remove_command(id=id)
    else:
        print("                   :(                    ")
        print("|------------------404------------------|")
        print("|        You wrote incorrect command    |")
        print("|------------------404------------------|")