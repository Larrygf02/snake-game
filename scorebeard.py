from turtle import Turtle

class Scorebeard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score {self.score}", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score {self.score}", align="center", font=("Arial", 24, "normal"))
        return self.score

    