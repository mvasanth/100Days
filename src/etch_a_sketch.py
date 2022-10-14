from turtle import Turtle, Screen
"""
Implement the game etch a sketch, where the user can draw with the keyboard. Use the following keys
w to move forward,
s to move backward,
d to move in a clockwise direction
a to move in the counter clockwise direction
up arrow to move up
down arrow to move down
left arrow to turn left
right arrow to turn right, and 
c to clear the screen.
"""
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

def move_left():
    timmy.setheading(timmy.heading() + 10)

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