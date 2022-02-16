# Tip calculator

def tip_calc():

    total = float(input("What was the total bill:\n"))
    percent = int(input("What percentage tip would you like to give:\n")) / 100
    splitters = int(input("How many people are splitting the bill:\n"))

    tip_amount = (total * percent)
    amount_each  = (total + tip_amount) / splitters
    print("Each person should pay: " + "$" + str(round(amount_each, 2)))

tip_calc()