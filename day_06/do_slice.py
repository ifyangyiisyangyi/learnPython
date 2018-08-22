# _*_ coding:utf _*_
def trim(s):
	if s[:1] != " " and s[-1:] != " ":
		return s
	elif s[:1] == " ":
		s = s[1:]
		return trim(s)
	elif s[-1:] == " ":
		s = s[:-1]
		return trim(s)
# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
