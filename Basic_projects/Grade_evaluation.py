# Evaluate the grade and assign pass, merit, distinction, or fail
grade = float(input("Please input your grade: "))
print()

if (grade >= 50) and (grade < 65):
    print("This is a pass")

elif (grade >= 65) and (grade < 80):
    print("This is a merit")
    
elif (grade >= 80) and (grade <= 100):
    print("This is a distinction")
    
elif (grade >= 0) and (grade < 50):
    print("This is a fail")
    
else:
    print("Invalid entry")