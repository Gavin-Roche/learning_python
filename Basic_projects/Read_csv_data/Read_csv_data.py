# This program reads a CSV file, splits the data by commas, converts it into integers, and prints the results.

# Opening the CSV file to read
file = open("CSV.csv", "r")
dataIn = file.read()

# Splitting the data by commas to get a list
myList = dataIn.split(",")

# Closing the file after reading
file.close()

# Printing the raw data and the list created from the data
print(dataIn)
print(myList)

# Converting the list items to integers
myList = [int(item) for item in myList]

# Printing the list after converting the items to integers
print(myList)
