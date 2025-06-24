# This program collects sales data for multiple salespeople.
# It asks the user to input the number of salespeople, their names, and their sales amounts.
# The data is then written to two CSV files: one for names and another for sales.
# Finally, it calculates and displays the total sales for the day.

namesList = []
salesList = []
salesTotal = 0

numSalesPeople = int(input("Please enter the number of salespeople: "))

fileNames = open("sellersNames.csv", "a")
fileSales = open("sellersSales.csv", "a")

for items in range(numSalesPeople):
    name = input("Please input the seller's name: ")
    namesList.append(name)
    fileNames.write(name + ",")
    sales = float(input("Please input the seller's sales: "))
    salesList.append(sales)
    fileSales.write(str(sales) + ",")
fileNames.close()
fileSales.close()

print("Name\tSales")
for i in range(numSalesPeople):
    print(namesList[i], "\t", end="")
    print(salesList[i], "\t", end="")
    salesTotal = salesTotal + float(salesList[i])
    print()

print()
print("The total sales for the day is: ", salesTotal)
