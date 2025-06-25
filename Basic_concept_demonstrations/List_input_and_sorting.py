# Take user input, sort the list in ascending and descending order
myList = []
numOfNums = int(input("Number of numbers: "))

for items in range(numOfNums):
    myList.append(int(input("Please enter numbers: ")))  # Appending numbers to the list

myList.sort()
print("Sorted ascending", myList)
myList.sort(reverse=True)
print("Sorted descending", myList)