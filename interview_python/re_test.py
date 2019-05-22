"""
字符串a = "not 404 found 张三 99 深圳"，每个词中间是空格，用正则过滤掉英文和数字，最终输出"张三 深圳"
"""
import re

s = "not 404 found 张三 99 深圳"

list = s.split(' ')
print('list: ', list)
res = re.findall('\d+|[a-zA-Z]+', s)
print('res: ', res)
# for i in res:
#     if i in list:
#         print(i)
#         list.remove(i)
# print(list)
# result = ' '.join(list)
# print(result)

list = ['a', 'b', 'c']
res = ['a', 'b']
for i in list:
    if i in res:
        list.remove(i)
print(list)  # 为什么没有剔除 'b'？

