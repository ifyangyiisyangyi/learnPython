# 5. 最长公共子串
'''
给你一个字符串 s，找到 s 中最长的回文子串。

如果字符串的反序与原始字符串相同，则该字符串称为回文字符串
'''


# 暴力破解
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = s[0]
        for i in range(n - 1):
            for j in range(i, n):
                if s[i] == s[j]:  # 回文串必然是首尾字符相同
                    res = s[i:j + 1]
                    if res == res[::-1] and len(res) > len(ans):
                        ans = res
        return ans


if __name__ == '__main__':
    a = Solution()
    assert a.longestPalindrome('babad') == 'bab'
    assert a.longestPalindrome('cbbd') == 'bb'
    assert a.longestPalindrome('abbcbabc') == 'cbabc'
