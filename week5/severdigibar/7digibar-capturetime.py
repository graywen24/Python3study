import turtle
import time
def drawLine(draw):  #draw is True or False
    turtle.pendown() if draw else  turtle.penup()
    #turtle.pencolor("red")
    turtle.forward(40)
    turtle.right(90)  #每次右转90度

def drawDigi(digi):
    #下面的4条线
    drawLine(True) if digi in [2,3,4,5,6,8,9] else drawLine(False)  #线条1：中间的第一个横线
    drawLine(True) if digi in [0,1,3,4,5,6,7,8,9] else drawLine(False) #线条2：2 不需要用到
    drawLine(True) if digi in [0,2,3,5,6,8,9] else drawLine(False)  #第三条线1，4 7，不会用到
    drawLine(True) if digi in [0,2,6,8] else drawLine(False) #第四条线1，3，4，5，7，9不会用到
    #
    turtle.left(90)   #此时回到起点了乌龟头是> 所以开始绘制5 需要左边转90度
    drawLine(True) if digi in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digi in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digi in [0,1,2,3,4,7,8,9] else drawLine(False)
    #调用完函数drawline 乌龟头会right90 就是朝向起点位置<- 所以需要他转 180度 回到右变
    #turtle.right(180)   #这里左右180度都可以 只是要乌龟头朝另外一边罢了
    turtle.penup() #画笔拿起来 飞一端 空隙
    turtle.fd(20)   #每个数字间飞一段距离


def drawDate(date):  #输入时间格式是 %Y-%m=%d+
    turtle.pencolor("red")
    for i in date:
        if i == "-":  #-在输入格式中 表示年
            turtle.write("年",font=("Arial",18,"normal"))
            turtle.pencolor("green")
            turtle.fd(40)
        elif i == "=":
            turtle.write("Month",font=("Arial",18,"normal"))
            turtle.pencolor("blue")
            turtle.fd(40)
        elif i == "+":
            turtle.write("日", font=("Arial", 18, "normal"))
            turtle.pencolor("yellow")
        else:
            drawDigi(eval(i))


def main():
    turtle.setup(800,350,200,200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    drawDate(time.strftime("%Y-%m=%d+",time.gmtime()))
    turtle.done()

main()   #调用 函数
