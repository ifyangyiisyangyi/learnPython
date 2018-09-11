# encoding=utf-8
# 我们把变量从内存中变成可存储或传输的过程称之为序列化
import pickle

f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)