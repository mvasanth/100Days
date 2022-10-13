from turtle import Turtle, Screen
timmy = Turtle()
my_screen = Screen()

def move_forward():
    timmy.forward(10)

def move_backward():
    timmy.backward(10)

def move_counterclockwise():
    direction = timmy.heading()
    timmy.setheading(direction - 5)
    timmy.forward(10)

def move_clockwise():
    direction = timmy.heading()
    timmy.setheading(direction + 5)
    timmy.forward(10)
    
def clear_screen():
    timmy.clear()
    timmy.reset()

def move_up():
    timmy.setheading(90)
    move_forward()

def move_down():
    timmy.setheading(270)
    move_forward()

def move_right():
    timmy.setheading(timmy.heading() - 10)
    move_forward()

def move_left():
    timmy.setheading(timmy.heading() + 10)
    move_forward()

def etch_a_sketch():

    my_screen.listen()
    my_screen.onkey(move_forward, "w")
    my_screen.onkey(move_backward, "s")
    my_screen.onkey(move_counterclockwise, "a")
    my_screen.onkey(move_clockwise, "d")
    
    my_screen.onkey(move_up, "Up")
    my_screen.onkey(move_down, "Down")
    my_screen.onkey(move_right, "Right")
    my_screen.onkey(move_left, "Left")

    my_screen.onkey(clear_screen, "c")

    my_screen.exitonclick()

etch_a_sketch()