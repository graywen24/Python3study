import time
t = time.ctime()
print(t)

try:
    num = eval(input("pls input a value:"))
    print(num**2)
    isinstance(num,int)
    #print("input is->"+ num)
    # print(isinstance(num,int)) #False
except NameError :
    print("NameError issue, it is not a inter")
else:
    print("it is an inter. no NameError so continue to end")
finally:
    print("this is end".center(20,"-"))
