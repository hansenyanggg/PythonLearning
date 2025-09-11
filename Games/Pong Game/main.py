from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
scoreboard = Scoreboard()
ball = Ball()

# Screen Setup
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("2 Player Pong Game by Hansen")
screen.tracer(0)

# User input
paddle_left = Paddle((-350,0))
paddle_right = Paddle((350,0))

screen.listen()
screen.onkey(paddle_left.up, "w")
screen.onkey(paddle_left.down, "s")
screen.onkey(paddle_right.up, "Up")
screen.onkey(paddle_right.down, "Down")

game_is_on = True
DELAY_TIME = 0.05
while game_is_on:
    screen.update()
    time.sleep(DELAY_TIME)
    ball.move()

    # Ball is hitting the top/bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # condition for ball hitting the left paddle
    if ball.distance(paddle_left) < 50 and ball.xcor() < -330:
        ball.bounce_x()
        scoreboard.add_l_score()
        DELAY_TIME *= 0.8

    # condition for ball hitting the right paddle
    elif ball.distance(paddle_right) < 50 and ball.xcor() > 330:
        ball.bounce_x()
        scoreboard.add_r_score()
        DELAY_TIME *= 0.8

    # condition for right paddle misses
    elif ball.xcor() > 345:
        scoreboard.add_l_score()
        ball.reset()
        DELAY_TIME =0.05

    # condition for left paddle misses
    elif ball.xcor() < -345:
        scoreboard.add_r_score()
        ball.reset()
        DELAY_TIME =0.05







screen.exitonclick()






