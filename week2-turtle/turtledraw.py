import turtle
#turtle.setup(650,350,200,200)
turtle.penup() #without it will have line
turtle.forward(-250)
turtle.pd()
turtle.pensize(25)
turtle.pencolor("purple")   #
turtle.seth(-40)    #海龟面对方向 让海龟转向 seth(angle)
for i in range(4):
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(10,80/2)
turtle.forward(40)  #neck part
turtle.circle(18,180)
turtle.forward(40*2/3)

turtle.done
