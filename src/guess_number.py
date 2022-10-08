from art import guess_number_logo
import random

def guess_number():
    print(guess_number_logo.logo)
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    number = random.choice(range(1, 101))
    print(f"Psst, the number is {number}")
    guess = 0

    difficulty = input("Choose a difficulty, type 'easy' or 'hard': " )

    if difficulty == "easy":
        attempts = 10
    elif difficulty == "hard":
        attempts = 5

    while guess != number and attempts > 0:
        print(f"You have {attempts} remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess == number:
            print(f"You win! The number was {guess}")
            break
        else:
            attempts -= 1
            if guess > number:
                print("Too High")
            else:
                print("Too Low")
            
            if attempts == 0:
                print("You have run out of guesses. You lose.")
            else:
                print("Guess again.")

guess_number()