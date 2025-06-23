# This program counts the number of vowels in a given sentence

sentence = input("Please enter a sentence: ")
vowels = 0

for char in sentence:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u" or char == "A" or char == "E" or char == "I" or char == "O" or char == "U":
        vowels += 1
        
print(vowels)
