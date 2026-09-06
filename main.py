from utils.command_checker import command_checker

try:
    command = input("add, list, done, remove: ")
except ValueError:
    print("Something went wrong..")
    print(ValueError)


command_checker(command=command)