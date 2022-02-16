def bmi_calc():
    height = input("Please enter your height in meters: ")
    weight = input("Please enter your weight in kilograms: ")

    x = float(height) * 1.75

    print("Your body mass index is ", round(float(weight) / float(x)))

bmi_calc()