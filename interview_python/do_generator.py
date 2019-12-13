# -*- coding: utf-8 -*-
L = [x * x for x in range(10)]
print(L)
L2 = (x * x for x in range(10))
for i in L2:
	print(i)