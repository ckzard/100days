import random

def pass_gen():
    final_pass = []
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    symbols = ["!", '#', '$', '%', '&', '(', ')', '*', '+']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    num_letters = int(input("How many letters do you want: \n"))
    num_symbols = int(input("How many symbols do you want: \n"))
    num_numbers = int(input("How many numbers do you want: \n"))

    # pass_length = num_letters + num_symbols + num_numbers
    #find index of character
    for num in range(1, num_letters):
        rando = random.randint(0, len(letters) - 1)
        final_pass.append(letters[rando])

    for num in range(1, num_symbols):
        rando = random.randint(0, len(symbols) - 1)
        final_pass.append(symbols[rando])

    for num in range(1, num_numbers):
        rando = random.randint(0, len(numbers) - 1)
        final_pass.append(numbers[rando])
    
    random.shuffle(final_pass)

    shuffled = ''

    for x in final_pass:
        shuffled += str(x)
    
    print(shuffled)
pass_gen()  