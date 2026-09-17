from commands.list_command import list_command
from commands.add_command import add_command
from commands.done_command import done_command
from commands.remove_command import remove_command
from termcolor import colored

def command_checker(*, command):
    if command == "list":
        list_command()
    elif command == "add":
        text = input("Enter text: ")
        done = input("Is Done (True/False): ")
        if done == "True" or done == "False":
            add_command(text=text,done=done)
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