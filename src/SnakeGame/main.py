from turtle import Screen
import time
from snake import Snake

window = Screen()
window.setup(width=600, height=600)
window.bgcolor("black")
window.title("Snake Game!")
window.tracer(0)

snake = Snake()

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
    
window.exitonclick()