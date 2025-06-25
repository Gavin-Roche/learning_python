# Read data from a CSV file, modify values, and write to another CSV file
file = open("Random_numbers.csv", "r")
dataIn = file.read()
file.close()
print(dataIn)

myList = dataIn.split(",")
print(myList)
print()
print(len(myList))
del myList[-1]  # Remove the last empty item
myList = [int(item) for item in myList]  # Convert strings to integers
print(myList)

file = open("List_output.csv", "w")
for i in range(len(myList)):
    if myList[i] > 30:  # Modify numbers greater than 30 to 30
        myList[i] = 30
    file.write(str(myList[i]) + ",")
file.close()

print()
print(myList)