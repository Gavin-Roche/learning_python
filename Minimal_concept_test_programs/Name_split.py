# Splits the input full name into first and last name
name = str(input("Input your first and second name: "))
spaceLoc = name.index(" ") 

fname = name[:spaceLoc]
lname = name[spaceLoc+1:]

print(fname)
print(lname)