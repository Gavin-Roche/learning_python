# This program collects and displays the names of the user's pets
petList = []
totalPets = int(input("How many pets do you have: "))

if totalPets > 0:
    for pet in range(totalPets):
        name = input("Enter pet's name: ")
        petList.append(name)
    print("The names of your pets are: ")
    for pet in range(totalPets):
        print(petList[pet])
else:
    print("Buy one so!!!")