# 34. 在排序数组中查找元素的第一个和最后一个位置
'''
给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回 [-1, -1]。
'''
from typing import List


class Solution:
    def searchRage(self, nums: List[int], target: int) -> List[int]:
        lst = []
        for k, v in enumerate(nums):
            if v == target:
                lst.append(k)
        if len(lst) < 1:
            return [-1, -1]
        else:
            return [lst[0], lst[-1]]


if __name__ == '__main__':
    a = Solution()
    assert a.searchRage([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert a.searchRage([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
    assert a.searchRage([], 0) == [-1, -1]
    assert a.searchRage([3, 3, 3], 3) == [0, 2]
    assert a.searchRage([1], 1) == [0, 0]
