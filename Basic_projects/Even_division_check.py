# Check if one number divides evenly into another
num1 = int(input("Input number 1: "))
num2 = int(input("Input number 2: "))

if num1 % num2 == 0:
    print(num1, "divides evenly into", num2)
else:
    print(num1, "doesn't divide evenly into", num2)