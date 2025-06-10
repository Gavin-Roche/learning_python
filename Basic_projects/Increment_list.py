# This program increments each number in the list by 1

myList = []

for i in range(5):
    number = int(input("Please enter a number: "))
    myList.append(number)
print(myList)

for i in range(5):
    myList[i] += 1
print(myList)
