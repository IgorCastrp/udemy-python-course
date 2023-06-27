import turtle as t
from challenge_4 import random_color
edw = t.Turtle()
screen = t.Screen()

edw.speed("fastest")
edw.pensize()

angle = 0
count = 0
for i in range(73):
    edw.circle(100)
    edw.setheading(angle)
    edw.pencolor(random_color())
    angle += 5
    count += 1
    if count % 10 == 0:
        angle += 10


screen.exitonclick()


# =================== UDEMY CODE =================== #

# def draw_spirograph(size_of_gap):
#     for i in range(int(360/size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         time.setheading(tim.heading() + size_of_gap)
#
# draw_spirograph(5)
