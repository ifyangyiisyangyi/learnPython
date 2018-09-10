# -*- coding: utf-8 -*-
class Student(object):
	def __init__(self, name, score):
		self.name = name
		self.score = score
	def get_grade(self):
		if self.score >= 90:
			return 'A'
		elif self.score >= 60:
			return 'B'
		else:
			return 'C'
lisa = Student('lisa', 99)
bart = Student('bart', 59)
print(lisa.name, lisa.get_grade())
print(bart.name, bart.get_grade())