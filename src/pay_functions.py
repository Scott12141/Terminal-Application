
from daily_functions import monday, tuesday, wednesday, thursday, friday, saturday, sunday, user_base_rate
from colored import fg, attr
from datetime import date, datetime
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
    weekly_pay(weekly_accumulated)
    # print(f"Your {fg('yellow')}weekly pay{attr('reset')} is: $",format(weekly_accumulated,".2f"))
    # with open(file_name, "a")as pay_file:
    #         writer = csv.writer(pay_file)
    #         writer.writerow(["Weekly Total: ", format(weekly_accumulated,".2f")])

def weekly_pay(weekly_accumulated):
    yearly_income = (weekly_accumulated / 7) * 365
    medilevy = yearly_income * .02
    weekly_medilevy = (medilevy / 365) * 7
    if yearly_income <= 18200:
        print(f"Your {fg('yellow')}weekly pay{attr('reset')} is: $",format(weekly_accumulated,".2f"))
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Weekly Total Gross: ", format(weekly_accumulated,".2f")])
            

    elif yearly_income > 18200 and yearly_income <= 29032:
        yearly_tax = (yearly_income - 18200) * .19
        weekly_tax = (yearly_tax / 365) * 7
        weekly_tax = float(format(weekly_tax,".0f"))
        net_pay = weekly_accumulated - weekly_tax
        net_pay = format(net_pay,".2f")
        print(f"Your {fg('yellow')}gross weekly pay{attr('reset')} is: $",format(weekly_accumulated,".2f"))
        print(f"Your {fg('yellow')}net weekly pay{attr('reset')} is: ${net_pay} (Tax: {weekly_tax})")
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Weekly Total Gross: ", format(weekly_accumulated,".2f")])
            writer.writerow(["Weekly Total Net: ", net_pay])

    elif yearly_income > 29032 and yearly_income <= 45000:
        yearly_tax = (yearly_income - 18200) * .19
        weekly_tax = ((yearly_tax / 365) * 7) + weekly_medilevy
        weekly_tax = float(format(weekly_tax,".0f"))
        net_pay = weekly_accumulated - weekly_tax
        net_pay = format(net_pay,".2f")
        print(f"Your {fg('yellow')}gross weekly pay{attr('reset')} is: $",format(weekly_accumulated,".2f"))
        print(f"Your {fg('yellow')}net weekly pay{attr('reset')} is: ${net_pay} (Tax: {weekly_tax})")
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Weekly Total Gross: ", format(weekly_accumulated,".2f")])
            writer.writerow(["Weekly Total Net: ", net_pay])

    elif yearly_income > 45000 and yearly_income <= 120000:
        yearly_tax = (yearly_income - 45000) * .325
        weekly_static_tax = (5092 /365) * 7
        weekly_tax = ((yearly_tax / 365) * 7) + (weekly_medilevy + weekly_static_tax)
        weekly_tax = float(format(weekly_tax,".0f"))
        net_pay = weekly_accumulated - weekly_tax
        net_pay = format(net_pay,".2f")
        print(f"Your {fg('yellow')}gross weekly pay{attr('reset')} is: $",format(weekly_accumulated,".2f"))
        print(f"Your {fg('yellow')}net weekly pay{attr('reset')} is: ${net_pay} (Tax: {weekly_tax})")
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Weekly Total Gross: ", format(weekly_accumulated,".2f")])
            writer.writerow(["Weekly Total Net: ", net_pay])

    elif yearly_income > 120000 and yearly_income <= 180000:
        yearly_tax = (yearly_income - 120000) * .37
        weekly_static_tax = (29467 /365) * 7
        weekly_tax = ((yearly_tax / 365) * 7) + (weekly_medilevy + weekly_static_tax)
        weekly_tax = float(format(weekly_tax,".0f"))
        net_pay = weekly_accumulated - weekly_tax
        net_pay = format(net_pay,".2f")
        print(f"Your {fg('yellow')}gross weekly pay{attr('reset')} is: $",format(weekly_accumulated,".2f"))
        print(f"Your {fg('yellow')}net weekly pay{attr('reset')} is: ${net_pay} (Tax: {weekly_tax})")
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Weekly Total Gross: ", format(weekly_accumulated,".2f")])
            writer.writerow(["Weekly Total Net: ", net_pay])  

    else:
        yearly_tax = (yearly_income - 180000) * .45
        weekly_static_tax = (51667 /365) * 7
        weekly_tax = ((yearly_tax / 365) * 7) + (weekly_medilevy + weekly_static_tax)
        weekly_tax = float(format(weekly_tax,".0f"))
        net_pay = weekly_accumulated - weekly_tax
        net_pay = format(net_pay,".2f")
        print(f"Your {fg('yellow')}gross weekly pay{attr('reset')} is: $",format(weekly_accumulated,".2f"))
        print(f"Your {fg('yellow')}net weekly pay{attr('reset')} is: ${net_pay} (Tax: {weekly_tax})")
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Weekly Total Gross: ", format(weekly_accumulated,".2f")])
            writer.writerow(["Weekly Total Net: ", net_pay]) 



def view_pay_history(file_name):
    print(f"{fg('yellow')}Viewing pay history{attr('reset')}")
    with open(file_name, "r") as pay_file:
        reader = csv.reader(pay_file)
        for row in reader:
            print(row)

def pay_week(file_name):
    date_inputs = ''
    while True:
        date_inputs = input(f"Please enter starting date of pay week in the format, {fg('yellow')}DD-MM-YYYY{attr('reset')} : ")
        try:
            date_outputs = datetime.strptime(date_inputs, "%d-%m-%Y").date()
            with open(file_name, "a")as pay_file:
                writer = csv.writer(pay_file)
                writer.writerow(["Pay week: ", date_outputs])
            break
        except ValueError:
            print(f"{fg('red')}That is not a valid date.{attr('reset')}")




    
