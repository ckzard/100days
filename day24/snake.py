from turtle import Turtle

move_distance = 20

class Snake:

    def __init__(self):

        
        self.body_parts = []
        self.create_snake()
        self.head = self.body_parts[0]
    
    def create_snake(self):

        x_value = 0

        for part in range(3):
            body = Turtle(shape="square")
            body.penup()
            body.color("white")
            body.setx(x_value)
            x_value -= 20
            self.body_parts.append(body)

    def move(self):
        for part in range(len(self.body_parts) - 1, 0, -1):
    
        #get the coords for the second to last item, to give to the last item
            new_x = self.body_parts[part - 1].xcor()
            new_y = self.body_parts[part - 1].ycor()

            #giving the last item in the list, the coords to move it forward
            self.body_parts[part].goto(new_x, new_y)

        #move the self forward while game_start is true    
        self.body_parts[0].forward(move_distance)

    def up(self):
        if self.body_parts[0].heading() != 270:
            self.body_parts[0].setheading(90)

    def down(self):
        if self.body_parts[0].heading() != 90:
            self.body_parts[0].setheading(270)
    
    def left(self):
        if self.body_parts[0].heading() != 0:
            self.body_parts[0].setheading(180)

    def right(self):
        if self.body_parts[0].heading() != 180:
            self.body_parts[0].setheading(0)

    def grow(self):
        body = Turtle(shape="square")
        body.penup()
        body.color("white")
        body.setx(600)
        body.sety(600)
        self.body_parts.append(body)

    def reset_snake(self):
        for part in self.body_parts:
            part.goto(1000, 100)
        self.body_parts.clear()
        self.create_snake()
        self.head = self.body_parts[0]