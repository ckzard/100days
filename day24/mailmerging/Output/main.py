#create a letter useing starting_letter.txt
#for each name in invited names txt
#replace [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

names = []
starting_lett = []

with open("../Input/Names/invited_names.txt", "r") as names_file:
    #readlines() can be used instead of the for loop
    for line in names_file:
        names.append(line)

with open ("../Input/Letters/starting_letter.txt", "r") as starting_letter:
    for line in starting_letter:
        starting_lett.append(line)

#starting_lett.replace(PLACEHOLDER, stripped_name)

for name in names:
    clean_name2 = name.strip('\n')

    starting_lett[0] = f"Dear {clean_name2}, \n"

    clean_name = name.strip('\n')

    new_letter = ''

    for line in starting_lett:
        new_letter += line

    # print("".join([line for line in starting_lett]))
    w = open(f"./ReadyToSend/{clean_name}.txt", "w+")
    w.write("".join(starting_lett))
    w.close()

