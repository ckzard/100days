import random

def coin_flip():
    randonumber = random.randint(0, 1)

    if randonumber == 1:
        print("Heads")
    else:
        print("Tails")

coin_flip()