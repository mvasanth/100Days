import random
from turtle import Turtle, Screen

color_dict = {
        "violet": "dark orchid",
        "indigo" : "navy",
        "blue": "deep sky blue",
        "green" : "lime green",
        "yellow": "yellow",
        "orange": "dark orange",
        "red": "red"
    }

def get_colors():
    return (list(color_dict.keys()), list(color_dict.values()))

def get_color_name(color):
    return (list(color_dict.keys())[list(color_dict.values()).index(color)])

def turtle_race():
    """
    Implements a turtle race game, where there are 7 turtles. Each corresponding to a color of the rainbow.
    The user makes a bets as to which turtle will win the race. 
    Reports if the user's bet won, and the winning turtle.
    """
    window = Screen()
    window.setup(width=500, height=400)
    (names, colors) = get_colors()
    y_positions = [-120, -80, -40, 0, 40, 80, 120]
    is_race_on = True
    turtles = []
    min_speed = 0
    max_speed = 10
    start_coord_x = -230
    end_coord_x = 230

    # Display rainbow colored turtles
    for i in range(0, len(colors)):
        t = Turtle('turtle')
        t.penup()
        t.color(colors[i])
        t.goto(start_coord_x, y_positions[i])
        turtles.append(t)
    
    # ASk the user for a bet
    guess = window.textinput("Make a bet!", "Which turtle will win? Enter a color:")
    print(f"You are betting on turtle: {guess}.")

    # Do not start the game prematurely
    if not guess in names:
        is_race_on = False
    else:
        # Turtle race begins!
        while is_race_on:
            for turtle in turtles:
                speed = random.randint(min_speed, max_speed)
                turtle.forward(speed)

                if turtle.xcor() > end_coord_x:
                    # turtle.color() returns a tuple of colors.
                    # turtle.color()[0] corresponds to the pencolor, the other is the fillcolor.
                    winning_turtle = turtle.color()[0]
                    is_race_on = False

        # Winner evaluation
        winning_turtle_name = get_color_name(winning_turtle)

        if guess == winning_turtle_name:
            print(f"You won! The {winning_turtle_name} indeed won the race!")
        else:
            print(f"You lose. The {winning_turtle_name} won the race!")

    window.exitonclick()

turtle_race()