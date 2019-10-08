"""
doctest
"""


def test(n):
    """
    用于判断传入参数n的奇偶性
    >>> test(1)
    1是奇数
    >>> test(2)
    2是偶数
    """
    if n % 2 == 0:
        print(f'{n}是偶数')
    else:
        print(f'{n}是奇数')


if __name__ == '__main__':
    test(3)
