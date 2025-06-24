# This program calculates the total cost of milk based on hours spent in the house
hours = []
liters = []
cost = float(input("Please enter the price of the milk: "))

for i in range(7):
    number = int(input("Please enter a number of hours Stephen was in the house: "))
    hours.append(number)
print(hours)

for i in range(7):
    entry = hours[i] / 2
    liters.append(entry)
print(liters)

totalLiters = sum(liters)
print(totalLiters)

totalCost = totalLiters * cost
print(round(totalCost, 2))