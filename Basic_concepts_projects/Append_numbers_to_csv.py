# Append 10 user-input numbers to a CSV file
file = open("Numbers.csv", "a")

for i in range(10):
    number = input("Please input a number: ")
    file.write(number + ",")
file.close()