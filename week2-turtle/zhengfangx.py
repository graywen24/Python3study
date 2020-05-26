'''描述
使用turtle库，绘制一个正方形。‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬
'''
'''
bad idea
import turtle
#turtle.setup(650,350,200,200)
turtle.penup()
turtle.forward(-250)
turtle.pd()
turtle.pensize(15)
turtle.pencolor("pink")
turtle.fd(250)
turtle.seth(90)
turtle.fd(250)
turtle.seth(-180)
turtle.fd(250)
turtle.seth(-90)
turtle.fd(250)
'''
import turtle
turtle.pensize(15)
turtle.pencolor("red")
for i in range(4):
    turtle.fd(100)
    turtle.left(90)

turtle.done()

