from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race, Enter a color: ")

#TURTLE RACE

is_race_on = False
colors = ["red", "orange", "yellow", "green", "blue", 'purple']
# contestants = [timmy, tommy, tammy, tonny, tilly, jeff]
all_turtles = []
i = 0
y_value = -100


#setup the turtles
for t in range(0, 6):
    new_turtle = Turtle()
    new_turtle.penup()

    new_turtle.shape("turtle")

    new_turtle.color("black")
    new_turtle.fillcolor(colors[i])
    i += 1

    new_turtle.goto((-240, y_value))
    y_value += 50
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() >= 240:
            print(turtle.color()[1], "wins")
            if turtle.color()[1] == user_bet:
                print("YOU WON!!!!")
            else:
                print("your turtle was too slow :O")
            is_race_on = False


screen.exitonclick()