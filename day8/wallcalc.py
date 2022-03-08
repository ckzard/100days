import math

def area_calc(height, width, coverage=5):
    num_cans = (height * width) / 5

    print("You will need", math.ceil(num_cans), "cans of paint for this wall!")

area_calc(3, 9)