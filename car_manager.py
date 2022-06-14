from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []

    def add_car(self):
        new_car = Turtle(shape="square")
        new_car.pu()
        new_car.shapesize(1.0, 1.5)
        new_car.color(random.choice(COLORS))
        new_car.setpos(280, random.randint(-200, 220))
        new_car.setheading(180)
        self.cars.append(new_car)

    def move_car(self):
        for car in self.cars:
            if car.xcor() > -350:
                car.forward(MOVE_INCREMENT)
            else:
                car.clear()
