# from turtle import Turtle, Screen
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("red")
# screen = Screen()
# screen.exitonclick()

#Draw a Square
# from turtle import Turtle, Screen
# turtle_square = Turtle()
# turtle_square.shape("turtle")
# turtle_square.color("red")
#
# for _ in range(4):
#     turtle_square.forward(100)
#     turtle_square.right(90)
#
# screen = Screen()
# screen.exitonclick()

#Draw a dashed lines
# from turtle import Turtle, Screen
# turtle_dashed = Turtle()
# turtle_dashed.shape("turtle")
# turtle_dashed.color("red")
#
# for _ in range(15):
#     turtle_dashed.forward(10)
#     turtle_dashed.penup()
#     turtle_dashed.forward(10)
#     turtle_dashed.pendown()
#
# screen = Screen()
# screen.exitonclick()


#Draw Different shapes

# from turtle import Turtle, Screen
# import random
# shapes = Turtle()
# shapes.shape("turtle")
# colors = ["red", "blue", "green", "yellow", "pink", "orange", "brown"]
#
# def draw_shape(num_sides):
#
#     angle = 360/num_sides
#     for _ in range(num_sides):
#         shapes.forward(100)
#         shapes.right(angle)
#
# for shape_side_n in range(3,11):
#
#     shapes.color(random.choice(colors))
#     draw_shape(shape_side_n)

# screen = Screen()
# screen.exitonclick()


#Draw a random walk
# import turtle as t
# from turtle import Turtle, Screen
# import random
#
# timmy = Turtle()
# screen = Screen()
# timmy.shape("turtle")
#
# def random_color():
#     r = random.randint(0,255)
#     b = random.randint(0,255)
#     g = random.randint(0,255)
#     random_colours = (r,g,b)
#     return random_colours
#
# t.colormode(255)
# # colors = ["red", "blue", "green", "yellow", "pink", "orange", "brown"]
# directions = [0, 90, 180, 270]
# timmy.pensize(15)
# timmy.speed(5)
#
# for _ in range(200):
#     timmy.color(random_color())
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))
#
# screen.exitonclick()


#Spirography
# from turtle import Turtle, Screen
# import turtle as t
# import random
#
# timmy = Turtle()
# timmy.shape("turtle")
# t.colormode(255)
#
# def random_color():
#     r = random.randint(0,255)
#     b = random.randint(0,255)
#     g = random.randint(0,255)
#     colour = (r,g,b)
#     return colour
#
# timmy.speed(25)
# timmy.color(random_color())
#
# def draw_spirograph(size_of_gap):
#     for _ in range(int(360/ size_of_gap)):
#         timmy.color(random_color())
#         timmy.circle(100)
#         timmy.setheading(timmy.heading() + size_of_gap)
# draw_spirograph(5)
#
# screen = Screen()
# screen.exitonclick()


#Dots Painting



