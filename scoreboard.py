from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.score = 0
        self.write(arg=f"Score: {self.score}", align='center', font=('Arial', 20, 'bold'))

    def add_score(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score: {self.score}", align='center', font=('Arial', 20, 'bold'))

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(arg=f"Game Over! Your score is {self.score}", align='center', font=('Arial', 20, 'bold'))