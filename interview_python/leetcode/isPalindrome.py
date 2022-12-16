# 125. 验证回文串
'''
如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。则可以认为该短语是一个 回文串 。

字母和数字都属于字母数字字符。

给你一个字符串 s，如果它是 回文串 ，返回 true ；否则，返回 false 。


'''
import re

'''
用正则将字符串中的字母和数字过滤出来，然后再拼成字符串，如果字符串反转后和原串一样，就是回文串
'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        comp = re.compile(r"[0-9a-z]")
        s_list = comp.findall(s.lower())
        res = "".join(i for i in s_list)
        return res == res[::-1]


if __name__ == '__main__':
    a = Solution()
    assert a.isPalindrome("A man, a plan, a canal: Panama") == True
    assert a.isPalindrome("race a car") == False
    assert a.isPalindrome(" ") == True
    assert a.isPalindrome("0P") == False
