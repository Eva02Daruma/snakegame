from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=680, height=680)
screen.bgcolor("black")
screen.title("Mi juego de Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.turbo_on, "w")
screen.onkey(snake.turbo_off, "s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(snake.snake_speed)
    snake.move()

    # Detectar colision con comida
    if snake.head.distance(food) < 15:
        food.refrsh()
        snake.color_segment()
        snake.extend()
        scoreboard.increase_score()

    # detectar colision con pared
    if snake.head.xcor() > 320 or snake.head.xcor() < -320 or snake.head.ycor() > 320 or snake.head.ycor() < -320:
        scoreboard.reset()
        snake.reset()

    # detectar colision con cola
    for segment in snake.segmentos[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

    # Niveles
    if scoreboard.score < 9:
        screen.bgcolor("black")
    elif scoreboard.score >= 10:
        pass


screen.exitonclick()
