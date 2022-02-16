def days_left():
    age = input("What is your current age: \n")

    life_span_days = (90 - int(age)) * 365
    life_span_weeks = (90 - int(age)) * 52
    life_span_months = (90 - int(age)) * 12

    print(f"You have {life_span_days} days, {life_span_weeks} weeks, and {life_span_months} months left.")

days_left()
