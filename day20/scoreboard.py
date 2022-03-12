from ctypes import alignment
from tkinter import CENTER, font
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.score = 0
        x_pos = 0
        y_pos = 260
        self.goto(x_pos, y_pos)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", align=ALIGNMENT, font=FONT)