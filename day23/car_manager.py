COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from secrets import choice
from turtle import Turtle
import random
import time
import threading


class CarManager:
    
    def __init__(self):
        
        self.cars = []

    def gen_car(self):
        random_chance = random.randint(1, 6)
        
        
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.color(choice(COLORS))
            new_car.penup()
            new_car.goto(280, random.randint(-380, 380))
            self.cars.append(new_car)


    def move_cars(self):

        for car in self.cars:
            new_x = car.xcor() - 10
            car.goto(new_x, car.ycor())
