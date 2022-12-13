# 3. 无重复字符的最长子串
'''
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
'''


class Solution:
    '''滑动窗口，依次将元素添加到窗口中，直到不符合要求，就将窗口左边的元素移除'''

    def lengthOfLongestSubstring(self, s: str) -> str:
        if not s: return 0
        n = len(s)
        left = 0
        look_up = set()
        cur_len = 0
        max_len = 0
        for i in range(n):
            cur_len += 1
            while s[i] in look_up:
                cur_len -= 1
                look_up.remove(s[left])
                left += 1
            look_up.add(s[i])
            if max_len < cur_len: max_len = cur_len
        return max_len

    def lengthOfLongestSubstring2(self, s: str) -> str:
        n = len(s)
        lst = []
        max_len = 0
        for i in range(n):
            while s[i] in lst:
                del lst[0]
            lst.append(s[i])
            max_len = max(max_len, len(lst))
        return max_len


if __name__ == '__main__':
    a = Solution()
    assert a.lengthOfLongestSubstring("abcabcbb") == 3
    assert a.lengthOfLongestSubstring("bbbbb") == 1
    assert a.lengthOfLongestSubstring("pwwkew") == 3
    assert a.lengthOfLongestSubstring("") == 0

    assert a.lengthOfLongestSubstring2("abcabcbb") == 3
    assert a.lengthOfLongestSubstring2("bbbbb") == 1
    assert a.lengthOfLongestSubstring2("pwwkew") == 3
    assert a.lengthOfLongestSubstring2("") == 0
