def answer():
    ans = input("Does it move?")
    if ans == "yes":
        ans = input("Should it?")
        if ans == "no":
            print("Apply Tape")
        elif ans == "yes":
            print("No problem, do nothing")
    elif ans == "no":
        ans = input("Should it?")
        if ans == "no":
            print("No problem, do nothing")
        elif ans == "yes":
            print("Apply lubricant")  
   
answer()