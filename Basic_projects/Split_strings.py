#splitting of strings exercise
name  = input("Input both name: ")
if name.count(" ") == 0:
    print("Please enter names with space.")
else:
    index = name.index(" ")
    firstName = name[:index]
    lastName  = name[index+1:]
    print("Forename:",firstName)
    print("Surname:",lastName)
