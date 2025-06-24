# This program takes a birth month as input, determines its numerical value,  
# and calculates how many months away it is from the current month.
from datetime import datetime

# Get the current date and time
current_datetime = datetime.now()

# Get the current month (as an integer)
current_month = current_datetime.month

month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

bdMonth = input("Please input month of birth: ")
bdMonth.capitalize()
bdMonthNum = None  

# Find the numerical value of the birth month
for i in range(len(month)):
    if bdMonth == month[i]:
        bdMonthNum = i + 1  
        break  

if bdMonthNum is None:
    print("Invalid month input")  # Handle incorrect input
else: 
    monthAway = bdMonthNum - current_month 

    # Determine how many months away the birthday is
    if monthAway > 0:
        print(bdMonth,"is in", monthAway, "months")  
    elif monthAway == 0:
        print("It is", bdMonth, "now")  
    else:
        print(bdMonth,"is in", monthAway + 12, "months")  # Adjust for next year