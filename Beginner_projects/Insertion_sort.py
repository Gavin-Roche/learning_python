# Insertion Sort Algorithm Implementation
myList = [81, 486, 89, 899, 87, 546, 56, 567, 78, 78]

# Iterate through the list starting from the second element (index 1)
for index in range(1, len(myList)):
    itemInsert = myList[index]
    position = index

    # Shift elements to the right to make space for the current value
    while position > 0 and myList[position - 1] > itemInsert:
        myList[position] = myList[position - 1]
        position -= 1

    # Insert the current value in its correct sorted position
    myList[position] = itemInsert  

print(myList)