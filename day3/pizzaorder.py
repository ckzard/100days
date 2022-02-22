from msvcrt import kbhit
from re import L


def pizza_order():

    size = input("What size pizza do you want (S, M, L): \n")

    while size != "S" and size != "M" and size != "L":
        size = input("What size pizza do you want (S, M, L): \n")

    add_pepp = input("Do you want pepperoni? (Y / N): \n")

    while add_pepp != "Y" and add_pepp != "N":
        add_pepp = input("Do you want pepperoni? (Y / N): \n")

    extra_cheese = input("Do you want extra cheese? (Y / N): \n")

    while extra_cheese != "Y" and extra_cheese != "N":
        extra_cheese = input("Do you want extra cheese? (Y / N): \n")

    total = 0

    if size == "S":
        total += 15
    elif size == "M":
        total += 20
    else:
        total += 25

    if extra_cheese:
        total += 1
    
    if add_pepp == "Y":
        if size == "M" or size == "L":
            total += 3
        else:
            total += 2

    print("Your final bill for this", size, "pizza is: $" + str(total))


pizza_order()  

    