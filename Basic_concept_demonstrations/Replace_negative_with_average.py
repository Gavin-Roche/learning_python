# Calculate the average of non-negative numbers and replace negative numbers with it
totalValidNumsAdded = 0
countOfValidNums = 0
numBS = [1, -19, -4, 3, -9, 6]

for item in numBS:
    if item >= 0:
        totalValidNumsAdded += item
        countOfValidNums += 1

averageOfValidNums = totalValidNumsAdded / countOfValidNums
print(averageOfValidNums)

for counter in range(len(numBS)):
    if numBS[counter] < 0:
        numBS[counter] = averageOfValidNums

print(numBS)