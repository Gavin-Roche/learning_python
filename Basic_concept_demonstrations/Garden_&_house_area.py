# Getting inputs from the user
gardenLength = float(input("What is the garden length in meters: "))
gardenWidth  = float(input("What is the garden width in meters: "))
houseLength  = float(input("What is the house length in meters: "))
houseWidth   = float(input("What is the house width in meters: "))

# Calculating areas
gardenCalculated = gardenLength * gardenWidth
houseCalculated  = houseLength * houseWidth
fullyCalculated  = gardenCalculated - houseCalculated

print()
print("The area of the garden is", gardenCalculated, "sq meters")
print("The area of the house is", houseCalculated, "sq meters")
print("The area of the garden minus the house is", fullyCalculated, "sq meters")

# Time calculations
timeSeconds = fullyCalculated / 2  # Example calculation for time in seconds
timeMinutes = timeSeconds / 60  # Converting seconds to minutes

if timeMinutes >= 1:
    print("It will take", round(timeMinutes, 2), "minutes")
else:
    print("It will take", round(timeSeconds, 2), "seconds")