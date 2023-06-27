import random
import turtle
from turtle import Turtle, Screen
from random import randrange

# ==================== MY CODE ==================== #

# 360 // (numbers of corners) = 360 / 4 = 90

tim = Turtle()
screen = Screen()

tim.speed("fastest")


def change_color():
    red = randrange(0, 255)
    green = randrange(0, 255)
    blue = randrange(0, 255)

    tim.color(red, green, blue)


def make_form():
    for i in range(sides):
        tim.right(360/sides)
        tim.forward(100)


screen.colormode(255)

draw = True
while draw:
    sides = 3
    while sides != 10:
        make_form()
        change_color()
        sides += 1
    draw = False

screen.exitonclick()

# ==================== UDEMY CODE ==================== #
#
# import turtle as t
#
# tim = t.Turtle()
#
# colors = ["red", "blue", "yellow", "purple", "red", "black"]
#
#
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for i in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side_n)

