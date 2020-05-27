#leonardo fibonacci
def fibonacci(n):
    if n ==1 or n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

val = eval(input("input int number： "))
if val <=0:
    print("input number >0")
else:
    res = fibonacci(val)
    print("fibonacci result is %d" %res)
print("here end of using recursion".center(50,"*"))
# 迭代方式
def fab(n):
    n1 = 1
    n2 = 1
    n3 = 1
    if n < 1:
        print("输入有误")
        return -1
    while(n-2)>0:
        n3 = n2+n1
        n1 = n2
        n2 = n3
        n -=1
    return n3
print("here we start to use fab(5)iterate".center(50,"*"))
val = eval(input("input 5:"))
res = fab(val)
if res != -1:
    print("总共有%d兔斯基呀!"%res)

