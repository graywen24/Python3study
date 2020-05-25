
try:
    a = eval(input("input a int number:"))
    while a < 10:
        a=a+1
        print(a)
except NameError:
    print("not a int number")
except TypeError:
    print("type error")
except SyntaxError:
    print("syntax,check you chinese input")
else:
    print("no error in try will reach here")