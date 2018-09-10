# -*- coding: utf-8 -*-
# 子类继承父类，就拥有了父类的方法，子类可以覆盖父类的方法
class Animal(object):
	def run(self):
		print('Animal is running...')

class Dog(Animal):
	def run(self):
		print('Dog is running...')


class Cat(Animal):
	pass
	# def run(self):
	# 	print('cat is running...')

def run_twice(animal):
	animal.run()
	animal.run()

a = Animal()
d = Dog()
c = Cat()

print('a is a Animal?', isinstance(a, Animal))
print('a is a Dog', isinstance(a, Dog))
print('a is a Cat', isinstance(a, Cat))
print('---------------------------------------')

print('d is a Animal', isinstance(d, Animal))
print('d is a Dog', isinstance(d, Dog))
print('d is a Cat', isinstance(d, Cat))
print('---------------------------------------')

run_twice(c)