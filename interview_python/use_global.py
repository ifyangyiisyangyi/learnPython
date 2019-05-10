'''
如何在一个函数内部修改全局变量
'''

a = 5
def fun():
    global a  # 此处不可以写 global a = 4
    a = 4
fun()
print(a) # 4