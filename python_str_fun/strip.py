'''
strip() 去除首尾空格
'''
import string
s = '  abc '
def fun(str):
    return str.strip(' a')
print(fun(s))

