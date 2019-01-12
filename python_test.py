# 求0-500的和
print(sum(range(0,101)))
print('---------------------------------')

# 如何在一个函数内部修改全局变量的值
a = 5
def fn():
    global a
    a = 4    
fn()
print(a)
print('---------------------------------')

# 字典如何删除键和合并两个字典
dic = {'name':'yangyi', 'sex':1}
del dic['name'] #删除键
print(dic)
dic2 = {'age':30}
dic.update(dic2)
print(dic)
print('---------------------------------')

# python实现列表去重的方法
def fnc(x):
    a = set(x)              # 通过集合去重
    return [i for i in a]   # 集合转为列表
s = [1,1,2,5,6]
print(fnc(s))
print('---------------------------------')

s = "ajldjlajfdljfddd"
a = set(s)  # 集合去重
# b = [i for i in a] # 转成list
b = list(a) # 转为list
b.sort() # list排序
res = ''.join(b) # 生成str
print(res)
print('---------------------------------')

# 用lambda函数实现两个数相乘
sum = lambda x, y : x * y
print(sum(2, 2))
print('---------------------------------')

# 列表合并
list1 = [1,2,5]
list2 = [2,4,7]
list1.extend(list2)
list1.sort(reverse = False)
print(list1)
