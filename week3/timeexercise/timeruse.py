import time
#perf_counter
'''
>>> start = time.perf_counter()
>>> end = time.perf_counter()
>>> end - start
10.245079723
>>> time.perf_counter()
41.764763326
>>> time.perf_counter()
53.652997128
'''
def wait():
    time.sleep(3.3)
print("start--"+time.ctime())
wait()
print("end --" + time.ctime())
