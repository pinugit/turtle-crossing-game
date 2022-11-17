from turtle import Turtle, Screen
from level import Level
from time import sleep

screen = Screen()
screen.setup(width=400, height=400)
screen.tracer(0)
level = Level()
level.start()

player = Turtle()
player.shape("turtle")
player.penup()
player.left(90)
player.goto(0, -150)


def forword():
    player.forward(20)
    screen.update()


screen.listen()
screen.onkey(fun=forword, key="space")

game_is_on = True
while game_is_on:
    level.move()
    sleep(0.1)
    screen.update()
    for car in level.cars_list:
        if car.xcor() < -220:
            level.make_car()
            car.color("white")
            level.cars_list.remove(car)


screen.exitonclick()
