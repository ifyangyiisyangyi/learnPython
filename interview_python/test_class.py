# # -*- coding: utf-8 -*-
# class Student(object):
# 	def __init__(self, name, score = 60):
# 		self.name = name
# 		self.score = score
# 	def get_score(self):
# 		return self.score
# peter = Student('peter') # 构造方法中的 score = 60, score 是默认参数，可以不传入
# print(peter.get_score())
# lisa = Student("lisa", 30)
# print(lisa.name, lisa.get_score()) # 在python3中，print是一个函数，打印出来的值会以空格分隔
# print(lisa.name, lisa.get_score(), sep = '') # 重新定义分隔符


# class Solution():
# 	def SortNum(self, nums):
# 		num_list = list(set(nums))
# 		num_odd = []
# 		num_even = []
# 		for num in num_list:
# 			if int(num) % 2 == 0:
# 				num_even.append(num)
# 			else:
# 				num_odd.append(num)
# 		num_even = sorted(num_even, reverse=True)
# 		num_odd = sorted(num_odd)
# 		num_odd.extend(num_even)
# 		return num_odd

#
# if __name__ == '__main__':
# 	num_list = [1,9,8,2,3,7,6,4,5,5]
# 	solution = Solution()
# 	num_odd = solution.SortNum(num_list)
# 	print(num_odd)



# def fun(ss):
#     ss[0] = 20
#     ss = [4,5,6]
#
# ss = [1,2,3]
# fun(ss)
# print(ss)

# def arrsum(arr):
#     arrlength=len(arr)
#     S=[None]*arrlength#记录连续的计算和
#     MS=[None]*arrlength#记录最大的和
#     S[0]=arr[0]
#     MS[0]=arr[0]
#     i=1
#     while i<arrlength:
#         S[i]=max(S[i-1]+arr[i],arr[i])
#         MS[i]=max(MS[i-1],S[i])
#         i+=1
#     return MS[arrlength-1]
# if __name__=="__main__":
#     arr=[1,-2,4,8,-4,7,-1,-5]
#     data=sum=arrsum(arr)
#     print(data)

# str = '''
#
# 4
# 4
# 3
# 3
# 3
# 4
# 4
# 4
#
# 4
# 4
# 3
# 3
# 4
# 3
# 3
# 3
#
# 3
# 4
# 3
# 3
# 3
# 3
# 4
# 4
# 4
# 5
# 5
# 3
#
# '''
#
# sum = 0
# res = str.replace('\n', '')
# for i in res:
#     sum += int(i)
# print(sum)


# a = [1,2, 3]
# def add(a = [1, 2, 3]):
#      a.append(4)
# add()
# def outprint():
#       print(a)
# outprint()
from typing import List



# def findClosestElements(arr, m, x):
# 	arr.sort(key=lambda v: abs(v - x))
# 	return sorted(arr[:m])
#
#
# if __name__ == '__main__':
# 	res = findClosestElements([1,2,3,8,9], 2, 2)
# 	print(res)


# class Solution:
#     def maxRepeating(self, sequence: str, word: str) -> int:
#         cnt = 1
#         while word*cnt in sequence:
#             cnt+=1
#         return cnt-1
#
#
# a = Solution()
# res = a.maxRepeating('ababcab', 'ab')
# print(res)


arr = [1, 2, 3]

print(max(arr))