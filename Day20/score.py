from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("red")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 0, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(f"GameOver", align="center", font=("Arial", 50, "normal"))

    def score_increase(self):
        self.score +=1
        self.clear()
        self.update_score()