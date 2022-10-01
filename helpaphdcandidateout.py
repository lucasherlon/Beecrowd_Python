# -*- coding: utf-8 -*-

n = int(input())

for i in range(n):
    exp = str(input()).split('+')

    if(len(exp) == 2):
        n1 = int(exp[0])
        n2 = int(exp[1])
        soma = n1 + n2
        print(soma)
    else:
        print("skipped")
