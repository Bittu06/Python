"""
We are going to write a program that generates a random number and asks the user to 
guess it. 
If the player’s guess is higher than the actual number, the program displays “Lower 
number please”. Similarly, if the user’s guess is too low, the program prints “higher 
number please” When the user guesses the correct number, the program displays the 
number of guesses the player used to arrive at the number. 
Hint: Use the random module.
"""

import random

# Generate a random number between 1 and 100
random_number = random.randint(1, 100)

# Initialize the number of guesses
number_of_guesses = 0

# Loop until the user guesses the correct number
while True:
    # Get the user's guess
    guess = int(input("Guess a number between 1 and 100: "))
    
    # Increment the number of guesses
    number_of_guesses += 1

    # Check if the user's guess is correct
    if guess == random_number:
        print(f"Congratulations! You guessed the correct number in {number_of_guesses} guesses.")
        break
    elif guess > random_number:
        print("Lower number please.")
    else:
        print("Higher number please.")

        