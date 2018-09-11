# -*- coding: utf-8 -*-
# python的内置函数 open() 可以文件对象，传入文件路径和标识符

# try:
# 	f = open('c:/aaa/yangyi.txt', 'r')
# 	s = f.read()
# 	print(s)
# finally:
# 	if f:
# 		f.close()

# fpath = r'c:/aaa/yangyi.txt'
# with open(fpath, 'r') as f:
# 	s = f.read()
# 	print(s)

fpath = r'c:/aaa/yangyi.txt'
with open(fpath, 'r') as f:
	for line in f.readlines():
		print(line.strip())