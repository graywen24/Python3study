print(len("123456"))   #6
# str(x) oppsite to eval()
print(type(str(1.23)))  # ---> "1.23"
str([1,2]) #"[1,2]"   
print(hex(425)) #十六进制小写  "0x1a9"
print(oct(425)) #八进制小写  “0o651”


##### unicode ######
#chr()  #返回unicode符号
# ord()   #返回值是unicdoe对应的十进制整数。
chr(1004) # return unicode  
print("1+1=2"+chr(10004)) #1+1=2✔
print(chr(9801))    #♉ 金牛座 so Aris is 9800
for i in range(12):
    print(chr(9800+i), end=" ")   #♈ ♉ ♊ ♋ ♌ ♍ ♎ ♏ ♐ ♑ ♒ ♓

 
