from random import randint, choice
from turtle import Turtle, Screen, colormode
from turtle import Turtle

def draw_square(kurma):
    """
    Challenge 1: Draw a square.
    """
    for _ in range(4):
        kurma.forward(100)
        kurma.right(90)

def draw_dashed_line(kurma):
    """
    Challenge 2: Draw a dashed line.
    """
    kurma.pensize(3)
    kurma.color("purple")

    for _ in range(20):
        kurma.pendown()
        kurma.forward(10)
        kurma.penup()
        kurma.forward(10)

    kurma.pendown()

def draw_shapes(kurma):
    """
    Challenge 3: Draw the following shapes: triangle, square, pentagon, hexagon, heptagon, octogon, nonagon and decagon
                 Each with a random colour, overlaid on top of the other.
    """
    kurma.pensize(3)
    sides = 3

    for i in range(3, 11):
        sides = i
        angle = 360/sides
        (r, g, b) = getColour()
        kurma.color(r, g, b)
        for _ in range(sides):
            kurma.forward(100)
            kurma.right(angle)

def reset(kurma):
    """
    Clear the screen and restore the turtle to the starting/default position.
    """
    kurma.home()
    kurma.clear()

def draw_random_walk(kurma):
    """
    Challenge 4: Draw a Random walk
    """
    kurma.pensize(5)
    kurma.speed(7)
    directions = ["f", "b"]
    angles = ["r", "l"]
    i = 0

    while i < 100:
        # draw the walk
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        kurma.color(r, g, b)
        direction = choice(directions)
        
        if direction == "f":
            kurma.forward(20)
        elif direction == "b":
            kurma.backward(20)
        
        angle = choice(angles)

        if angle == "r":
            kurma.right(90)
        elif angle == "l":
            kurma.left(90)
        
        i += 1

def getColour():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)

# Challenge 5: Draw a Spirograph
def draw_spirograph(kurma, shift):
    kurma = Turtle()
    kurma.pensize(2)
    kurma.speed(7)
    kurma.shape("turtle")

    for _ in range(int(360/shift)):
        (r, g, b) = getColour()
        kurma.color(r, g, b)
        kurma.circle(100)
        kurma.setheading(kurma.heading() + shift)

def main():
    kurma = Turtle()
    kurma.color("DarkOrchid4")
    kurma.shape("turtle")
    colormode(255)

    draw_square(kurma)

    reset(kurma)
    draw_dashed_line(kurma)

    reset(kurma)
    draw_shapes(kurma)

    reset(kurma)
    draw_random_walk(kurma)

    reset(kurma)
    draw_spirograph(kurma, 5)

    my_screen = Screen()
    my_screen.exitonclick()

main()