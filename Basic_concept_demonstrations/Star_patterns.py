# This program prints different star patterns based on user input.

# Rectangle pattern
rows = int(input("Input rows number: "))
cols = int(input("Input columns number: "))

for rowIndex in range(rows):
    for colIndex in range(cols):
        print("*", end="")
    print()

print()  # Blank line for separation

# Right-angled triangle pattern
row = 10
for i in range(row):
    for j in range(i + 1):
        print("*", end="")
    print()

print()  # Blank line for separation

# Pyramid pattern
rows = int(input("Input rows number: "))
for i in range(rows):
    for j in range(rows + 1):
        if j <= rows - (i + 1):
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print()

# Rectangle base for pyramid
for k in range(14):
    for i in range(rows + 1):
        print("*", end=" ")
    print()