import time
'''
时间获取 time() ctime() gmtime()
时间格式化 strftime() strptime()
程序计时 sleep() perf_counter()
 time.ctime()
'Wed May 20 16:58:20 2020'
time.gmtime()
time.struct_time(tm_year=2020, tm_mon=5, tm_mday=20, tm_hour=8, tm_min=58, tm_sec=33, tm_wday=2, tm_yday=141, tm_isdst=0)
%Y year
%m  month
%B  January- December
%b  Jan,Feb,Mar- Dec

%A  Monday, Tuesday - Sunday
%a  Mon,Tue,Wed,Thu,Fri,Sat,Sun
%d  date 01-31
%H   24h 00-23
%I   12h 01-12
%p   AM/PM 
%M   min 00-59
%S   sec 00-59
'''
t = time.ctime()
print(t)
res = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
print(res)   #2020-05-20 09:13:37

timeStr = "2020-05-20 09:13:37"
a = time.strptime(timeStr,"%Y-%m-%d %H:%M:%S")
print(a)
#time.struct_time(tm_year=2020, tm_mon=5, tm_mday=20, tm_hour=9, tm_min=13, tm_sec=37, tm_wday=2, tm_yday=141, tm_isdst=-1) 