'''
最下面压着的第N个 从a->c  a-c
剩下的除了最大的以外 只有n-1个了
(n-1)一开始从a到b 过渡 是为了给n让路呀，其实需要c作为过渡
然后要把所有的(n-1)移动到目标c
现在（n-1）在b上了，所以需要过渡柱a 轨迹就是b->过渡a->c  b-a-c
'''
count = 0
def hanoi(n,left,mid,right):  #参数2left-起点，参数4 right- 终点，mid 过渡参数放中间
    global count
    if n == 1:
        print("一个盘子，第step - %d 从起点 %s ---> 终点(%s)" %(1,left,right))
        count +=1
    else:
        hanoi(n-1,left,mid,right) #从起点left-->终点right
        print(" %d:第%d个圆盘先要从 起点(%s)-> 到(%s)" % (count,n-1,left,right))
        count +=1 #每次移动都要加一
        hanoi(n-1, mid, left, right)  #现在在过渡柱的mid-》 要去终点right， 中间参数是left


hanoi(3,"a","b","c")



