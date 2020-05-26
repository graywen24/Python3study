#str.lower() str.upper()
print("ABCDEFG".lower())    #abcdefg
print("abcdef".upper())  #ABCDEF

#str.split(sep=None)
print("A,B,C".split(","))  #['A', 'B', 'C']
print(type("A,B,C".split(",")))   #it is a list
print(("wenwen".split("e"))[1])  #['w', 'nw', 'n'] --> nw

#str.count(sub)
print("an apple a day".count("a")  )   # 4 

#str.replace(old, new)
print("python".replace("t","aaa-aaa")) #pyaaa-aaahon

#str.center(width,[,填充符])
print("wenwen".center(20,"=")) #只能有一个填充的 
#=======wenwen=======
print("wenwen".center(20," "))
#      wenwen       

#str.strip(char) 去掉左右两个侧的空格
print("=   python    =".strip(" =")) #去掉空格和=
print("=   python    =".strip("="))  #去掉了=
print("=   python    =".strip(" =np"))  #空格和=np都不在了


#str.join(iter)
print(",".join("12345"))  #在一段字符串中间添加分隔符
#"1,2,3,4,5"













