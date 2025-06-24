# Converts distance from miles to kilometers and calculates flight cost
distanceMiles = 7061
distanceKm = 7061 * 1.60935
pricePreKm = 700

print("Distance from Fermi to Singapore in miles is", distanceMiles, "is equal to", round(distanceKm, 2))
print("The cost to fly to Singapore at €", pricePreKm, "per Km is €", round(distanceKm * pricePreKm, 2))