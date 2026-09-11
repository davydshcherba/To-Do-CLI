from utils.command_checker import command_checker

while True:
    try:
        print("")
        command = input("add, list, done, remove: ")
        command_checker(command=command)
    except ValueError:
        print("Something went wrong..")
        print(ValueError)
    except KeyboardInterrupt:
        print("\nGood Bye")
        exit()


