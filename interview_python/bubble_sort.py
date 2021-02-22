# -*- coding: utf-8 -*-
# 冒泡排序

import numpy as np


def bubble_sort(list):
    for i in list:
        for j in range(len(list) - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]


arr = np.random.randint(1000, size=10)  # 生成1000以内的10个随机值
bubble_sort(arr)
print(arr)
