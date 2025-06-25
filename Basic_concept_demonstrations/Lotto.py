import random

ticket = []

# Ask the user to pick 3 numbers between 1 and 10
for counts in range(3):
    user_number = int(input("Please pick a number between 1 and 10: "))
    ticket.append(user_number)

print("Your ticket is: ", ticket)
print("The draw will start now, good luck!")

drum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = []

# Define the lotto function to simulate the lottery draw
def lotto(ticket):
    for times in range(3):
        draw = drum[random.randint(0, len(drum) - 1)]
        result.append(draw)
    print("The draw was: ", result)


lotto(ticket)

result.sort()
ticket.sort()

# Check if the user's ticket matches the draw results
if result == ticket:
    print("You win!")
else:
    print("You lose!")