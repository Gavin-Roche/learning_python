# Sort a list in ascending and descending order
myList = [1, 19, 8, 5, 9]
myList.sort()
print("Sorted ascending", myList)
myList.sort(reverse=True)
print("Sorted descending", myList)

# Remove negative numbers from a list
numBS = [1, -19, 8, -5, 9]
for item in numBS:
    if item < 0:
        numBS.remove(item)
print(numBS)