from turtle import Turtle
import random

MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.car = Car()
        self.car.move()

class Car(Turtle):

    COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
    STARTING_MOVE_DISTANCE = 5

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(self.COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(280, random.randint(-250, 250))
        self.setheading(180)
    
    def move(self):
        self.forward(self.STARTING_MOVE_DISTANCE)
        
