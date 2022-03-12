from random import randint, random
import colorgram
from turtle import Turtle, Screen

# colors = colorgram.extract("day18/ashepika.jpg", 30)
# rgb_colors = []

# for color in colors:
#     rgb_colors.append(tuple(color.rgb))

# print(rgb_colors)

color_list = [(52, 117, 91), (42, 104, 131), (140, 183, 167), (181, 154, 54), (18, 52, 42), (185, 148, 102), (27, 51, 59), (124, 80, 59), (70, 163, 119), (27, 86, 69), (69, 36, 31), (112, 173, 186), (212, 223, 220), (60, 159, 168), (25, 82, 88), (242, 214, 84), (249, 239, 225), (147, 212, 198), (170, 97, 92), (189, 227, 237), (53, 62, 77), (59, 49, 51), (163, 97, 98), (95, 50, 44), (77, 73, 37), (87, 53, 56), (100, 74, 76), (46, 135, 213), (135, 212, 228), (168, 165, 166)]

screen = Screen()
screen.colormode(255)

timmy = Turtle()
x_value = -300
y_value = -300
timmy.speed(15)
timmy.pensize(25)


for row in range(10):
    
    timmy.penup()
    timmy.setx(x_value)
    timmy.sety(y_value)
    timmy.pendown()

    for line in range(10):
        timmy.color(color_list[randint(0, len(color_list) - 1)])
        timmy.pendown()
        timmy.fd(3)
        timmy.penup()
        timmy.fd(50)
    
    y_value += 50














screen.exitonclick()