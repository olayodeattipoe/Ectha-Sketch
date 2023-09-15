from turtle import Turtle, Screen

screen = Screen()
tim = Turtle()
screen.listen()


def forward():
    tim.forward(10)


def backward():
    tim.backward(10)


def right():
    tim.right(10)


def left():
    tim.left(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.onkey(right, 'd')
screen.onkey(left, 'a')
screen.onkey(forward, 'w')
screen.onkey(backward, 's')
screen.onkey(clear, 'c')


screen.exitonclick()

