#daydayup2.py
#一年365 每天进步千分之5 Or 1% 累计进步多少
#一年365 每天退步千分之5 or 1% 累计退步多少

dayfactor = 0.005
dayup = pow(1+dayfactor,365)
print("dayup--->",dayup)

daydown = pow(1-dayfactor,365)
print("daydown--->",daydown)
print("upup:{:.2f},downdown:{:.2f}".format(dayup,daydown))

dayfactor = 0.01
dayup = pow(1+dayfactor,365)
print("dayup--->",dayup)

daydown = pow(1-dayfactor,365)
print("daydown--->",daydown)
print("upup:{:.2f},downdown:{:.2f}".format(dayup,daydown))

#upup:37.78,downdown:0.03
