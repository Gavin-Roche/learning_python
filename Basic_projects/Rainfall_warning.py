# This program checks weekly rainfall and warns if it exceeds a specified threshold
rain = []
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
maxRain = float(input("How much rain is needed before you are warned: "))

for i in range(7):
    dailyEntry = float(input("Please enter rainfall amount in ml: "))
    rain.append(dailyEntry)

#print(rain)
print()
totalRain = sum(rain)
print("The total rainfall for the week is:", totalRain)

averageRain = totalRain / 7
print("The average rainfall for the week is:", averageRain)

for i in range(len(rain)):
    if rain[i] >= maxRain:
        print("The rainfall was greater than", maxRain, "on", days[i])