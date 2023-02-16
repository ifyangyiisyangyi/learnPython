# 1. 两数之和

'''
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
'''
from typing import List


class Solution:
    def twosum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        for i in range(l):
            for j in range(i + 1, l):
                if nums[i] + nums[j] == target:
                    return [i, j]

# 哈希表，时间复杂度 O(N)
class Solution2:
    def twosum(self, nums:List[int], target:int) -> List[int]:
        hashtable = dict()
        for k, v in enumerate(nums):
            if target - v in hashtable:
                return [hashtable[target - v], k]
            hashtable[nums[k]] = k
        return []

if __name__ == '__main__':
    a = Solution2()
    assert a.twosum([2, 7, 11, 15], 9) == [0, 1]
    assert a.twosum([3, 2, 4], 6) == [1, 2]
    assert a.twosum([3, 3], 6) == [0, 1]
