def cypher():

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    while direction != 'encode' and direction != 'decode':
            direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    text = input("Type your message: \n").lower()

    shift = int(input("Type the shift number:\n"))
    while shift > 36:
            shift = int(input("Type a lower number:\n"))
            
    encoded = ''
    decoded = ''
    #ERROR catching here for bad inputs


    if direction == 'encode':
        print("Encoding.....")
        for letter in text:
            if letter == ' ':
                    encoded += letter
            for num in range(0, len(alphabet)):
                if letter == alphabet[num]:
                    if num + shift >= len(alphabet):
                        encoded += alphabet[num + shift - len(alphabet)]
                    else:
                        encoded += alphabet[num + shift]
        print(encoded)

    elif direction == 'decode':
        print("Decoding.....")
        for letter in text:
            if letter == ' ':
                    decoded += letter
            for num in range(0, len(alphabet)):
                if letter == alphabet[num]:
                    if num + shift >= len(alphabet):
                        decoded += alphabet[num - shift + len(alphabet)]
                    else:
                        decoded += alphabet[num - shift]

        print(decoded)

cypher()