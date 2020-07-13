'''
How to count the number of ways if the person can climb up to m stairs for a given value m.
For example, if m is 4, the person can climb 1 stair or 2 stairs or 3 stairs or 4 stairs at a time.

Approach: For the generalization of above approach the following recursive relation can be used.
ways(n, m) = ways(n-1, m) + ways(n-2, m) + ... ways(n-m, m) 
xIn this approach to reach nth stair, try climbing all possible number of stairs lesser than equal to n from present stair.
'''
# A program to count the number of ways 
# to reach n'th stair 
  
# Recursive function used by countWays 
def fib(n, m): 
    if n <= 1: 
        return n 
    res = 0
    i = 1
    while i<= m and i<= n: 
        res = res + fib(n-i, m) 
        i = i + 1
    return res 
      
# Returns number of ways to reach s'th stair     
def countWays(s, m): 
    return fib(s + 1, m) 
      
  
# Driver program 
s, m = 4, 3
print("Number of ways =", countWays(s, m))
  
