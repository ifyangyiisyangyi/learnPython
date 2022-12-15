# 14. 最长公共前缀
'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""
'''
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix, l = strs[0], len(strs)
        for i in range(1, l):
            prefix = self.lcp(prefix, strs[i])  # 前两个字符串的公共前缀赋给prefix，再拿prefix依次跟后面的元素去提取公共前缀
            if not prefix:
                break
        return prefix

    def lcp(self, str1: str, str2: str) -> str:  # 两个字符串取最长公共前缀
        index, l = 0, min(len(str1), len(str2))
        while index < l and str1[index] == str2[index]:
            index += 1
        return str1[:index]


if __name__ == '__main__':
    a = Solution()
    assert a.longestCommonPrefix(["flower", "flow", "flight"]) == 'fl'
    assert a.longestCommonPrefix(["dog", "racecar", "car"]) == ''
