# This program reverses the input sentence

sentence = input("Please input sentence: ")
length = len(sentence)

for char in range(length):
    print(sentence[(length - 1) - char], end="")
