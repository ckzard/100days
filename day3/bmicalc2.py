def bmi_calc():
    height = input("Please enter your height in meters (e.g 1.80): ")
    weight = input("Please enter your weight in kilograms (e.g 62): ")
    weight_description = ''

    height_calc = float(height) * 1.75
    x = round(float(weight) / float(height_calc))

    if x < 18.5:
        weight_description = "underweight"
    elif x >= 18.5 and x <= 25:
        weight_description = "normal weight"
    elif x > 25 and x <= 30:
        weight_description = "overweight"
    elif x > 30 and x <= 35:
        weight_description = "obese"
    else:
        weight_description = 'clinically obese'

    print("Your body mass index is ", x, 'meaning you are ', weight_description)

bmi_calc()