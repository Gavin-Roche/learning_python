# This is the bubble sort algorithm
myList = [8, 3, 7, 9, 15, 24, 1]
swapped = True
passes = 1

# Print the original unsorted list
print("Original List:", myList)
print()

# Bubble Sort Algorithm
while swapped:  # Continue looping as long as a swap occurred in the previous pass
    print("Pass", passes)  # Print the current pass number
    swapped = False
    # Iterate through the list comparing elements next to each other
    for i in range(len(myList) - 1):
        if myList[i] > myList[i + 1]:
            temp = myList[i + 1] # Swap the two elements
            myList[i + 1] = myList[i]
            myList[i] = temp
            swapped = True  # Mark that a swap occurred
        print(myList)
    passes += 1  # Increment the passes counter

# Print the sorted list after sorting is complete
print("\nSorted List:", myList)
