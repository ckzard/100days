from turtle import Screen
from scoreboard import ScoreBoard
from snake import Snake
from food import Food
import time

# SNAKE 2.0s

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake")
screen.tracer(0)

#create the snake object
snake = Snake()

#create food object
food = Food()

#create scoreboard
scoreboard = ScoreBoard()

#listen for key strokes
screen.listen()

screen.onkeypress(snake.up, 'w')
screen.onkeypress(snake.down, 's')
screen.onkeypress(snake.left, 'a')
screen.onkeypress(snake.right, 'd')

game_start = True

while game_start == True:
    #managing animation
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision with food
    if snake.head.distance(food) < 15:
        print("nom nom")
        food.refresh()
        snake.grow()
        scoreboard.increase_score()

    #detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        # game_start = False
        scoreboard.reset_score()
        snake.reset_snake()

# list_ex[::-1] <--- this will reverse the list
    #detect collision with self
    for part in snake.body_parts[1:]:
       if snake.head.distance(part) < 10:
            # game_start = False
            scoreboard.reset_score()
            snake.reset_snake()
    

    
screen.exitonclick()