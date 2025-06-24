# Plotting a simple line graph
import matplotlib.pyplot as plt
myList = [1536, 63, 46, 41, 4, -2, 56]
plt.plot(myList)
plt.show()

# Plotting a line graph with custom markers and labels
numBS = [1, 2, 6, 5, 6, 5, 6, 1, 5]
plt.plot(numBS, "rs")
plt.title("brothers and sisters")
plt.xlabel("List index")
plt.ylabel("num Brother and sisters")
plt.show()

# Plotting a bar graph
numBS = [1, 2, 6, 5, 6]
names = ["john", "tom", "kate", "tim", "sally"]
plt.bar(names, numBS)
plt.title("Brothers, Sisters")
plt.xlabel("students")
plt.ylabel("Num Brothers and Sisters")
plt.show()

# Plotting two datasets on the same plot
numBS = [1, 2, 6, 5, 6]
names = ["john", "tom", "kate", "tim", "sally"]
age = [98, 26, 51, 23, 12]
plt.plot(names, numBS)
plt.plot(age)
plt.show()

# Plotting a pie chart
numBS = [1, 2, 6, 5, 6]
names = ["john", "tom", "kate", "tim", "sally"]
plt.pie(numBS, labels=names)
plt.title("Brothers and Sisters")
plt.show()