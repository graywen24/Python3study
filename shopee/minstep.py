'''
Misha wants to climb a staircase consisting of n stairs. 
In one step she can either climb one or two stairs. 
But, Misha wants the total number of steps taken 
at the end of the staircase to be divisible by a number m.

? min number of steps need to take to climb 

input :
The first line contains the integer: n
The second line contains the integer: m

output:
pirnt a single number - the min number of steps divisible by m
if there is no way to climb the staris while satisfying the requirements, then pirnt -1
constraints
1<=n<=100000
1<=m<=10

'''
#!/bin/python3

import re
import sys
import math
import random
import os

def fio(n):
    if （n == 1 or n ==2):
        return n
    return fio(n-1)+fio(n-2)

def solve(n,m):
    # Write your code hered
    totalSteps = fio(n)
    if fin % m == 0:  
        return int(fin/m)
        #print(fin/m)
    else:
        print("-1")


n = eval(input("here is total steps n:"))
m = eval(input("here is m :"))
outcome = solve(n,m)
print(outcome)
