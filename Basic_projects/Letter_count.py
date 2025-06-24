# This program counts the number of occurrences of a specified letter in a sentence
sentence = input("Please enter sentence: ")
findLetter = input("Please input the letter you want to find: ")
numLetters = 0

for char in sentence:
    if char == findLetter:
        numLetters += 1

if numLetters == 0:
    print("There is no", findLetter, "in your sentence")
else:
    print("The number of", findLetter, "in your sentence is", numLetters)