import turtle

# Variables
INITIAL_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DIST = 20

class Snake():
    def __init__(self):
        self.snake_segment = []
        self.create_snake()
        self.head = self.snake_segment[0]

    def create_snake(self):
        for coordinates in INITIAL_POSITION:
            self.add_segment(coordinates)

    def add_segment(self,position):
        new_segment = turtle.Turtle(shape="square")
        new_segment.penup()
        new_segment.goto(position)
        self.snake_segment.append(new_segment)

    def extend(self):
        self.add_segment(self.snake_segment[-1].position())

    def move(self):
        for i in range(len(self.snake_segment)-1,0,-1):
            x = self.snake_segment[i-1].xcor()
            y = self.snake_segment[i-1].ycor()
            self.snake_segment[i].goto(x,y)
        self.head.forward(MOVE_DIST)

    def go_left(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def go_up(self):
        if self.head.heading() != 270:
            self.snake_segment[0].setheading(90)

    def go_down(self):
        if self.head.heading() != 90:
            self.snake_segment[0].setheading(270)

    def go_right(self):
        if self.head.heading() != 0:
            self.snake_segment[0].setheading(180)





