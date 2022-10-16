from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

window = Screen()
window.title("Welcome to a game of Pong!")
window.setup(width=800, height=600)
window.bgcolor("black")
window.tracer(0)

# net = Turtle("square")
# net.color("white")
# net.penup()
# net.goto(0, -300)
# net.setheading(90)
# net.pensize(10)

# for i in range(20):
#     net.pendown()
#     net.forward(20)
#     net.penup()
#     net.forward(30)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()

window.listen()
window.onkey(l_paddle.move_up, "w")
window.onkey(l_paddle.move_down, "s")
window.onkey(r_paddle.move_up, "Up")
window.onkey(r_paddle.move_down, "Down")

ball.move()
window.update()

is_game_on = True

while is_game_on:
    window.update()
    time.sleep(0.1)
    ball.move()

    # Detect collision with the wall
    if ball.is_colliding_with_wall():
        ball.bounce_y()
    
    # Detect collision with either of the paddles 
    if ball.is_colliding_with_paddle(r_paddle) or ball.is_colliding_with_paddle(l_paddle):
        ball.bounce_x()

window.exitonclick()