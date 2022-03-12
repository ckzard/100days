from turtle import Turtle, Screen, tiltangle
import random
#import turtle as t <--- this is aliasing so you can just do like t.Turtle()
# import heroes

tim = Turtle()

screen = Screen()
screen.colormode(255)

tim.shape("turtle")

tim.color("black")

#Square
# for _ in range(4):
#     tim.fd(100)
#     tim.right(90)
tim.fillcolor("red")

#Dashed line
# for _ in range(10):
#     tim.fd(20)
#     tim.color("white")
#     tim.fd(20)
#     tim.color("black")

#Dashed line
# for _ in range(20):
#     tim.fd(20)
#     tim.penup()
#     tim.fd(20)
#     tim.pendown()

#Super shape

# sides = 3
# angle_degree = 360 / sides
# shape_number = 8

# for shape in range(shape_number):
#     for side in range(sides):
#         tim.fd(100)
#         tim.right(angle_degree)

#     tim.color((random.randint(1, 255),random.randint(1, 255),random.randint(1, 255)))
#     sides += 1
#     angle_degree = 360 / sides

#random walk
# tim.speed(100)
# tim.pensize(15)
# iterations = 500
# rotations = [0, 90, 180, 270]
# left_or_right = [1, 2]

# for _ in range(iterations):
    
#     tim.color((random.randint(1, 255),random.randint(1, 255),random.randint(1, 255)))
#     rando_rotation = rotations[random.randint(0, len(rotations) - 1)]
#     rando_direction = left_or_right[random.randint(0, len(left_or_right) - 1)]
#     if rando_direction == 1:
#         tim.left(rando_rotation)
#     else:
#         tim.right(rando_rotation)
#     tim.fd(30)

#Manual circle
# tim.speed("fastest")
# tim.pensize(1)
# for _ in range(360):
#     tim.fd(1)
#     tim.right(1)

#Spirograph
# r = 100
# for _ in range(100):
#     tim.color((random.randint(1, 255),random.randint(1, 255),random.randint(1, 255)))
#     tim.circle(r)
#     tim.right(10)
























screen.exitonclick()