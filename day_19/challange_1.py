from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.speed("slow")


def move_forwards():
    tim.forward(20)


def move_backwards():
    tim.backward(20)


def counter_clockwise():
    tim.left(360)


def clockwise():
    tim.right(360)


screen.listen()
screen.delay(50)
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=tim.reset)

screen.exitonclick()


# ================= UDEMY CODE ================= #
#
# from turtle import Turtle, Screen
#
# tim = Turtle()
# screen = Screen()
#
#
# def move_forwards():
#     tim.forward(10)
#
# def move_backwards():
#     tim.backward(10)
#
# def turn_left():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)
#
# def turn_right():
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# screen.listen()
# screen.onkey(move_forwards, "Up")
# screen.onkey(move_backwards, "Down")
# screen.onkey(turn_left, "Left")
# screen.onkey(turn_right, "Right")
# screen.onkey(clear, "c")
#
# screen.exitonclick()
