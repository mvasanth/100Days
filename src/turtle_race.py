import random
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
    return list(color_dict.keys())

def turtle_race():
    window = Screen()
    window.setup(width=500, height=400)
    colors = get_colours()
    y_positions = [-120, -80, -40, 0, 40, 80, 120]
    is_race_on = True
    turtles = []

    for i in range(0, len(colors)):
        t = Turtle('turtle')
        t.penup()
        t.color(colors[i])
        t.goto(-240, y_positions[i])
        turtles.append(t)
    
    guess = window.textinput("Make a bet", "Which turtle will win? Enter a color of the rainbow:")
    print(guess)

    if not guess in colors:
        is_race_on = False
    else:
        while is_race_on:
            for turtle in turtles:
                speed = random.randint(1, 10)
                turtle.forward(speed)

                if turtle.xcor() > 230:
                    print("This turtle has won")
                    is_race_on = False

    window.exitonclick()

turtle_race()