import os

def coffee_machine():

    """
    Coffee machine needs to receive coins
    Print resources
    Check the resources are sufficient for the drink

    """

    resource_water = 300
    #300
    resource_milk = 200
    #200
    resource_coffee = 100
    #100
    resource_money = 0

    flavours = {
        "espresso" : {"water": 50, "coffee" : 18, "milk" : 0, "price" : 1.50},
        "latte" : {"water": 200, "coffee" : 24, "milk" : 150, "price" : 2.50},
        "cappuccino" : {"water": 250, "coffee" : 24, "milk" : 100, "price" : 3.00}
    }

    penny = 0.01
    dime = 0.10
    nickel = 0.05
    quarter = 0.25

    user_input = ''

    while user_input != 'quit':

        user_input = input("What would you like (espresso/latte/cappucino) or type 'quit' to quit: \n")

        if user_input == 'report':
            print("Coffee ->", resource_coffee)
            print("Milk ->", resource_milk)
            print("Water ->", resource_water)
            print("Money ->", resource_money)

        if user_input == 'espresso' or user_input == 'latte' or user_input == 'cappuccino':
            if user_input == 'espresso':
                if resource_water >= flavours[user_input]["water"] and resource_coffee >= flavours[user_input]["coffee"]:
                    print("Please insert coins", "$" + str(float(flavours[user_input]["price"])))

                    quarters = int(input("How many quarters?: "))
                    dimes = int(input("How many dimes?: "))
                    nickels = int(input("How many nickels?: "))
                    pennies = int(input("How many pennies?: "))

                    total = (quarters * quarter) + (dimes * dime) + (nickels * nickel) + (pennies * penny)

                    if total == flavours[user_input]["price"]:
                        print("Dispensing.......")
                        print(f"here is your {user_input} enjoy!")
                        f = open('day15/coffee.txt', 'r')
                        print("".join([line for line in f]))

                        resource_water -= flavours[user_input]["water"]
                        resource_coffee -= flavours[user_input]["coffee"]
                        resource_money += total

                    if total > flavours[user_input]["price"]:
                        print("Dispensing.......")
                        print(f"here is your {user_input} enjoy!")
                        f = open('day15/coffee.txt', 'r')
                        print("".join([line for line in f]))
                        print("here is", total - flavours[user_input]["price"], "in change!")
                        
                        resource_water -= flavours[user_input]["water"]
                        resource_coffee -= flavours[user_input]["coffee"]
                        resource_money += total - flavours[user_input]["price"]

                    if total < flavours[user_input]["price"]:
                        print("Not enough money entered, money refunded!")
                else:
                    if resource_water <= flavours[user_input]["water"]:
                        print("There is not enough water")
                    if resource_coffee <= flavours[user_input]["coffee"]:
                        print("There is not enough coffee")      
            else:
                if resource_water >= flavours[user_input]["water"] and resource_coffee >= flavours[user_input]["coffee"] and resource_milk >= flavours[user_input]['milk']:
                    print("Please insert coins", "$" + str(float(flavours[user_input]["price"])))

                    quarters = int(input("How many quarters?: "))
                    dimes = int(input("How many dimes?: "))
                    nickels = int(input("How many nickels?: "))
                    pennies = int(input("How many pennies?: "))

                    total = (quarters * quarter) + (dimes * dime) + (nickels * nickel) + (pennies * penny)

                    if total == flavours[user_input]["price"]:
                        print("Dispensing.......")
                        print(f"here is your {user_input} enjoy!")
                        
                        f = open('day15/coffee.txt', 'r')
                        print("".join([line for line in f]))

                        resource_water -= flavours[user_input]["water"]
                        resource_coffee -= flavours[user_input]["coffee"]
                        resource_milk -= flavours[user_input]["milk"]
                        resource_money += total

                    if total > flavours[user_input]["price"]:
                        print("Dispensing.......")
                        print(f"here is your {user_input} enjoy!")
                        print("here is", total - flavours[user_input]["price"], "in change!")
                        
                        f = open('day15/coffee.txt', 'r')
                        print("".join([line for line in f]))

                        resource_water -= flavours[user_input]["water"]
                        resource_coffee -= flavours[user_input]["coffee"]
                        resource_milk -= flavours[user_input]["milk"]
                        resource_money += total - flavours[user_input]["price"]

                    if total < flavours[user_input]["price"]:
                        print("Not enough money entered, money refunded!")
                else:
                    if resource_water <= flavours[user_input]["water"]:
                        print("There is not enough water")
                    if resource_coffee <= flavours[user_input]["coffee"]:
                        print("There is not enough coffee")
                    if resource_milk <= flavours[user_input]["milk"]:
                        print("There is not enough milk")
    
            
coffee_machine()





