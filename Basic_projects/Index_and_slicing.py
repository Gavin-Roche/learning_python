# First block: slicing string
myString = "Frank Lampey"
print(myString[-9:-3])  # This outputs "n Lam"

# Second block: last character
print(myString[len(myString)-1])  # This outputs "y"

# Third block: checking substring and finding index
myName = "Jack Jones"
spaceLoc = myName.find("n")  # Using find() to avoid error if "n" is not found
print("Contains 'Jon':", "Jon" in myName)  # More readable way to check if 'Jon' exists
print(spaceLoc)  # This will print 5, the index of 'n'