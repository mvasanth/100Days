from art import guess_number_logo
import random
import os

def guess_number():
    print(guess_number_logo.logo)
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    number = random.choice(range(1, 101))
    guess = 0

    difficulty = input("Choose a difficulty, type 'easy' or 'hard': " )

    if difficulty == "easy":
        attempts = 10
    elif difficulty == "hard":
        attempts = 5
    else:
        print("Invalid input.")
        return

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

def main_loop():
  done = False
  clear = lambda: os.system('clear')
  
  while not done:
    game_input = input("Do you want to play a game of guessing the number? Type 'y' or 'n': ")
  
    if game_input == 'y':
      clear()
      guess_number()
    else:
      done = True

main_loop()