'''
统计在一个队列中的数字，有多少个正数，多少个负数，如[1, 3, 5, 7, 0, -1, -9, -4, -5, 8]

'''

s = [1, 3, 5, 7, 0, -1, -9, -4, -5, 8]

a = [i for i in s if i > 0]
print(f"正数个数{len(a)}")
b = [i for i in s if i < 0]
print(f"负数个数{len(b)}")
