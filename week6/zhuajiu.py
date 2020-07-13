import random
 
# 团队成员名对应随机数字典
nsdlTeamMember = {'小1':0, '小2':0, '小3':0, '小3':0, '小5':0, '小6':0, '小7':0, '小8':0}

def teamMarking(teamMember):
    #存储生成非重复随机数的列表
    chooseNumList = []
    for i in range(len(teamMember.keys())):
        num = random.randint(1,len(teamMember.keys()))
        while num in chooseNumList:
            num = random.randint(1,len(teamMember.keys()))
        chooseNumList.append(num) 
        print(chooseNumList)

    print("一共有个%d成员，抓阄结果如下："% len(teamMember.keys()))
    i = 0
    for k,v in teamMember.items():
        v = chooseNumList[i]
        print("here is v-->%s" %v)
        #print("here is k-->%s" %k)
        i +=1
        print(k.ljust(8) + str(v).rjust(4))

if __name__ == "__main__":
    teamMarking(nsdlTeamMember)
