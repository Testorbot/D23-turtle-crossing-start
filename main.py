import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

DURATION = 0.3

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)
screen.listen()

player = Player()
cars = CarManager()
score = Scoreboard()

screen.onkey(player.move, "Up")

duration_time = DURATION

game_is_on = True
while game_is_on:
    time.sleep(duration_time)
    screen.update()

    # randomly add car
    if random.randint(1, 10) % 4 == 0:
        cars.add_car()
    cars.move_car()

    # detect car collision with player
    for car in cars.cars:
        if car.distance(player) < 20:
            score.game_over()
            game_is_on = False

    if player.check_end():
        score.score_increase()
        duration_time *= 0.5

screen.exitonclick()
