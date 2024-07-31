from turtle import Turtle, Screen

timmy = Turtle()
tom = Turtle()
tom.shape("turtle")
screen = Screen()


def move_forward():
    timmy.forward(10)


def move_backward():
    timmy.backward(10)


def move_left():
    timmy.left(10)


def move_right():
    timmy.right(10)


def clear_screen():
    screen.reset()


screen.onkey(move_forward, "Right")
screen.onkey(move_backward, "Left")
screen.onkey(move_left, "Up")
screen.onkey(move_right, "Down")
screen.onkey(clear_screen, "space")
screen.listen()

screen.exitonclick()
