# here is convertpy.py
'''
c = (F -32)/1.8
f = c*1.8 + 32
'''


tempStr = input("输入温度:")
if tempStr[-1] in ["F","f"]:
    F = (eval(tempStr[0:-1]))*1.8 + 32   
    print("F with formate {:.2f}C-->",format(F)) # will show {:.2f}F--> 93.2
    print("F with formate and using dot {:.2f}摄氏度-->".format(F)) #with dot
    print("F without formate -->", F)
elif tempStr[-1] in ["c","C"]:
    C = (eval(tempStr[0:-1]) - 32)/1.8
    print("here is c value -->", C)
    print("C with formate--->{:.3f}华氏度".format(C))
else:
    print("something wrong")