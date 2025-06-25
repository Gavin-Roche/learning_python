# This program calculates the volume of a cylinder and determines how many cylinders can be filled with a given amount of liquid
radius = float(input("Enter radius of the cylinder: "))
height = float(input("Enter height of the cylinder: "))

volume = 3.14 * (radius ** 2) * height  # Volume formula for a cylinder

print("The volume of the cylinder is", volume)

liquid = float(input(f"Enter the volume of liquid (greater than {volume}): "))

print("The number of cylinders that would be fully filled by the liquid is:", liquid // volume, "cylinder(s)")