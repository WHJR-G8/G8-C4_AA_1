import turtle

side = int(input("Enter the value for side: "))
speed = int(input("Enter the speed for turtle to move: "))
color = input("Enter the pencolor")

for i in range(4):
    turtle.speed(speed)
    turtle.pencolor(color)
    turtle.forward(side)
    turtle.left(90)
