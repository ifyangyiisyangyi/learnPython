"""
字符串去重排序
"""


def fun(s):
    s = set(s)
    s = list(s)
    s.sort(reverse=False)
    res = "".join(s)
    print(res)
    return res


fun('ajldjlajfdljfddd')  # adfjl


def fun2(str1, str2):  # Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
    res = str1.join(str2)
    print(res)
    return res


fun2('-', ['a', 'b', 'c'])  # a-b-c
fun2('', ('1', '2', '3'))  # 123
fun2('-', {'a', 'b', 'c'})  # c-b-a   ???


def fun3(s):
    s.sort(reverse=True) # 字符串排序
    print(s)
    return s


fun3(['b', 'a', 'e', 'a'])  # ['e', 'b', 'a', 'a']


a = [3,1,2]
b = sorted(a)
print(b)