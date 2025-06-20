# Selection Sort Algorithm Implementation
myList = [85, 24, 64, 4, 65, 94, 1, 6]
# Iterate through each the list (excluding the last one)
for index in range(len(myList) - 1):
    print(myList)
    nextMinValue = myList[index + 1]

    # Find the smallest value in the unsorted portion of the list
    for unsortedIndex in range(index + 1, len(myList)):
        if myList[unsortedIndex] < nextMinValue:
            nextMinValue = myList[unsortedIndex]
    
    # Swap the found minimum value with the current element if necessary
    if nextMinValue < myList[index]:
        nextMinIndex = myList.index(nextMinValue)
        myList[nextMinIndex] = myList[index]
        myList[index] = nextMinValue
        
print(myList)