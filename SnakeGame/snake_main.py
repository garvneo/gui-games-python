from turtle import Screen
from snake import Snake
from food import Food
from scorecard import Scorecard
import time

screen = Screen()
screen.setup(width=1200, height=700)
screen.bgcolor("black")
screen.title("Gaurav's Snake Game")


game_is_on = True

screen.tracer(0)

snake = Snake()
food = Food()
score = Scorecard()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


while game_is_on:
    # to handle the lag
    screen.update()
    time.sleep(0.1)

    snake.move_snake()

    # detect snake's collision with food
    if snake.head.distance(food) < 15:
        score.refresh()
        food.refresh()
        snake.extend()

    # detect snake's collision with wall
    if (
        snake.head.xcor() > 580
        or snake.head.xcor() < -580
        or snake.head.ycor() > 350
        or snake.head.ycor() < -350
    ):
        score.reset()
        snake.reset()

    # detect snake's collision with tail
    for scales in snake.snake[1:]:
        if snake.head.distance(scales) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()
