# Check if the entered password matches the stored password in the file
ans = 1
while ans == 1:
    userInput = input("Please input password: ")

    file = open("Password.txt", "r")
    password = file.read()
    file.close()

    if userInput == password:
        ans = 0
        print("Correct password")
    else:
        print("Incorrect password")
        print()
