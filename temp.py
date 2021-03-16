# -*- coding: utf-8 -*-



import itertools
j=0
for i in itertools.product('春晓有生海霞敏晶文倩爱群佳', repeat = 2):
    name = '刘王'+''.join(i)
    print(name,end=",")
    j=j+1
    if j % 10 == 0:
        print('\n')

