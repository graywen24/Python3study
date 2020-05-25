from random import random
from time import perf_counter

DRAFTS = 1000*1000
hits = 0.0
start = perf_counter()
for i in range(1, DRAFTS):
    x, y = random(),random()
    #print("x--->",x)
    #print("y-->",y)
    dist = pow(x**2 + y**2, 0.5)
    if dist <= 1.0:
        hits += 1
print("hits->",hits)
print("DRAFTS-->",DRAFTS)
#理解 圆形*pi= 正方形面试
pi = 4*(hits/DRAFTS)
print("圆周率：{}".format(pi))
print("时间:{:.5f}s".format(perf_counter()-start))