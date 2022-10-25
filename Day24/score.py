from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("red")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 0, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")

        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GameOver", align="center", font=("Arial", 50, "normal"))

    def score_increase(self):
        self.score +=1
        self.clear()
        self.update_score()