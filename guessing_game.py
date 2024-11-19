"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""

# Import the random module.
import random
# Create the start_game function.

def start_game():
# Write your code inside this function.
    answer = random.randint(1,10)
    n = 3                               #the times for guess

    while n > 0:
        try:
            guess_number = int(input("Plz guess a number between 1 and 10: "))

            if guess_number < 1 or guess_number > 10:
                print("Please enter a number betwee 1 to 10")
                continue

            if guess_number > answer:
                print("Plz guess a smaller number")
            elif guess_number < answer:
                print("Plz guess a bigger number ")
            else: 
                print("Bingo!")
                break
            n -= 1
        except ValueError:
            print("Plz enter a number, between 1 and 10")
    else:
        print(f"Unfortunately, you do not have anymore time to guess. The correct number is {answer}")

start_game()
    
#   When the program starts, we want to:
#   ------------------------------------
#   1. Display an intro/welcome message to the player.
#   2. Store a random number as the answer/solution.
#   3. Continuously prompt the player for a guess.
#     a. If the guess is greater than the solution, display to the player "It's lower".
#     b. If the guess is less than the solution, display to the player "It's higher".

#   4. Once the guess is correct, stop looping, inform the user they "Got it"
#      and show how many attempts it took them to get the correct number.
#   5. Let the player know the game is ending, or something that indicates the game is over.

# ( You can add more features/enhancements if you'd like to. )


# Kick off the program by calling the start_game function.
