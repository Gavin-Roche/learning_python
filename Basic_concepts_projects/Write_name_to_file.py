# Write user's name to a file
name = input(str("Please enter your name: "))
file = open("name.txt", "w")
file.write(name)
file.close()
