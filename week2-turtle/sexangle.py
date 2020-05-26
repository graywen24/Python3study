'''使用turtle库，绘制一个六边形
'''
'''import turtle
#turtle.setup(650,350,200,200)
turtle.penup()
turtle.forward(-100) #backfward 250
turtle.seth(-90)
turtle.forward(250)
turtle.pd()
turtle.pensize(10)
turtle.pencolor("red")
turtle.left(90)
turtle.forward(200)
turtle.seth(60)
turtle.forward(200)
turtle.seth(120)
turtle.forward(200)
turtle.seth(180)   #= left(60)
turtle.forward(200)
turtle.left(60)
turtle.forward(200)
turtle.left(60)
turtle.forward(200)
turtle.done()
'''
import turtle
turtle.pensize(15)
turtle.pencolor("red")
for i in range(6):
    turtle.fd(100)
    turtle.left(60)

turtle.done()