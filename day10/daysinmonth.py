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

def days_in_month(year, month):

    leap = is_leap_year(year)
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if leap == True and month == 2:
        print("29")
    else:
        print(month_days[month - 1])


days_in_month(2022, 2)