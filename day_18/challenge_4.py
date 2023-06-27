from turtle import Turtle, Screen
import random

ark = Turtle()
screen = Screen()
ark.pensize(15)
screen.colormode(255)
ark.speed("fastest")


def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color = red, blue, green
    return color


def random_move():
    random.choice((ark.forward, ark.backward))(30)
    random.choice((ark.right, ark.left))(90)


def main():
    for i in range(300):
        random_move()
        ark.pencolor(random_color())

    screen.exitonclick()

# ============== UDEMY CODE ============== #

# import turtle as t
# import random
#
# tim = t.Turtle()
#
# colours = ["red", "green", "blue"]
# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")
#
# for i in range(200):
#     tim.color(random.choice(colours))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))


