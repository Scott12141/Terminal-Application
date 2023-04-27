
from daily_functions import monday, tuesday, wednesday, thursday, friday, saturday, sunday


def user_base_rate():
    global base_rate
    base_rate = float(input("Please enter your base rate of pay  : "))
    return base_rate;

def pay_calculator():

    weekly_accumulated = 0
    pay_day = ""
    base_rate = user_base_rate()

    while pay_day != "finished" or "Finished":
        
        pay_day = input("Please enter a day you've worked, or 'finished' when your pay weeks complete  : ")

        # Monday
        if pay_day in ["monday", "Monday", "mon", "Mon"]:
            monday_pay = monday()
            weekly_accumulated += monday_pay
            print(f"Weekly pay so far: $",format(weekly_accumulated,".2f"))

        # Tuesday
        elif pay_day in ["tuesday", "Tuesday", "tue", "Tue", "tues", "Tues"]:
            tuesday_pay = tuesday()
            weekly_accumulated += tuesday_pay
            print(f"Weekly pay so far: $",format(weekly_accumulated,".2f"))

        # Wednesday
        elif pay_day in ["wednesday", "Wednesday", "wed", "Wed", "weds", "Weds"]:
            wednesday_pay = wednesday()
            weekly_accumulated += wednesday_pay
            print(f"Weekly pay so far: $",format(weekly_accumulated,".2f"))

        # Thursday
        elif pay_day in ["thursday", "Thursday", "thur", "Thur", "thurs", "Thurs"]:
            thursday_pay = thursday()
            weekly_accumulated += thursday_pay
            print(f"Weekly pay so far: $",format(weekly_accumulated,".2f"))

        # Friday
        elif pay_day in ["friday", "Friday", "fri", "Fri"]:
            friday_pay = friday()
            weekly_accumulated += friday_pay
            print(f"Weekly pay so far: $",format(weekly_accumulated,".2f"))
        # Saturday
        elif pay_day in ["saturday", "Saturday", "sat", "Sat"]:
            saturday_pay = saturday()
            weekly_accumulated += saturday_pay
            print(f"Weekly pay so far: $",format(weekly_accumulated,".2f"))
        # Sunday
        elif pay_day in ["sunday", "Sunday", "sun", "Sun"]:
            sunday_pay = sunday()
            weekly_accumulated += sunday_pay
            print(f"Weekly pay so far: $",format(weekly_accumulated,".2f"))
        # Loop ender
        elif pay_day in ["Finished", "finished", "exit", "Exit", "quit", "Quit"]:
            break
        else:
            print("Please enter one of the days of the week or finished")
    
    print(f"Your weekly pay is: $",format(weekly_accumulated,".2f"))


