import turtle
turtle.shape("turtle") # Set the shape of the turtle to "turtle" (optional, default shape is "classic")
scr = turtle.Screen()
scr.bgcolor("pink") #set the background color of the screen
turtle.penup()#remove the trail by the turtle
turtle.pendown()
turtle.pensize(2)#default is 1
# turtle.color("black","red")#black outline and red fill



# Loop to draw a pentagon
# for i in range(0,5):
#     turtle.forward(100) #Send the turtle forward 100 steps
#     turtle.right(72) # Turn the turtle right by 72 degrees
# # turtle.exitonclick() # Exit the turtle graphics window when clicked

# for n in range(0,5):
#     turtle.forward(50)
#     turtle.right(0)

# draw a circle
# num_sides = 360 #assume a circle as 360 lines
# turtle.fillcolor("yellow")
# turtle.begin_fill()
# for _ in range(num_sides):
#     turtle.forward(1)
#     turtle.right(1)
# turtle.end_fill()

# for p in range(0,6):
#     turtle.forward(100)
#     turtle.right(144)


turtle.color("green", "white")
turtle.begin_fill()
for i in range(0, 4):
    turtle.forward(50)
    turtle.right(90)
turtle.penup()
turtle.end_fill()
turtle.forward(100)

turtle.pendown()
turtle.color("blue", "grey")
for i in range(0, 4):
    turtle.forward(50)
    turtle.right(90)
turtle.penup()
turtle.end_fill()
turtle.forward(100)

turtle.pendown()
turtle.color("yellow", "purple")
for i in range(0, 4):
    turtle.forward(50)
    turtle.right(90)
turtle.penup()
turtle.end_fill()

turtle.exitonclick()