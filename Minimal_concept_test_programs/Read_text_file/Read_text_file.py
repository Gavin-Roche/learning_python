# Read text file and print its content
file = open("Text_file.txt", "r")
dataIn = file.read()
file.close()
print(dataIn)