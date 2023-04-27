

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
        friday_pay = ((base_rate * 1.25) * 2) + ((base_rate * 1.5) * (hours_worked - 2))
        print(f"Friday's pay is: $",format(friday_pay,".2f"))
        return friday_pay
    

def saturday():
    shift_worked = input("What shift did you work on Saturday? Please enter 'Day', 'Afternoon' or 'Night'.  ")
    hours_worked = float(input("Please enter hours worked on Saturday  : "))
    public_holiday = input("Was Saturday a public holiday? y/n.  ")

    if public_holiday in ["y", "Y", "yes", "Yes"]:
        saturday_pay = (base_rate * 2.5) * hours_worked
        print(f"Saturday's pay is: $",format(saturday_pay,".2f"))
        return saturday_pay
        
    elif public_holiday in ["n", "N", "no" "No"] and shift_worked in ["day", "Day"]:
        saturday_pay = (base_rate * 1.5) * hours_worked
        print(f"Saturday's pay is: $",format(saturday_pay,".2f"))
        return saturday_pay
        
    elif public_holiday in ["n", "N", "no" "No"] and shift_worked in ["afternoon", "Afternoon"]:
        saturday_pay = (base_rate * 1.5)  * hours_worked
        print(f"Saturday's pay is: $",format(saturday_pay,".2f"))
        return saturday_pay
    
    elif public_holiday in ["n", "N", "no" "No"] and shift_worked in ["night", "Night"]:
        saturday_pay = ((base_rate * 1.5) * 2) + ((base_rate * 1.8) * (hours_worked - 2))
        print(f"Saturday's pay is: $",format(saturday_pay,".2f"))
        return saturday_pay
    

def sunday():
    shift_worked = input("What shift did you work on Sunday? Please enter 'Day', 'Afternoon' or 'Night'.  ")
    hours_worked = float(input("Please enter hours worked on Sunday  : "))
    public_holiday = input("Was Sunday a public holiday? y/n.  ")

    if public_holiday in ["y", "Y", "yes", "Yes"]:
        sunday_pay = (base_rate * 2.5) * hours_worked
        print(f"Sunday's pay is: $",format(sunday_pay,".2f"))
        return sunday_pay
        
    elif public_holiday in ["n", "N", "no" "No"] and shift_worked in ["day", "Day"]:
        sunday_pay = (base_rate * 1.8)  * hours_worked
        print(f"Sunday's pay is: $",format(sunday_pay,".2f"))
        return sunday_pay
        
    elif public_holiday in ["n", "N", "no" "No"] and shift_worked in ["afternoon", "Afternoon"]:
        sunday_pay = (base_rate * 1.8)  * hours_worked
        print(f"Sunday's pay is: $",format(sunday_pay,".2f"))
        return sunday_pay
    
    elif public_holiday in ["n", "N", "no" "No"] and shift_worked in ["night", "Night"]:
        sunday_pay = ((base_rate * 1.8) * 2) + ((base_rate * 1.25) * (hours_worked - 2))
        print(f"Sunday's pay is: $",format(sunday_pay,".2f"))
        return sunday_pay