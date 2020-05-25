import random as r
#r.seed(10)
print("random number with seed 10-->",r.random())

print("random number without seed is ->",r.random())

print(r.randint(10,1000))
print(r.randrange(10,100,5)) #10 到100 随机整数，步长为5
print((r.getrandbits(16))) #生成一个K比特长的随机整数
print(r.uniform(10,50)) #10到50的随机小数
print(r.uniform(10.99,10.999)) #10.99到10.999的随机小数

s = [1,2,3,4,5,6,7,8,9,0]
print(r.choice(s))   #选取S序列中随机元素
print(r.shuffle(s))  #结果为None
r.shuffle(s)  #这里才是打乱   #打乱序列s
print(type(r.shuffle(s)))   #NoneType
print(s)