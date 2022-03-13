from turtle import Turtle

FONT = {"Courier", 24, "normal"}
ALIGNMENT = "center"
END_FONT = {"Courier", 100, "normal"}

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color = ("black")
        self.penup()
        self.goto(-280, 380)
        self.write(f"Score: {self.score}", font=FONT)
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.score += 1
        self.goto(-280, 380)
        self.penup()
        self.write(f"Score: {self.score}", font=FONT)

    
    def game_over(self):
        self.clear()
        self.penup()
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
        self.goto(0, -50)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        self.clear()
        self.score = 0
        self.goto(-280, 380)
        self.penup()
        self.write(f"Score: {self.score}", font=FONT)
