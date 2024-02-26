from turtle import Turtle, Screen

tim = Turtle()
tim.color("blue")


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def turn_left():
    tim.left(15)


def turn_right():
    tim.right(15)


def reset_screen():
    tim.home()
    tim.clear()


screen = Screen()
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=reset_screen)
screen.exitonclick()
