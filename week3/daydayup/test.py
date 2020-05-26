def dayup(df):
    dayup = 1
    for i in range(365):
        if i % 7 in [6,0]:
            dayup = dayup*(1 - 0.01)
            #print(dayup)
        else:
            dayup = dayup*(1 + df)
            #print(dayup)
    return dayup
         
dayfactor = 0.01
while dayup(dayfactor) < 37.78:
    dayfactor += 0.001  #here is us 0.01 will be 0.02
 
print("工作日努力参数需要是{:.4f}".format(dayfactor))