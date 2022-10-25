# from turtle import Turtle, Screen
#
# timmy = Turtle()
#
# def move_fowd():
#     timmy.forward(10)
# def move_bckd():
#     timmy.backward(10)
# def turn_left():
#     new_heading = timmy.heading() + 10
#     timmy.setheading(new_heading)
# def turn_right():
#     new_heading = timmy.heading() + 10
#     timmy.setheading(new_heading)
# def clear():
#     timmy.clear()
#     timmy.penup()
#     timmy.home()
#     timmy.pendown()
#
# screen = Screen()
# screen.listen()
# screen.onkey(move_fowd, "w")
# screen.onkey(move_bckd, "s")
# screen.onkey(turn_left, "a")
# screen.onkey(turn_right, "d")
# screen.onkey(clear, "c")
# screen.exitonclick()



#Turtle Race
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=400, height=500)

colors = ["red", "blue", "green", "yellow", "purple", "orange"]
y_position = [-150, -100, -50, 0, 50]
user_bet = screen.textinput(title="Make your Bet", prompt="Which color will win the race? Enter a color:")
print(f"You choose {user_bet} color Turtle")
is_race_on = False
all_turtle = []

for turtle_index in range(0,5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won!, The {winning_color} is the winner")
            else:
                print(f"You loose!, The {winning_color} is the winner")

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()