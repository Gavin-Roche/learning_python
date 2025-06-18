# This program generates a series of random numbers between 0 and 100.
# It writes each random number to a CSV file and also writes the total sum of the numbers at the end.

import random

# Creating or clearing the file initially
file = open("Random_number_game.csv", "w")
file.write("")
file.close()

# Initializing variables
numbersofnumbers = 5
total = 0

# Generating random numbers and writing them to the CSV file
for items in range(numbersofnumbers):
    randNumber = random.randint(0, 100)
    total += randNumber
    
    file = open("Random_number_game.csv", "a")
    file.write(str(randNumber) + "\n")
    file.close()

# Writing the total sum to the file
file = open("Random_number_game.csv", "a")
file.write(str(total) + "\n")
file.close()

# Informing the user that the operation is done
print("Done")
