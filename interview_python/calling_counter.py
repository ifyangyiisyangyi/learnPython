"""
统计python函数被调用几次
"""


class CallingCounter(object):
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)


@CallingCounter
def test():
    print('我被调用了')


if __name__ == '__main__':
    test()
    test()
    print(f'调用: {test.count}次')
