# -*- coding: UTF-8 -*-

# Filename : test.py
# author by : www.runoob.com

# 获取用户输入十进制数
#dec = int(input("输入数字："))
dec = input("输字符串：")
print(type(dec))
print("十进制数为：", dec)
print("转换为二进制为：", bin(dec))
print("转换为八进制为：", oct(dec))
print("转换为十六进制为：", hex(dec))