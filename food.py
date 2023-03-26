from turtle import Turtle
import random

COLORS = ("blue", "red", "green", "purple", "pink", "yellow")

color_ran = random.choice(COLORS)


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(color_ran)
        self.speed("fastest")
        self.refrsh()

    def refrsh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        self.color(color_ran)
