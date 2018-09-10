# -*- coding: utf-8 -*-
class Student(object):
	def __init__(self, name, score = 60):
		self.name = name
		self.score = score
	def get_score(self):
		return self.score
peter = Student('peter') # 构造方法中的 score = 60, score 是默认参数，可以不传入
print(peter.get_score())
lisa = Student("lisa", 30)
print(lisa.name, lisa.get_score()) # 在python3中，print是一个函数，打印出来的值会以空格分隔
print(lisa.name, lisa.get_score(), sep = '') # 重新定义分隔符
