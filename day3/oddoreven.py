def odd_even():
    
    char_inputted = input("Please enter a number, and I will tell you if its odd or even (enter q to quit) \n")

    while char_inputted != "q":
        
        if int(char_inputted) % 2 == 0:
            print("Its even")
        else:
            print("its odd")

        char_inputted = input("Please enter a number, and I will tell you if its odd or even (enter q to quit) \n")

odd_even()