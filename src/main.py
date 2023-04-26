from functions import pay_calculator, monday


print("Welcome to the Weekly Pay Calculator app!")

def start_menu():
    print("1. To calculate a new pay week please enter 1")
    print("2. To view your pay history please enter 2")
    print("5. To exit please enter 3")
    selection = input("Please enter your selection:  ")
    return selection

# pay_week = {
#     "Monday": monday_pay,
#     "Tuesday": tuesday_pay,
#     "Wednesday": wednesday_pay,
#     "Thursday": thursday_pay,
#     "Friday": friday_pay,
#     "Saturday": saturday_pay,
#     "Sunday": sunday_pay    
# }

user_selection = ""

while user_selection != "3":
    user_selection = start_menu()
    if (user_selection == "1"):
        pay_calculator()
        # add_todo(file_name)
    elif (user_selection == "2"):
        # remove_todo(file_name)
        print("2")
    elif (user_selection == "3"):
        print("You are now exiting")
        continue
    else:
        print("Please enter a number")

    input("Press enter to continue.....")



print("Thank you for using the pay calculator")