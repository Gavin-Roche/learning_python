# Function to count occurrences of a number in the list
def countNum(theList, number):
    timesOccur = 0
    for i in range(len(theList)):
        if theList[i] == number:
            timesOccur += 1
    return timesOccur

# List to search within
theList = [1, 3, 59, 84, 11, 11, 51, 19, 19, 22, 56, 22, 66, 43, 22, 9, 2, 100]
number = int(input("Enter number: "))

# Get the count of occurrences and print the result
answer = countNum(theList, number)

if answer == 1:
    print(number, "is in the list", answer, "time")
else:
    print(number, "is in the list", answer, "times")