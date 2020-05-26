'''
c = (F -32)/1.8
f = c*1.8 + 32
'''

#sampel here
print("let us start")

tempStr = input("pls input tempreture here:")
if tempStr[-1] in ["F","f"]:
    C = (eval(tempStr[0:-1]) - 32)/1.8
    print("so the C temp is {:.2f}-C".format(C))
elif tempStr[-1] in ["c","C"]:
    F = 1.8*(eval(tempStr[0:-1])) + 32
    print("so the F temp is {:.2f}F".format(F))
else:
    print("something wrong")
