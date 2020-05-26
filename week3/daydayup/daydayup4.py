#只有工作日daydayup 4.63
#365 daydayup 37.78 
#工作日模式努力到什么水平，才能与别人每天都努力1% 一样呢
#A user: 一年365天 永不停歇 1% up dayday
#B user: 5天1% 努力 休息2天1%下降
def dayup(df):
    dayup = 1 #初始值为1
    for i in range(365):
        if i % 7 in [0,6]:
            dayup = dayup*(1 - 0.01) #周末退步的参数不变
            #print("weekend dayup:{:.2f}".format(dayup))
        else:
             dayup = dayup*(1 + df) #每天努力多少
             #print("weekday dayup:{:.2f}".format(dayup))
             
    return  dayup
dayfactor = 0  #初始赋值 可以是0.001
while dayup(dayfactor) < 37.78:
    dayfactor +=0.001   #here is us 0.01 will be 0.02
    #print("dayfactor ======{:.3f}".format(dayfactor))   
    
print("工作日努力参数需要是{:.3f}".format(dayfactor))
print(type(dayup)) #class function 
print(type(dayfactor))  # float type
#工作日努力参数需要是0.019
#pow(dayup,365)