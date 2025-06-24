# This program calculates the user's weight on either Mars or the Moon
userWeight = float(input("input weight in kgs:"))

planet = input("input moon or mars:")

mars = 0.38
moon = 0.165

if planet == "mars":
    newWeight = userWeight * mars
elif planet == "moon":
    newWeight = userWeight * moon
else:
    newWeight = "Invalid planet"

print("This would weigh", newWeight, "Kgs on the", planet)