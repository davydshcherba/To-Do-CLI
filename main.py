from utils.command_checker import command_checker

while True:
    try:
        print(r""" 
        
       _____ ____        ____  ____    ____  _     _ 
      /__ __Y  _ \      /  _ \/  _ \  /   _\/ \   / \
        / \ | / \|_____ | | \|| / \|  |  /  | |   | |
        | | | \_/|\____\| |_/|| \_/|  |  \__| |_/\| |
        \_/ \____/      \____/\____/  \____/\____/\_/
                    by:Davyd Shcherba                        
        
        
        """)
        print("")
        command = input("add, list, done, remove: ")
        command_checker(command=command)
    except ValueError:
        print("Something went wrong..")
        print(ValueError)
    except KeyboardInterrupt:
        print("\nGood Bye")
        exit()


