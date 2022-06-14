from turtle import Turtle

SCORE_POS = (-200, 220)

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.pu()
        self.ht()
        self.setpos(SCORE_POS)
        self.score = 1
        self.score_display()

    def score_display(self):
        self.write(f"Level: {self.score}", False, align='center', font=FONT)

    def score_increase(self):
        self.score += 1
        self.clear()
        self.score_display()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", False, align='center', font=FONT)
