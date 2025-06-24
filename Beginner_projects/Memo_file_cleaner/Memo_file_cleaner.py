import csv
import string

# Define the alphabet and select the wanted letters (A to X)
alphabet = list(string.ascii_uppercase)
wanted_letters = alphabet[:24]  # I am interested in the first 24 letters of the alphabet (A to X)

# Function to sort the list based on input data and the number of items
def sort_list(number_of_items):
    # Initialize the main list with 7 columns (empty lists)
    main_list = [[], [], [], [], [], [], []]
    sorted_list = []  # This will hold the sorted data

    number_of_items += 1  # Adjust the count to include the number of items
    with open("Memo_file.csv") as x:
        csv_read = csv.reader(x)
        for row in csv_read:
            letter_pairs = row[0]  # First element in the row (the letter pair string)
            if "=" in letter_pairs:  # Only process rows that contain "="
                # Iterate over the 7 columns in each row
                for position in range(7):
                    column = row[position]  # Get the value from the current column
                    main_list[position].append(column)  # Append the value to the respective list

        # Sorting the data based on the main list
        for i in range(len(main_list[0])):  # Iterate over the rows (same length as first column)
            letter_list = []  # This will hold the list of letters for the current row
            for a in range(7):
                if main_list[a][i] != "":  # If the column is not empty
                    if a:
                        letter_list.append(main_list[a][i].capitalize())  # Capitalize for non-first columns
                    else:
                        letter_list.append(main_list[a][i])
                    if a == 6:  # If it's the last column, append the letter list to the sorted list
                        sorted_list.append(letter_list)
                else:
                    sorted_list.append(letter_list)  # Append the letter list when an empty entry is found
                    if number_of_items:  # If number_of_items is set, process the word count
                        number_words(a, number_of_items, letter_list)  # Call to process the word count
                    break

    return sorted_list  # Return the sorted list


# Function to print out a specific word based on conditions
def number_words(a, number_of_items, letter_list):
    if len(letter_list) <= number_of_items:
        if a == number_of_items:
            print(letter_list[0])  # Print the first word if conditions match


# Function to write the sorted list to a CSV file
def write_to_file(sorted_list, wanted_letters):
    with open('Cleaned_memo_file.csv', 'w', newline='') as x:
        write = csv.writer(x)
        write.writerow([wanted_letters[0]])  # Write the first wanted letter as a header
        for i in range(len(sorted_list)):
            # Check if the first letter of the entry matches the wanted letter
            if sorted_list[i][0][1:2] == wanted_letters[0]:
                write.writerow([])  # Write a blank line before each new section
                write.writerow(sorted_list[i][0][:1])  # Write only the first part of the entry
            write.writerow(sorted_list[i])  # Write the full entry


# Function to generate and write letter pairs (combinations of letters)
def write_out_letters(wanted_letters):
    letters_list = []  # This will hold all generated letter pairs
    for i in range(len(wanted_letters)):
        first_letter = wanted_letters[i]
        if i:
            letters_list.append("")  # Add an empty string as separator between sections
        letters_list.append(first_letter)  # Append the first letter
        for j in range(len(wanted_letters)):
            second_letter = wanted_letters[j]
            if first_letter != second_letter:  # Avoid repeating letter pairs like "AA"
                letters_together = first_letter + second_letter + " ="  # Combine letters with "="
                letters_list.append(letters_together)  # Add the combined pair to the list

    # Write the generated letter pairs to a CSV file
    with open('Letter_pairs.csv', 'w', newline='') as x:
        write = csv.writer(x)
        for pair in letters_list:
            write.writerow([pair])  # Write each pair in a new row


# Run the sorting function (input 0 to match any word count or a specific number)
sorted_list = sort_list(0)  # Adjust the value to get pairs with that number of words or less
write_to_file(sorted_list, wanted_letters)  # Write sorted data to a file called 'Cleaned_memo_file.csv'
write_out_letters(wanted_letters)  # Write letter pairs to a separate file called 'Letter_pairs.csv'
