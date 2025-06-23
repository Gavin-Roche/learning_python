# Convert time in HH:MM:SS format to total seconds

time = input("Please enter time in 03:60:51 format: ")

hours = int(time[:2])
mins  = int(time[3:5])
secs  = int(time[6:])

timeInSecs = (hours * 60 ** 2) + (mins * 60) + secs

print()
print(hours, "hours", mins, "minutes", secs, "seconds =", timeInSecs, "seconds")
