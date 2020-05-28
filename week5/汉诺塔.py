count = 0
def hanota(n,src,dst,mid):
    global count
    
    if n == 1:
        print("恒等于1:第{}步，从一个从{}层的{}柱 搬到--->{}柱".format(count,1,src,dst))
        count +=1
    else:
        hanota(n-1,src,mid,dst)
        print("第{}步，从一个从{}层的{}柱 搬到--->{}柱".format(count,n,src,dst))
        count +=1
        hanota(n-1,mid,dst,src)
        print("after mid,dst,src ")

if __name__ == "__main__":
    n = eval(input("输入基层汉诺塔"))
    print('ok,'+str(n)+"开始搬运了,...")
    src,mid,dst = "A","b","c"
    hanota(n,src,dst, mid)
    print(count)