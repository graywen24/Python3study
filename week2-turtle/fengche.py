'''使用turtle库，绘制一个风轮效果，其中，每个风轮内角为45度，风轮边长150像素。
'''
import turtle as t
for i in range (4):
    t.fd(150)
    #t.seth(-90)
    t.right(90)
    t.circle(-150,45)
    t.goto(0,0)
    t.left(45)
