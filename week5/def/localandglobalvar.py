'''
规则1： local var and global var are different
规则2： 局部变量为组合数据类型并且没有创建的 等同于全局变量
'''''
n,s = 10,11  #global
def fact(n):
    print("star local var fact()".center(50, "="))
    s = 1
    for i in range(1,n+1):
        s *=i
    print("inside def 's' ->",s)

    return s
print("返回函数值{0}-返回s的值{1}".format(fact(n),s))
print("end local var fact()".center(50, "="))
'''
inside def 's' -> 3628800
返回函数值3628800-返回s的值11 #这里返回的s的值就是最开始的11
'''

#global para
a,b = 5,10
def globalfact(a):
    global b
    for i in range(1,a+1):
        b *=i
    print("inside def gloabal 'b' ->", b)
    return b
print("返回函数值{0}-返回b的值{1}".format(globalfact(a),b))
'''
inside def gloabal 'b' -> 1200
返回函数值1200-返回b的值1200
这里返回的b的值是函数里面的值 1200 因为这个b是一个全局变量
'''

print("规则2： 局部变量为组合数据类型并且没有创建的 等同于全局变量".center(100,"*"))
ls = ["F","f"]  #真实创建了ls的列表
def fact2(a):
    ls.append(a)  #此处ls是列表类型 但是 未被创建，所以视为 全局变量
    return
fact2("FF") #此处全局变量ls被添加了一个FF的元素
print(ls)  #['F', 'f', 'FF']

print("规则2-反向： 局部变量为组合数据类型并且没有创建的 等同于全局变量".center(100,"*"))
ls = ["F","f"]
def fact3(a):
    ls = []   #创建了ls为一个空的列表 此时ls变成局部变量
    ls.append(a)
    return
fact3("FF")
print(ls)   #['F', 'f']

