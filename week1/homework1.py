
str = input()
if str[-1] in ["F","f"]:
    C = (eval(str[0:-1]) - 32)/1.8
    print("{:.2f}C".format(C))
elif str[-1] in ["c","C"]:
    F = (eval(str[0:-1]))*1.8 + 32
    print("{:.2f}F".format(F))
else:
    print("输入格式错误")