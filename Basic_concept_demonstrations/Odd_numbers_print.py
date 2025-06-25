# This program prints odd numbers from 1 to the entered value
value = int(input("Please input a value: "))

for i in range(1, value+1, 2):
    print(i)