UserInput = int(input("number: "))  # Get user input
splitList = list(map(int, str(UserInput)))  # Convert number to list of digits
seen = set()  # Store seen numbers to detect cycles

while True:  
    squared = sum(i**2 for i in splitList)  # Sum of squares of digits
    
    if squared == 1:  # If it reaches 1, it's a Happy Number
        print(UserInput, "is a Happy Number!")
        break
    
    if squared in seen:  # If we see the same number again, it's an Unhappy Number (Cycle detected)
        print(UserInput, "is an Unhappy Number.")
        break
    
    seen.add(squared)  # Add current number to the set
    splitList = list(map(int, str(squared)))  # Convert squared sum back to digit list