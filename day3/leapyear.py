def is_leap_year(given_year):

    # given_year = int(input("Please enter the year, and I will tell you if its a leap year: \n"))

    if given_year % 4 == 0:
        if given_year % 20 == 0:
            if given_year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
