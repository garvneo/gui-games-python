from turtle import Turtle
from random import randint, choice

COLORS = [
    "red",
    "yellow",
    "green",
    "cyan",
    "blue",
    "orange",
    "lime",
    "light salmon",
    "medium spring green",
    "brown",
    "dark orange",
    "purple",
]

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Cars:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = randint(1, 3)
        if random_chance == 3:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2, outline=2)
            new_car.penup()
            new_car.goto(500, randint(-240, 240))
            new_car.color(choice(COLORS))
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
