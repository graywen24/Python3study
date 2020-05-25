
def fact(n):
    print("start  fact()".center(50, "="))
    s = 1
    for i in range(2,n+1):   #start from 1 else will start from 0
        print("i->",i)
        s *= i
        print("s->",s)
    print("end  fact()".center(50, "="))
    return s
print("fianl ->",fact(5))


#可选参数必须放在 必要参数后面
#  a//b 取整 a%b 取余数 a**b a的b次方
def fact1(n,m=1):
    print("start  fact1()".center(50, "-"))
    s = 1
    for i in range(1,n+1):
        s *=i
        print("s->", s)
    print("end  fact1()".center(50, "-"))
    return s//m
print("final ->",fact1(5,9))

#可变参数的数量
#def(n,*b) 可以是*a *b *c
def fact2(n,*b):
    print("start  fact2()".center(50,"="))
    s = 1
    for i in range(1,n+1):
        s *=i
    for item in b:
        print("item-->",item)
        s =s*item   #item=1->3628800*1;item=5->3628800*5=18144000
        print("item inside s->",s)
    print("end fact2()".center(50, "="))
    return s
fact2(10,1,5)
'''
------------------start  fact2()------------------
item--> 1
item inside s-> 3628800
item--> 5
item inside s-> 18144000
-------------------end fact2()--------------------
'''