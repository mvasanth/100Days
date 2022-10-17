from turtle import Turtle

class Player(Turtle):
    STARTING_POSITION = (0, -280)
    MOVE_DISTANCE = 10
    FINISH_LINE_Y = 280
    MOVE_ORIENTATION = 90

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(self.MOVE_ORIENTATION)
        self.goto(self.STARTING_POSITION)

    def move(self):
        self.forward(self.MOVE_DISTANCE)
