import turtle as t
import random as r

color_list = [
    (240, 242, 245), (223, 236, 228), (236, 230, 216), (140, 176, 207),
    (25, 32, 48), (26, 107, 159), (237, 225, 235), (209, 161, 111),
    (144, 29, 63), (230, 212, 93), (4, 163, 197), (218, 60, 84), (229, 79, 43),
    (195, 130, 169), (54, 168, 114), (28, 61, 116), (172, 53, 95),
    (108, 182, 90), (110, 99, 87), (193, 187, 46), (240, 204, 2), (1, 102, 119),
    (19, 22, 21), (50, 150, 109), (172, 212, 172), (118, 36, 34),
    (221, 173, 188), (227, 174, 166), (153, 205, 220), (184, 185, 210)
    ]

klik = t.Turtle()
screen = t.Screen()

screen.setup(1200, 700)
screen.colormode(255)
klik.speed("fastest")
klik.ht()

lines = 0
klik.penup()
klik.sety(-150)
while lines != 10:
    klik.setx(-150)
    for i in range(10):
        klik.dot(20, r.choice(color_list))
        klik.penup()
        klik.fd(50)
    klik.sety(klik.ycor() + 50)
    lines += 1

screen.exitonclick()

# ====================== UDEMY CODE ====================== #
#
# import turtle as turtle_module
# import random
#
# turtle_module.colormode(255)
# tim = turtle_module.Turtle()
# tim.speed("fastest")
# tim.penup()
# tim.hideturtle()
# color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
# tim.setheading(225)
# tim.forward(300)
# tim.setheading(0)
# number_of_dots = 100
#
# for dot_count in range(1, number_of_dots + 1):
#     tim.dot(20, random.choice(color_list))
#     tim.forward(50)
#
#     if dot_count % 10 == 0:
#         tim.setheading(90)
#         tim.forward(50)
#         tim.setheading(180)
#         tim.forward(500)
#         tim.setheading(0)
#
#
#
#
#
#
#
#
#
# screen = turtle_module.Screen()
# screen.exitonclick()






















#import colorgram
#
#
# def get_colours(img, number_colors):
#     rgb_colors = []
#     for i in range(number_colors):
#         colors = colorgram.extract(img, number_colors)
#         red = colors[i].rgb[0]
#         green = colors[i].rgb[1]
#         blue = colors[i].rgb[2]
#         color_tuple = (red, green, blue)
#         rgb_colors.append(color_tuple)
#     return rgb_colors


# ====================== UDEMY CODE ====================== #
#
# rgb_colors = []
# colors = colorgram.extract("imagee.jpg", 20)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
