import time

start_time = time.time()
print(sum(range(1, 10000001)))
t = time.time() - start_time
print(f"耗时{t}秒")  # 耗时1.1359498500823975秒秒


i = 0
sum = 0
start_time2 = time.time()
while i < 10000001:
    sum += i
    i += 1
print(sum)
t2 = time.time() - start_time2
print(f"耗时{t2}秒") # 耗时4.183811664581299秒


