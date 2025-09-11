from turtle import Turtle

MOVE_DIST = 25


class Paddle(Turtle):
    '''class generating a paddle for the Pong Game'''
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(position)


    def up(self):
        new_y = self.ycor() + MOVE_DIST
        self.goto(x=self.xcor(), y=new_y)

    def down(self):
        new_y = self.ycor() - MOVE_DIST
        self.goto(x=self.xcor(), y=new_y)

