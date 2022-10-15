from turtle import Screen
from paddle import Paddle

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

user_paddle = Paddle()
window.update()

window.listen()
window.onkey(user_paddle.move_up, "Up")
window.onkey(user_paddle.move_down, "Down")

window.exitonclick()