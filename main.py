from turtle import Turtle,Screen
tim = Turtle()
screen = Screen()
def forward():
    tim.forward(10)

def back():
    tim.backward(10)

def left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(forward, "w")
screen.onkey(back, "s")
screen.onkey(right, "d")
screen.onkey(left, "a")
screen.onkey(clear, "c")
screen.exitonclick()







