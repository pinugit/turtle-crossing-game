from turtle import Turtle
from random import randint, choice


class Level:

    def __init__(self) -> None:
        self.moving_speeds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.car_number = 20
        self.cars_list = []

    def start(self):
        for i in range(self.car_number):
            turtle = Turtle()
            turtle.penup()
            turtle.shape("square")
            turtle.right(180)
            turtle.turtlesize(1, 2)
            turtle.goto(randint(-160, 160), randint(-120, 120))
            self.cars_list.append(turtle)

    def move(self):
        for cars in self.cars_list:
            cars.forward(choice(self.moving_speeds))

    def make_car(self):
        turtle = Turtle()
        turtle.penup()
        turtle.shape("square")
        turtle.right(180)
        turtle.turtlesize(1, 2)
        turtle.goto(160, randint(-120, 120))
        self.cars_list.append(turtle)
