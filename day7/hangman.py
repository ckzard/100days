def game_start():

    lives = 5
    word_to_guess = 'cheese'
    word_split = []
    for letter in word_to_guess:
        word_split.append(letter)

    user_guess = []

    for letter in word_to_guess:
        user_guess.append('-')

    print(user_guess)

    while user_guess != word_split and lives > 0:
        guess = input("Please enter a possible letter in the word: \n")

        print("You guessed", guess)
        count = 0
        for letter in word_to_guess:
            if letter == guess:
                user_guess[count] = guess

            count += 1
        if guess not in word_to_guess:
            lives -= 1

        print(user_guess)
        print("You have", lives, "left!")

    print("The word was", word_to_guess)


game_start()

