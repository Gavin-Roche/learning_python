# This program sorts a list of numbers in descending order and writes the sorted list to a CSV file.
# It also prints the maximum and minimum values from the list.

myList = [64, 63, 21, 1, 0, 3, 56, 3, 0, 2, 3, 7]

# Sorting the list in descending order
myList.sort(reverse=True)
print(myList)

# Writing the sorted list to a CSV file
file = open("Sorted_list.csv", "w")
for i in range(len(myList)):
    num = myList[i]
    file.write(str(num) + ",")
file.close()

# Printing the maximum and minimum values of the list
print("Max: ", myList[0], "Min: ", myList[-1])
