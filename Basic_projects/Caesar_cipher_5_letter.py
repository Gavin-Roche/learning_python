# Simple Caesar cipher that encrypts a 5-letter word using a shift key

alphabet = "abcdefghijklmnopqrstuvwxyz"

print("This program can only handle 5-letter words\n")

letter1 = input("Please enter letter 1: ")
letter2 = input("Please enter letter 2: ")
letter3 = input("Please enter letter 3: ")
letter4 = input("Please enter letter 4: ")
letter5 = input("Please enter letter 5: ")

key = int(input("Please enter an encryption key: "))

# Encrypt each letter using Caesar cipher
letter_encrypt1 = (alphabet.index(letter1) + key) % 26
encrypted_letter1 = alphabet[letter_encrypt1]

letter_encrypt2 = (alphabet.index(letter2) + key) % 26
encrypted_letter2 = alphabet[letter_encrypt2]

letter_encrypt3 = (alphabet.index(letter3) + key) % 26
encrypted_letter3 = alphabet[letter_encrypt3]

letter_encrypt4 = (alphabet.index(letter4) + key) % 26
encrypted_letter4 = alphabet[letter_encrypt4]

letter_encrypt5 = (alphabet.index(letter5) + key) % 26
encrypted_letter5 = alphabet[letter_encrypt5]

print()
print("Your encrypted word is: " + encrypted_letter1 + encrypted_letter2 + encrypted_letter3 + encrypted_letter4 + encrypted_letter5)