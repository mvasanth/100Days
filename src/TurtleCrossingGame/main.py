import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

MAX_LEVELS = 10

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

kurma = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(kurma.move, "Up")

is_game_on = True
loop_var = 0
scoreboard.write_level()

while is_game_on:
    time.sleep(car_manager.move_speed)
    screen.update()

    car_manager.keep_cars_moving()

    if loop_var % 20 == 0:
        car_manager.add_new_car()

    loop_var += 1

    # The car manager only needs to keep track of all the cars that are presently on the screen.
    car_manager.update_cars()

    # Detect collision with any car
    for car in car_manager.get_cars():
        if kurma.distance(car) < 20:
            scoreboard.game_over()
            is_game_on = False
    
    # Detect if the turtle has reached the end of the screen and up the level, and speed up the cars.
    if kurma.is_level_cleared():
        kurma.reset_player()
        scoreboard.increment_level()
        car_manager.increase_speed()
    
    if scoreboard.get_level() == MAX_LEVELS:
        scoreboard.declare_winner()
        is_game_on = False

screen.exitonclick()
    
