import random

def dice_game():
    print("Welcome to my dice game!!")  # Greet the player

# Get the player's name and lucky number input
your_name = input("Please enter your name: ")
lucky_number = int(input("Please select a lucky number between 1 and 6: "))

# Initialize computer's dice roll
computer_die_roll = random.randint(1, 6)
print("The computer rolled: ", computer_die_roll)  # Display the computer's roll

# Check if the player's guess matches, is too high, or too low
if computer_die_roll > lucky_number:
    print("You guessed too low!")
elif computer_die_roll < lucky_number:
    print("You guessed too high!")
else:
    print("You guessed correct, well done!")
