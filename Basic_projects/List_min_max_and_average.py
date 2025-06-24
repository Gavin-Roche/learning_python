# Finding min and max values after sorting
myList = [1, 36, 3, 5, 8, 39, 48, 2, 1, 8788, 36, 21, 2, 1]
myList.sort()
print(myList)
minNum = myList[0]
maxNum = myList[-1]
print(minNum)
print(maxNum)

# Using built-in functions to find min and max values
myList = [1, 36, 69, 8, 5, 2, 31, 56, 89, 49, 4, 45, 94]
minValue = min(myList)
maxValue = max(myList)
print(minValue)
print(maxValue)

# Finding min and max manually
myList = [32, 6, 95, 9, 5, 21, 59, 849, 84]
minValue = myList[0]
maxValue = myList[0]
for item in myList:
    if item < minValue:
        minValue = item
    if item > maxValue:
        maxValue = item
print(minValue)
print(maxValue)

# Calculating the average manually
myList = [32, 6, 95, 9, 5, 21, 59, 849, 84]
sumValue = 0
for item in myList:
    sumValue += item
average = sumValue / len(myList)
print(average)

# Calculating the average using built-in function
myList = [32, 6, 95, 9, 5, 21, 59, 849, 84]
average = sum(myList) / len(myList)
print(average)