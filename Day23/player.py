from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GameOver", align="center", font=("Arial", 50, "normal"))


    def is_at_final(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def go_to_start(self):
        self.goto(STARTING_POSITION)





