def love_calculator(name1, name2):
    word1 = "TRUE"
    word2 = "LOVE"

    true = 0
    love = 0

    for letter in name1:
        if letter.upper() in word1:
            true += 1
            print(letter)
        if letter.upper() in word2:
            love += 1
            print(letter)

    for letter in name2:
        if letter.upper() in word1:
            true += 1
            print(letter)
        if letter.upper() in word2:
            love += 1
            print(letter)

    print(str(true) + str(love) + "%")

love_calculator("Christopher Burns", "Gabriella Brasileiro Santos")