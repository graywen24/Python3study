count = 0
def hanota(n,src,dst,mid):
    global count
    
    if n == 1:
        print("第{}步，从一个第{}层的{}--->{}柱".format(count,n,src,dst))
        count +=1
    else:
        hanota(n-1,src,mid,dst)
        print("第{}步，从一个第{}层的{}柱--->{}柱".format(count,n,src,dst))
        count +=1
        hanota(n-1,mid,dst,src)
       

if __name__ == "__main__":
    n = eval(input("输入基层汉诺塔"))
    print('ok,'+"有"+str(n)+"层的汉诺塔开始搬运了,...")
    src,mid,dst = "a","b","c"
    hanota(n,src,dst, mid)
    print(count)