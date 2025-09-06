# TODO: Ask the user for an input
user_choice = input("Pick a choice (rock/paper/scissors): ")

# TODO: Make a random choice for the computer
# Note: Read the slide for this part
cpu_choice = None

# TODO: Determine if the user wins, the cpu wins, or its a draw

# Challenge: TODO: Robust Input
# Challenge: TODO: Multi-rounds

from random import choice

options = ["rock", "paper", "scissors"]
random_option = choice(options)
print(random_option )