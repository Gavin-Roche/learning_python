sentence = input("Enter a sentence: ")
spaceCount = 0

for character in sentence:
    if character == " ":
        spaceCount  += 1
        
wordCount = spaceCount + 1
print("Words: ", wordCount)