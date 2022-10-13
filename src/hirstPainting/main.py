import colorgram
from turtle import Turtle, Screen, colormode
import random

def getColours():
    rgb_colors = []

    colours = colorgram.extract('/workspaces/100Days/src/hirstPainting/image.jpg', 2 ** 32)
    for colour in colours:
        rgb_color = (colour.rgb.r, colour.rgb.g, colour.rgb.b)
        rgb_colors.append(rgb_color)
    
    return rgb_colors

# This is the list of colours returned by the function above.
# This list is saved as the function is time intensive. Do not run it multiple times.
colors = [(211, 154, 97), (52, 107, 132), (176, 78, 34), (238, 246, 243), (200, 142, 33), (116, 155, 171), (124, 79, 98), (122, 175, 157), (229, 197, 128), (231, 238, 242), (190, 88, 109), (55, 38, 19), (11, 51, 65), (44, 168, 125), (197, 122, 141), (50, 125, 120), (167, 21, 29), (225, 94, 80), (244, 162, 160), (4, 28, 26), (38, 32, 34), (80, 148, 170), (162, 26, 21), (236, 165, 170), (98, 125, 160), (167, 207, 192), (22, 79, 91), (162, 203, 212), (55, 62, 76), (31, 85, 82), (184, 189, 203), (74, 65, 44)]

def draw_hirst_spot_painting(colors):
    colormode(255)
    my_screen = Screen()
    tim = Turtle()
    tim.hideturtle()
    tim.speed("fastest")
    tim.pensize(1)
    tim.penup()
    x = -220
    y = -220
    tim.setposition(x, y)

    for _ in range(10):
        tim.penup()
        tim.setposition(x, y)
        tim.pendown()

        for _ in range(10):
            tim.dot(20, random.choice(colors))
            tim.penup()
            tim.forward(50)
            tim.pendown()
        
        y += 50
    
    my_screen.exitonclick()

draw_hirst_spot_painting(colors)

