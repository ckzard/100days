import time
from turtle import Screen, onkeypress
from player import Player
from car_manager import CarManager
from scoreboardcrossing import Scoreboard
import threading

#turtle crossing

#screen code
screen = Screen()
screen.bgcolor("white")
screen.setup(600, 800)
screen.tracer(0)

#create player
player = Player()
carmanager = CarManager()
scoreboard = Scoreboard()

game_is_on = True

# def reset_game():
    
#     game_is_on = True
#     player.reset_player()
#     scoreboard.reset_score()

screen.listen()

onkeypress(player.move, "w")
# onkeypress(reset_game, "space")

while game_is_on:
    time.sleep(0.05)
    screen.update()
    carmanager.gen_car()
    carmanager.move_cars()

    #detect collision between turtle and car
    for car in carmanager.cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    #detect collision with top of screen to increase score
    if player.ycor() >= 390:
        player.reset_player()
        scoreboard.update_score()

screen.exitonclick()