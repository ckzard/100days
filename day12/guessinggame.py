import random


def number_guesser():
    f = open("day12/guessy.txt", 'r')
    print("".join([line for line in f]))

    print("Welcome to the Number Guessing Game! \n")
    print("I am thinking of a number between 1 and 100. \n")

    num_chosen = random.randint(1, 100)
    print(num_chosen)

    difficulty_choice = input("Choose a difficulty. Type 'Easy' or 'Hard': \n")

    attempts = 0

    if difficulty_choice == 'Easy':
        print("You have 10 attempts remaining to guess the number.")
        print("\n")
        attempts = 10
    
    if difficulty_choice == 'Hard':
        print("You have 5 attempts remaining to guess the number.")
        print("\n")
        attempts = 5

    guess = 0

    while guess != num_chosen:

        if attempts == 0:
            guess = num_chosen
            print("You've run out of guesses :(")
            print("the number was", num_chosen)
            return

        guess = int(input("Make a guess: \n"))

        if guess > num_chosen:
            print("Too high.")
            print("Guess again.")
            attempts -= 1
            print(f"You have {attempts} remaining!")
            print("---------------------------------")

        elif guess < num_chosen:
            print("Too low.")
            print("Guess again.")
            attempts -= 1
            print(f"You have {attempts} remaining!")
            print("---------------------------------")
            
        else:
            attempts -= 1
            print("YOUUUUUUUUUU GOT IT!!!!!!!!!!!!!!!!!")
            print(f"With {attempts} remaining")
        

number_guesser()
