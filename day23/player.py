STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    def __init__(self):

       super().__init__()

       self.shape("turtle")
       self.setheading(90)
       self.color("black")
       self.penup()
       self.goto(STARTING_POSITION[0], STARTING_POSITION[1])

    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def reset_player(self):
       self.goto(STARTING_POSITION[0], STARTING_POSITION[1]) 