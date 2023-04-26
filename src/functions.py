
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
        elif pay_day in ["tuesday", "Tuesday", "tue", "Tue"]:
            tuesday_pay = tuesday()
            weekly_accumulated += tuesday_pay
            print(f"Weekly pay so far: $",format(weekly_accumulated,".2f"))

        # Wednesday
        elif pay_day in ["wednesday", "Wednesday", "wed", "Wed"]:
            wednesday_pay = wednesday()
            weekly_accumulated += wednesday_pay
            print(f"Weekly pay so far: $",format(weekly_accumulated,".2f"))

        # Thursday
        elif pay_day in ["thursday", "Thursday", "thur", "Thur"]:
            thursday_pay = thursday()
            weekly_accumulated += thursday_pay
            print(f"Weekly pay so far: $",format(weekly_accumulated,".2f"))

        # Friday
        elif pay_day in ["friday", "Friday", "fri", "Fri"]:
            friday_pay = friday()
            weekly_accumulated += friday_pay
            print(f"Weekly pay so far: $",format(weekly_accumulated,".2f"))
        # Loop ender
        elif pay_day in ["Finished", "finished", "exit", "Exit", "quit", "Quit"]:
            break
        else:
            print("Please enter one of the days of the week or finished")
    
    print(f"Your weekly pay is: $",format(weekly_accumulated,".2f"))


def monday():
    shift_worked = input("What shift did you work on Monday? Please enter 'Day', 'Afternoon' or 'Night'.  ")
    hours_worked = float(input("Please enter hours worked on Monday  : "))
    public_holiday = input("Was Monday a public holiday? y/n.  ")

    if public_holiday in ["y", "Y", "yes", "Yes"]:
        monday_pay = (base_rate * 2.5) * hours_worked
        print(f"Monday's pay is: $",format(monday_pay,".2f"))
        return monday_pay
        
    elif public_holiday in ["n", "N", "no", "No"] and shift_worked in ["day", "Day"]:
        monday_pay = base_rate  * hours_worked
        print(f"Monday's pay is: $",format(monday_pay,".2f"))
        return monday_pay
        
    elif public_holiday in ["n", "N", "no", "No"] and shift_worked in ["afternoon", "Afternoon"]:
        monday_pay = (base_rate * 1.15)  * hours_worked
        print(f"Monday's pay is: $",format(monday_pay,".2f"))
        return monday_pay
    
    elif public_holiday in ["n", "N", "no", "No"] and shift_worked in ["night", "Night"]:
        monday_pay = (base_rate * 1.25)  * hours_worked
        print(f"Monday's pay is: $",format(monday_pay,".2f"))
        return monday_pay

def tuesday():
    shift_worked = input("What shift did you work on Tuesday? Please enter 'Day', 'Afternoon' or 'Night'.  ")
    hours_worked = float(input("Please enter hours worked on Tuesday  : "))
    public_holiday = input("Was Tuesday a public holiday? y/n.  ")

    if public_holiday in ["y", "Y", "yes", "Yes"]:
        tuesday_pay = (base_rate * 2.5) * hours_worked
        print(f"Tuesday's pay is: $",format(tuesday_pay,".2f"))
        return tuesday_pay
        
    elif public_holiday in ["n", "N", "no" "No"] and shift_worked in ["day", "Day"]:
        tuesday_pay = base_rate  * hours_worked
        print(f"Tuesday's pay is: $",format(tuesday_pay,".2f"))
        return tuesday_pay
        
    elif public_holiday in ["n", "N", "no" "No"] and shift_worked in ["afternoon", "Afternoon"]:
        tuesday_pay = (base_rate * 1.15)  * hours_worked
        print(f"Tuesday's pay is: $",format(tuesday_pay,".2f"))
        return tuesday_pay
    
    elif public_holiday in ["n", "N", "no" "No"] and shift_worked in ["night", "Night"]:
        tuesday_pay = (base_rate * 1.25)  * hours_worked
        print(f"Tuesday's pay is: $",format(tuesday_pay,".2f"))
        return tuesday_pay
    
def wednesday():
    shift_worked = input("What shift did you work on Wednesday? Please enter 'Day', 'Afternoon' or 'Night'.  ")
    hours_worked = float(input("Please enter hours worked on Wednesday  : "))
    public_holiday = input("Was Wednesday a public holiday? y/n.  ")

    if public_holiday in ["y", "Y", "yes", "Yes"]:
        wednesday_pay = (base_rate * 2.5) * hours_worked
        print(f"Wednesday's pay is: $",format(wednesday_pay,".2f"))
        return wednesday_pay
        
    elif public_holiday in ["n", "N", "no" "No"] and shift_worked in ["day", "Day"]:
        wednesday_pay = base_rate  * hours_worked
        print(f"Wednesday's pay is: $",format(wednesday_pay,".2f"))
        return wednesday_pay
        
    elif public_holiday in ["n", "N", "no" "No"] and shift_worked in ["afternoon", "Afternoon"]:
        wednesday_pay = (base_rate * 1.15)  * hours_worked
        print(f"Wednesday's pay is: $",format(wednesday_pay,".2f"))
        return wednesday_pay
    
    elif public_holiday in ["n", "N", "no" "No"] and shift_worked in ["night", "Night"]:
        wednesday_pay = (base_rate * 1.25)  * hours_worked
        print(f"Wednesday's pay is: $",format(wednesday_pay,".2f"))
        return wednesday_pay

def thursday():
    shift_worked = input("What shift did you work on Thursday? Please enter 'Day', 'Afternoon' or 'Night'.  ")
    hours_worked = float(input("Please enter hours worked on Thursday  : "))
    public_holiday = input("Was Thursday a public holiday? y/n.  ")

    if public_holiday in ["y", "Y", "yes", "Yes"]:
        thursday_pay = (base_rate * 2.5) * hours_worked
        print(f"Thursday's pay is: $",format(thursday_pay,".2f"))
        return thursday_pay
        
    elif public_holiday in ["n", "N", "no" "No"] and shift_worked in ["day", "Day"]:
        thursday_pay = base_rate  * hours_worked
        print(f"Thursday's pay is: $",format(thursday_pay,".2f"))
        return thursday_pay
        
    elif public_holiday in ["n", "N", "no" "No"] and shift_worked in ["afternoon", "Afternoon"]:
        thursday_pay = (base_rate * 1.15)  * hours_worked
        print(f"Thursday's pay is: $",format(thursday_pay,".2f"))
        return thursday_pay
    
    elif public_holiday in ["n", "N", "no" "No"] and shift_worked in ["night", "Night"]:
        thursday_pay = (base_rate * 1.25)  * hours_worked
        print(f"Thursday's pay is: $",format(thursday_pay,".2f"))
        return thursday_pay
    
def friday():
    shift_worked = input("What shift did you work on Friday? Please enter 'Day', 'Afternoon' or 'Night'.  ")
    hours_worked = float(input("Please enter hours worked on Friday  : "))
    public_holiday = input("Was Friday a public holiday? y/n.  ")

    if public_holiday in ["y", "Y", "yes", "Yes"]:
        friday_pay = (base_rate * 2.5) * hours_worked
        print(f"Friday's pay is: $",format(friday_pay,".2f"))
        return friday_pay
        
    elif public_holiday in ["n", "N", "no" "No"] and shift_worked in ["day", "Day"]:
        friday_pay = base_rate  * hours_worked
        print(f"Friday's pay is: $",format(friday_pay,".2f"))
        return friday_pay
        
    elif public_holiday in ["n", "N", "no" "No"] and shift_worked in ["afternoon", "Afternoon"]:
        friday_pay = (base_rate * 1.15)  * hours_worked
        print(f"Friday's pay is: $",format(friday_pay,".2f"))
        return friday_pay
    
    elif public_holiday in ["n", "N", "no" "No"] and shift_worked in ["night", "Night"]:
        friday_pay = (base_rate * 1.25)  * hours_worked
        print(f"Friday's pay is: $",format(friday_pay,".2f"))
        return friday_pay