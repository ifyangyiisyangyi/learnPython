# -*- coding: utf-8 -*-
# 冒泡排序
def bubble_sort(list):
	for i in list:
		for j in range(len(list) - 1):
			if list[j] > list[j + 1]:
				list[j], list[j+1] = list[j+1], list[j]
arr = [1,5,3,13131,12431432,121312412,2]
bubble_sort(arr)
print(arr)