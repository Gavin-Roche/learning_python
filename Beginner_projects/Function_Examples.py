# This program includes multiple functions: exponentiation, comparison, string matching, and even/odd check.

# Function to calculate power
def power(baseNum, indexNum):
    return baseNum ** indexNum

# Explain and ask for inputs
print("This function calculates the result of a base number raised to the power of an exponent.")
num1 = int(input("Enter num 1 (base): "))
num2 = int(input("Enter num 2 (exponent): "))
print("The result of", num1, "raised to the power of", num2, "is", power(num1, num2))
print()

# Function to find the larger of two numbers
def larger(num1, num2):
    if num1 < num2:
        return num2
    elif num1 > num2:
        return num1
    else:
        return f"Both numbers are {num1}"

# Explain and ask for inputs
print("This function finds the larger of two numbers.")
num1 = int(input("Enter num 1: "))
num2 = int(input("Enter num 2: "))
print("The larger number between", num1, "and", num2, "is", larger(num1, num2))
print()

# Function to check if two strings are identical
def same(str1, str2):
    if str1 == str2:
        print("The strings are identical")
    else:
        print("The strings are not identical")

# Explain and ask for inputs
print("This function checks if two strings are identical.")
string1 = input("Enter string 1: ")
string2 = input("Enter string 2: ")
same(string1, string2)

print()

# Function to check if a number is even or odd
def evenOdd(num):
    return num % 2 == 0

# Explain and ask for inputs
print("This function checks if a number is even or odd.")
number = int(input("Enter num: "))
if evenOdd(number):
    print("The number", number, "is even.")
else:
    print("The number", number, "is odd.")
