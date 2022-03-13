from ctypes import alignment
from tkinter import CENTER, font
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.score = 0
        with open('highscore.txt') as file:
            self.highscore = int(file.read())
        x_pos = 0
        y_pos = 260
        self.goto(x_pos, y_pos)
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def reset_score(self):

        if self.score > self.highscore:
            self.highscore = self.score
            with open('highscore.txt', mode='w') as file:
                file.write(str(self.highscore))

        self.score = 0
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER!", align=ALIGNMENT, font=FONT)