# Write the user's input name to a text file
name = input(str("Please input your name: "))
file = open("name.txt", "w")
file.write(name)
file.close()