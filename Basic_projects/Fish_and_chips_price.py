# Calculate total cost of fish and chips including VAT

fish  = float(input("Number of fish: "))
chips = float(input("Number of chips: "))

total = (fish * 4.5) + (chips * 2.8)

print("Fish and chips price €:", total)
print("The VAT should be: €", round(total * 0.09, 2))
