# 快速判断python变量是否为多个类型之一

def test(tag):
    if isinstance(tag,(list,str, bool)):
        print("输入参数合法，进行后续操作")

# 简单测试
tag = [1,2]
test(tag)

words = 'yy'
test(words)

a = False
test(a)

# help(isinstance)
print(isinstance('yy', bool))