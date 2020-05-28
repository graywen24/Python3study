import turtle
def drawLine(draw):  #draw is True or False
    turtle.pendown() if draw else  turtle.penup()
    turtle.pencolor("red")
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.forward(100)
   
    turtle.done()


drawLine(True)
