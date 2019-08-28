'''
统计字符串中最小字母的出现次数

1. 字符串转列表
2. 列表排序
3. 统计第一个元素的次数
'''


def letter_counter(str):
    if str == '':
        return 0
    else:
        lst = list(str)
        lst.sort()
        return lst.count(lst[0])


# 测试代码

case_1 = 'abcdea'
print(f'最小字母出现次数是{letter_counter(case_1)}')  # 最小字母出现次数是2
case_2 = ''
print(f'最小字母出现次数是{letter_counter(case_2)}')  # 最小字母出现次数是0
