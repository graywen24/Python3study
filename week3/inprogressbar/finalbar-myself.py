# -*- coding: utf-8 -*-
import time 
scale = 50
#print("start".center(int(scale/2),"-")) # 25
print("start".center((scale//2),"-"))   #25
startime = time.perf_counter()
for i in range(scale+1):
     a = "*"*i
     b = "."*(scale -i)
     c = (i/scale)*100
     duration = time.perf_counter()-startime
     print("\r{:^4.0f}%[{}->{}]{:^5.2f}sec".format(c,a,b,duration),end="")
     time.sleep(0.1)
print("\n"+"end".center(int(scale/2),"-"))

'''
两个整型相除，得到的还是整型，但是。如果一个浮点数除以一个非浮点数得到的还会是一个浮点数，
但是，计算的结果却是忽略小数部分，运算的结果类似两个整型相除，但是得到一个浮点数。另外"//"对于两个浮点数也是不例外的。
>>> scale=50
>>> scale//2
25
>>> scale/2
25.0
>>> scale//3
16
>>> scale/3
16.666666666666668
>>> scale=50.0
>>> scale/3
16.666666666666668
>>> scale//3
16.0
'''