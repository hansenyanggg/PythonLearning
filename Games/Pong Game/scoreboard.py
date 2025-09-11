from turtle import Turtle

class Scoreboard(Turtle):
    '''class generating a scoreboard for the Pong Game'''

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.goto(x=-100, y=250)
        self.write(self.l_score, align="center", font=("Arial", 24, "bold"))
        self.goto(x=100, y=250)
        self.write(self.r_score, align="center", font=("Arial", 24, "bold"))

    def add_l_score(self):
        self.clear()
        self.l_score += 1
        self.update()

    def add_r_score(self):
        self.clear()
        self.r_score += 1
        self.update()

    def reset(self):
        self.clear()
        self.l_score = 0
        self.r_score = 0
        self.update()

