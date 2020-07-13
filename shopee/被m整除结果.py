import math
import sys

def solve(n,m):
    # Write your code hered
    fin = fio(n)
    if fin % m == 0:  
        return int(fin/m)
        #print(fin/m)
    else:
        print("-1")
def fio(n):
    if n == 1:
        return n
    if n == 2:
        return n
    totalSteps = fio(n-1)+fio(n-2)
    return totalSteps

n = eval(input("here is total steps n:"))
m = eval(input("here is m :"))
outcome = solve(n,m)
print(outcome)