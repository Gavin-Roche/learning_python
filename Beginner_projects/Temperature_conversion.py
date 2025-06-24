# Function to extract the scale from the input string
def scale(temp):
    return temp[-1:]  # Returns the last character, which is the scale (C or F)

# Function to convert the temperature string to float
def number(temp):
    if temp[:-1].replace('.', '', 1).isdigit():  # Check if the number part is a valid float
        return float(temp[:-1])
    return None  # Return None if it's not a valid number

# Function to convert temperature based on scale
def convert(temp, scale):
    if scale == "F" or scale == "f":
        cel = (temp - 32) * 5 / 9  # Convert Fahrenheit to Celsius
        return cel
    elif scale == "C" or scale == "c":
        far = (temp * 9 / 5) + 32  # Convert Celsius to Fahrenheit
        return far
    else:
        return None  # Return None for invalid scale

# Input for temperature and scale
userInput = input("Input value and temperature type (e.g., 32F or 100C): ")

sca = scale(userInput)  # Extract scale (F or C)
tem = number(userInput)  # Convert the number part to float

# Convert the temperature based on the scale
convertedTemp = convert(tem, sca)

# Determine the output scale
if sca == "F" or sca == "f":
    scaleAns = "C"
elif sca == "C" or sca == "c":
    scaleAns = "F"
else:
    scaleAns = None

# Print the conversion result or error message
if scaleAns:
    print(tem, sca, "is equal to", round(convertedTemp, 1), scaleAns)
else:
    print("Incorrect input")
