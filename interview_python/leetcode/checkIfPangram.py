# 1832. 判断句子是否为全字母句
'''
全字母句 指包含英语字母表中每个字母至少一次的句子。

给你一个仅由小写英文字母组成的字符串 sentence ，请你判断 sentence 是否为 全字母句 。

如果是，返回 true ；否则，返回 false 。
'''


class Solution:
    def checkIfPangram(self, s: str) -> bool:
        lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
        s = list(set(s))
        s.sort()
        return lst == s

    def checkIfPangram2(self, s: str) -> bool:
        return len(set(s)) == 26


if __name__ == '__main__':
    a = Solution()
    assert a.checkIfPangram("leetcode") == False
    assert a.checkIfPangram("thequickbrownfoxjumpsoverthelazydog") == True

    assert a.checkIfPangram2("leetcode") == False
    assert a.checkIfPangram2("thequickbrownfoxjumpsoverthelazydog") == True
