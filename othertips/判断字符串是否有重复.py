# -*- coding: utf-8 -*-

def isDuplicate(str):
    for ch in str:
        counts = str.count(ch)
        print("character number -->", counts)
        if counts > 1:
            return True
    return False

if __name__ == '__main__':
    val = input("input a string")
    result = isDuplicate(val)
    if result:
        print(val+ " has duplicate")
    else:
        print(val+ " no duplicate")