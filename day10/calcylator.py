def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calc_app(prev_result='a'):

    f = open("day10/calcy.txt", "r")
    print(''.join([line for line in f]))
    print("\n")

    print("Welcome to the calculator")
    if prev_result != 'a':
        first_num = prev_result
    else:

        first_num = int(input("Please enter the first number: \n"))
    operation = input("Please enter the operation you would like to perform: (e.g: add, *, /, minus) \n")
    second_num = int(input("Please enter the second number: \n"))


    print("\n")
    print("calculating..............")
    print("\n")

    result = 0

    if operation == "add" or operation == '+' or operation == 'addition':
        result = add(first_num, second_num)
    elif operation == "substract" or operation == 'minus' or operation == '-':
        result = subtract(first_num, second_num)
    elif operation == "multiply" or operation == "times" or operation == "x" or operation == "*":
        result = multiply(first_num, second_num)
    elif operation == "divide" or operation == '/' or operation == 'division':
        result = divide(first_num, second_num)
    else:
        result = ("Operation not recognized....goodbye!")

    print(result)
    
    keep_calc = input("Do you want to keep calculating after " + str(result) + " type 'y' or 'n': \n")

    if keep_calc == 'n':

        go_again = input("Do you want to perform another operation? type 'y' or 'n': \n")

        if go_again == 'y':
            calc_app()
        else:
            print("\n")
            print("Okay, thats cool..............Goodbye")
            return
    else:

        calc_app(result)

calc_app()