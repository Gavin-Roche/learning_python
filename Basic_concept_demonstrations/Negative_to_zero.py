# Turns the negative numbers in the list to zero
myList = [1, -19, 27, 8, -5, 9]
print(myList)

for item in range(len(myList)):
    if myList[item] < 0:
        myList[item] = 0
print(myList)