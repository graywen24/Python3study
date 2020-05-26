#工作日的力量 
# 一周五个工作日 每天进步1%
#一周2个休息日 每天退步1%

i = 13
print(i%7)
dayup = 1.0
dayfactor = 0.01 #1%
for i in range(365):
    if i%7 in [6,0]: #那么就是星期六星期天
        dayup = dayup*(1-dayfactor)
    else:
        dayup = dayup*(1+dayfactor)
print("dadayup: {:.2f}".format(dayup))
#4.63