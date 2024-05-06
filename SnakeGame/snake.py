from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_BLOCKS = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()

    def create_snake(self):
        for pos in STARTING_POSITION:
            self.add_scales(pos)
        self.head = self.snake[0]
        self.snake[0].shape("triangle")
        self.snake[0].color("orange")

    def add_scales(self, pos):
        snake_head = Turtle(shape="square")
        snake_head.color("white")
        snake_head.penup()
        snake_head.goto(pos)
        self.snake.append(snake_head)

    def extend(self):
        self.add_scales(self.snake[-1].position())

    def move_snake(self):
        for scale in range(len(self.snake) - 1, 0, -1):
            self.snake[scale].goto(
                self.snake[scale - 1].xcor(), self.snake[scale - 1].ycor()
            )
        self.head.forward(MOVE_BLOCKS)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for scale in self.snake:
            scale.goto(1200, 1200)
        self.snake.clear()
        self.create_snake()
        # self.head = self.snake[0]
