from turtle import Turtle

FONT = ("Ink Free", 24, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.ht()
        self.pu()
        self.goto(x=-280, y=250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f"GAME OVER", align="center", font=FONT)
