from turtle import Turtle, Screen
import random

start_race = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("BET", "Name of first player:")
turtles = []


if user_bet:
    start_race = True

colors = ["red", "green", "blue", "yellow", "orange", "purple"]

position = 100
for color in colors:

    tim = Turtle(shape="turtle")
    tim.color(color)
    tim.penup()
    position -= 30
    tim.goto(-240, -position)
    turtles.append(tim)


while start_race:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            if user_bet.lower() == winner:
                print(f"Congratulations! The winner is {winner} turtle!")
            else:
                print(f"Sorry!, you lose! The winner is {winner} turtle")
            start_race = False
        steps = random.randint(0,10)
        turtle.forward(steps)



screen.exitonclick()
