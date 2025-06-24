# This program collects sales data for multiple salespeople.
# It asks the user to input the number of salespeople, their names, and their sales amounts.
# The data is written to a CSV file with both names and sales.
# It then calculates and displays the total sales for the day.

namesList = []
salesList = []
salesTotal = 0

# Get number of salespeople
numSalesPeople = int(input("Please enter the number of salespeople: "))

# Open CSV file for writing (append mode)
with open("Sellers.csv", "a") as file:
    for _ in range(numSalesPeople):
        name = input("Please input the seller's name: ")
        namesList.append(name)

        sales = float(input("Please input " + name + "'s sales: "))
        salesList.append(sales)

        file.write(name + "," + str(sales) + "\n")  # Write name and sales to the same line

# Display results
print("\nName\tSales")
for i in range(numSalesPeople):
    print(f"{namesList[i]}\t{salesList[i]}")
    salesTotal += salesList[i]

print("\nThe total sales for the day is: €" + str(round(salesTotal, 2)))
