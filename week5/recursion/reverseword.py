def rvs(s):
    if s == "":
        return s
    else:
        return rvs(s[1:])+s[0]

str = input("输入一个字符串:")
print("不包括最后一个字符-1-->' '%s" %str[:-1])  #abc->ab 不包括最后一个字符 -1
print("包括第一个0到最后一个字符--->%s" %str[0:]) #abc->abc 包括第一个0到最后一个字符
print("不包括第0个字符-->%s"%str[1:])  #abc->bc 不包括第0个字符 也就是a
print(rvs(str))  #abc->cba