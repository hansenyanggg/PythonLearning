from turtle import Turtle

class Ball(Turtle):
    '''class generating a ball for the Pong Game'''

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.x_move_dist = 5
        self.y_move_dist = 5

    def move(self):
        new_x = self.xcor() + self.x_move_dist
        new_y = self.ycor() + self.y_move_dist
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move_dist *= -1

    def bounce_x(self):
        self.x_move_dist *= -1

    def reset(self):
        self.goto(0, 0)
        self.bounce_x()
