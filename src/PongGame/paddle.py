from turtle import Turtle

class Paddle:
    WIDTH = 20
    HEIGHT = 100
    MOVE_DISTANCE = 20
    UP = 90
    DOWN = 270

    def __init__(self, pos):
        self.paddle = Turtle("square")
        self.paddle.color("white")
        self.paddle.penup()
        self.paddle.setheading(self.UP)
        self.paddle.shapesize(stretch_wid=1, stretch_len=5, outline=None)
        self.paddle.goto(pos)
    
    def move(self):
        self.paddle.forward(self.MOVE_DISTANCE)
    
    def move_up(self):
        self.paddle.setheading(self.UP)
        self.move()
    
    def move_down(self):
        self.paddle.setheading(self.DOWN)
        self.move()
    
    def get_paddle(self):
        return self.paddle