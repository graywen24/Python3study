'''
set recursion limit by default system is 1000
'''
import sys
print(sys.getrecursionlimit())   #1000
#sys.setrecursionlimit(10001)
#print(sys.getrecursionlimit())


#阶乘 1x2x3x4x5=5!

def jiechen(n):
    if n ==1:
        return 1
    else:
        return n*jiechen(n-1)


#如果输入<=0 会无穷递归 报错RecursionError: maximum recursion depth exceeded in comparison
var = eval(input("pls input a number:"))
if var <=0:
    print("u must input a number >0")
else:
    res = jiechen(var)
    print("%d 的阶乘是 %d" %(var,res))
