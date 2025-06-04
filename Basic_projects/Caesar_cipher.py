# Simple Caesar cipher that encrypts a 5-letter word using a shift key

alphabet = "abcdefghijklmnopqrstuvwxyz "

print("This program only handles strings with a-z and spaces")

string = input("Please the string to encrypt: ")
key = int(input("Please enter an encryption key: "))

encrypted_string = ""

# Encrypt each letter using Caesar cipher
for letter in string:
    letter = letter.lower()
    if letter in alphabet:
        index = alphabet.index(letter)
        new_index = (index + key) % len(alphabet)
        encrypted_letter = alphabet[new_index]
    else:
        encrypted_letter = letter  # Keep non-alphabet characters unchanged
    encrypted_string += encrypted_letter
    
print()
print("The encrypted string is", '"' + encrypted_string + '"')