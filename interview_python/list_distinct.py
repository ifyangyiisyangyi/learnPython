"""
列表去重
"""

a = [1, 2, 3, 3]

b = set(a)

print(b)

a = [x for x in b]

print(a)
