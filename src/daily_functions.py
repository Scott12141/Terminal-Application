
from colored import fg, attr
import csv

def user_base_rate():
    global base_rate
    base_rate = ''
    while True:
        input_rate = (input(f"Please enter your {fg('yellow')}base rate{attr('reset')} of pay : "))
        try:
            base_rate = float(input_rate)
            if base_rate <= 0:
                raise ValueError
            break
        except ValueError:
            print(f"{fg('red')} '{input_rate}' is not a valid base rate of pay, please re-enter{attr('reset')}")

    return base_rate;


# MONDAY
def monday(file_name):
    shift_worked = input(f"What {fg('yellow')}shift{attr('reset')} did you work on Monday? Please enter 'Day', 'Afternoon' or 'Night'.  ")
    hours_worked = float(input(f"Please enter {fg('yellow')}hours worked{attr('reset')} on Monday  : "))
    public_holiday = input(f"Was Monday a {fg('yellow')}public holiday?{attr('reset')}  y/n.  ")

    if public_holiday in ["y", "Y", "yes", "Yes"]:
        monday_pay = (base_rate * 2.5) * hours_worked
        print(f"{fg('yellow')}Monday's{attr('reset')} pay is: $",format(monday_pay,".2f"))
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Monday", format(monday_pay,".2f")])
            return monday_pay
             
    elif public_holiday in ["n", "N", "no", "No"] and shift_worked in ["day", "Day"]:
        monday_pay = base_rate  * hours_worked
        print(f"{fg('yellow')}Monday's{attr('reset')} pay is: $",format(monday_pay,".2f"))
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Monday", format(monday_pay,".2f")])
            return monday_pay
        
    elif public_holiday in ["n", "N", "no", "No"] and shift_worked in ["afternoon", "Afternoon"]:
        monday_pay = (base_rate * 1.15)  * hours_worked
        print(f"{fg('yellow')}Monday's{attr('reset')} pay is: $",format(monday_pay,".2f"))
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Monday", format(monday_pay,".2f")])
            return monday_pay
    
    elif public_holiday in ["n", "N", "no", "No"] and shift_worked in ["night", "Night"]:
        monday_pay = (base_rate * 1.25)  * hours_worked
        print(f"{fg('yellow')}Monday's{attr('reset')} pay is: $",format(monday_pay,".2f"))
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Monday", format(monday_pay,".2f")])
            return monday_pay


# TUESDAY
def tuesday(file_name):
    shift_worked = input(f"What {fg('yellow')}shift{attr('reset')} did you work on Tuesday? Please enter 'Day', 'Afternoon' or 'Night'.  ")
    hours_worked = float(input(f"Please enter {fg('yellow')}hours worked{attr('reset')} on Tuesday  : "))
    public_holiday = input(f"Was Tuesday a {fg('yellow')}public holiday?{attr('reset')} y/n.  ")

    if public_holiday in ["y", "Y", "yes", "Yes"]:
        tuesday_pay = (base_rate * 2.5) * hours_worked
        print(f"{fg('yellow')}Tuesday's{attr('reset')} pay is: $",format(tuesday_pay,".2f"))
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Tuesday", format(tuesday_pay,".2f")])
            return tuesday_pay
        
    elif public_holiday in ["n", "N", "no" "No"] and shift_worked in ["day", "Day"]:
        tuesday_pay = base_rate  * hours_worked
        print(f"{fg('yellow')}Tuesday's{attr('reset')} pay is: $",format(tuesday_pay,".2f"))
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Tuesday", format(tuesday_pay,".2f")])
            return tuesday_pay
        
    elif public_holiday in ["n", "N", "no" "No"] and shift_worked in ["afternoon", "Afternoon"]:
        tuesday_pay = (base_rate * 1.15)  * hours_worked
        print(f"{fg('yellow')}Tuesday's{attr('reset')} pay is: $",format(tuesday_pay,".2f"))
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Tuesday", format(tuesday_pay,".2f")])
            return tuesday_pay
    
    elif public_holiday in ["n", "N", "no" "No"] and shift_worked in ["night", "Night"]:
        tuesday_pay = (base_rate * 1.25)  * hours_worked
        print(f"{fg('yellow')}Tuesday's{attr('reset')} pay is: $",format(tuesday_pay,".2f"))
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Tuesday", format(tuesday_pay,".2f")])
            return tuesday_pay
    

# WEDNESDAY
def wednesday(file_name):
    shift_worked = input(f"What {fg('yellow')}shift{attr('reset')} did you work on Wednesday? Please enter 'Day', 'Afternoon' or 'Night'.  ")
    hours_worked = float(input(f"Please enter {fg('yellow')}hours worked{attr('reset')} on Wednesday  : "))
    public_holiday = input(f"Was Wednesday a {fg('yellow')}public holiday?{attr('reset')} y/n.  ")

    if public_holiday in ["y", "Y", "yes", "Yes"]:
        wednesday_pay = (base_rate * 2.5) * hours_worked
        print(f"{fg('yellow')}Wednesday's{attr('reset')} pay is: $",format(wednesday_pay,".2f"))
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Wednesday", format(wednesday_pay,".2f")])
            return wednesday_pay
        
    elif public_holiday in ["n", "N", "no" "No"] and shift_worked in ["day", "Day"]:
        wednesday_pay = base_rate  * hours_worked
        print(f"{fg('yellow')}Wednesday's{attr('reset')} pay is: $",format(wednesday_pay,".2f"))
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Wednesday", format(wednesday_pay,".2f")])
            return wednesday_pay
        
    elif public_holiday in ["n", "N", "no" "No"] and shift_worked in ["afternoon", "Afternoon"]:
        wednesday_pay = (base_rate * 1.15)  * hours_worked
        print(f"{fg('yellow')}Wednesday's{attr('reset')} pay is: $",format(wednesday_pay,".2f"))
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Wednesday", format(wednesday_pay,".2f")])
            return wednesday_pay
    
    elif public_holiday in ["n", "N", "no" "No"] and shift_worked in ["night", "Night"]:
        wednesday_pay = (base_rate * 1.25)  * hours_worked
        print(f"{fg('yellow')}Wednesday's{attr('reset')} pay is: $",format(wednesday_pay,".2f"))
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Wednesday", format(wednesday_pay,".2f")])
            return wednesday_pay


# THURSDAY
def thursday(file_name):
    shift_worked = input(f"What {fg('yellow')}shift{attr('reset')} did you work on Thursday? Please enter 'Day', 'Afternoon' or 'Night'.  ")
    hours_worked = float(input(f"Please enter {fg('yellow')}hours worked{attr('reset')} on Thursday  : "))
    public_holiday = input(f"Was Thursday a {fg('yellow')}public holiday?{attr('reset')} y/n.  ")

    if public_holiday in ["y", "Y", "yes", "Yes"]:
        thursday_pay = (base_rate * 2.5) * hours_worked
        print(f"{fg('yellow')}Thursday's{attr('reset')} pay is: $",format(thursday_pay,".2f"))
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Thursday", format(thursday_pay,".2f")])
            return thursday_pay
        
    elif public_holiday in ["n", "N", "no" "No"] and shift_worked in ["day", "Day"]:
        thursday_pay = base_rate  * hours_worked
        print(f"{fg('yellow')}Thursday's{attr('reset')} pay is: $",format(thursday_pay,".2f"))
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Thursday", format(thursday_pay,".2f")])
            return thursday_pay
        
    elif public_holiday in ["n", "N", "no" "No"] and shift_worked in ["afternoon", "Afternoon"]:
        thursday_pay = (base_rate * 1.15)  * hours_worked
        print(f"{fg('yellow')}Thursday's{attr('reset')} pay is: $",format(thursday_pay,".2f"))
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Thursday", format(thursday_pay,".2f")])
            return thursday_pay
    
    elif public_holiday in ["n", "N", "no" "No"] and shift_worked in ["night", "Night"]:
        thursday_pay = (base_rate * 1.25)  * hours_worked
        print(f"{fg('yellow')}Thursday's{attr('reset')} pay is: $",format(thursday_pay,".2f"))
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Thursday", format(thursday_pay,".2f")])
            return thursday_pay
    

# FRIDAY
def friday(file_name):
    shift_worked = input(f"What {fg('yellow')}shift{attr('reset')} did you work on Friday? Please enter 'Day', 'Afternoon' or 'Night'.  ")
    hours_worked = float(input(f"Please enter {fg('yellow')}hours worked{attr('reset')} on Friday  : "))
    public_holiday = input(f"Was Friday a {fg('yellow')}public holiday?{attr('reset')} y/n.  ")

    if public_holiday in ["y", "Y", "yes", "Yes"]:
        friday_pay = (base_rate * 2.5) * hours_worked
        print(f"{fg('yellow')}Friday's{attr('reset')} pay is: $",format(friday_pay,".2f"))
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Friday", format(friday_pay,".2f")])
            return friday_pay
        
    elif public_holiday in ["n", "N", "no" "No"] and shift_worked in ["day", "Day"]:
        friday_pay = base_rate  * hours_worked
        print(f"{fg('yellow')}Friday's{attr('reset')} pay is: $",format(friday_pay,".2f"))
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Friday", format(friday_pay,".2f")])
            return friday_pay
        
    elif public_holiday in ["n", "N", "no" "No"] and shift_worked in ["afternoon", "Afternoon"]:
        friday_pay = (base_rate * 1.15)  * hours_worked
        print(f"{fg('yellow')}Friday's{attr('reset')} pay is: $",format(friday_pay,".2f"))
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Friday", format(friday_pay,".2f")])
            return friday_pay
    
    elif public_holiday in ["n", "N", "no" "No"] and shift_worked in ["night", "Night"]:
        friday_pay = ((base_rate * 1.25) * 2) + ((base_rate * 1.5) * (hours_worked - 2))
        print(f"{fg('yellow')}Friday's{attr('reset')} pay is: $",format(friday_pay,".2f"))
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Friday", format(friday_pay,".2f")])
            return friday_pay
    

# SATURDAY
def saturday(file_name):
    shift_worked = input(f"What {fg('yellow')}shift{attr('reset')} did you work on Saturday? Please enter 'Day', 'Afternoon' or 'Night'.  ")
    hours_worked = float(input(f"Please enter {fg('yellow')}hours worked{attr('reset')} on Saturday  : "))
    public_holiday = input(f"Was Saturday a {fg('yellow')}public holiday?{attr('reset')} y/n.  ")

    if public_holiday in ["y", "Y", "yes", "Yes"]:
        saturday_pay = (base_rate * 2.5) * hours_worked
        print(f"{fg('yellow')}Saturday's{attr('reset')} pay is: $",format(saturday_pay,".2f"))
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Saturday", format(saturday_pay,".2f")])
            return saturday_pay
        
    elif public_holiday in ["n", "N", "no" "No"] and shift_worked in ["day", "Day"]:
        saturday_pay = (base_rate * 1.5) * hours_worked
        print(f"{fg('yellow')}Saturday's{attr('reset')} pay is: $",format(saturday_pay,".2f"))
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Saturday", format(saturday_pay,".2f")])
            return saturday_pay
        
    elif public_holiday in ["n", "N", "no" "No"] and shift_worked in ["afternoon", "Afternoon"]:
        saturday_pay = (base_rate * 1.5)  * hours_worked
        print(f"{fg('yellow')}Saturday's{attr('reset')} pay is: $",format(saturday_pay,".2f"))
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Saturday", format(saturday_pay,".2f")])
            return saturday_pay
    
    elif public_holiday in ["n", "N", "no" "No"] and shift_worked in ["night", "Night"]:
        saturday_pay = ((base_rate * 1.5) * 2) + ((base_rate * 1.8) * (hours_worked - 2))
        print(f"{fg('yellow')}Saturday's{attr('reset')} pay is: $",format(saturday_pay,".2f"))
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Saturday", format(saturday_pay,".2f")])
            return saturday_pay
    

# SUNDAY
def sunday(file_name):
    shift_worked = input(f"What {fg('yellow')}shift{attr('reset')} did you work on Sunday? Please enter 'Day', 'Afternoon' or 'Night'.  ")
    hours_worked = float(input(f"Please enter {fg('yellow')}hours worked{attr('reset')} on Sunday  : "))
    public_holiday = input(f"Was Sunday a {fg('yellow')}public holiday?{attr('reset')} y/n.  ")

    if public_holiday in ["y", "Y", "yes", "Yes"]:
        sunday_pay = (base_rate * 2.5) * hours_worked
        print(f"{fg('yellow')}Sunday's{attr('reset')} pay is: $",format(sunday_pay,".2f"))
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Sunday", format(sunday_pay,".2f")])
            return sunday_pay
        
    elif public_holiday in ["n", "N", "no" "No"] and shift_worked in ["day", "Day"]:
        sunday_pay = (base_rate * 1.8)  * hours_worked
        print(f"{fg('yellow')}Sunday's{attr('reset')} pay is: $",format(sunday_pay,".2f"))
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Sunday", format(sunday_pay,".2f")])
            return sunday_pay
        
    elif public_holiday in ["n", "N", "no" "No"] and shift_worked in ["afternoon", "Afternoon"]:
        sunday_pay = (base_rate * 1.8)  * hours_worked
        print(f"{fg('yellow')}Sunday's{attr('reset')} pay is: $",format(sunday_pay,".2f"))
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Sunday", format(sunday_pay,".2f")])
            return sunday_pay
    
    elif public_holiday in ["n", "N", "no" "No"] and shift_worked in ["night", "Night"]:
        sunday_pay = ((base_rate * 1.8) * 2) + ((base_rate * 1.25) * (hours_worked - 2))
        print(f"{fg('yellow')}Sunday's{attr('reset')} pay is: $",format(sunday_pay,".2f"))
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Sunday", format(sunday_pay,".2f")])
            return sunday_pay
        
