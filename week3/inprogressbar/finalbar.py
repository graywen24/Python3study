import time
scale = 50
print("start".center(int(scale/0.5),"-"))
#print(scale/0.5) #100.0 is float
#print(int(scale/0.5)) will be 100 int
start = time.perf_counter()
for i in range(scale+1):
    a = "*"*i
    b = "."*(scale-i)
    c = (i/scale)*100
    dur = time.perf_counter()-start
    print("\r{:^3.0f}%[{}->{}]{:=<8.2f}sec".format(c,a,b,dur),end="")  #>]5.16====sec  dur左对齐 公8个字符
    time.sleep(0.1)
print("\n"+"end".center(int(scale/0.5),"-"))


