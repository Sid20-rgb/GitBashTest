import turtle

screen = turtle.Screen()

pen = turtle.Turtle()
side = 6
length = 70

angle = 360//side

for i in range(side):
    pen.forward(length)
    pen.right(angle)

turtle.done()