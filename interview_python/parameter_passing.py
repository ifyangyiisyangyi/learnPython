'''
python 的函数参数传递
'''
a = 1
def fun(a):
    print("a的值是: ", a)
    a = 2
    print("a的值是: ", a)
fun(a)
print("a的值是: ", a)