def is_leap_year():

    given_year = int(input("Please enter the year, and I will tell you if its a leap year: \n"))

    if given_year % 4 == 0:
        if given_year % 20 == 0:
            if given_year % 400 == 0:
                print("its a leap year")
            else:
                print("its not a leap year")
        else:
            print("its a leap year")
    else:
        print("its not a leap year")

is_leap_year()