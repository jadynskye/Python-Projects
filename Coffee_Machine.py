#Coffee machine in Python!

Hot_coffee_flavors = [
    {
        "Name" : "Espresso",
        "Price" : 1.50,
        "Ingredients" : {
            "Water" : 50,
            "Coffee" : 18
        }
    },

    {
        "Name" : "Latte",
        "Price" : 2.50,
        "Ingredients" : {
            "Water" : 200,
            "Coffee" : 150,
            "Milk" : 150

        }
    },

    {
        "Name" : "Cappuccino",
        "Price" : 3.00,
        "Ingredients" : {
            "Water" : 250,
            "Coffee" : 24,
            "Milk" : 100
        }
    } 
]

water = 500
milk = 500
coffee = 400 
money = 0

#inventory to keep items more accessible
inventory = {"Water": water, "Milk": milk, "Coffee": coffee}

#check the resources in the drinks and compare them with the inventory
def check_resources(drink, inventory):
        #if items are missing append them here - it will return true or false for if missing
        missing = []

        for item in drink:
            if drink[item] > inventory[item]:
                missing.append(item)

        if missing:
            print("Sorry, not enough:", ", ".join(missing))
            return False
        return True

def process_coins(cost):
    quarters = .25
    dimes = .10
    nickles = .05
    pennies = .01

    total = cost

    users_quarters = int(input("How many quarters? "))
    users_dimes = int(input("How many dimes? "))
    users_nickles = int(input("How many nickles? "))
    users_pennies = int(input("How many pennies? "))

    total_paid = (users_quarters * quarters) + (users_dimes * dimes) + (users_nickles * nickles) + (users_pennies * pennies)

    if total_paid < cost:
        print("Sorry you did not insert enough money, money refunded")
        return False

    change = total_paid - cost
    print(f"Change returned: ${change:.2f}")
    return True

def update_report(drink, inventory, cost):
    #for every item in drink, minus and save the result back in inventory 
    for item in drink:
        inventory[item] -= drink[item]
    #update cash 
    return cost
    
        
#start of program 
machine = True

while machine == True:

    print("\n  Jadyns coffee house menu \n"
          "=============================\n"
          f"      {Hot_coffee_flavors[0]['Name']}: ${Hot_coffee_flavors[0]['Price']}\n"
          f"      {Hot_coffee_flavors[1]['Name']}: ${Hot_coffee_flavors[1]['Price']}\n"
          f"      {Hot_coffee_flavors[2]['Name']}: ${Hot_coffee_flavors[2]['Price']}\n"
          "=============================\n"
    )
        
    inital_choice = input("Hi welcome to Jadyns Coffee Shop, What would you like? ").lower()

    if inital_choice == "espresso":

        ok = check_resources(Hot_coffee_flavors[0]['Ingredients'], inventory)

        if ok:
            paid = process_coins(Hot_coffee_flavors[0]['Price'])
            if paid:
                money += update_report(Hot_coffee_flavors[0]['Ingredients'], inventory, Hot_coffee_flavors[0]['Price'])
        
    elif inital_choice == "latte":
        ok = check_resources(Hot_coffee_flavors[1]['Ingredients'], inventory)

        if ok:
            paid = process_coins(Hot_coffee_flavors[1]['Price'])
            if paid:
                money += update_report(Hot_coffee_flavors[1]['Ingredients'], inventory, Hot_coffee_flavors[1]['Price'])

    elif inital_choice == "cappuccino":
        ok = check_resources(Hot_coffee_flavors[2]['Ingredients'], inventory)

        if ok:
            paid = process_coins(Hot_coffee_flavors[2]['Price'])
            if paid:
                money += update_report(Hot_coffee_flavors[2]['Ingredients'], inventory, Hot_coffee_flavors[2]['Price'])

    elif inital_choice == "report":
        print("\n==================\n"
            "  Coffee Report\n"
            "==================\n"
            f"Water: {inventory['Water']}ml\n"
            f"Milk: {inventory['Milk']}ml\n"
            f"Coffee: {inventory['Coffee']}g\n"
            f"Money: ${money:.2f}\n")
    elif inital_choice == "off":
        print("Machine is turning off, goodbye.")
        machine = False
    else:
        print("Sorry that was not a valid chioce, please try again")

