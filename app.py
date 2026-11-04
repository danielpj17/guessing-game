import random
from analyticskit import *

while True:
    secret_number = random.randint(1, 10)
    guess = int(single_input("Guess a number between 1 and 10."))

    if guess == secret_number:
        show_message('You win!', "You win! You guessed the correct number.")
    else:
        show_message('You lose', f"You lose. The correct number was {secret_number}.")

    play_again = single_input('Would you like to play again? Enter y/n.')
    if play_again.lower() != 'y':
        break# Insert your python code here
