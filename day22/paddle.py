from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        # 3 white squares on top of each other on the borders of the screen
        # self.paddle_pieces = []
        super().__init__()

        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(5, 1)
        self.goto(position)
        

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
        
    
    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)