# Program 1: Check if a name is in the list
testList = ["tim", "eve", "adam", "gavin"]
name = str(input("Please input name: "))
name = name.lower()
name2 = name.capitalize()

if name in testList:
    print(name2, "is in the list")
else:
    print(name2, "is not in the list")


# Program 2: Append and insert items into the list
myList = [1, 19, 27, 8, 5, 9, 1]
print(myList)
myList.append(11)
print(myList)
myList.insert(1, 13)
print(myList)

# Program 3: Find the frequency of a number in the list
myList = [1, 19, 27, 65, 69, 35, 27, 27, 3, 27]
numSought = 27

freqNum = 0
counter = 0

while counter < len(myList):
    if myList[counter] == numSought:
        freqNum += 1
        print("Found at index:", counter)
    counter += 1
print(numSought, "is in the list", freqNum, "times")