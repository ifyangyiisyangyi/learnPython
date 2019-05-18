"""
lambda
"""

res = lambda a, b: a * b
print(res(2, 3))


def fun(*args):  # 字符串拼接
    s = ''
    for i in args:
        if isinstance(i, str):
            s += i
        else:
            print('请输入字母')
            return
    print(s)


fun('a', 'b', 'c', 'd')
