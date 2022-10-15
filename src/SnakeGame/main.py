from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

window = Screen()
window.setup(width=600, height=600)
window.bgcolor("black")
window.title("Snake Game!")
window.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

window.listen()
window.onkey(snake.move_up, "Up")
window.onkey(snake.move_down, "Down")
window.onkey(snake.move_left, "Left")
window.onkey(snake.move_right, "Right")

window.update()
is_game_on = True

while is_game_on:
    window.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.get_snake_head().distance(food) < 15:
        snake.grow_snake()
        food.refresh()
        scoreboard.increment_score()
    
    # Detect collision with the wall
    if snake.is_colliding_with_wall():
        scoreboard.game_over()
        is_game_on = False
    
    # Detect collision with it's own body
    if snake.is_colliding_with_body():
        scoreboard.game_over()
        is_game_on = False
    
window.exitonclick()