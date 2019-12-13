# -*- coding: utf-8 -*-
# 访问权限，变量前加两个下划线  __name，就变成私有变量
class Student(object):
	def __init__(self, name, gender):
		self.name = name
		self.__gender = gender
	def get_gender(self):
		return self.__gender
	def set_gender(self, a):
		self.__gender = a
		return self.__gender
# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')