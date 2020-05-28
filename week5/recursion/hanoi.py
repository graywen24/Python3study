'''
最下面压着的第N个 从a->c  a-c
剩下的除了最大的以外 只有n-1个了
(n-1)一开始从a到b 过渡 是为了给n让路呀，其实需要c作为过渡
然后要把所有的(n-1)移动到目标c
现在（n-1）在b上了，所以需要过渡柱a 轨迹就是b->过渡a->c  b-a-c
'''
count = 1
def hanoi(n,left,guodu,right):
    #global count
    if n == 1:
        print("step - %d 从起点 %s ---> 终点(%s)" %(count,left,right))
        #count +=1
    elif n > 1:
        #print("第%d 个圆盘起点(%s) ---》终点(%s)" %(n,left,right))
        print("第step - %d 第%d个圆盘先要从 起点(%s)-> 到(%s),过渡的柱子就是(%s)" % (count,n-1,left,guodu,right))
        print(left, '--->', right)

        hanoi(n-1,left,right,guodu)

        #count +=1 #每次移动都要加一
        #print("第%d-1 个圆盘现在在过渡柱%s上，所以要从%s ->终点(%s), 过渡柱子是(%s)" % (n, guodu,left.right))
        hanoi(n-1, guodu, left, right)
    else:
        print("输入正的圆盘数")

hanoi(3,"a","b","c")



