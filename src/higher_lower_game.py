import higher_lower_game_data
from art import higher_lower_logo
import random
import os

def get_option(data):
    """
    Randomly returns an element from the data list.
    """
    return random.choice(data)

def get_second_option(data, A):
    """
    Randomly returns an element from the data list.
    Ensures that the element returned does not match the first choice.
    """
    B = get_option(data)
    while B == A:
        B = get_option(data)
    
    return B

def compare(user_choice, other, score):
    """
    Compares the follower count of the two options.
    Returns the score, and a Boolean. 
    The Boolean is False, if the game needs to go on. 
    The Boolean is True, if the game needs to be ended.
    """
    if user_choice["follower_count"] > other["follower_count"]:
        score += 1
        return (score, False)
    else:
        return (score, True)

def play_game():
    """
    Implements a fun, simple version of the Higher-Lower game!
    """
    score = 0
    has_game_ended = False
    clear = lambda: os.system('clear')
    A = get_option(higher_lower_game_data.data)
    B = get_second_option(higher_lower_game_data.data, A)

    while not has_game_ended:
        clear()
        print(higher_lower_logo.logo)

        A = B
        B = get_second_option(higher_lower_game_data.data, A)
        
        if score > 0:
            print(f"You're right! Current Score: {score}")
        
        print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
        print(higher_lower_logo.vs)
        print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}.")
        user_option = input("Who has more followers? Type 'A' or 'B': ")

        if user_option == "A":
            (score, has_game_ended) = compare(A, B, score)
        else:
            (score, has_game_ended) = compare(B, A, score)

    clear()
    print(higher_lower_logo.logo)
    print(f"Sorry, that's wrong. Final score: {score}")

play_game()