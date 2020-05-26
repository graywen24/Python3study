'''
lambda 函数是一种匿名函数，没有名字的函数
返回值是函数名
lambda函数能在一行表示函数
'''
f = lambda x,y: x*y
print(f(10,10))  #100
print(f(2,10))  #2*10=20

f = lambda : print("here is the lambda result")
f()
