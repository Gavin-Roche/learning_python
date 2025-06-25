"""
This script processes raw CAP (Common Agricultural Policy) payment data from an uncleaned CSV file, 
extracting names, addresses, and payment amounts. The cleaned data is then written to a new CSV file 
with structured formatting.

Steps:
1. Reads raw data from "Uncleaned_2009_cap_data.csv".
2. Extracts name, address, and payment amount using string operations.
3. Writes the cleaned data to "2009_farmers_cap_payments.csv".
"""
import csv

# Function to split a string based on given indices
def splitter(data, split_place_back, split_place_front):
    if split_place_back == 'none':
        split_place_back = len(data)  # If 'none', take the rest of the string
    return data[split_place_front:split_place_back]


# Function to write parsed data into a CSV file
def writer(names, addresses, money_list):
    with open('2009_farmers_cap_payments.csv', 'a', newline='') as x:
        write = csv.writer(x)
        for i in range(len(names)):
            row = [names[i], addresses[i], money_list[i]]  # Store data in a list
            write.writerow(row)  # Write the row into CSV


# Creating the output CSV file with headers
with open('2009_farmers_cap_payments.csv', 'w', newline='') as x:
    write = csv.writer(x)
    write.writerow(["Name", "Address", "Payment"])  # Writing column headers

# Lists to store parsed data
names = []
addresses = []
money_list = []

# Reading and processing the uncleaned CSV file
with open("Uncleaned_2009_cap_data.csv") as x:
    csv_read = csv.reader(x)
    for row in csv_read:
        data = row[0]  # Extracting the first column from each row
        
        # Finding first comma to separate name
        first_comma = data.find(",")
        name = splitter(data, first_comma, 0)  # Extract name
        names.append(name)

        # Extract everything after the name
        other_than_name = splitter(data, "none", first_comma + 2)
        
        # Find positions of delimiters in the remaining string
        placement = [
            other_than_name.find(","),
            other_than_name.find(" "),
            other_than_name.find("-"),
            other_than_name.find("€")
        ]
        while -1 in placement:  # Remove invalid indices
            placement.remove(-1)
        
        second_split = min(placement)  # Get the nearest delimiter position
        address = splitter(other_than_name, second_split, 0)  # Extract address
        addresses.append(address)

        third_split = placement[-1]  # Last found delimiter (usually before the money value)

        # Extracting payment amount
        money = splitter(other_than_name, "none", third_split)
        
        # Clean and convert the payment amount
        money_maths = splitter(money, "none", 1)  # Remove first character (currency symbol)
        money_maths = money_maths.replace(", ", "")  # Remove commas if present
        money_maths = float(money_maths)  # Convert string to float
        
        money_list.append(money)  # Append extracted money value

    # Writing processed data to the output CSV
    writer(names, addresses, money_list)