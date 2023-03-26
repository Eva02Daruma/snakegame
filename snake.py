from turtle import Screen, Turtle
import time
import random

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
SNAKE_COLOR = "white"
COLORS = ("green", "blue")
rancolor = random.choice(COLORS)


# colores de serpiente:  impar blanco , par color

class Snake:

    def __init__(self):
        self.segmentos = []
        self.create_snake()
        self.head = self.segmentos[0]
        self.snake_speed = 0.1

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        nuevo_segmento = Turtle("square")
        nuevo_segmento.color(SNAKE_COLOR)
        nuevo_segmento.penup()
        nuevo_segmento.goto(position)
        self.segmentos.append(nuevo_segmento)

    def turbo_on(self):
        self.snake_speed = 0.05
        print(f"Turbo On ")

    def turbo_off(self):
        self.snake_speed = 0.1
        print(f"Turbo OFF ")

    def reset(self):
        for seg in self.segmentos:
            seg.goto(1000, 1000)
        self.segmentos.clear()
        self.snake_speed = 0.1
        self.create_snake()
        self.head = self.segmentos[0]

    def color_segment(self):
        # colorear segmentos impar blanco y par color
        for seg in self.segmentos[1::2]:
            seg.color(rancolor)

    def extend(self):
        # añade un nuevo segmento a la serpiente
        for position in STARTING_POSITIONS:
            self.add_segment(self.segmentos[-1].position())

    def move(self):
        # con este codigo todos los segmentos de la serpiente estaran seguiendo al primer segmento
        for seg_num in range(len(self.segmentos) - 1, 0, -1):
            new_x = self.segmentos[seg_num - 1].xcor()
            new_y = self.segmentos[seg_num - 1].ycor()
            self.segmentos[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
