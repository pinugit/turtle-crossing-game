from turtle import Turtle, Screen
from level import Level
from scoreboard import Scoreboard
from time import sleep
import math


screen = Screen()
screen.setup(width=400, height=400)
screen.tracer(0)
level = Level()
level.start()

player = Turtle()
player.shape("square")
player.penup()
player.left(90)
player.goto(0, -150)
Scoreboard = Scoreboard()


def backward():
    player.backward(20)
    screen.update()


def forward():
    player.forward(20)
    screen.update()


screen.listen()
screen.onkey(fun=forward, key="w")
screen.onkey(fun=backward, key="s")

game_is_on = True

while game_is_on:
    level.move()
    sleep(0.1)
    screen.update()
    for cars in level.cars_list:
        # here key is a turtle object(car)
        if cars.xcor() < -220:
            level.make_car()
            level.cars_speeds.remove(
                level.cars_speeds[level.cars_list.index(cars)])
            cars.color("white")
            cars.clear()
            level.cars_list.remove(cars)
        if cars.distance(player) < 30 and math.isclose(float(player.ycor()), cars.ycor(), abs_tol=20):
            print("exit")
            game_is_on = False

    if player.ycor() > 180:
        player.goto(0, -160)
        level.progress()
        Scoreboard.scoreincrease()
sleep(1)
screen.clear()
Scoreboard.finalscore()
screen.exitonclick()
