#Turtle

# from turtle import Turtle, Screen, pos

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# from turtle import *
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()


#using Pypi(For tables)

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Students_Names", ["Punit", "Rakesh", "Vishal"])
table.add_column("Students_Branch", ["CSE", "EE", "ME"])
table.add_row(["Sunil", "ECE"])
print(table)
