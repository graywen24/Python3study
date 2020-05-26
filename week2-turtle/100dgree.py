'''使用turtle库，绘制一个叠边形，其中，叠边形内角为100度。
https://zhuanlan.zhihu.com/p/83979476
'''
'''import turtle as t
#t.setup(650,350,200,200)
t.pencolor("red")
t.fd(150)
t.seth(80)
t.fd(150)
t.seth(160)
t.fd(150)
t.seth(240)
t.fd(150)
t.seth(320)
t.fd(150)
t.seth(400)
t.fd(150)
t.seth(480)
t.fd(150)
t.seth(560)
t.fd(150)
t.seth(640)
t.fd(150)
t.done()
'''
import turtle
turtle.pensize(5)
turtle.pencolor("red")
for i in range(9):
    turtle.fd(100)
    turtle.left(80)

turtle.done()