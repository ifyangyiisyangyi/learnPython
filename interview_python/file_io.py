# -*- coding: utf-8 -*-

# 打开一个文件对象，并读取
# f = open('c:/aaa/aaa.txt', 'r')
# print(f.read())
# f.close()

# try...finally
# try:
# 	f = open('c:/aaa/aaa.txt','r')
# 	print(f.read())
# finally:
# 	if f:
# 		f.close()

# with 方法读文件
# with open('c:/aaa/aaa.txt', 'r') as f:
# 	print(f.read())

# with方法写文件
# with open('c:/aaa/aaa.txt', 'w') as f:
	# f.write('hello, world')

# 追加
# with open('c:/aaa/aaa.txt', 'a') as f:
# 	f.write("\n""second line")

# 按行读取
# with open('c:/aaa/aaa.txt', 'r') as f:
# 	for line in f.readlines():
# 		print(line.strip())

