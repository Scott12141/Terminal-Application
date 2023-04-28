
from daily_functions import monday, tuesday, wednesday, thursday, friday, saturday, sunday, user_base_rate
from colored import fg, attr
from datetime import date
import csv


file_name = "pay_history.csv"


def pay_calculator(file_name):
    
    weekly_accumulated = 0
    pay_day = ""
    pay_week(file_name)
    base_rate = user_base_rate()

    while pay_day != "finished" or "Finished":
        
        pay_day = input(f"Please enter a {fg('yellow')}day{attr('reset')} you've worked, or {fg('yellow')}'finished'{attr('reset')} when your pay weeks complete : ")

        # Monday
        if pay_day in ["monday", "Monday", "mon", "Mon"]:
            monday_pay = monday(file_name)
            weekly_accumulated += monday_pay
            print(f"{fg('yellow')}Weekly pay{attr('reset')} so far: $",format(weekly_accumulated,".2f"))

        # Tuesday
        elif pay_day in ["tuesday", "Tuesday", "tue", "Tue", "tues", "Tues"]:
            tuesday_pay = tuesday(file_name)
            weekly_accumulated += tuesday_pay
            print(f"{fg('yellow')}Weekly pay{attr('reset')} so far: $",format(weekly_accumulated,".2f"))

        # Wednesday
        elif pay_day in ["wednesday", "Wednesday", "wed", "Wed", "weds", "Weds"]:
            wednesday_pay = wednesday(file_name)
            weekly_accumulated += wednesday_pay
            print(f"{fg('yellow')}Weekly pay{attr('reset')} so far: $",format(weekly_accumulated,".2f"))

        # Thursday
        elif pay_day in ["thursday", "Thursday", "thur", "Thur", "thurs", "Thurs"]:
            thursday_pay = thursday(file_name)
            weekly_accumulated += thursday_pay
            print(f"{fg('yellow')}Weekly pay{attr('reset')} so far: $",format(weekly_accumulated,".2f"))

        # Friday
        elif pay_day in ["friday", "Friday", "fri", "Fri"]:
            friday_pay = friday(file_name)
            weekly_accumulated += friday_pay
            print(f"{fg('yellow')}Weekly pay{attr('reset')} so far: $",format(weekly_accumulated,".2f"))

        # Saturday
        elif pay_day in ["saturday", "Saturday", "sat", "Sat"]:
            saturday_pay = saturday(file_name)
            weekly_accumulated += saturday_pay
            print(f"{fg('yellow')}Weekly pay{attr('reset')} so far: $",format(weekly_accumulated,".2f"))

        # Sunday
        elif pay_day in ["sunday", "Sunday", "sun", "Sun"]:
            sunday_pay = sunday(file_name)
            weekly_accumulated += sunday_pay
            print(f"{fg('yellow')}Weekly pay{attr('reset')} so far: $",format(weekly_accumulated,".2f"))

        # Loop ender
        elif pay_day in ["Finished", "finished", "exit", "Exit", "quit", "Quit"]:
            break
        else:
            print(f"{fg('red')}Please enter one of the days of the week or finished{attr('reset')}")
    
    print(f"Your {fg('yellow')}weekly pay{attr('reset')} is: $",format(weekly_accumulated,".2f"))
    with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Weekly Total: ", format(weekly_accumulated,".2f")])

def view_pay_history(file_name):
    print(f"{fg('yellow')}Viewing pay history{attr('reset')}")
    with open(file_name, "r") as pay_file:
        reader = csv.reader(pay_file)
        for row in reader:
            print(row)

def pay_week(file_name):
    date_inputs = input(f"Please enter starting date of pay week in the format, {fg('yellow')}YYYY-MM-DDDD{attr('reset')}:  ").split('-')
    year, month, day = [int(i) for i in date_inputs]
    week_of_pay = date(year, month, day)
    with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Pay week: ", week_of_pay])



    
