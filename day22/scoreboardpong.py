from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        #two numbers, one for each player, indicating their score
        #line demarcating the center of the field
        self.score_1 = 0
        self.score_2 = 0

        self.color("white")
        self.penup()
        x_pos = 0
        y_pos = 260
        self.goto(x_pos, y_pos)
        self.write(f"{self.score_1} : {self.score_2}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def update_score(self):
       self.clear()
       self.write(f"{self.score_1}: {self.score_2}", align=ALIGNMENT, font=FONT)
       self.hideturtle()

    def game_over(self):
        x_pos = 0
        y_pos = 0
        self.goto(x_pos, y_pos)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
        x_pos = 0
        y_pos = -50
        self.goto(x_pos, y_pos)

        if self.score_1 > self.score_2:
            self.write(f"Player 1 Wins", align=ALIGNMENT, font=FONT)
        else:
            self.write(f"Player 2 Wins", align=ALIGNMENT, font=FONT)