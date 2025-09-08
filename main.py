import turtle

from food import Food
from snake import Snake
from scoreboard import Scoreboard
import time



screen = turtle.Screen()
snake = Snake()
food = Food()
scoreboard = Scoreboard()


# Screen Properties
screen.setup(600,600)
screen.colormode(255)
screen.bgcolor((204,255,153))
screen.title("Snake Game by Hansen Yang")
screen.tracer(0)

screen.listen()
screen.onkey(snake.go_up, "w")
screen.onkey(snake.go_left, "d")
screen.onkey(snake.go_down, "s")
screen.onkey(snake.go_right, "a")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.15)
    snake.move()

    # hitting food
    if snake.head.distance(food) < 15:
        food.generate()
        snake.extend()
        scoreboard.add_score()

    # hitting wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    # hitting its snake body.tail
    for segment in snake.snake_segment[1:]:
        if snake.head.distance(segment) < 5:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()


