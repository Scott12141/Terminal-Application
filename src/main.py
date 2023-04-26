


print("Welcome to the Weekly Pay Calculator app!")

def start_menu():
    print("1. Enter 1 to calculate a new pay week")
    print("2. Enter 2 to view your pay history")
    print("5. Enter 3 to exit")
    selection = input("Please enter your selection:  ")
    return selection

user_selection = ""

while user_selection != "3":
    user_selection = start_menu()
    if (user_selection == "1"):
        print("1")
        # add_todo(file_name)
    elif (user_selection == "2"):
        # remove_todo(file_name)
        print("2")
    elif (user_selection == "3"):
        print("You are now exiting")
        continue
    else:
        print("Invalid input")

    input("Press enter to continue.....")

print("Thank you for using the pay calculator")