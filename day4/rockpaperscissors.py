import random

def rock_paper_scissors():

    choice = input("Please choose rock, paper or scissors (r, p, s): \n")

    while choice != 'r' and choice != 'p' and choice != 's':

        choice = input("Please choose rock, paper or scissors (r, p, s): \n")

    if choice == 'r':
        choice = "Rock"
    elif choice == 'p':
        choice = 'Paper'
    else:
        choice = "Scissors"

    bot_choice = random.randint(1, 3)

    if bot_choice == 1:
        bot_choice = 'Rock'
    elif bot_choice == 2:
        bot_choice = 'Paper'
    else:
        bot_choice = 'Scissors'


    print('You chose', choice, 'the enemy chose', bot_choice)

    if (choice == bot_choice):
        print("You both chose", choice, "try again")
        rock_paper_scissors()

    if (choice == "Rock" and bot_choice == "Scissors"):
        print(choice, 'beats', bot_choice)
    if (choice == "Paper" and bot_choice == "Rock"):
        print(choice, 'beats', bot_choice)
    if (choice == "Scissors" and bot_choice == "Paper"):
        print(choice, 'beats', bot_choice)
    if (bot_choice == "Rock" and choice == "Scissors"):
        print(bot_choice, 'beats', choice)
    if (bot_choice == "Paper" and choice == "Rock"):
        print(bot_choice, 'beats', choice)
    if (bot_choice == "Scissors" and choice == "Paper"):
        print(bot_choice, 'beats', choice)
    
rock_paper_scissors()