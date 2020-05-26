#coomment
temp = input("输入温度")
if temp[-1] in ["F","f"]:
    cTemp = (eval(temp[0:-1])-32)/1.8
    print("cTemp is {:.2f}C".format(cTemp))
elif temp[-1] in ["C", "c"]:
    fTemp = eval(temp[0:-1])*1.8 + 32
    print("fTemp is {:.2f}F".format(fTemp))
else:
    print("something wrong")