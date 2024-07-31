from turtle import Turtle


class Snake(object):
    positions = [(0, 0), (-10, 0)]

    def __init__(self, ):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in Snake.positions:
            self.add_segment(position)

    def add_segment(self, position):
        snake = Turtle(shape="square")
        snake.penup()
        snake.shapesize(0.5)
        snake.color("white")
        snake.goto(position)
        self.segments.append(snake)

    def extend_snake(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            x = self.segments[seg - 1].xcor()
            y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x, y)
        self.segments[0].forward(10)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()