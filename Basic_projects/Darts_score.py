"""
Darts 501 Scoring Game

- Players start with a score of 501.
- Each turn consists of 3 throws, and the total score for the turn is subtracted from 501.
- The goal is to reach exactly 0.
- If a player’s score goes below 0, the turn is "not counted" (the score is restored).
- The game continues until the player wins by reaching exactly 0.
"""

score = 501
while score != 0:
    UserInput = int(input("Total for 3 throws: "))
    score = score - UserInput  
    if score > 1:
        print(score)
    elif score == 0:
        print("You won!")
    else:
        score = score + UserInput
        print("Not counted")