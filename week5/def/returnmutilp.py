#return 多个参数 为一个元组类似 tuple用小括号
def fact1(n,m=1):
    print("start  fact1()".center(50, "-"))
    s = 1
    for i in range(1,n+1):
        s *=i
        print("s->", s)
    print("end  fact1()".center(50, "-"))
    return s//m,n,m
a=fact1(5,9)
print(a)
print(type(a))   #返回tuple 元组类型