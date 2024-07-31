from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(0.5)
        self.color("green")
        self.speed("fastest")
        self.move()

    def move(self):
        x = random.randrange(-270, 270)
        y = random.randrange(-270, 270)
        self.goto(x, y)