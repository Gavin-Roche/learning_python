import turtle

#Create a turtle object called pen
pen = turtle.Turtle()

#Create a window for the turtle
window = turtle.Screen()

pen.forward(100) #move forward 100 units
pen.left(90)     #turn left by 90 degrees
pen.forward(100)
pen.right(45)
pen.forward(100)
pen.left(90)
pen.forward(99.292799999999999)

#keep looping until window is closed
window.mainloop()