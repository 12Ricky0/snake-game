import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
turtle.colormode(255)
timmy.shape("turtle")
#timmy.pensize(1)
timmy.speed("fastest")
screen = Screen()




# for _ in range(50):
#   timmy.penup()
#  timmy.forward(10)
#   timmy.pendown()
#   timmy.forward(10)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


direction = [0, 90, 180, 270]
# def shape(num_sides):
#    angle = 360 / num_sides
#    for i in range(num_sides):
#        timmy.forward(100)
#        timmy.right(angle)


# for num in range(3, 6):
#    timmy.color(random.choice(colors))
#    shape(num)

for _ in range(3):

    timmy.color(random_color())
    timmy.circle(120, 180)
#    timmy.forward(100)
#    timmy.setheading(random.choice(direction))


screen.exitonclick()
