# Character to ASCII and back
character = "☼"
asciiNum = ord(character)
print(asciiNum)
print(type(asciiNum))

print()

output = chr(asciiNum)
print(output)
print(type(output))

# Capitalize string
string1 = "hello"
string1 = string1.capitalize()
print(string1)

# String length
string1 = "hello"
string1 = len(string1)
print(string1)

# Accessing specific character
myString = "Frank Lampey"
print(myString[6])