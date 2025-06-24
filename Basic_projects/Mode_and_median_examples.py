# Median example
import statistics

myList = [1, 19, 27, 8, 5, 11]
medianValue = statistics.median(myList)
print(medianValue)

# Counting occurrences of each item
myList = ["r", "b", "g", "g", "r"]
colourNames = []
colourCounts = []
for item in myList:
    if item not in colourNames:
        colourNames.append(item)
for colour in colourNames:
    total = myList.count(colour)
    colourCounts.append(total)
print(colourNames)
print(colourCounts)

# Mode example
colourCounts = [4, 4, 4]
colourNames = ["red", "green", "blue"]

maxFreq = max(colourCounts)
if maxFreq != 1:
    for i in range(len(colourCounts)):
        if colourCounts[i] == maxFreq:
            print(colourNames[i], "is a mode")
else:
    print("No mode in list")