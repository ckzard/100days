from turtle import Turtle, Screen, onkey, onkeypress
from ball import Ball
from scoreboardpong import ScoreBoard
from paddle import Paddle
import time
#Pong
#screen setup
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")

#turn off the animation
screen.tracer(0)

#creating Paddle objects
#left
paddle_1 = Paddle((-350, 0))
#right
paddle_2 = Paddle((350, 0))

#ball
ball = Ball()
#scoreboard
scoreboard = ScoreBoard()

#event listening
screen.listen()

onkeypress(paddle_1.move_up, 'w')
onkeypress(paddle_1.move_down, 's')

onkeypress(paddle_2.move_up, "Up")
onkeypress(paddle_2.move_down, "Down")

game_is_on = True
sleep_speed = 0.05
while game_is_on:

    time.sleep(sleep_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() <= -280:
        ball.bounce_y()

    #detect collision with right paddle
    if ball.distance(paddle_2) < 60 and ball.xcor() > 325:
        ball.bounce_x()
        sleep_speed -= 0.001
    if ball.distance(paddle_1) < 60 and ball.xcor() < -325: 
        ball.bounce_x()
        sleep_speed -= 0.001

    if ball.xcor() > 410:
        print("left player wins")
        scoreboard.score_1 += 1
        scoreboard.update_score()
        game_is_on = False
        

    if ball.xcor() < -410:
        print("right player wins")
        scoreboard.score_2 += 1
        scoreboard.update_score()
        game_is_on = False

scoreboard.game_over()        



screen.exitonclick()
