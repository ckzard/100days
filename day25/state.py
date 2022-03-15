from turtle import Turtle

class State(Turtle):

    def __init__(self, state, position):
        super().__init__()
        
        if position[0] < 0:
            self.setheading(270)
        else:
            self.setheading(180)

        self.color = "black"
        self.penup()
        self.goto(position)
        self.write(state)
        self.hideturtle()
