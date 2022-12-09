# 7. 整数反转
'''
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。

假设环境不允许存储 64 位整数（有符号或无符号）。
'''


class Solution:
    def reverse(self, x: int) -> int:
        num = int(str(abs(x))[::-1])  # 去符号后，转成字符转并反转，再转成整型
        s = -num if x < 0 else num  # 加上符号
        return s if -2 ** 31 <= s <= 2 ** 31 - 1 else 0  # 判断是否超出32位整数范围


if __name__ == '__main__':
    a = Solution()
    assert a.reverse(123) == 321
    assert a.reverse(-123) == -321
    assert a.reverse(120) == 21
