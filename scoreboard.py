from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 1
        self.printscore()

    def finalscore(self):
        self.goto(0, 0)
        self.write(f"Your score was {self.score}", align="Center", font=(10))

    def printscore(self):
        self.reset()
        self.hideturtle()
        self.penup()
        self.goto(-170, 170)
        self.write(f"Level : {self.score}", font=(8))

    def scoreincrease(self):
        self.score += 1
        self.printscore()
