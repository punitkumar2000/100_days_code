#To Extract the colors
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('download.jfif', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
from turtle import Turtle,Screen
import turtle as turtle_module
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.speed(250)
timmy.penup()
timmy.hideturtle()
turtle_module.colormode(255)

color_list = [(197, 165, 119), (144, 81, 56), (220, 201, 138), (61, 95, 121), (165, 150, 54), (136, 162, 180), (131, 34, 23), (52, 119, 87), (73, 37, 29), (190, 96, 82), (145, 177, 150), (100, 76, 80), (165, 147, 157), (21, 92, 68), (28, 59, 75), (225, 177, 167), (59, 44, 46), (133, 29, 33), (180, 202, 179), (26, 84, 89), (88, 147, 129), (13, 70, 58), (42, 65, 89), (180, 99, 102), (216, 181, 186), (182, 191, 204)]

timmy.setheading(225)
# timmy.penup()
timmy.forward(300)
timmy.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    timmy.dot(20, random.choice(color_list))
    timmy.speed(250)
    # timmy.penup()
    timmy.forward(50)
    # timmy.pendown()

    if dot_count % 10 ==0:
        timmy.setheading(90)
        # timmy.penup()
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        # timmy.pendown()
        timmy.setheading(0)

screen = Screen()
screen.exitonclick()