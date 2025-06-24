# Find the median of a sorted list
myList = [1, 19, 27, 8, 5, 9, 11]
myList.sort()

if len(myList) % 2 == 0:
    middlePlusOne = len(myList) // 2
    median = (myList[middlePlusOne - 1] + myList[middlePlusOne]) // 2
else:
    middle = len(myList) // 2
    median = myList[middle]

print(median)