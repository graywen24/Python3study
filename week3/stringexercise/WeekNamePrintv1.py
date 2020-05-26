#操作符
# x + y 
# n*x x*n 乘法
# x in s x是s的子字符串 是则返回True, else return False
#input 1-7 inter and output will show 星期几
weekStr = "星期一星期二星期三星期四星期五星期六星期天"
weekId = eval(input("input 1-7:"))
weekPos = (weekId - 1)*3
print(weekStr[weekPos:weekPos+3])


