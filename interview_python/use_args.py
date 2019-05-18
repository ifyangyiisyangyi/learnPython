"""
*args,**kwargs
"""


def fun(arg, *args):
    print(arg)
    for i in args:
        print(i)


fun(1, 2, 3)  # 1 2 3
fun([1, 2, 3])  # [1,2,3]


def fun2(**kwargs):
    for x, y in kwargs.items():
        print('key=%s; value=%s' % (x, y))
    return


b = {"b": "b"}
fun2(**b)  # key=b; value=b

fun2(a=1, b=2)  # key=a; value=1  key=b; value=2

a = {'name': 'yy'}
b = {'sex': 'male'}
c = dict(a, **b)
print(c) # {'name': 'yy', 'sex': 'male'}

a.update(b)
print(a) # {'name': 'yy', 'sex': 'male'}
