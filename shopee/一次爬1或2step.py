'''
There are n stairs, a person standing at the bottom wants to reach the top. 
The person can climb either 1 stair or 2 stairs at a time. 
Count the number of ways, the person can reach the top.
n =1 only 1 way to reach
n=2 there are 2 ways to reach
n =3 (1,1,1) (1,2)(2,1) 3 ways
n = 4 (1,1,1,1)(1,1,2)(1,2,1)(2,1,1)(2,2) 5 ways
way(4) =way(3)+way(2)
way(3)=way(2)+way(1)
way(n)=way(n-1)+way(n-2)
The above expression 
is actually the expression for Fibonacci numbers, 
but there is one thing to notice, the value of ways(n) is equal to fibonacci(n+1).
ways(1) = fib(2) = 1
ways(2) = fib(3) = 2
ways(3) = fib(4) = 3
'''
##################
'''
def totalways(n):
    if n == 1:
        return n
    if n == 2:
        return n
    else:
        return totalways(n-1)+totalways(n-2)

f = eval(input("give a total steps number:"))
print(totalways(f))
'''
def fib(n):
    if n <=1:
        return n
    return fib(n-1)+fib(n-2)
#return no. of ways to reach nth stairs
def countWay(s):
    return fib(s+1)

s = eval(input("input a number:"))
print(countWay(s))
