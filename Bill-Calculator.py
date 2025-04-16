#This is my first project that I have created, showcasing my use of if, elif, and else statements, f-strings, the round() funciton, and other math functions.
#tip calculator project day 1

bill = float(input("Welcome to the tip calculator! \nWhat was the total of the bill? $ "))
tip = int(input("How much tip would you like to leave? 10? 15? or your own value? "))
people = int(input("How many people to split the bill? "))

total = 0

if tip == 10:
    total_tip = bill * .10 
    total_bill = total_tip + bill
    total = round(total_bill / people, 2)
elif tip == 15:
    total_tip = bill * .15
    total_bill = total_tip + bill
    total = round(total_bill / people, 2)
else:
    tip_percentage = tip / 100
    total_tip = bill * tip_percentage 
    total_bill = total_tip + bill
    total = round(total_bill / people, 2)
    

print(f"Each person will pay ${total} ")


#An easier, more condensed way without if statements 


bill = int(input("Welcome to the tip calculator! \nWhat was the total of the bill? $ "))
tip = float(input("How much tip would you like to leave? 10? 15? or your own value? "))
people = int(input("How many people to split the bill? "))

bill_with_tip = round((tip / 100) * bill + bill, 2)
bill_total = round(bill_with_tip / people,2)

print(f"Each person should pay ${bill_total}")