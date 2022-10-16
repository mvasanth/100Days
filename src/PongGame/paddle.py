from turtle import Turtle
from scoreboard import ScoreBoard

class Paddle(Turtle):
    WIDTH = 20
    HEIGHT = 100
    MOVE_DISTANCE = 20
    UP = 90
    DOWN = 270

    def __init__(self, pos):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.setheading(self.UP)
        self.shapesize(stretch_wid=1, stretch_len=5, outline=None)
        self.goto(pos)
        self.scoreboard = ScoreBoard()
    
    def move(self):
        self.forward(self.MOVE_DISTANCE)
    
    def move_up(self):
        self.setheading(self.UP)
        self.move()
    
    def move_down(self):
        self.setheading(self.DOWN)
        self.move()
    
    def show_score(self, pos):
        self.scoreboard.write_score(pos)
    
    def increment_score(self):
        self.scoreboard.increment_score()