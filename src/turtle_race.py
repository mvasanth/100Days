from random import randint
from turtle import Turtle, Screen, colormode

def get_colours():
    color_dict = {
        "violet": "dark violet",
        "indigo" : "indigo",
        "blue": "deep sky blue",
        "green" : "lime green",
        "yellow": "yellow",
        "orange": "dark orange",
        "red": "red"
    }
    return list(color_dict.values())

def turtle_race():
    window = Screen()
    window.setup(width=500, height=400)
    guess = window.textinput("Make a bet!", "Which color turtle will win? Enter a color of the rainbow: ") 
    print(guess)

    y_positions = [-120, -80, -40, 0, 40, 80, 120]
    is_race_on = True
    
    colors = get_colours()
    print(colors)

    if guess in colors:
        is_race_on = False
    else:
        for i in range(0, len(colors)):
            t = Turtle('turtle')
            t.penup()
            t.color(colors[i])
            t.goto(-240, y_positions[i])
        
        while is_race_on:
            is_race_on = False
            
    window.exitonclick()

turtle_race()