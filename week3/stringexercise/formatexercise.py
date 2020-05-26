# format 
# ： 引导符号

#一组
# 填充  
# 对齐 < 左对齐 >右对 ^居中对齐
# 宽度 

#居中=占位宽度20
print("{:=^20}".format("python")) # =======python=======
print("{0:=^20}".format("python"))# =======python=======

#* 为占位符 文字左对齐 占位20个
print("{0:*<20}".format("BIT")) # BIT*****************

#占位符- 20个长度 文字右对齐
print("{:->20}".format("PYTHON")) #--------------PYTHON
print("{:>20}".format("PYTHON"))  #              PYTHON

#另外一组
#, 数字的千位分隔符
#. 精度 .2f .3E 
#类型 整数b-二进制 c-unicode d-unicode o-八进制 x- X 
# 浮点： e E f %

print("{0:,.2f}".format(12345.6789))
#12,345.68   在千位3前面加了, 分割 2f 表示2位浮点 加了， 表示千位加个逗号
print("{:,.2%}".format(123456))
#12,345,600.00%     2%表示2位百分数显示


print("{0:b}".format(425)) #110101001 
print("{0:c}".format(425)) #Ʃ  unicode
print("{0:d}".format(425)) #425  十进制
print("{0:o}".format(425)) #651  八进制
print("{0:x}".format(425)) #1a9  十六进制
print("{0:X}".format(425)) #1A9   大写十六进制 

#-----------------
print("{0:e}".format(3.14)) #3.140000e+00
print("{0:E}".format(3.14)) #3.140000E+00
print("{:,.2f}".format(314000)) #-- diff 314,000.00
print("{:f}".format(3.14)) #3.140000
print("{0:%}".format(3.14)) #314.000000%













