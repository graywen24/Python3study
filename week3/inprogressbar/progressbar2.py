import time

scale = 10
print("start".center(20,"-"))   #-------kaishi-------
for i in range(101):
    print("\r{:=^5}%".format(i),end="")   #=100=%
    print("\r{:3}%".format(i),end="") 
    time.sleep(0.1)

print("end".center(20,"-")) 