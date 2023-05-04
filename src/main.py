from pay_functions import pay_calculator, view_pay_history
from colored import fg, attr
import csv

# Creates a csv file if one isnt already present 
file_name = "pay_history.csv"
try:
    pay_file = open(file_name, "r")
    pay_file.close()
except FileNotFoundError:
    pay_file = open(file_name, "w")
    pay_file.write("pay_day,pay_amount\n")
    pay_file.close()

# Displays a greeting for the user
print(f"{fg('yellow')}Welcome to the Weekly Pay Calculator app!{attr('reset')}")
# Creates a function that runs the menu for a users seection
def start_menu():
    print(f"1. To calculate a new pay week {fg('yellow')} please enter 1 {attr('reset')}")
    print(f"2. To view your pay history {fg('yellow')} please enter 2 {attr('reset')}")
    print(f"3. To exit {fg('yellow')} please enter 3 {attr('reset')}")
    selection = input("Please enter your selection:  ")
    return selection
# Runs a loop to get the users selection, if the user enters 1 it starts the calculator,
# 2 it accesses the csv file, 3 it ends the application
user_selection = ""
while user_selection != "3":
    user_selection = start_menu()
    if (user_selection == "1"):
        pay_calculator(file_name)
        
    elif (user_selection == "2"):
        view_pay_history(file_name)

    elif (user_selection == "3"):
        print(f"You are now {fg('yellow')}exiting.{attr('reset')}")
        continue
    else:
        print(f"{fg('red')} Please enter a number 1-3.{attr('reset')}")
        continue
    input(f"{fg('yellow')}Press enter {attr('reset')}to continue.....")

print(f"{fg('yellow')}Thank you for using the pay calculator!{attr('reset')}")