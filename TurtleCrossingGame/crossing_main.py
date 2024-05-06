from turtle import Screen
from player import Player
from cars import Cars
from scorecard import Scorecard
import time

screen = Screen()
screen.title("Gaurav's Road Crossing Game")
screen.setup(width=1000, height=600)
screen.tracer(0)

player = Player()
cars = Cars()
level = Scorecard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)  # function to pause the code for 0.5 seconds
    screen.update()
    cars.create_car()
    cars.move()

    # Detect collision with cars

    for car in cars.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            level.game_over()

    # Detect crossing of finishing line

    if player.is_at_finishline():
        player.goto_start()
        level.level_up()
        cars.increase_speed()

screen.exitonclick()
