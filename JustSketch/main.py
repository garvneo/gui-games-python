from turtle import Turtle, Screen

rocky = Turtle()
rocky.shape("turtle")
rocky.color("orange")
screen = Screen()


def move_forward():
    rocky.forward(10)


def move_backword():
    rocky.backward(10)


def turn_left():
    new_heading = rocky.heading() + 10
    rocky.setheading(new_heading)
    # rocky.left(10)


def turn_right():
    rocky.right(10)


def clear():
    rocky.clear()
    rocky.penup()
    rocky.home()
    rocky.pendown()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backword, "s")
screen.onkey(turn_right, "d")
screen.onkey(turn_left, "a")
screen.onkey(clear, "c")
screen.exitonclick()
