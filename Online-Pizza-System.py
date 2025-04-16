#Python Pizza Delivery Program 

print("\nWelcome to Jadyns Pizza Place!")
size = input("What size would you like your pizza? S M or L ").strip().upper() #strip the spaces and make input uppercase
total = 0

#if/else/elif statements to choose size of pizza

if size == 'S':
    total = 10
elif size == 'M':
    total = 12
elif size == 'L':
    total = 15
else:
    print("Sorry invalid response, please restart your order.")

print(f"\nYour total so far is ${total}\n")

#Toppings for pizza 

toppings = input(
    "Would you like toppings or a plain cheese pizza?\n"
    "Type y to see the toppings availible and n to continue. "
    ).strip().lower()
#Show of toppings
if toppings == "y":
    print(
        "\nToppings:        \n"
        "Pepperoni = $1   \n"
        "Extra cheese = $2\n"
        "Olives = $1      \n"
        "Bacon = $4       \n"
        )
    selected_topping1 = input("Choose one, what would you like? ").strip().lower()
    #using if statements - need to find a way to be able to put in multiple choices at once
    if selected_topping1 == "pepperoni":
        total += 1
    if selected_topping1 == "extra cheese":
        total += 2
    if selected_topping1 == "olives":
        total += 1
    if selected_topping1 == "bacon":
        total += 4
    print(f"\nYour total is now ${total}\n")

    topping2 = input("Would you like to choose another? Type y for yes and n for no ").strip().lower()
    if topping2 == 'y':
        print(
        "\nToppings:        \n"
        "Pepperoni = $1   \n"
        "Extra cheese = $2\n"
        "Olives = $1      \n"
        "Bacon = $4       \n"
        )
        selected_topping2 = input("Choose one, what would you like? ").strip().lower()
        if selected_topping2 == "pepperoni":
            total += 1
        if selected_topping2 == "extra cheese":
            total += 2
        if selected_topping2 == "olives":
            total += 1
        if selected_topping2 == "bacon":
            total += 4
        print(f"\nYour total is now ${total}\n")
    else:
        print("Okay no problem, let's continue with your order!")
else:
    print(f"\nThank you for your order! Your total is {total}")
type_of_order = input("\nIs this order for pickup or delivery? ").strip().lower()
if type_of_order == "pickup":
    print("\nPerfect! Please come by in about 15-20 minutes")
else:
    address = input("\nWhat is your address? ")
    print(f"\nPerfect! We will see you at {address} in about 20 minutes. Please have the total of {total} ready at the door!")

#calculating tip if wanted 

tip_choice = input("\nDo you need help with calculating how much tip is necessary? Type y for yes and n for no ").strip().lower()
if tip_choice == 'y':
    tip_amount = input("How much would you like to leave? 10%, 15%, or 20%? ")
    if tip_amount == 10:
       total = (total * .10) + total
    elif tip_amount == 15:
        total = (total * .15) + total
    else:
        total = (total * .20) + total
    print(f"Your new total is ${total}")
else:
    print("Okay! See you soon!")