from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 250
UP = 90

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.go_start_pt()
        self.setheading(UP)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def go_start_pt(self):
        self.goto(STARTING_POSITION)

    def check_end(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.go_start_pt()
            return True
        else:
            return False

