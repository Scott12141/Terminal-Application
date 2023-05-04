
from colored import fg, attr
import csv

# Gets user input of thier base rate, runs try/except to make sure the value is a float and not negative.
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

# Gets user input of thier hours worked, runs try/except to make sure the value is a float and less than minimum hours.
def user_hours_worked(day_of_week):
    global hours_worked
    hours_worked = ''
    while True:
        input_hours = (input(f"Please enter {fg('yellow')}hours worked {attr('reset')}on {day_of_week} : "))
        try:
            hours_worked = float(input_hours)
            if hours_worked < 4:
                raise ValueError
            break
        except ValueError:
            print(f"{fg('red')} '{input_hours}' is not a valid amount of hours worked, please re-enter{attr('reset')}")
    return hours_worked;

# Gets user input of the shift they worked, runs if/else to make sure the input is a valid string.
def user_shift_worked(day_of_week):
    global shift_worked
    shift_worked = ''
    while True:
        input_shift = input(f"What {fg('yellow')}shift{attr('reset')} did you work on {day_of_week}? Please enter 'Day', 'Afternoon' or 'Night'.  ")
        if input_shift in ["Day", "day", "afternoon", "Afternoon", "night", "Night"]:
            shift_worked = input_shift
            break   
        else:
            print(f"{fg('red')} '{input_shift}' is not a valid shift worked, please re-enter{attr('reset')}")
    return shift_worked;

# Gets user input to see if it was a public holiday, runs if/else to make sure the input is a valid string.
def ph_penalties(day_of_week):
    global public_holiday
    public_holiday = ''
    while True:
        input_ph = input(f"Was {day_of_week} a {fg('yellow')}public holiday?{attr('reset')}  y/n.  ")
        if input_ph in ["y", "Y", "yes", "Yes", "n", "N", "no", "No"]:
            public_holiday = input_ph
            break   
        else:
            print(f"{fg('red')} '{input_ph}' is not a valid responce, please enter y or n{attr('reset')}")
    return public_holiday;

# Calculates Public Holiday loading rate of pay 
def public_holiday_pay(base_rate, hours_worked):
    ph_pay = (base_rate * 2.5) * hours_worked
    return ph_pay
# Calculates Day shift rate of pay 
def day_shift_pay(base_rate, hours_worked):
    ds_pay = base_rate  * hours_worked
    return ds_pay
# Calculates Afternoon shift loading rate of pay 
def arvo_shift_pay(base_rate, hours_worked):
    as_pay = (base_rate * 1.15)  * hours_worked
    return as_pay
# Calculates Night shift loading rate of pay 
def night_shift_pay(base_rate, hours_worked):
    ns_pay = (base_rate * 1.25)  * hours_worked
    return ns_pay
# Calculates Saturday loading rate of pay 
def sat_loading_pay(base_rate, hours_worked):
    satl_pay = (base_rate * 1.5) * hours_worked
    return satl_pay
# Calculates Sunday loading rate of pay 
def sun_loading_pay(base_rate, hours_worked):
    sunl_pay = (base_rate * 1.8) * hours_worked
    return sunl_pay

# Creates a function to calculate how much pay the user gets on any given day thats entered based on:
# which shift they worked, then writes it to the csv
# MONDAY
def monday(file_name):
    user_shift_worked("Monday")
    user_hours_worked("Monday")
    ph_penalties("Monday")

    if public_holiday in ["y", "Y", "yes", "Yes"]:
        monday_pay = public_holiday_pay(base_rate, hours_worked)
        print(f"{fg('yellow')}Monday's{attr('reset')} pay is: $",format(monday_pay,".2f"))
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Monday", format(monday_pay,".2f")])
            return monday_pay
             
    elif public_holiday in ["n", "N", "no", "No"] and shift_worked in ["day", "Day"]:
        monday_pay = day_shift_pay(base_rate, hours_worked)
        print(f"{fg('yellow')}Monday's{attr('reset')} pay is: $",format(monday_pay,".2f"))
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Monday", format(monday_pay,".2f")])
            return monday_pay
        
    elif public_holiday in ["n", "N", "no", "No"] and shift_worked in ["afternoon", "Afternoon"]:
        monday_pay = arvo_shift_pay(base_rate, hours_worked)
        print(f"{fg('yellow')}Monday's{attr('reset')} pay is: $",format(monday_pay,".2f"))
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Monday", format(monday_pay,".2f")])
            return monday_pay
    
    elif public_holiday in ["n", "N", "no", "No"] and shift_worked in ["night", "Night"]:
        monday_pay = night_shift_pay(base_rate, hours_worked)
        print(f"{fg('yellow')}Monday's{attr('reset')} pay is: $",format(monday_pay,".2f"))
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Monday", format(monday_pay,".2f")])
            return monday_pay
    

# TUESDAY
def tuesday(file_name):
    user_shift_worked("Tuesday")
    user_hours_worked("Tuesday")
    ph_penalties("Tuesday")

    if public_holiday in ["y", "Y", "yes", "Yes"]:
        tuesday_pay = public_holiday_pay(base_rate, hours_worked)
        print(f"{fg('yellow')}Tuesday's{attr('reset')} pay is: $",format(tuesday_pay,".2f"))
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Tuesday", format(tuesday_pay,".2f")])
            return tuesday_pay
        
    elif public_holiday in ["n", "N", "no" "No"] and shift_worked in ["day", "Day"]:
        tuesday_pay = day_shift_pay(base_rate, hours_worked)
        print(f"{fg('yellow')}Tuesday's{attr('reset')} pay is: $",format(tuesday_pay,".2f"))
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Tuesday", format(tuesday_pay,".2f")])
            return tuesday_pay
        
    elif public_holiday in ["n", "N", "no" "No"] and shift_worked in ["afternoon", "Afternoon"]:
        tuesday_pay = arvo_shift_pay(base_rate, hours_worked)
        print(f"{fg('yellow')}Tuesday's{attr('reset')} pay is: $",format(tuesday_pay,".2f"))
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Tuesday", format(tuesday_pay,".2f")])
            return tuesday_pay
    
    elif public_holiday in ["n", "N", "no" "No"] and shift_worked in ["night", "Night"]:
        tuesday_pay = night_shift_pay(base_rate, hours_worked)
        print(f"{fg('yellow')}Tuesday's{attr('reset')} pay is: $",format(tuesday_pay,".2f"))
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Tuesday", format(tuesday_pay,".2f")])
            return tuesday_pay
    

# WEDNESDAY
def wednesday(file_name):
    user_shift_worked("Wednesday")
    user_hours_worked("Wednesday")
    ph_penalties("Wednesday")

    if public_holiday in ["y", "Y", "yes", "Yes"]:
        wednesday_pay = public_holiday_pay(base_rate, hours_worked)
        print(f"{fg('yellow')}Wednesday's{attr('reset')} pay is: $",format(wednesday_pay,".2f"))
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Wednesday", format(wednesday_pay,".2f")])
            return wednesday_pay
        
    elif public_holiday in ["n", "N", "no" "No"] and shift_worked in ["day", "Day"]:
        wednesday_pay = day_shift_pay(base_rate, hours_worked)
        print(f"{fg('yellow')}Wednesday's{attr('reset')} pay is: $",format(wednesday_pay,".2f"))
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Wednesday", format(wednesday_pay,".2f")])
            return wednesday_pay
        
    elif public_holiday in ["n", "N", "no" "No"] and shift_worked in ["afternoon", "Afternoon"]:
        wednesday_pay = arvo_shift_pay(base_rate, hours_worked)
        print(f"{fg('yellow')}Wednesday's{attr('reset')} pay is: $",format(wednesday_pay,".2f"))
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Wednesday", format(wednesday_pay,".2f")])
            return wednesday_pay
    
    elif public_holiday in ["n", "N", "no" "No"] and shift_worked in ["night", "Night"]:
        wednesday_pay = night_shift_pay(base_rate, hours_worked)
        print(f"{fg('yellow')}Wednesday's{attr('reset')} pay is: $",format(wednesday_pay,".2f"))
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Wednesday", format(wednesday_pay,".2f")])
            return wednesday_pay
   

# THURSDAY
def thursday(file_name):
    user_shift_worked("Thursday")
    user_hours_worked("Thursday")
    ph_penalties("Thursday")

    if public_holiday in ["y", "Y", "yes", "Yes"]:
        thursday_pay = public_holiday_pay(base_rate, hours_worked)
        print(f"{fg('yellow')}Thursday's{attr('reset')} pay is: $",format(thursday_pay,".2f"))
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Thursday", format(thursday_pay,".2f")])
            return thursday_pay
        
    elif public_holiday in ["n", "N", "no" "No"] and shift_worked in ["day", "Day"]:
        thursday_pay = day_shift_pay(base_rate, hours_worked)
        print(f"{fg('yellow')}Thursday's{attr('reset')} pay is: $",format(thursday_pay,".2f"))
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Thursday", format(thursday_pay,".2f")])
            return thursday_pay
        
    elif public_holiday in ["n", "N", "no" "No"] and shift_worked in ["afternoon", "Afternoon"]:
        thursday_pay = arvo_shift_pay(base_rate, hours_worked)
        print(f"{fg('yellow')}Thursday's{attr('reset')} pay is: $",format(thursday_pay,".2f"))
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Thursday", format(thursday_pay,".2f")])
            return thursday_pay
    
    elif public_holiday in ["n", "N", "no" "No"] and shift_worked in ["night", "Night"]:
        thursday_pay = night_shift_pay(base_rate, hours_worked)
        print(f"{fg('yellow')}Thursday's{attr('reset')} pay is: $",format(thursday_pay,".2f"))
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Thursday", format(thursday_pay,".2f")])
            return thursday_pay
    

# FRIDAY
def friday(file_name):
    user_shift_worked("Friday")
    user_hours_worked("Friday")
    ph_penalties("Friday")

    if public_holiday in ["y", "Y", "yes", "Yes"]:
        friday_pay = public_holiday_pay(base_rate, hours_worked)
        print(f"{fg('yellow')}Friday's{attr('reset')} pay is: $",format(friday_pay,".2f"))
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Friday", format(friday_pay,".2f")])
            return friday_pay
        
    elif public_holiday in ["n", "N", "no" "No"] and shift_worked in ["day", "Day"]:
        friday_pay = day_shift_pay(base_rate, hours_worked)
        print(f"{fg('yellow')}Friday's{attr('reset')} pay is: $",format(friday_pay,".2f"))
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Friday", format(friday_pay,".2f")])
            return friday_pay
        
    elif public_holiday in ["n", "N", "no" "No"] and shift_worked in ["afternoon", "Afternoon"]:
        friday_pay = arvo_shift_pay(base_rate, hours_worked)
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
    user_shift_worked("Saturday")
    user_hours_worked("Saturday")
    ph_penalties("Saturday")

    if public_holiday in ["y", "Y", "yes", "Yes"]:
        saturday_pay = public_holiday_pay(base_rate, hours_worked)
        print(f"{fg('yellow')}Saturday's{attr('reset')} pay is: $",format(saturday_pay,".2f"))
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Saturday", format(saturday_pay,".2f")])
            return saturday_pay
        
    elif public_holiday in ["n", "N", "no" "No"] and shift_worked in ["day", "Day"]:
        saturday_pay = sat_loading_pay(base_rate, hours_worked)
        print(f"{fg('yellow')}Saturday's{attr('reset')} pay is: $",format(saturday_pay,".2f"))
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Saturday", format(saturday_pay,".2f")])
            return saturday_pay
        
    elif public_holiday in ["n", "N", "no" "No"] and shift_worked in ["afternoon", "Afternoon"]:
        saturday_pay = sat_loading_pay(base_rate, hours_worked)
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
    user_shift_worked("Sunday")
    user_hours_worked("Sunday")
    ph_penalties("Sunday")

    if public_holiday in ["y", "Y", "yes", "Yes"]:
        sunday_pay = public_holiday_pay(base_rate, hours_worked)
        print(f"{fg('yellow')}Sunday's{attr('reset')} pay is: $",format(sunday_pay,".2f"))
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Sunday", format(sunday_pay,".2f")])
            return sunday_pay
        
    elif public_holiday in ["n", "N", "no" "No"] and shift_worked in ["day", "Day"]:
        sunday_pay = sun_loading_pay(base_rate, hours_worked)
        print(f"{fg('yellow')}Sunday's{attr('reset')} pay is: $",format(sunday_pay,".2f"))
        with open(file_name, "a")as pay_file:
            writer = csv.writer(pay_file)
            writer.writerow(["Sunday", format(sunday_pay,".2f")])
            return sunday_pay
        
    elif public_holiday in ["n", "N", "no" "No"] and shift_worked in ["afternoon", "Afternoon"]:
        sunday_pay = sun_loading_pay(base_rate, hours_worked)
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
    