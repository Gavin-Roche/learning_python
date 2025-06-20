#this program sums from 1 to entered number

number = int(input("please enter a whole number: "))
count  = 1
total  = 0

#this loop allows us to calculate correct total

while count <= number:
    total = total + count
    count = count + 1
    
print(total)