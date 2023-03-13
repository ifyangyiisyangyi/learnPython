# 658 找到 K 个最接近的元素

'''
给定一个 排序好 的数组 arr ，两个整数 k 和 x ，从数组中找到最靠近 x（两数之差最小）的 k 个数。返回的结果必须要是按升序排好的。

整数 a 比整数 b 更接近 x 需要满足：
|a - x| < |b - x| 或者
|a - x| == |b - x| 且 a < b
'''
from typing import List


class Solution:
    def findCloestElement(self, arr: List[int], k: int, x: int) -> List[int]:
        arr.sort(key=lambda v: (v - x))
        return sorted(arr[:k])


if __name__ == '__main__':
    a = Solution()
    assert a.findCloestElement([1, 2, 3, 4, 5], 4, 3) == [1, 2, 3, 4]
