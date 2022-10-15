from turtle import Turtle

class Paddle:
    WIDTH = 20
    HEIGHT = 100
    MOVE_DISTANCE = 20
    UP = 90
    DOWN = 270
    START_X = 350
    START_Y = 0

    def __init__(self):
        self.paddle = self.build_paddle()
    
    def build_paddle(self):
        paddle_seg = Turtle("square")
        paddle_seg.color("white")
        paddle_seg.penup()
#        paddle_seg.setheading(self.UP)
        paddle_seg.shapesize(stretch_wid=5, stretch_len=1, outline=None)
        paddle_seg.goto((self.START_X, self.START_Y))
        return paddle_seg
    
    def move(self):
        self.paddle.forward(self.MOVE_DISTANCE)
    
    def move_up(self):
        self.paddle.setheading(self.UP)
        self.move()
    
    def move_down(self):
        self.paddle.setheading(self.DOWN)
        self.move()