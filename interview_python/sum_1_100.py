"""
1-100的和
"""


def fun():
    return sum(range(1, 101))


a = fun()
print(a)  # 5050

i = 0
b = 0
while i < 101:
    b += i
    i += 1
print(b)  # 5050

print(sum(range(1, 101)))  # 5050
