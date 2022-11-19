from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 1
        self.printscore()
        self.graphics()

    def finalscore(self):
        self.goto(0, 0)
        self.write(f"Your score was {self.score}", align="Center", font=(10))

    def printscore(self):
        self.reset()
        self.hideturtle()
        self.penup()
        self.goto(-170, 170)
        self.write(f"Level : {self.score}", font=(8))
        self.graphics()

    def scoreincrease(self):
        self.score += 1
        self.printscore()

    def graphics(self):
        self.penup()
        self.goto(-100, 180)
        self.pendown()
        self.goto(100, 180)
        self.penup()
        self.goto(0, 180)
        self.write("Finish line", align="Center")
