from turtle import Turtle
from random import randint, choice


class Level:

    def __init__(self) -> None:
        self.moving_speeds = [2, 3, 4]
        self.car_number = 10
        self.increased_car = 0
        self.cars_list = []
        self.cars_speeds = []
        self.color_list = ["orange", "red", "green", "blue", "black", "brown"]

    def start(self):
        for i in range(self.car_number):
            turtle = Turtle()
            turtle.penup()
            turtle.shape("square")
            turtle.color(choice(self.color_list))
            turtle.right(180)
            turtle.turtlesize(1, 2)
            turtle.goto(randint(-160, 160), randint(-120, 120))
            self.cars_list.append(turtle)
            self.cars_speeds.append(choice(self.moving_speeds))

    def move(self):
        for i in range(len(self.cars_list)):
            self.cars_list[i].forward(self.cars_speeds[i])

    def make_car(self):
        turtle = Turtle()
        turtle.penup()
        turtle.shape("square")
        turtle.color(choice(self.color_list))
        turtle.right(180)
        turtle.turtlesize(1, 2)
        turtle.goto(160, randint(-120, 120))
        self.cars_list.append(turtle)
        self.cars_speeds.append(choice(self.moving_speeds))

    def progress(self):
        self.increased_car += 1
        for i in range(self.increased_car):
            self.make_car()
