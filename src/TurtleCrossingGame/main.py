import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager, Car
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

cars = []
kurma = Player()

screen.listen()
screen.onkey(kurma.move, "Up")

game_is_on = True
loop_var = 0

while game_is_on:
    time.sleep(0.1)
    screen.update()

    for car in cars:
        car.move()

    if loop_var % 20 == 0:
        car = Car()
        cars.append(car)

    loop_var += 1

    # Detect collision with any car
    cars_present = screen.turtles()
    print(cars_present)

    # Detect if the turtle has reached the end of the screen 
    
