'''
字典中如何删除键和合并两个字典
'''

a = {'name' : 'yangyi', 'age' : 30}
b = {'sex' : 'male'}
a.update(b) # 不能写成 c = a.update(b)
print(a) # {'name': 'yangyi', 'age': 30, 'sex': 'male'}
del a['sex']
print(a) # {'name': 'yangyi', 'age': 30}