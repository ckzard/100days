import game_data
import random
import os

def high_low():

    follower_answer = 0
    correct_answers = 0
    failed_answers = 0

    while failed_answers == 0:
        os.system("clear")
        rando_items = gen_random_items()
        f = open("day14/highlow.txt", "r")
        print("".join([line for line in f]))

        print("Compare", rando_items[0]["name"], "a", rando_items[0]["description"], "from", rando_items[0]["country"])

        # v = open("day14/versus.txt", 'r')
        # print("".join([line for line in v]))

        print("=====================================================")

        print("Against", rando_items[1]["name"], "a", rando_items[1]["description"], "from", rando_items[1]["country"])

        if correct_answers > 0:
            print("You have", correct_answers, "point")

        follower_answer = input("Who has more followers? Type 'A' or 'B': \n")

        higher_follower_count = ''

        if rando_items[0]["follower_count"] > rando_items[1]["follower_count"]:
            higher_follower_count = 'A'
        else:
            higher_follower_count = 'B'

        if follower_answer != higher_follower_count:
            failed_answers += 1
            print("OOPS, you got that one wrong!")
            print(rando_items[0]["name"], "has", rando_items[0]["follower_count"], " million followers \n")
            print(rando_items[1]["name"], "has", rando_items[1]["follower_count"], " million followers \n")
            print(correct_answers)
            #ending the game
        else:
            correct_answers +=1
            print("Correct!")
            print(rando_items[0]["name"], "has", rando_items[0]["follower_count"], " million followers \n")
            print(rando_items[1]["name"], "has", rando_items[1]["follower_count"], " million followers \n")
            #continuing the while loop

def gen_random_items():

    rando_items = []

    #generate a random number to grab an item from the dictionary and add it to the list
    for n in range (0, 2):
        new_item = game_data.data[random.randint(0, len(game_data.data) - 1)]

        #ensure we are not generating the same number
        if new_item not in rando_items:
            rando_items.append(new_item)
        else:
            new_item = game_data.data[random.randint(0, len(game_data.data) - 1)]
            rando_items.append(new_item)

    return(rando_items)

high_low()
