'''
变态跳台阶 一只青蛙一次可以跳上1级台阶，
也可以跳上2级……它也可以跳上n级。
求该青蛙跳上一个n级的台阶总共有多少种跳法。
'''
n = eval(input("input how many steps:"))
sum = pow(2,n-1)
print(sum)

#https://blog.csdn.net/whl_program/article/details/82700261