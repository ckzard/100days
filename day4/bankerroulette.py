import random

def banker_roulette():
    names = input("Enter the names of the possible bill payers separated by a comma: \n").split(', ')
    rando = random.randint(1, len(names) - 1)

    print(names[rando], "will be paying the bill tonight hurray!")


banker_roulette()